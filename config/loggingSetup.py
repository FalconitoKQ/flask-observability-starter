import structlog

def logging_setup():
    # Konfiguracja procesorów structlog
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"), # Poprawiona ścieżka
            structlog.processors.JSONRenderer()
        ]
    )
    return structlog.get_logger()