from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from demo.tasks import execute_long_work


def base_view(request):

    print('GET call')

    print('Inserting into queue')
    async_id = execute_long_work.delay('Dummy message')
    print(async_id)

    return HttpResponse("Here's the text of the Web page.")
