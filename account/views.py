from django.views.generic import CreateView
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.urls import reverse_lazy


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/customuser_form.html'
    success_url = reverse_lazy('blog-home')


class Profile(CreateView):
    form_class = CustomUserChangeForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('blog-home')
