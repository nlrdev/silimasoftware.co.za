from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from silimasoftware.views import (
    silimasoftware,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", silimasoftware.as_view(), name="silimasoftware"),
    path("<slug:page>/", silimasoftware.as_view(), name="silimasoftware"),
    path("<slug:page>/<slug:function>/", silimasoftware.as_view(), name="silimasoftware"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
