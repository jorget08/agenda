from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, # Equivalente al detailview
    DestroyAPIView, # Equivalente a deleteview
    UpdateAPIView,
    RetrieveUpdateAPIView
    )

from .models import Person, Reunion, Hobby
from .serializers import (PersonSerializer, PersonSerializer2, PersonaSerializer, 
                          ReunionSerializer, PersonSerializer3,ReunionSerializer2,
                          ReunionSerializerLink, PersonPagination, CountReunionSerializer)


class ListaListView(ListView):
    template_name = "persona/listar_personas.html"

    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()


#REST
class PersonListAPIView(ListAPIView):

    # convertirmos la lista en JSON (ese proceso se le llama serializar), es tomar el valor (Person.objects.all())
    # y transformarlo en un JSON, lo mismo al revez, de JSON a valores que podamos mostrar
    serializer_class = PersonSerializer


    def get_queryset(self):
        return Person.objects.all()



class ListUsingVueExample(TemplateView):
    template_name = 'persona/lista.html'




class PersonSearchApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):

        # filtrando datos por urls

        palabra_clave = self.kwargs['kword']
        return Person.objects.filter(full_name__icontains=palabra_clave)



class PersonCreateView(CreateAPIView):

    serializer_class = PersonSerializer2


class PersonRDetailView(RetrieveAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.filter()


class PersonDeleteView(DestroyAPIView):

    serializer_class = PersonSerializer2
    queryset = Person.objects.all()


"""Con esta vista se esta obligado a actualizar todos los campos y no solo el que uno quiera"""
class PersonUpdateView(UpdateAPIView):

    serializer_class = PersonSerializer2
    queryset = Person.objects.all()


"""Con esta vista podemos actualizar el campo que queramos ademas de que nos muestra que valor tiene ese campo"""
class PersonRetriveUpdateView(RetrieveUpdateAPIView):

    serializer_class = PersonSerializer2
    queryset = Person.objects.all()


"""Mismo listado de personas solo que con serilizadores sin un modelo definido"""
class PersonApiLista(ListAPIView):

    serializer_class = PersonaSerializer
    queryset = Person.objects.all()


class PersonListAll(ListAPIView):

    serializer_class = PersonSerializer2
    queryset = Person.objects.all()


class ReunionApiList(ListAPIView):

    serializer_class = ReunionSerializer
    queryset = Reunion.objects.all()


class PersonaApiList2(ListAPIView):
    serializer_class = PersonSerializer3
    queryset = Person.objects.all()


class ReunionApiList2(ListAPIView):
    serializer_class = ReunionSerializer2
    queryset = Reunion.objects.all()



class ReunionApiLink(ListAPIView):
    serializer_class = ReunionSerializerLink
    queryset = Reunion.objects.all()


class PersonPaginateList(ListAPIView):

    serializer_class = PersonSerializer3
    pagination_class = PersonPagination
    queryset = Person.objects.all()



class ReunionByJobs(ListAPIView):

    #Como en el manager pusimos una variable cantidad y el persona__job no podemos usar el serializador normal trae todo
    #sobre el objeto pues el resultado de la busqueda del manager nos trae es el nombre del job y la cantidad
    #osea nos trae esos 2 campos que no esta n en el modelo; asi que creamos el serializador sin modelo de lo que va a mostrar
    serializer_class = CountReunionSerializer

    
    queryset = Reunion.objects.cantidad_reuniones_job()