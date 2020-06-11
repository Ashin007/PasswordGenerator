from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, "generator/home.html")


def generated_password(request):
    gen_password = ""
    length = int(request.GET.get('length'))
    alpha_char = list('abcdefhijklmnpqrstuvwxyz')
    if request.GET.get('uppercase'):
        alpha_char.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get('special'):
        alpha_char.extend("!@#$%^&*()")
    if request.GET.get('numbers'):
        alpha_char.extend("1234567890")
    for pas in range(length):
        gen_password += random.choice(alpha_char)
    return render(request, "generator/generated_password.html", {"password":gen_password})
