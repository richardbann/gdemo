from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from demo.views import DemoView, FileDownload
from django.views.generic import RedirectView


urlpatterns = [
    path("%s/<path:path>" % settings.MEDIA_URL[1:-1], FileDownload.as_view()),
    path("favicon.ico", RedirectView.as_view(url='/static/favicon.ico')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('demo/', DemoView.as_view()),
    path('blog/', include('blog.urls')),
)
