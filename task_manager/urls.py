from django.contrib import admin
from django.urls import path
from tasks.views import tasks_view, add_task_view, delete_task_view, home_view, completed_tasks_view, complete_task_view, all_tasks_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view),
    path("tasks/", tasks_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
    path("completed_tasks/", completed_tasks_view),
    path("complete_task/<int:index>/", complete_task_view),
    path("all_tasks/", all_tasks_view),
]
