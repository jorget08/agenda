from django.urls import path

from . import views

app_name = 'persona'

urlpatterns = [
    path(
        route = 'personas/',
        view = views.ListaListView.as_view(),
        name = 'lista'
    ),
    path(
        route = 'api/persona/lista/',
        view = views.PersonListAPIView.as_view(),
        name = 'lista_api'
    ),
    path(
        route = 'lista/vue',
        view = views.ListUsingVueExample.as_view(),
        name = 'lista_vue'
    ),
    path(
        route = 'api/persona/search/<kword>',
        view = views.PersonSearchApiView.as_view(),
        name = 'lista_vue'
    ),
    path(
        route = 'api/persona/create',
        view = views.PersonCreateView.as_view(),
        name = 'create'
    ),
    path(
        route = 'api/persona/detail/<pk>',
        view = views.PersonRDetailView.as_view(),
        name = 'detail'
    ),
    path(
        route = 'api/persona/delete/<pk>',
        view = views.PersonDeleteView.as_view(),
        name = 'delete'
    ),
    path(
        route = 'api/persona/update/<pk>',
        view = views.PersonUpdateView.as_view(),
        name = 'update'
    ),
    path(
        route = 'api/persona/update2/<pk>',
        view = views.PersonRetriveUpdateView.as_view(),
        name = 'update2'
    ),
    path(
        route = 'api/personas',
        view = views.PersonApiLista.as_view(),
        name = 'lista-personas'
    ),
    path(
        route = 'api/listado',
        view = views.PersonListAll.as_view(),
        name = 'lista-personas-all'
    ),
    path(
        route = 'api/reuniones',
        view = views.ReunionApiList.as_view(),
        name = 'lista-reuniones'
    ),
    path(
        route = 'api/persona2',
        view = views.PersonaApiList2.as_view(),
        name = 'lista-personas2'
    ),
    path(
        route = 'api/reuniones2',
        view = views.ReunionApiList2.as_view(),
        name = 'lista-reuniones2'
    ),

    path(
        route = 'api/reuniones/link',
        view = views.ReunionApiLink.as_view(),
        name = 'lista-reuniones-link'
    ),

    path(
        route = 'api/persona/paginacion',
        view = views.PersonPaginateList.as_view(),
        name = 'lista-persona-paginacion'
    ),

    path(
        route = 'api/reunion/job',
        view = views.ReunionByJobs.as_view(),
        name = 'conteo-job'
    ),
]
