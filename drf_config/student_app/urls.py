from django.urls import path
from .views import *
urlpatterns = [
    path("operations",student_view),
    path("update/<int:id>",update_student),
]
