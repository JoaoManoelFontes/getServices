#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

import dotenv


def main() -> None:
    """Run administrative tasks."""
    # Load environment variables from .env file
    dotenv_path = Path(__file__).parent / ".env"
    if dotenv_path.exists():
        dotenv.load_dotenv(dotenv_path)
    else:
        raise Exception("No .env file found!")  # noqa: EM101 TRY003 TRY002

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        msg = (
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
        raise ImportError(
            msg,
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
