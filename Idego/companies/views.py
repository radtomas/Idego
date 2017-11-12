from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CompanyCreateForm, UserEditForm, UserCreateForm
from .models import Company
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'companies/index.html'


class CompaniesListView(LoginRequiredMixin, ListView):
    queryset = Company.objects.all()


class CompaniesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CompanyCreateForm
    template_name = 'companies/form.html'

    permission_required = 'companies.add_company'

    success_url = '/companies/'


class UsersListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return User.objects.all()


class UsersDetailView(LoginRequiredMixin, DetailView):
    queryset = User.objects.all()

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(User, pk=pk)
        return obj


class UsersCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'companies/form.html'

    permission_required = 'auth.add_user'

    success_url = '/users/'


class UsersEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = UserEditForm
    template_name = 'companies/form.html'

    permission_required = 'auth.change_user'

    success_url = '/users/'

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(User, pk=pk)
        return obj


class UsersDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = User
    success_url = '/users/'

    permission_required = 'auth.delete_user'

