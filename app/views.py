from django.shortcuts import get_object_or_404, render, redirect
from .models import User
from .forms import UserForm


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'user_form.html', {'form': form})

def user_update(request, id):
    user = get_object_or_404(User, id=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})
