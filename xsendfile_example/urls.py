from django.urls import path

from xsendfile_example import views

urlpatterns = [
    path('', views.serve_file),
    path('<path:path>', views.serve_file),
]
