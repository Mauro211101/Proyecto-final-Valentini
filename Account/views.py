from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Account.models import Profile
# Create your views here.

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("index")

class Login(LoginView):
    next_page = reverse_lazy("post-list")

class Logout(LogoutView):
    template_name = "registration/logout.html"

class CreateProfile(CreateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = ['acerca_de_mi','imagen']
    
    def form_valid(self,form):
        form.instance.user= self.request.user
        return super().form_valid(form)


class ProfileDetail(DetailView):
    model = Profile

class UpdateProfile(UpdateView):
    model = Profile
    fields = ['acerca_de_mi','imagen']
    
    def test_func(self):
        user_ = self.request.user
        profile_id = self.kwargs.get("pk")
        return Profile.objects.filter(user=user_).exists()

    

