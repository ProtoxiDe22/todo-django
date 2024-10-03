from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Profile
from .forms.forms_auth import RegisterForm, LoginForm, ProfileForm



class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'todo/auth/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('todo:home')
        # If the form is not valid, re-render the page with the form errors
        return render(request, 'todo/auth/register.html', {'form': form})
    
    
class LoginView(View):
    template_name = 'todo/auth/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get('next') or 'todo:home'
                return redirect(next_url)
            else:
                form.add_error(None, "Invalid credentials")
        return render(request, self.template_name, {'form': form})
    
class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('todo:login')
    
    def get(self, request):
        logout(request)
        return redirect('todo:home')
class UserProfileView(LoginRequiredMixin, View):
    template_name = 'todo/auth/userProfile.html'

    # Get the user 'User' object and try to get the profile, if it doesn't exist yet, create it
    # then render the page with the user_form and profile_form
    def get(self, request):
        user_form = RegisterForm(instance=request.user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('todo:user_profile')
        else:
            return redirect('todo:user_profile', {'profile_form': profile_form, 'error': 'there was an error in your form.'})