from django.urls import path,include,re_path
from .views import *
from rest_framework import routers
from . import views
#from .core import views as core_views
 
# import everything from views

 
# define the router
router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register(r'Sass', SassViewSet)
router.register(r'Sonas', SonasViewSet)



urlpatterns = [
 # re_path(r'^signup/$',signup, name='signup'),
  #re_path(r'^login/$',login, name='login'),
  path('signup/',views.signup,name='signup'),
  path('login/',views.login,name='login'),
  #path('student-details',StudentDetailAPI.as_view()),
  #path('lecturer-details',LecturerDetailAPI.as_view()),
  #path('student-register',StudentRegisterAPIView.as_view()),
  #path('lecturer-register',LecturerRegisterAPIView.as_view()),
  path('sass',views.Sass),
  path('sonas',views.Sonas),
  #path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls')),
 # path('sass-view', SassCreate.as_view())
]