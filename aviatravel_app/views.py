from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.views.generic.list import ListView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from aviatravel_app.serializers import TicketsSerializer
from aviatravel_app.models import(
		TravelTicket,
		Country,
		City,
		Images,
		Category,
	)



class VaucherListView(ListView):
	model = TravelTicket
	
	def get(self,  request, *args, **kwargs):
		all_pro = self.model.objects.all()
		data = TicketsSerializer(all_pro, many=True).data
		return render(request,'body.html', {'articles': data})
"""

class VaucherJsonListView(ListView):
	model = TravelTicket
	
	def get(self,  request, *args, **kwargs):
		all_pro = self.model.objects.all()
		data = TicketsSerializer(all_pro, many=True).data
		print({'articles': data})
		return HttpResponse(data, content_type="application/json")
"""		
# list all db bjects
class VaucherApiListView(APIView):

	def get(self, request):
		ticket = TravelTicket.objects.all()
		serialiser = TicketsSerializer(ticket, many=True)
		print(serialiser.data)
		return Response(serialiser.data)

	#def post(self):
	#	pass




















