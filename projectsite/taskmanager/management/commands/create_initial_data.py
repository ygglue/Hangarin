from django.core.management.base import BaseCommand
import Faker
from taskmanager.models import Task, SubTask, Category, Priority, Note

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_task(10)
        self.create_note(10)
        self.create_subtask(10)

    def create_task(self, count):
        fake = Faker('en_PH')
        for _ in range(count):
            Task.objects.create(
                title = fake.sentence(nb_words = 5),
                description = fake.paragraph(nb_sentences = 3),

            )
        self.stdout.write(self.style.SUCCESS('Initial data for students created successfully.'))

    def create_note(self, count):
        fake = Faker()

        for _ in range(count):
            Note.objects.create(
                content=fake.sentence(nb_words = 5)
            )

        self.stdout.write(self.style.SUCCESS(
        'Initial data for Note created successfully.'))


    def create_subtask(self, count):
        fake = Faker()
        for _ in range(count):
            OrgMember.objects.create(
                student=Student.objects.order_by('?').first(),
                organization=Organization.objects.order_by('?').first(),
                date_joined=fake.date_between(start_date="-2y", end_date="today")
            )
        self.stdout.write(self.style.SUCCESS('Initial data for student organization created successfully.'))