from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = (
        "Runs database migrations and dumps all Property records to "
        "'property_backup.json'. Switch DATABASE_URL to the target "
        "database, then run 'loaddata property_backup.json' to restore."
    )

    def handle(self, *args, **options):
        # Step 1: Apply all pending migrations to the connected database.
        self.stdout.write("Running migrations...")
        call_command("migrate", verbosity=1, stdout=self.stdout, stderr=self.stderr)
        self.stdout.write(self.style.SUCCESS("Migrations applied successfully."))

        # Step 2: Dump all Property records to a JSON fixture file.
        output_file = "property_backup.json"
        self.stdout.write(f"Dumping Property data to '{output_file}'...")
        with open(output_file, "w") as f:
            call_command(
                "dumpdata",
                "listings.Property",
                indent=2,
                stdout=f,
                stderr=self.stderr,
            )
        self.stdout.write(
            self.style.SUCCESS(
                f"Property data exported to '{output_file}' successfully."
            )
        )

        self.stdout.write(
            self.style.WARNING(
                "\nNext steps:\n"
                "  1. Switch DATABASE_URL to the Postgres-UIwj database.\n"
                "  2. Run: python manage.py migrate\n"
                "  3. Run: python manage.py loaddata property_backup.json"
            )
        )
