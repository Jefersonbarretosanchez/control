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
from .models import Requerimientos, HistoricoGeneral

# Create your views here.
class Historico(LoginRequiredMixin,ListView):
    model=Requerimientos
    template_name='historico.html'
    context_object_name='requerimientos'
    queryset=HistoricoGeneral.objects.all().order_by('fecha_registro')
    paginate_by=10

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

    def form_valid(self, form):
        response = super().form_valid(form)

        HistoricoGeneral.objects.create(
            usuario=self.request.user,
            correo_usuario=self.request.user.email,
            tipo_cambio="Creacion",
            tipo_activo="Persona",
            activo_modificado='Requerimiento',  # id de la persona
            descripcion=f'Se creo el "requerimiento" "{
                form.instance.requerimiento}"'
        )
        return response

class RequerimientosUpdate(LoginRequiredMixin, UpdateView):
    """Actualiza Requerimientos"""
    model = Requerimientos
    form_class = RequerimientosFormEdit
    template_name = 'edit.html'
    success_url = reverse_lazy('requerimientos')

    def form_valid(self, form):
        if form.has_changed():
            for field in form.changed_data:
                original_value = form.initial[field]
                current_value = form.cleaned_data[field]
                HistoricoGeneral.objects.create(
                    usuario=self.request.user,
                    correo_usuario=self.request.user.email,
                    tipo_cambio="Actualización",
                    tipo_activo="Requerimiento",
                    activo_modificado=field,
                    valor_anterior=original_value,
                    valor_nuevo=current_value,
                    descripcion=f'Cambio en {field}: de {
                        original_value} a {current_value}'
                )
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
