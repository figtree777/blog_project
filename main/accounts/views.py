from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['email'] = forms.EmailField(required=True)
        form.fields['username'] = forms.CharField(required=True)
        form.fields['password1'].label = 'Password'
        form.fields['password2'].label = 'Confirm Password'

        return form
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


