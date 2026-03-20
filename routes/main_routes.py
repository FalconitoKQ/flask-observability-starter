from flask import Blueprint, Response, render_template
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

main_bp = Blueprint('main', __name__)

@main_bp.get('/healthy')
def healthy():
    return {"status": "ok"}

@main_bp.get('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@main_bp.get('/')
def index():
    return render_template('index.html')
