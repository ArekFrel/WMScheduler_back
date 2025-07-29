
from django.contrib import admin
from django.urls import path
from Scheduler.views import F1ManList
from Planner.views import ItemsToPlanList, pdf_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/scheduler/f1man/', F1ManList.as_view(), name='f1man'),
    path('api/planner/itemstoplan/', ItemsToPlanList.as_view(), name='itemstoplan'),
    path('api/pdf_view/<str:filename>/', pdf_view, name='pdf_view'),
]
