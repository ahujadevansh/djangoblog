from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_variables,sensitive_post_parameters
from django.views.generic import UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm


# To systematically hide all local variables of a function from error logs, 
# do not provide any argument to the sensitive_variables decorator.
# To systematically hide all POST parameters of a request in error reports, 
# do not provide any argument to the sensitive_post_parameters decorator.

@sensitive_post_parameters()
@sensitive_variables('username','form')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"{username} registered sucessfully. Log in to continue")
            return redirect('users_login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


# @sensitive_post_parameters('username')
# @login_required
# def profile(request):
#     if request.method == 'POST' :
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)
#         if p_form.is_valid() and u_form.is_valid() :
#             p_form.save()
#             u_form.save()
#             messages.info(request,"Your Profile is updated")
#             return redirect('users_profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     context = {
#         'u_form' : u_form,
#         'p_form' : p_form,
#     }
#     return render(request,'users/profile.html',context)


# If one of your views receives an HttpRequest object with POST parameters susceptible to
#  contain sensitive information,you may prevent the values of those parameters 
# from being included in the error reports using the sensitive_post_parameters decorator

# To decorate every instance of a class-based view, you need to decorate the class definition 
# itself. To do this you apply the decorator to the dispatch() method of the class.

@method_decorator(sensitive_post_parameters('username'), name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProfileView(View):


    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form' : u_form,
            'p_form' : p_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid() :
            p_form.save()
            u_form.save()
            messages.info(request,"Your Profile is updated")
            return redirect('users_profile')
