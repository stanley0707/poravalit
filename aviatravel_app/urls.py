from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from aviatravel_app.views import ( 
        VaucherListView,
        VaucherApiListView
    )

urlpatterns = [
    url(r'^$', VaucherListView.as_view()), 
    url(r'^tickets$', VaucherApiListView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
