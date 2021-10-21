from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse


def getRoutes(request):
    return JsonResponse(' API', safe=False)