from django.urls import path
from . import views

urlpatterns = [

    


    # 🔐 Authentication
    path('auth/teacher/signup/', views.TeacherSignupView.as_view(), name='teacher-signup'),
    path('auth/student/signup/', views.StudentSignupView.as_view(), name='student-signup'),
    path('auth/teacher/login/', views.TeacherLoginView.as_view(), name='teacher-login'),
    path('auth/student/login/', views.StudentLoginView.as_view(), name='student-login'),

    # 👨‍🏫 Teachers
    path('teachers/', views.TeacherViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('teachers/<int:pk>/', views.TeacherViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),

    # 🎓 Students
    path('students/', views.StudentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('students/<int:pk>/', views.StudentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),

    # 📅 Events
    path('events/', views.EventViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('events/<int:pk>/', views.EventViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]
