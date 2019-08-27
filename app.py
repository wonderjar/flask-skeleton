from victoria import create_app

from config import config

import os

env = os.environ.get('FLASK_ENV', 'development')

app = create_app(config[env])