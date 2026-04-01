# flask-observability-starter
A ready-to-run Flask setup with monitoring and logging built in.

## Architecture

- `nginx` receives HTTP traffic on `http://localhost`
- `flask_app` serves the application and exposes `/metrics`
- `prometheus` scrapes metrics from Flask on `http://flask_app:5000/metrics`
- `grafana` connects to Prometheus on the internal Docker network

## Run

```bash
docker compose up --build
```

Then open:

- App: `http://localhost`
- Health check: `http://localhost/healthy`
- Metrics: `http://localhost/metrics`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000` (`admin` / `admin`)

## What each file does

- `run.py` configures Flask, logging, request metrics, and reverse-proxy support
- `routes/main_routes.py` defines the app routes, including `/metrics`
- `config/metrics.py` defines Prometheus counters and histograms
- `nginx.conf` proxies traffic from Nginx to Flask
- `prometheus.yml` tells Prometheus what to scrape
- `docker-compose.yml` wires the services together on one Docker network
