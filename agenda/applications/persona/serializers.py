from rest_framework import serializers, pagination

from .models import Person, Reunion, Hobby

# Puede trabajarse con modelo o sin modelo como los formularios que esta el Form y el ModelForm
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id', 'full_name', 'job', 'email',
        )


class PersonSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()

    # Si queremos añadir un campo que el objeto no tiene en el modelo para alguna necesidad que pueda surgir
    # solo debemos poner el campo y decir que no es requerido, asi si alguno tiene el campo lo mostrara y los que no 
    # pues no mostrara sino los campos del modelo
    activo = serializers.BooleanField(required=False)



class ReunionSerializer(serializers.ModelSerializer):
    # Para el ForeignKey, asi en el campo de persona nos muestra todo sobre la persona
    persona = PersonSerializer2()

    class Meta:
        model = Reunion
        fields = (
            'id', 'fecha', 'hora', 'asunto', 'persona'
        )



class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('__all__')



"""Puede ser con modelo o sin el modelserializer y poner los campos que va a tener y el orden de estos en que se va a mostrar"""
class PersonSerializer3(serializers.ModelSerializer):
    # Para los many to many
    hobbies = HobbySerializer(many=True)

    class Meta:
        model = Person
        fields = ('__all__')



class ReunionSerializer2(serializers.ModelSerializer):
    # Para el ForeignKey, asi en el campo de persona nos muestra todo sobre la persona
    persona = PersonSerializer2()

    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion

        # Puedo quitar de los fields la fecha y la hora si no quiere mostrarla pues ya las estoy mostrando juntas en el fecha_hora
        fields = (
            'id', 'fecha', 'hora', 'asunto', 'persona', 'fecha_hora'
        )

    def get_fecha_hora(self, obj):
        return str(obj.fecha) + ' - ' + str(obj.hora)



class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona'
        )

        # Para genernar el link con el que se va a acceder al detalle de ForeignKey, para no 
        # mostrar todo como hemos hecho antes pues si son muchos registros se ocuparia demasiado espacio
        extra_kwargs = {
            # El campo que va a tener el link; el nombre de la url que tiene la vista; mediente que atributo
            # se genera la url(en la vista detail esta -> api/persona/detail/<pk>) asi que el atributo aqui es por pk
            'persona': {'view_name': 'persona:detail', 'lookup_field': 'pk'}
        }



class PersonPagination(pagination.PageNumberPagination):
    #Cuantos va a mostrar por pagina
    page_size = 5

    #tamaño maximo que quiero que cargue en memoria
    max_page_size = 100



class CountReunionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()