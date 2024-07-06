from django.urls import reverse_lazy
from app.security.forms.group_module_permission import GroupModulePermissionForm
from app.security.models import GroupModulePermission
from app.security.instance.menu_module import MenuModule
from app.security.mixins.mixins import (
    CreateViewMixin,
    DeleteViewMixin,
    ListViewMixin,
    PermissionMixin,
    UpdateViewMixin,
)
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q


class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = "security/group_module_permissions/list.html"
    model = GroupModulePermission
    context_object_name = "group_module_permissions"
    permission_required = "view_group_module_permission"

    def get_queryset(self):
        q1 = self.request.GET.get("q")  # ver
        if q1 is not None:
            self.query.add(Q(group__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by("group__name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["create_url"] = reverse_lazy("security:group_module_permission_create")
        return context


class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = GroupModulePermission
    template_name = "security/group_module_permissions/form.html"
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy("security:group_module_permission_list")
    permission_required = "add_group_module_permission"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["grabar"] = "Grabar Módulo"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        group_module_permission = self.object
        messages.success(self.request, f"Éxito al crear los permisos del Grupo Módulo {group_module_permission.group}.")
        return response


class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = GroupModulePermission
    template_name = "security/group_module_permissions/form.html"
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy("security:group_module_permission_list")
    permission_required = "change_group_module_permission"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["grabar"] = "Actualizar Módulo"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        group_module_permission = self.object
        messages.success(
            self.request, f"Éxito al actualizar los permisos del Grupo Módulo {group_module_permission.group}."
        )
        return response


class GroupModulePermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = GroupModulePermission
    template_name = "security/delete.html"
    success_url = reverse_lazy("security:group_module_permission_list")
    permission_required = "delete_group_module_permission"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["grabar"] = "Eliminar Módulo"
        context["name"] = f"¿Desea Eliminar los permisos del Grupo Módulo: {self.object.group}?"
        context["back_url"] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = (
            f"Éxito al eliminar lógicamente los permisos del Grupo Módulo {self.object.group}."
        )
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
