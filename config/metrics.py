from prometheus_client import Counter
from flask import request, Blueprint
import structlog

metrics_bp = Blueprint('metrics', __name__)
logger = structlog.get_logger() # Inicjalizacja loggera dla tego modułu

REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

@metrics_bp.before_app_request
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