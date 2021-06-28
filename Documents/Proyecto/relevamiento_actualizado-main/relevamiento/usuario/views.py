from django.http import request
from django.http import HttpResponseRedirect #from django.http.response import HttpResponseRedirect
from relevamiento.usuario.forms import LoginForm
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

# Imports necesarios para poder trabajar con seguroidad en login 
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache 
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login,logout, authenticate
from .forms import LoginForm
# Create your views here.


class Login(FormView):
    template_name = 'farmacia/login.html'
    form_class = LoginForm
    success_url =  reverse_lazy('index')

    # @method_decorator(csrf_protect)
    # @method_decorator(never_cache)
    
    # def dispatch(self,request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return HttpResponseRedirect(self.get_success_url())
    #     else:
    #         return super(Login, self).dispatch(request,*args, **kwargs)
    
    # def form_valid(self, form):
    #     login(self.request,form.get_user())
    #     return super(Login,self).form_valid(form)

