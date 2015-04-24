from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from annotations.models import Annotation
from annotations.serializers import AnnotationSerializer
from .forms import AnnotationForm

def annotation_form(request):
    form = AnnotationForm()
    return render(request, 'annotations/form.html', { 'form' : form })

@api_view(['GET', 'POST'])
def annotation_list(request, format=None):
    """
    List all annotations
    """

    if request.method == 'GET':
        list = Annotation.objects.all()
        serializer = AnnotationSerializer(list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AnnotationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def annotation_detail(request, pk, format=None):
    """
    Retrieve, update or delete a annotation instance.
    """
    try:
        annotation = Annotation.objects.get(pk=pk)
    except Annotation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnnotationSerializer(annotation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AnnotationSerializer(annotation, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        annotation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def annotation_next(request, pk, format=None):
    """
    Retrieve, next annotation or false
    """
    try:
        annotation = Annotation.objects.get(pk=pk)
        try:
            next = Annotation.objects.filter(start_time__gt=annotation.start_time)[0]
            serializer = AnnotationSerializer(next)
            return Response(serializer.data)
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Annotation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def annotation_prev(request, pk, format=None):
    """
    Retrieve, next annotation or false
    """
    try:
        annotation = Annotation.objects.get(pk=pk)
        try:
            prev = Annotation.objects.filter(start_time__lt=annotation.start_time)[0]
            serializer = AnnotationSerializer(prev)
            return Response(serializer.data)
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Annotation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


