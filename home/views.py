from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerilizer
# Create your views here.

class HomeView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerilizer(instance=persons, many=True)
        return Response(data=ser_data.data)
   