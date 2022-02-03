from django.shortcuts import  render
from django.views import generic

from .models import UserDb

class User_info(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'test.html'
        User_list = UserDb.objects.all()
        return render(request, template_name, {"User_list : User_list"})


