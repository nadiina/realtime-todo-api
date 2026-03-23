from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from todo_list.models import Task, Profile
from faker import Faker
import random

fake = Faker('uk_UA')


class Command(BaseCommand):
    help = 'Populate database with test data for To-Do List'

    def handle(self, *args, **options):
        self.stdout.write('Creating test data...')

        users = []
        for i in range(5):
            username = fake.user_name()
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    email=fake.email(),
                    username=username,
                    password='password123',
                    first_name=fake.first_name(),
                    last_name=fake.last_name()
                )
                Profile.objects.create(
                    user=user,
                    birth_date=fake.date_of_birth(minimum_age=18, maximum_age=60)
                )
                users.append(user)

        self.stdout.write(f'Created {len(users)} users.')

        if not users:
            users = list(User.objects.all())

        for i in range(10):
            Task.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.text(max_nb_chars=100),
                is_completed=random.choice([True, False]),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated database!'))