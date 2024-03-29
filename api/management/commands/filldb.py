import contextlib
import csv

from django.core.management import BaseCommand

from portfolio.models import Crypto


class Command(BaseCommand):
    """
    Reads csv files, creates objects from data, very basic
    """
    def handle(self, *args, **options):

        p = 'data/'

        with contextlib.ExitStack() as stack:
            cryptoes = csv.DictReader(
                stack.enter_context(open(f'{p}crypto.csv', 'r'))
            )

            for row in cryptoes:
                Crypto.objects.get_or_create(
                    id=int(row['id']),
                    tag=row['tag'],
                    name=row['name']
                )
