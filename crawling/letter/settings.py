import os
from pathlib import path

SATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myprofile', 'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')