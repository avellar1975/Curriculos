from django.urls import path
from curriculos.base.views import home, consultar, cadastrar, alterar


app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('consultar', consultar, name='consultar'),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('alterar', alterar, name='alterar'),

]
