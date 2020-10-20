# Create your views here.
from django.shortcuts import redirect


def blog(request):
    return redirect("/blog/")
