import random

from django.core.management import BaseCommand

from books.models import Country, Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        ukraine = Country.objects.create(name="Ukraine")
        poland = Country.objects.create(name="Poland")
        germany = Country.objects.create(name="Germany")

        countries = [ukraine, poland, germany]

        for book in Book.objects.all():
            country = random.choice(countries)

            book.country = country
            book.save()
