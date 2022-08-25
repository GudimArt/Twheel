import uvicorn
from config import settings as _settings


if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host = _settings.server_host,
        port = _settings.server_port,
        reload = True
    )
    