from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib import messages

from .models import ListedPet
import json



class ListedPetListView(LoginRequiredMixin, ListView):
    model = ListedPet
    template_name = 'adtool/home.html'
    context_object_name = 'ListedPets'
    paginate_by = 6

    def get_queryset(self):
        if self.request.method == "GET":
            selected_value = int(self.request.GET.get('sort-by', 10))
            if selected_value == 10:
                return ListedPet.objects.filter(is_taken=False).order_by('-id')

            return ListedPet.objects.filter(is_taken=False, criteria=selected_value).order_by('-id')



class ListedPetDetailView(LoginRequiredMixin, UserPassesTestMixin,  DetailView):
    model = ListedPet

    def test_func(self):
        return True


class ListedPetCreateView(LoginRequiredMixin, CreateView):
    model = ListedPet
    fields = ['name', 'image', 'criteria', 'start_date', 'end_date', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListedPetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ListedPet
    fields = ['name', 'image', 'criteria', 'start_date', 'end_date', 'description', 'is_taken']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        advertisement = self.get_object()
        if self.request.user == advertisement.user:
            return True
        return False


class ListedPetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = ListedPet
    success_url = '/'

    def test_func(self):
        listed_pet = self.get_object()
        if self.request.user == listed_pet.user:
            return True
        return False



@login_required
def mypets(request):
    pets = ListedPet.objects.filter(user=request.user)
    context = {
        'pets': pets
    }
    return render(request, 'adtool/mypets.html', context)

def landing(request):
    return render(request, 'adtool/landing.html')

def about(request):
    return render(request, 'adtool/about.html')


"""
AJAX SECTION
"""