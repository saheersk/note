from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.v1.actions.serializers import NoteSerializer
from web.models import Note


@api_view(['GET'])
def actions(request):
    
    instances = Note.objects.all()

    context = {
        "request": request
    }

    serializer = NoteSerializer(instances, many=True, context=context)

    response_data = {
        "status_code": status.HTTP_200_OK,
        "data": serializer.data,
    }

    return Response(response_data)


@api_view(["GET"])
def actions_read(request, pk):
    print("s")
    if Note.objects.filter(pk=pk).exists():
        instance = Note.objects.get(pk=pk)

        context = {
            "request": request
        }

        serializer = NoteSerializer(instance, context=context)
            
        response_data = {
            "status_code": status.HTTP_200_OK,
            "data": serializer.data,
        }     

        return Response(response_data)

    else:
        response_data = {
            "status_code": status.HTTP_200_OK,
            "message": "Note not exists",
        }

        return Response(response_data)
  

@api_view(["POST"])
def actions_post(request):
    data = request.data

    context = {
        "request": request,
    }

    serializer = NoteSerializer(data=data, context=context)

    if serializer.is_valid():
        serializer.save()

    response_data = {
        "status_code": status.HTTP_201_CREATED,
        "data": serializer.data,
        "message": "Created"
    }

    return Response(response_data)


@api_view(["PUT"])
def actions_update(request, pk):

    if Note.objects.filter(pk=pk).exists():
        instance = get_object_or_404(Note, pk=pk)
        data = request.data

        context = {
            "request": request
        }

        serializer = NoteSerializer(data=data, instance=instance, context=context)
                
        if serializer.is_valid():
            serializer.save()

        response_data = {
            "status_code": status.HTTP_201_CREATED,
            "data": serializer.data,
            "message": "Updated"
        }

        return Response(response_data) 

    else:
       response_data = {
            "status_code": status.HTTP_200_OK,
            "message": "Note not exists",
       }

       return Response(response_data)


@api_view(["DELETE"])
def actions_delete(request, pk): 

    if Note.objects.filter(pk=pk).exists():
        instance = get_object_or_404(Note, pk=pk)

        instance.delete()

        response_data = {
            "status_code": status.HTTP_202_ACCEPTED,
            "message": "Deleted"
        }   

        return Response(response_data)

    else:
        response_data = {
            "status_code": status.HTTP_200_OK,
            "message": "Note not exists",
        }
        return Response(response_data)