from django.urls import path

from .views import ApplicationTypeListView

urlpatterns = [
    path(
        "",
        ApplicationTypeListView.as_view(),
        name="application-types"
    ),
]