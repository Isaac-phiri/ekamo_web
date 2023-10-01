from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from account.views import CustomUserViewSet, AgentTypeViewSet, AgentProfileViewSet



router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'agent-type', AgentTypeViewSet, basename='agent')
router.register(r'agent-profile', AgentProfileViewSet, basename='agent')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)),
    path('control/crm/', include('account.urls')),
    path('', include('transactions.urls'))

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
