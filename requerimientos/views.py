from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, CreateView, UpdateView, FormView
from .forms import RequerimientosForm,RequerimientosFormEdit
from .models import Requerimientos

# Create your views here.
class RequerimientosList(LoginRequiredMixin, ListView):
    """Funcion Lista Requerimientos En El Home"""
    model = Requerimientos
    template_name = 'requerimientos.html'
    context_object_name = 'requerimientos'
    queryset = Requerimientos.objects.all().order_by('-fechacreacion')
    paginate_by = 10

class RequerimientosCreate(LoginRequiredMixin, CreateView):
    """Creacion de Requerimientos"""
    model = Requerimientos
    template_name = 'create.html'
    form_class = RequerimientosForm
    success_url = reverse_lazy('requerimientos')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.user = request.user
            print(new_req)
            new_req.save()
            return redirect('requerimientos')

class RequerimientosUpdate(LoginRequiredMixin, UpdateView):
    """Actualiza Requerimientos"""
    model = Requerimientos
    form_class = RequerimientosFormEdit
    template_name = 'edit.html'
    success_url = reverse_lazy('requerimientos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Login(FormView):
    model = User
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('requerimientos')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('login')
