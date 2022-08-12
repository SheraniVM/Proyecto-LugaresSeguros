from rest_framework import serializers
from places.models import Place #De places se trae Place
from comments.models import Comment
from comments.serializers import CommentPlaceListSerializer

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class PlaceListCommentSerializer(serializers.ModelSerializer):
    #tiene que tener el mismo nombre que el atributo que queremos traer a nuestro serializador
    comment = serializers.SerializerMethodField()

    class Meta: 
        model = Place
        fields = (
            'id', 
            'name',
            'comment',
        )

    def get_comment(self, obj):
        selected_comment = Comment.objects.filter(place__id = obj.id)
        return CommentPlaceListSerializer(selected_comment, many=True).data