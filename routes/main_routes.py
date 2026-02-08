from flask import Blueprint, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from config.metrics import REQUESTS_TOTAL

main_bp = Blueprint('main', __name__)

@main_bp.get('/healthy')
def healthy():
    return {'status': 'enabled'}

@main_bp.get('/metrics')
def metrics():
    # Udostępnienie metryk dla Prometheusa
    return Response(generate_latest(), content_type=CONTENT_TYPE_LATEST)