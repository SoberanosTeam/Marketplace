from django.urls import path

app_name = "search"

from .view import (
                        SearchProductView,
                    )

urlpatterns = [
    path('', SearchProductView.as_view(), name='list'),
]