from django.urls import path
from main import views
urlpatterns = [
    path('', views.Index),
    path('secure/',views.sshh, name='sshh')

]