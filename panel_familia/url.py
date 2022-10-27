from django.urls import URLPattern, path
from panel_familia.views import FamiliarActualizar, FamiliarBorrar, FamiliarCrear,FamiliarList

urlpatterns = [
    path('', FamiliarList.as_view(), name = "familiar-list"), 
    path('crear', FamiliarCrear.as_view(),name = "familiar-crear"),
    path('<int:pk>/borrar', FamiliarBorrar.as_view(),name = "familiar-borrar"),
    path('<int:pk>/actualizar', FamiliarActualizar.as_view(),name = "familiar-Actualizado"),
]