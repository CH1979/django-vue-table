from django.urls import path

from api.views import RowListView

urlpatterns = [
    path('rows/', RowListView.as_view())
]
