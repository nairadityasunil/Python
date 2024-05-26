from django.shortcuts import render
from django.http import HttpResponse
import math
# Create your views here.

def fact(request, n):
    result = math.factorial(n)
    return HttpResponse("Factorial : "+str(result))
