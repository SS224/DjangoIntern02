from django.contrib import admin
from django.urls import path
from appOne import views as v1
from appTwo import views as v2
from appThree import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', v1.d1),
    path('hi/', v1.d2),
    path('hey/', v1.d3),
    path('hellotwo/', v2.d1),
    path('hellothree/', v3.d1)
]
