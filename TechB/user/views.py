from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usermodel
from .serializers import UserSerializer

@api_view(['GET', 'POST'])
def Addtask(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        tasks = Usermodel.objects.all()
        serializer = UserSerializer(tasks, many=True)
        return JsonResponse({'tasks': serializer.data}, safe=False)
