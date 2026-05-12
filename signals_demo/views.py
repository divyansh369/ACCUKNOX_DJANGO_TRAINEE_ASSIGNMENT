import threading
import time

from django.db import transaction
from django.http import HttpResponse

from .models import MyModel


def test_signal(request):

    print(f"\nCaller Thread ID: {threading.get_ident()}")

    start_time = time.time()

    try:

        with transaction.atomic():

            MyModel.objects.create(name="Divyansh")

    except Exception as e:

        print(f"\nException Raised: {e}")

    end_time = time.time()

    print(f"\nTotal Time Taken: {end_time - start_time}")

    return HttpResponse("Transaction Test Completed")