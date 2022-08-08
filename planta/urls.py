from django.urls import path

from . import views

app_name= "planta"
urlpatterns = [
    path('', views.index, name = "index"),
    path('saludo/', views.saludar, name = "saludo"),
    path('saludo-especial/<str:dato>', views.saludoEspecial, name = "especial"),
    path('mul/<int:num>', views.multiplicacion, name = "mul"),
    path('sum/<int:sum1>/<int:sum2>/', views.suma, name = "sum"),
    path('login-Formulario/', views.loginFormulario, name = "loginFormulario"),
    path('login/', views.login, name = "login"),
    path('sumar-Formulario/', views.sumaFormulario, name = "sumarFormulario"),
    path('suma/', views.sumar, name = "sumar"),




]