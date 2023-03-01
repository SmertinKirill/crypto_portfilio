import contextlib
import csv

from django.core.management import BaseCommand

from models import Crypto

Crypto.objects.all().delete()
# class Command(BaseCommand):
#     """
#     Reads csv files, creates objects from data, very basic
#     """
#     def handle(self, *args, **options):

#         p = 'static/data/'

#         with contextlib.ExitStack() as stack:
#             cryptoes = csv.DictReader(
#                 stack.enter_context(open(f'{p}crypto.csv', 'r'))
#             )

#             for row in cryptoes:
#                 Crypto.objects.get_or_create(
#                     id=int(row['id']),
#                     tag=row['tag'],
#                     name=row['name']
#                 )
