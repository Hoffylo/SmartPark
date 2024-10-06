from rest_framework import generics
from .models import User, Vehiculo, Estacionamiento, Reserva, Pago, Espacio
from .serializers import UserSerializer, VehiculoSerializer, EstacionamientoSerializer, ReservaSerializer, PagoSerializer, EspacioSerializer
from django.http import JsonResponse

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VehiculoListCreate(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class VehiculoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class EstacionamientoListCreate(generics.ListCreateAPIView):
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer

class EstacionamientoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer

class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class PagoListCreate(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class EspacioListCreate(generics.ListCreateAPIView):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer

class EspacioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer




def api_root(request):
    return JsonResponse({
        'message': 'Bienvenido a la API de SmartPark',
        'endpoints': {
            'users': '/api/users/',
            'vehiculos': '/api/vehiculos/',
            'estacionamientos': '/api/estacionamientos/',
            'reservas': '/api/reservas/',
            'pagos': '/api/pagos/',
            'espacios': '/api/espacios/',
        }
    })
