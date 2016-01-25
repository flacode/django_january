from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib import messages
from reviewers.forms import AuthenticationForm, RegistrationForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return HttpResponseRedirect(reverse('reviews:user_review_list'))
                else:
                    messages.error(request, "The user is inactive")
            else:
                messages.error(request, "Please enter a correct email address and password. Note that both fields may "
                                        "be case-sensitive. Please first register if you don't have an account"
                               )
    else:
        form = AuthenticationForm()
    return render(request, 'reviewers/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'reviewers/registration_complete.html', {'user': user})
    else:
        form = RegistrationForm()
    return render(request, 'reviewers/register.html', {'form': form})


def logout(request):
    django_logout(request)
    return render(request, 'reviewers/logged_out.html')

# from django.shortcuts import render
# from .forms import RegistrationForm, LoginForm
# from django.views import generic
# from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
#
#
# # Create your views here.
#
# class Registration(generic.View):
#     form_class = RegistrationForm
#     template_name = 'reviewers/registration.html'
#
#     def get(self, request):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Thanks for registering!, please login")
#             return HttpResponseRedirect(reverse('reviews:review_list'))
#         return render(request, self.template_name, {'form': form})
#
#
# class Login(generic.View):
#     form = LoginForm
#     template_name = 'reviewers/login.html'
#
#     def get(self, request):
#         form = self.form()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect(reverse('reviews:review_list'))
#         return render(request, self.template_name, {'form': form})
