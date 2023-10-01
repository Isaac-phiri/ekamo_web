# views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import AgentProfile
from .forms import AgentProfileForm
from django.urls import reverse_lazy
from django.views import View
# views.pyfrom django.views import View
from django.views.generic import TemplateView

class DashboardIndex(TemplateView):
    template_name = 'admin/index.html'


class AgentProfileListView(View):
    model = AgentProfile
    context_object_name = 'agent_profiles'
    template_name = 'admin/agents.html' 

    # def get_queryset(self):
    #     # Get the user's account_type_id
    #     user_account_type = self.request.user.account_type
    #     if user_account_type:
    #         return user_account_type.agents_to_manage.all()
    #     else:
    #         return AgentProfile.objects.none()  # Return an empty queryset if no account_type is found

    # def get(self, request, *args, **kwargs):
    #     agent_profiles = self.get_queryset()
    #     return render(request, self.template_name, {'agent_profiles': agent_profiles})
    #     # agent_id = self.request.user.account_type.agents_to_manage.id

        # Filter AgentProfile instances based on the user's account_type
        # return AgentProfile.objects.filter(agents_to_manage=account_type)
# 
class AgentProfileDetailView(DetailView):
    model = AgentProfile
    template_name = 'admin/transactions.html'
    context_object_name = 'agent_profile'
 
# class AgentProfileUpdateView(UpdateView):
#     model = AgentProfile
#     form_class = AgentProfileForm
#     template_name = 'agent_profile_form.html'
#     success_url = reverse_lazy('agent_profile_list')
 