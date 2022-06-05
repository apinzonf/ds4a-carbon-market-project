import os
import traceback
from pathlib import Path


DEFAULT_VERSION = "1.0.default"


def get_version():
    app_version = os.getenv('VERSION', DEFAULT_VERSION)
    if app_version == DEFAULT_VERSION:
        try:
            version_path = Path('./version')
            text = version_path.read_text()
            app_version = text.split('"')[1]
        except Exception as e:
            traceback.print_exc()
    return app_version

