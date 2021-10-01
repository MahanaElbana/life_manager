from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # ----- Todo -------#
    path('todo/' ,include('todo.urls',namespace="todo")),
    path('media/' ,include('media_manager.urls',namespace="media")),
    path('pomodoro/' ,include('pomodoro.urls',namespace="pomodoro")),
    path('sticknote/' ,include('sticknote.urls',namespace="sticknote")),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)