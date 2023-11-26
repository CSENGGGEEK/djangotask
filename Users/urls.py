from django.urls import path
from django.contrib.auth import views as auth_views 
from . views import signup,login,logout
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout-message/', logout, name='logout_message'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)