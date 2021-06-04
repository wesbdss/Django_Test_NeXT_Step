from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import * 

# from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
import json
from django.utils import timezone
from api.models import person, person_media, person_media_type, person_type, person_audit

from PIL import Image

import base64


def cpf_validade(numbers):
    cpf = [int(d) for d in numbers if d.isdigit()]
    if len(cpf) != 11:
        return False
    if cpf == cpf[::-1]:
        return False
    
    for i in range(9,11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


# Create your views here.

class PersonList(viewsets.ModelViewSet):
    """
        Lista as all persons
    """
    queryset = person.objects.all()
    serializer_class = person_serializer
    # def get(self, request, format=None):
    #     persons = person.objects.all()
    #     serializer = person_serializer(persons, many=True)
    #     return Response(serializer.data)
    def create(self, request, format=None):
        if (not cpf_validade(request.POST['cpf'])):
            return Response("Cpf Inválido")
        serializer = person_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk ,format=None):
        if (not cpf_validade(request.POST['cpf'])):
            return Response("Cpf Inválido")
        person_obj = person.objects.get(pk=pk)
        if person_obj != None:
            person_obj.name = request.POST['name']
            person_obj.cpf= request.POST['cpf']
            person_obj.phone= request.POST['phone']
            person_obj.last_update= timezone.now()
            person_type_obj = person_type.objects.get(pk=request.POST['person_type'])
            person_obj.person_type= person_type_obj
            person_obj.save()
            return Response("updated", status = status.HTTP_204_NO_CONTENT)
        return Response("Erro update", status = status.HTTP_400_BAD_REQUEST)

        

class Person_mediaList(viewsets.ModelViewSet):
    """
        Lista as all person_media
    """
    queryset = person_media.objects.all()
    serializer_class = person_media_serializer

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.name = request.data.get("name")
    #     instance.save()

    #     serializer = self.get_serializer(instance)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = person_media_serializer(data = request.data)
    #     if serializer.is_valid():
    #         person_media.objects.create()
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Person_typeList(viewsets.ModelViewSet):
    """
        Lista as all person_type
    """
    queryset = person_type.objects.all()
    serializer_class = person_type_serializer


class Person_media_typeList(viewsets.ModelViewSet):
    """
        Lista as all person_media
    """
    queryset = person_media_type.objects.all()
    serializer_class = person_media_type_serializer

class Person_auditList(viewsets.ModelViewSet):
    """
        Lista as all person_audit
    """
    queryset = person_audit.objects.all()
    serializer_class = person_audit_serializer