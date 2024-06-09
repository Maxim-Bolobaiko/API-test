from django.urls import path

from .views import AdvertisementDetailView, AdvertisementListView

urlpatterns = [
    path(
        "advertisements/",
        AdvertisementListView.as_view(),
        name="advertisement_list",
    ),
    path(
        "advertisements/<int:ad_id>/",
        AdvertisementDetailView.as_view(),
        name="advertisement_detail",
    ),
]
