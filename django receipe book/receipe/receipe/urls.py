from django.contrib import admin
from django.urls import path
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('receipes/',receipes,name="receipes"),
    path('delete_receipe/<id>/',delete_receipe,name="delete_receipe"),
    path('update_receipe/<id>/',update_receipe,name="update_receipe"),
    path('login/',login_page,name="login_page"),
    path('register/',register,name="register"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
    
urlpatterns+=staticfiles_urlpatterns()
