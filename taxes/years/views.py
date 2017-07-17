# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

# make a form to create a new object and editing it
# from django.views.generic.edit import CreateView, UpdateView, DeleteView

# this will redirect to whatever link you make it redirect too
from django.core.urlresolvers import reverse_lazy

from .models import Year2013


# generic view
class IndexView(generic.ListView):
    template_name = 'years/index.html'
    context_object_name = 'year2013'

    def get_queryset(self):
        return Year2013.objects.all()


# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.shortcuts import render
#
# # Create your views here.
#
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
