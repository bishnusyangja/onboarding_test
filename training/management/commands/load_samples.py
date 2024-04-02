from django.core.management.base import BaseCommand
from training.models import Activity, User, UserActivity
from model_bakery import baker


class Command(BaseCommand):
    help = 'Loads sample data'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample Data... ')

        abc = baker.make(User, first_name='ABC', last_name='Sharma', email='abc@example.com')

        writing = baker.make(Activity, name='Writing')
        reading = baker.make(Activity, name='Reading')
        discussion = baker.make(Activity, name='Discussion')
        baker.make(Activity, name='Game Play')
        baker.make(Activity, name='Writing and Speaking')
        baker.make(Activity, name='Reading and Speaking')

        self.stdout.write('Activity loading sucessful... ')

        baker.make(UserActivity, activity=writing, user=abc)
        baker.make(UserActivity, activity=reading, user=abc)
        baker.make(UserActivity, activity=discussion, user=abc)
        self.stdout.write('UserActivity loading sucessful... ')



        # self.stdout.write('options :', options)