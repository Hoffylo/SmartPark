from django.db import models

# Modelo para la tabla 'users'
class User(models.Model):
    rut = models.CharField(max_length=100, primary_key=True)
    id_user = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=11)
    tipo_user = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Modelo para la tabla 'vehiculos'
class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    rut = models.ForeignKey(User, on_delete=models.CASCADE, to_field='rut')  # Relación con 'User'
    placa = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"


# Modelo para la tabla 'estacionamientos'
class Estacionamiento(models.Model):
    id_estacionamiento = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=100)
    capacidad_total = models.IntegerField()
    espacios_disponibles = models.IntegerField()
    tarifa_hora = models.IntegerField()
    horario_apertura = models.TimeField()
    hora_cierre = models.TimeField()

    def __str__(self):
        return self.ubicacion


# Modelo para la tabla 'reserva'
class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    placa = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, to_field='placa')  # Relación con 'Vehiculo'
    rut = models.ForeignKey(User, on_delete=models.CASCADE, to_field='rut')  # Relación con 'User'
    id_estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)  # Relación con 'Estacionamiento'
    espacio_reservado = models.IntegerField()
    hora_entrada = models.DateTimeField()
    hora_salida = models.DateTimeField()
    estado_reserva = models.CharField(max_length=100)

    def __str__(self):
        return f"Reserva {self.id_reserva} - Usuario {self.rut}"


# Modelo para la tabla 'pagos'
class Pago(models.Model):
    id_pago = models.CharField(max_length=10, primary_key=True)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)  # Relación con 'Reserva'
    monto_reserva = models.IntegerField()
    fecha_pago = models.DateTimeField()
    id_comprobante = models.CharField(max_length=50)
    tipo_comprobante = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    estado_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Pago {self.id_pago} - {self.monto_reserva}"


# Modelo para la tabla 'espacios'
class Espacio(models.Model):
    id_espacio = models.AutoField(primary_key=True)
    id_estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)  # Relación con 'Estacionamiento'
    numero_espacio = models.CharField(max_length=10)
    piso = models.IntegerField()
    tipo_espacio = models.CharField(max_length=100)
    ocupado = models.BooleanField(default=False)
    sensor_id = models.IntegerField()

    def __str__(self):
        return f"Espacio {self.numero_espacio} - Piso {self.piso}"
