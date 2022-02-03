# Add your Views Here
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from tasks.models import Task


def deleteTask(index):
    Task.objects.filter(id=index).update(deleted=True)


def completeTask(index):
    Task.objects.filter(id=index).update(completed=True)


def tasks_view(request):
    tasks = Task.objects.filter(deleted=False)
    completedTasks = Task.objects.filter(completed=True)
    searchtasks = Task.objects.filter(deleted=False)
    search_term = request.GET.get("search")
    if search_term:
        searchtasks = tasks.filter(title__icontains=search_term)
    return render(request, "tasks.html", {"tasks": tasks, "completedTasks": completedTasks, "searchtasks": searchtasks, "searchQuery": search_term})


def home_view(request):
    tasks = Task.objects.filter(deleted=False)
    completedTasks = Task.objects.filter(completed=True)
    return render(request, "index.html", {"tasks": tasks, "completedTasks": completedTasks})


def completed_tasks_view(request):
    tasks = Task.objects.filter(deleted=False)
    completedTasks = Task.objects.filter(completed=True)
    searchCompletedTasks = Task.objects.filter(completed=True)
    search_term = request.GET.get("search")
    if search_term:
        searchCompletedTasks = completedTasks.filter(
            title__icontains=search_term)
    return render(request, "completedTasks.html", {"tasks": tasks, "completedTasks": completedTasks, "searchCompletedTasks": searchCompletedTasks, "searchQuery": search_term})


def all_tasks_view(request):
    tasks = Task.objects.filter(deleted=False)
    completedTasks = Task.objects.filter(completed=True)
    searchPending_tasks = Task.objects.filter(deleted=False)
    searchCompleted_tasks = Task.objects.filter(completed=True)
    search_termPending = request.GET.get("searchPending")
    search_termCompleted = request.GET.get("searchCompleted")
    if search_termPending:
        searchPending_tasks = tasks.filter(
            title__icontains=search_termPending)
    elif search_termCompleted:
        searchCompleted_tasks = completedTasks.filter(
            title__icontains=search_termCompleted)
    return render(request, "allTasks.html", {"tasks": tasks, "completedTasks": completedTasks, "searchPending_tasks": searchPending_tasks,  "searchCompleted_tasks": searchCompleted_tasks, "searchQueryPending": search_termPending, "searchQueryCompleted": search_termCompleted})


def add_task_view(request):
    task_value = request.GET.get("task")
    Task(title=task_value).save()
    return HttpResponseRedirect("/tasks")


def delete_task_view(request, index):
    deleteTask(index)
    return HttpResponseRedirect("/tasks")


def complete_task_view(request, index):
    completeTask(index)
    deleteTask(index)
    return HttpResponseRedirect("/tasks")
