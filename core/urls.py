from django.urls import path
from core import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    
    path('users/', views.UserListCreate.as_view(), name='user-list'),
    path('users/<str:pk>/', views.UserRetrieveUpdateDestroy.as_view(), name='user-detail'),

    path('vehiculos/', views.VehiculoListCreate.as_view(), name='vehiculo-list'),
    path('vehiculos/<int:pk>/', views.VehiculoRetrieveUpdateDestroy.as_view(), name='vehiculo-detail'),

    path('estacionamientos/', views.EstacionamientoListCreate.as_view(), name='estacionamiento-list'),
    path('estacionamientos/<int:pk>/', views.EstacionamientoRetrieveUpdateDestroy.as_view(), name='estacionamiento-detail'),

    path('reservas/', views.ReservaListCreate.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', views.ReservaRetrieveUpdateDestroy.as_view(), name='reserva-detail'),

    path('pagos/', views.PagoListCreate.as_view(), name='pago-list'),
    path('pagos/<str:pk>/', views.PagoRetrieveUpdateDestroy.as_view(), name='pago-detail'),

    path('espacios/', views.EspacioListCreate.as_view(), name='espacio-list'),
    path('espacios/<int:pk>/', views.EspacioRetrieveUpdateDestroy.as_view(), name='espacio-detail'),
]
