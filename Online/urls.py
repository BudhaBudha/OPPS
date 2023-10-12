from django.urls import path,include
from .views import *
from rest_framework import routers
 
# import everything from views

 
# define the router
router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register(r'Sass', SassViewSet)
router.register(r'Sonas', SonasViewSet)



urlpatterns = [
  path('student-details',StudentDetailAPI.as_view()),
  path('lecturer-details',LecturerDetailAPI.as_view()),
  path('student-register',StudentRegisterAPIView.as_view()),
  path('lecturer-register',LecturerRegisterAPIView.as_view()),
  path('sass',SassAPIView.as_view()),
  path('sonas',SonasAPIView.as_view()),
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls')),
 # path('sass-view', SassCreate.as_view())
]