
# from .serializer import stickStickStickNoteSerializer
# from .models import StickNote
# from rest_framework import generics

# #! ------------------------------  pomodoro --------------- ##
# class list_create_sticknote(generics.ListCreateAPIView):
#     queryset = StickNote.objects.all()
#     serializer_class = stickStickNoteSerializer  


# class update_delete_retreive_sticknote(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StickNote.objects.all()
#     serializer_class =stickStickNoteSerializer

from .serializer import StickNoteSerializer
from .models import StickNote
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status

# Create your views here. admin
class NoteList(generics.ListAPIView):
    queryset = StickNote.objects.all()
    serializer_class = StickNoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

class StickNoteCreate(generics.CreateAPIView):
    queryset = StickNote.objects.all()
    serializer_class = StickNoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StickNoteDetail(generics.RetrieveAPIView):
    queryset = StickNote.objects.all()
    serializer_class = StickNoteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def UserList(request):
    user_StickNotes = StickNote.objects.filter(owner=request.user)
    serializer = StickNoteSerializer(user_StickNotes, many=True)
    return Response(serializer.data)



@api_view(['GET','PUT','DELETE'])
def UserDetail(request, pk):
    try:
        user_StickNotes = StickNote.objects.filter(owner=request.user,pk=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    # GET
    if request.method == 'GET':
        serializer = StickNoteSerializer(user_StickNotes, many=True)
        return Response(serializer.data)

    # PUT
    elif request.method == 'PUT':
        serializer = StickNoteSerializer(user_StickNotes, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        user_StickNotes.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

