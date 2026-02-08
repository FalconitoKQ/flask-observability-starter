from flask import render_template, Flask, request, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

#
REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

@app.get('/')
def index():
    return "Hello World"

@app.get('/healthy')
def healthy():
    return {'status': 'enabled'}

@app.get('/metrics')
def metrics():
    return Response(generate_latest(), content_type=CONTENT_TYPE_LATEST)

@app.before_request
def count_requests():
    ep = request.path or "unknown"
    REQUESTS_TOTAL.labels(request.method, ep).inc()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
