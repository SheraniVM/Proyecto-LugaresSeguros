from django.shortcuts import get_object_or_404 #is a 2 in 1 is not necessary to indicate an exception
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.

#We will hace only POST and DELETE

class CommentView(APIView):
    

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentSingleView(APIView):

    def patch(self, request, pk):
        comment = Comment.objects.filter(pk=pk).first()
        if comment is None:
            return Response({'error': 'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CommentSerializer(comment, data=request.data, partial=True) #1)Value of comment 2)Request data 3)Partial changes (explicit for serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        place = get_object_or_404(Comment, pk=pk)
        place.delete()
        return Response('Comentario eliminado', status=status.HTTP_204_NO_CONTENT)

