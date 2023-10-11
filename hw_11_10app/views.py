from django.shortcuts import render
from django.http import JsonResponse

def generate_data(request):
    data = [i for i in range(1,11)]
    return JsonResponse({'data' : data})

