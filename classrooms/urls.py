from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from API import views as APIviews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('login/', TokenObtainPairView.as_view(), name='api-login'),
    path('register/', APIviews.UserCreateAPIView.as_view(), name='api-register'),
    path('api/classrooms/', APIviews.ClassroomListView.as_view(), name='api-classroom-list'),
    path('api/classrooms/<int:classroom_id>/', APIviews.ClassroomDetailsView.as_view(), name='api-classroom-detail'),
    path('api/classrooms/create/', APIviews.ClassroomCreateView.as_view(), name='api-classroom-create'),
    path('api/classrooms/<int:classroom_id>/update/', APIviews.ClassroomUpdateView.as_view(), name='api-classroom'
                                                                                                   '-update'),
    path('api/classrooms/<int:classroom_id>/delete/', APIviews.ClassroomDeleteView.as_view(), name='api-classroom'
                                                                                                   '-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
