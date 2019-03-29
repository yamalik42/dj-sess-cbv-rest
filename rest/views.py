from django.shortcuts import render
from .models import Question, Choice
from rest_framework import generics
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import permissions


class IsQuestionOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        def for_questions():
            q_to_del = Question.objects.get(pk=view.kwargs['pk'])
            return q_to_del.owner == request.user

        def for_choices():
            if request.method == 'POST':
                q_pk = request.data['question']
                q_to_choice = Question.objects.get(pk=q_pk)
                return q_to_choice.owner == request.user

            q_pk = Choice.objects.get(pk=view.kwargs['pk']).question.pk
            q_to_mod = Question.objects.get(pk=q_pk)
            return q_to_mod.owner == request.user

        give_perms = {
            'QuestionDetail': for_questions,
            'ChoiceList': for_choices,
            'ChoiceDetail': for_choices
        }

        view_class = view.__class__.__name__

        return give_perms[view_class]()


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        quest = serializer.save()
        quest.owner = self.request.user
        quest.save()


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsQuestionOwner | ReadOnly,)


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = (ReadOnly | IsQuestionOwner,)


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = (IsQuestionOwner | ReadOnly,)
