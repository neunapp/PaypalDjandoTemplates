from django.contrib import admin
from django.urls import path
from applications.tienda.views import (
    PayView, 
    HomeView, 
    CrearOrden,
    CapturarOdernPaypal
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('pay/', PayView.as_view(), name='pay-paypal'),
    path('api/orders', CrearOrden.as_view(),),
    path('api/orders/<order_id>/capture', CapturarOdernPaypal.as_view(),),
]
