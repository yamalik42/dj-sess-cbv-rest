from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from .models import Author, AuthorForm
import json
import pdb


# Create your views here.
class AuthorView(FormMixin, ListView):
    model = Author
    template_name = 'crud/authors.html'
    form_class = AuthorForm
    success_url = '/author'

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            print(request.POST)
            AuthorForm(request.POST).save()
            return self.form_valid(form)
        else:
            return HttpResponse('Bad Form Input(s)')

    def delete(self, request, _id):
        Author.objects.filter(id=_id).delete()
        return HttpResponse()

    def put(self, request, _id):
        a = Author.objects.get(id=_id)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        a.first_name = body['first_name']
        a.last_name = body['last_name']
        a.save()
        return HttpResponse()


def session_prac(request):
    request.session['visits'] = request.session.get('visits', 0) + 1
    count = request.session['visits']
    rspn_str = f'You have visited this site {count} time(s).'

    request.session.set_expiry(300)

    return HttpResponse(rspn_str)
