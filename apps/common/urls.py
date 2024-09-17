from rest_framework.urls import path
from . import views

create_task = views.TaskModelViewSet.as_view({"post": "create"})
update_task = views.TaskModelViewSet.as_view({"patch": "partial_update"})
destroy_task = views.TaskModelViewSet.as_view({"delete": "destroy"})
detail_task = views.TaskModelViewSet.as_view({"get": "retrieve"})
list_tasks = views.TaskModelViewSet.as_view({"get": "list"})


urlpatterns = [
    path("task/create/", create_task),
    path("tasks/list/", list_tasks),
    path("task/update/<int:pk>/", update_task),
    path("task/delete/<int:pk>/", destroy_task),
    path("task/detail/<int:pk>/", detail_task),
]