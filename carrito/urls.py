from django.conf.urls import url

from .views import carrito_detail, carrito_add, carrito_remove

urlpatterns = [
    url(r'^$', carrito_detail, name = 'carrito_detail'),
    url(r'^add/(?P<producto_id>\d+)$', carrito_add, name = 'carrito_add'),
    url(r'^remove/(?P<producto_id>\d+)$', carrito_remove, name = 'carrito_remove')
]