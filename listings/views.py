from django.shortcuts import render

# Create your views here.

from django.views.generic import *
from .models import Property
from .forms import PropertyForm


class PropertyListView(ListView):
    template_name="properties.html"
    queryset=Property.objects.all()

class PropertyDetailView(DetailView):
    template_name="property.html"
    queryset=Property.objects.all()

class PropertyCreateView(CreateView):
    form_class=PropertyForm
    template_name="add_property.html"
    queryset=Property.objects.all()

class PropertyUpdateView(UpdateView):
    template_name="property_update.html"
    queryset=Property.objects.all()
    fields="__all__"