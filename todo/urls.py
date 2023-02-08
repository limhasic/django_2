from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.todo_list, name='todo_list'),

    # /pk/로 설정하여 해당 todo를 연결할 수 있게 함
    path('<int:pk>/', views.todo_detail , name = 'todo_detail'),
    path('post/', views.todo_post, name='todo_post'),

    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'),

    path('done/', views.todo_done_list, name='todo_done_list'),
    path('done/<int:pk>', views.todo_done, name='todo_done'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# 스태틱 파일을 서빙할 수 있는 경로 지정, -> MEDIA_URL ->
# static
# 서빙