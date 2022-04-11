from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('user/<pk>/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('submit_project/', views.submit_project, name='submit_project'),
    path('project/<pk>/', views.project_detail, name='project_detail'),
    path('rate-project/<pk>', views.rate_project, name='rate_project'),
    # Rest API endpoints
    path('projects', views.ProjectViewSet.as_view(
        {'get': 'list'}), name='projects'),
    path('profiles/',
         views.ProfileViewSet.as_view({'get': 'list'}), name='profiles'),
]
