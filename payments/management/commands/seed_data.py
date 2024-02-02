from django.core.management.base import BaseCommand
from faker import Faker

from payments.models import Requisite, PaymentType, SourceType, Payment, PaymentStatus

fake = Faker()


class Command(BaseCommand):
    help = 'Seed the database with test data'

    def handle(self, *args, **kwargs):
        for _ in range(100):
            Requisite.objects.create(
                payment_type=fake.random_element(elements=[pt.value for pt in PaymentType]),
                source_type=fake.random_element(elements=[st.value for st in SourceType]),
                full_name=fake.name(),
                phone=fake.phone_number(),
                limit=fake.random_number(),
            )

        for _ in range(5000):
            Payment.objects.create(
                amount=fake.random_number(),
                requisites=fake.random_element(elements=Requisite.objects.all()),
                status=fake.random_element(elements=[ps.value for ps in PaymentStatus]),
            )

        self.stdout.write(self.style.SUCCESS('Data seeding complete'))
