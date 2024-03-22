from django.core.signing import TimestampSigner
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import AppointmentTable
from .serializers import AppointmentSerializer
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
@api_view(['POST'])
def create_appointment(request):
    # Extract data from the request
    data = request.data
    # Generate a random ID
    signer = TimestampSigner()
    id_randomly = signer.sign('random_id')  # You can replace 'random_id' with any unique identifier
    # Add the random ID to the data
    data['idRandomly'] = id_randomly
    print(id_randomly)
    # Serialize the data
    print(data)
    serializer = AppointmentSerializer(data=data)
    print(serializer)
    print(serializer.fields['email'].error_messages)
    if serializer.is_valid():
        # Save the appointment without selectedDate and selectedTime
        serializer.save()

        # Send email to the provided address
        send_mail(
            'Appointment Created',
            f'Your appointment has been successfully created. Click the link below to access: http://localhost:5173/recipient/{id_randomly}',
            'oussama.elamraoui99@gmail.com',  # Sender's email address
            [data['email']],  # Recipient's email address
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def retrieve_appointment(request):
    id_randomly = request.query_params.get('idRandomly', None)
    if id_randomly is not None:
        try:
            appointment = AppointmentTable.objects.get(idRandomly=id_randomly)
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AppointmentTable.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "idRandomly parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def update_appointment(request):
    id_randomly = request.data.get('idRandomly')
    new_selected_date = request.data.get('NewSelectedDate')
    new_selected_time = request.data.get('NewSelectedTime')

    if not (id_randomly and new_selected_date and new_selected_time):
        return Response({"error": "idRandomly, NewSelectedDate, and NewSelectedTime are required fields"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        appointment = AppointmentTable.objects.get(idRandomly=id_randomly)
    except AppointmentTable.DoesNotExist:
        return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)

    appointment.selectedDate = new_selected_date
    appointment.selectedTime = new_selected_time
    appointment.save()

    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data, status=status.HTTP_200_OK)
