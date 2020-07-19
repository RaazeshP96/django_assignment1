from django.views.generic import CreateView
from .forms import CustomUserChangeForm, CustomUserCreationForm


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/customuser_form.html'


class Profile(CreateView):
    form_class = CustomUserChangeForm
    template_name = 'account/profile.html'
