#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

load_dotenv()
# Add the apps/ directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'apps'))
def main():
    """Run administrative tasks."""
    env_file = '.env'  # Default to .env for development
    settings_module = 'main.settings.dev'  # Default to dev settings
    if os.environ.get('DJANGO_ENV') == 'production':
        settings_module = 'main.settings.prod'  # Use prod settings for production
        env_file = '.prod.env'  # Use .prod.env for production
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    os.environ['ENV_FILE'] = env_file  # Set the environment variable for decouple
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
