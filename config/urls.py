from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('adminka_for_bnpz/', admin.site.urls),
    path("api/v1/", include("bnpz.urls"))
]


admin.site.site_header = "BNPZ ADMIN"
admin.site.site_title = "Backend bnpz"