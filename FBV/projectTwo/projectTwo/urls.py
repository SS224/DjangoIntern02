from django.contrib import admin
from django.urls import path
from appOne import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getProducts),
    path('product/update/<int:id>', views.updateProduct)
]
