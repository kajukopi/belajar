from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import GeeksModel
from .forms import GeeksForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class GeeksCreate(CreateView):
 
    # specify the model for create view
    model = GeeksModel
 
    # specify the fields to be displayed
 
    fields = ['title', 'description']
    
    success_url ="/list/"
      
class GeeksList(ListView):
  
    # specify the model for list view
    model = GeeksModel
  
    def get_queryset(self, *args, **kwargs):
        qs = super(GeeksList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("id")
        return qs

class GeeksDetailView(DetailView):
    # specify the model to use
    model = GeeksModel
  
    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(GeeksDetailView,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        context["category"] = "MISC"        
        return context

@method_decorator(login_required, name='dispatch')
class GeeksUpdateView(UpdateView):
    # specify the model you want to use
    model = GeeksModel
 
    # specify the fields
    fields = [
        "title",
        "description"
    ]
     # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/list/"

@method_decorator(login_required, name='dispatch')
class GeeksDeleteView(DeleteView):
    
    # specify the model you want to use
    model = GeeksModel
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"

class GeeksFormView(FormView):
    # specify the Form you want to use
    form_class = GeeksForm
     
    # sepcify name of template
    template_name = "geeks/base.html"
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/list/"