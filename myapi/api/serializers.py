from rest_framework import serializers
from PIL import Image
from io import BytesIO

from api.models import person,person_media,person_media_type,person_type,person_audit
import base64


def image_to_b64(image_received):
    image = Image.open(image_received)
    image = image.resize((128,128), Image.ANTIALIAS)
    buffered = BytesIO()
    image.save(buffered, format='JPEG')
    return base64.b64encode(buffered.getvalue())

class person_serializer(serializers.ModelSerializer):
    class Meta:
        model = person
        # fields = '__all__'
        exclude = ['last_update']
    
    


class person_type_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)

    def create(self, v_data):
        # Cria com base no post
        
        person_type_obj = person_type.objects.create(**v_data)
        return person_type_obj
        


class person_media_type_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    # id 1 = Foto, id 2 = Biometria
    content = serializers.IntegerField()

class person_media_serializer(serializers.ModelSerializer):
    object_media = serializers.ImageField()
    
    class Meta:
        model = person_media
        fields = '__all__'
    
    
    def create(self,v_data):
        imb64 = image_to_b64(v_data['object_media'])
        person_media_obj = person_media.objects.create(person_id=v_data['person_id'],object_media = imb64)
        return person_media_obj
    

    


class person_audit_serializer(serializers.ModelSerializer):
    # person_id = serializers.IntegerField(read_only=True)
    # # type = 1 (add) type = 2 (update)
    # person_audit_type = serializers.IntegerField()
    # cpf_new = serializers.CharField(read_only=True)
    # cpf_old = serializers.CharField(read_only=True)
    # last_update = serializers.DateTimeField()

    class Meta:
        model = person_audit
        fields = '__all__'