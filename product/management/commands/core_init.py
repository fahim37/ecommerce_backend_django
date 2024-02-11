from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import connection
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):

        with connection.cursor() as cursor:
            cursor.execute("DROP SCHEMA public CASCADE;")
            cursor.execute("CREATE SCHEMA public;")

            # Apply migrations to create new tables
            self.stdout.write(self.style.SUCCESS("Dropped all tables."))
            self.stdout.write(self.style.SUCCESS("Applying migrations..."))
            call_command("migrate")

            self.stdout.write(self.style.SUCCESS("Database reset successfully."))

        User.objects.create_superuser(
            username="moshihud",
            password="123456",
        )
        User.objects.create_superuser(
            username="admin",
            password="123456",
        )
        self.stdout.write("Successfully created super user")
