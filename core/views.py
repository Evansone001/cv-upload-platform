
from pyexpat.errors import messages
from typing import Generic
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .models import Profile
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import ProfileForm
from core import forms
from django.views.generic.edit import CreateView
#from django.views.generic.edit import CreateView


def home(request):
    context = {
        'home_page': "active",
    }
    return render(request, 'core/home.html', context)


# class UploadView(CreateView):
#     model = Upload
#     fields = ['upload_file', ]
#     success_url = reverse_lazy('fileupload')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['documents'] = Upload.objects.all()
#         return  context


def profile(request):
    if request.POST:

        form = ProfileForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'CV form submitted successfully.')
            return render(request, 'core/profile.html', {'form': ProfileForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
            return render(request, 'core/profile.html', {'form': ProfileForm(request.GET)})
    else:
        form = ProfileForm()
    
    return render(request, 'core/profile.html', {'form': ProfileForm})


# @api_view(["POST"])
# def upload_data(request):
 #   professional = ProfessionalSerializer(data=request.data)

    # validating for already existing data
  #  if Professional.objects.filter(**request.data).exists():
  #      raise serializers.ValidationError('This data already exists')

  #  if professional.is_valid() :
   #     professional.save()
    #    return response(professional.data)
   # else:
    #   return response(status=STATUS.HTTP_404_NOT_FOUND)
