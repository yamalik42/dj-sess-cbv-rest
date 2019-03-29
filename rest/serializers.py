from rest_framework import serializers
from .models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'owner')


class ChoiceSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
            many=False,
            queryset=Question.objects.all()
        )

    class Meta:
        model = Choice
        fields = ('question', 'choice_text', 'votes')
