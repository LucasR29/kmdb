from django.core.management.base import BaseCommand, CommandError
from users.models import User


class Command(BaseCommand):
    help = "Create admin"

    def add_arguments(self, parser) -> None:
        parser.add_argument("-u", "--username", type=str, help="Set admin username")
        parser.add_argument("-p", "--password", type=str, help="Set admin password")
        parser.add_argument("-e", "--email", type=str, help="Set admin email")

    def handle(self, *args, **kwargs):
        username = kwargs["username"] or "admin"
        password = kwargs["password"] or "admin1234"
        email = kwargs["email"] or "admin@example.com"

        email_exist = User.objects.filter(email=email)
        username_exists = User.objects.filter(username=username)

        if username_exists.exists():
            raise CommandError("Username `%s` already taken." % username)

        if email_exist.exists():
            raise CommandError("Email `%s` already taken." % email)

        user = User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
            is_critic=True,
            is_staff=True,
        )

        self.stdout.write(
            self.style.SUCCESS("Admin `%s` successfully created!" % username)
        )
