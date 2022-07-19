from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="DReports"),
    path('add_report/',views.add_report, name="add_report")

]