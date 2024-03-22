from django.db import models

class AppointmentTable(models.Model):
    idRandomly = models.CharField(max_length=255)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    startDate = models.DateField()
    endDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    selectedDate = models.DateField()
    selectedTime = models.TimeField()
    def __str__(self):
        return f"Appointment ID: {self.idRandomly}"

