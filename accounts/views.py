from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import SingUpUserForm

class RegisterUser(CreateView):
    template_name = 'registration/register.html'
    form_class = SingUpUserForm

    def form_valid(self, form):
        form.save()

        return redirect('login')