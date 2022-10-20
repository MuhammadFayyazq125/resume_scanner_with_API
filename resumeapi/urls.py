from django.urls import path
from .views import resumeList , resumeDetails

urlpatterns = [
    path("<int:pk>/", resumeDetails.as_view(), name="detailcreate"),
    path("", resumeList.as_view(), name="listcreate")
]