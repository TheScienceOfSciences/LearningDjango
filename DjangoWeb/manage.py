#!/usr/bin/env python
# username: tossthedice
# email:    liftheavy182@outlook.com
# password: cashmoney427cake

"""
Command-line utility for administrative tasks.
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "DjangoWeb.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
