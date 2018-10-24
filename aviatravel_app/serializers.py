from aviatravel_app.models import TravelTicket
from rest_framework import  serializers


class TicketsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TravelTicket
        fields = '__all__'  
        