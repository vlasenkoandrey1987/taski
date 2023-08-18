from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('sentry-debug/', views.trigger_error),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
