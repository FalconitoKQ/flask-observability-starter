import time

from flask import Flask, g, request
from werkzeug.middleware.proxy_fix import ProxyFix

from config.loggingSetup import logging_setup
from config.metrics import REQUESTS_TOTAL, REQUEST_LATENCY_SECONDS
from routes.main_routes import main_bp

logger = logging_setup()


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)
    app.register_blueprint(main_bp)

    @app.before_request
    def start_timer():
        g.request_start = time.perf_counter()

    @app.after_request
    def observe_request(response):
        path = request.path or "unknown"
        method = request.method
        status_code = str(response.status_code)
        duration = time.perf_counter() - getattr(g, "request_start", time.perf_counter())

        REQUESTS_TOTAL.labels(method=method, path=path, status=status_code).inc()
        REQUEST_LATENCY_SECONDS.labels(method=method, path=path).observe(duration)

        logger.info(
            "http_request",
            method=method,
            path=path,
            status_code=response.status_code,
            duration_seconds=round(duration, 6),
            remote_addr=request.headers.get("X-Forwarded-For", request.remote_addr),
            user_agent=request.user_agent.string,
        )
        return response

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
