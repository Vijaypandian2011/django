from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import NameList

class NameListView(ListView):
    model = NameList
    template_name = 'namelist_management/name_list.html'

class NameCreateView(CreateView):
    model = NameList
    fields = ['name', 'phone_number', 'linkedin_url']
    success_url = reverse_lazy('name_list')

class NameUpdateView(UpdateView):
    model = NameList
    fields = ['name', 'phone_number', 'linkedin_url']
    success_url = reverse_lazy('name_list')

class NameDeleteView(DeleteView):
    model = NameList
    success_url = reverse_lazy('name_list')
