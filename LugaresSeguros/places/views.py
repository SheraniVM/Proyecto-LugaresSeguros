from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from places.models import Place
from places.serializers import PlaceSerializer

class PlaceView(APIView):
    def get(self, request):

        '''QuerySet -> Resultado de una Query. Lista de objetos.'''
        places = Place.objects.all()
        #print(places)
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class PlaceSingleView(APIView):
    '''def put(self, request, id):
        place = Place.objects.get(id=id)
        serializer = PlaceSerializer(place, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)'''

    def patch(sekf, request, id):
        place = Place.objects.filter(id=id).first()
        if place is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PlaceSerializer(place, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    '''def delete(self, request, id):
        place = Place.objects.get(id=id)
        place.delete()
        return Response({"message":"Lugar eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)'''

    def delete(self, request, id):
        place = Place.objects.filter(id=id).first()
        if place is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        place.delete()
        return Response({'message': 'Lugar eliminado satisfactoriamente'}, status=status.HTTP_200_OK)



