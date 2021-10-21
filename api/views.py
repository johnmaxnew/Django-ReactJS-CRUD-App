from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            "xyz": "xyz",
            "abc": "abc"
        }
    ]
    return Response(routes)