"""
Django command to wait for database to be available
"""

import time

from django.core.management.base import BaseCommand
from django.db import OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """Django command to wait for database to be available"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database is unavailable, \
                waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Databse available!'))
