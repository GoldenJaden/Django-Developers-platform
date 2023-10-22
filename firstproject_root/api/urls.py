from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Auth
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),

    # Projects
    path('projects/', views.GetProjects.as_view()),
    path('projects/<str:pk>/', views.GetProject.as_view()),
    path('projects/<str:pk>/vote/', views.projectVote),
    
    path('remove-tag/', views.removeTag)
]