# urls.py
from django.urls import path
from  .ekamo_views import *
app_name = 'account'


urlpatterns = [

    path('', DashboardIndex.as_view(), name='dash_index'),
    path('agent_profiles/', AgentProfileListView.as_view(), name='agent_profile_list'),
    path('agent_profiles/<int:pk>/', AgentProfileDetailView.as_view(), name='agent_profile_detail'),
   
]
