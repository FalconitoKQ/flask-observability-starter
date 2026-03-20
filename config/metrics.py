from prometheus_client import Counter, Histogram

REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total HTTP requests processed by the Flask app",
    ["method", "path", "status"],
)

REQUEST_LATENCY_SECONDS = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "path"],
)
