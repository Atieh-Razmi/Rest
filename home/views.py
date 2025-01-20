from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializer import PersonSerilizer, QuestionSerilizer, AnswerSerilizer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from permissions import IsOwnerORreadOnly
# Create your views here.

class HomeView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerilizer(instance=persons, many=True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerilizer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)
    
    
class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        srz_data = QuestionSerilizer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerORreadOnly]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = QuestionSerilizer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerORreadOnly]
    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response({'message':'question deleted'}, status=status.HTTP_200_OK)
