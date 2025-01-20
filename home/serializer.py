from rest_framework import serializers
from .models import Question, Answer


class PersonSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()


class QuestionSerilizer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, obj):
        result = obj.answers.all()
        return AnswerSerilizer(instance=result, many=True).data



class AnswerSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'




