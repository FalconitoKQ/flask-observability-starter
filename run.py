from flask import Flask, request
from config.loggingSetup import logging_setup
from config.metrics import REQUESTS_TOTAL
from routes.main_routes import main_bp

logger = logging_setup()

app = Flask(__name__)

app.register_blueprint(main_bp)

@app.before_request
def monitor_request():
    ep = request.path or "unknown"
    
    REQUESTS_TOTAL.labels(request.method, ep).inc()
    
    logger.info(
        "http_request",
        endpoint=ep,
        method=request.method,
        remote_addr=request.remote_addr,
        user_agent=request.user_agent.string
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)