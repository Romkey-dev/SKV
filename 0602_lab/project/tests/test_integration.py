import json
from threading import Thread
from urllib.request import urlopen

from werkzeug.serving import make_server

from app import app


def test_http_health():
    server = make_server("127.0.0.1", 0, app)
    worker = Thread(target=server.serve_forever)
    worker.start()
    try:
        with urlopen(f"http://127.0.0.1:{server.server_port}/health", timeout=5) as response:
            assert response.status == 200
            assert json.load(response) == {"status": "healthy"}
    finally:
        server.shutdown()
        worker.join(timeout=5)
        server.server_close()
