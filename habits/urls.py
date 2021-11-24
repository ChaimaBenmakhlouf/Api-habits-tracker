from django.urls import include, path
from rest_framework import routers
from . import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'habits', views.HabitViewSet)
router.register(r'users', views.UserViewSet)
print(router.urls)

urlpatterns = [
    path("doc/", TemplateView.as_view(template_name="habits/swagger-ui.html"), name="redoc"),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name="list"),
    path('', include(router.urls)),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
