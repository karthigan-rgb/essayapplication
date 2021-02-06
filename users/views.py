from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
# Create your views here.
def register(request):
    if request.method =='POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             user = form.save()
             username = form.cleaned_data.get('username')
             group = Group.objects.get(name='essayusers')
             user.groups.add(group)
             messages.success(request, f'Your Account has now been created')
             return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})


@login_required
def profile(request):
        if request.method =='POST':
            u_form = UserUpdateForm(request.POST,instance=request.user)

            if u_form.is_valid():
                u_form.save()
                messages.success(request, f'Your Account has now been Updated')
                return redirect('profile')
        else:
          u_form = UserUpdateForm(instance=request.user)

        context ={
            'u_form':u_form
        }
        return render(request,'users/profile.html', context)
