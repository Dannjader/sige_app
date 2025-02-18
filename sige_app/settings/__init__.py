from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
if os.environ.get('ENV') == 'sige_app.settings.production':
    from .production import *
elif os.environ.get('ENV') == 'sige_app.settings.development':
    from .development import *
elif os.environ.get('ENV') == 'sige_app.settings.base':
    from .base import *
