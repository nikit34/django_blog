from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "SwitchMe"
admin.site.index_title = "SwitchMe"
admin.site.site_title = "SwitchMe Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('main.urls')),
]
