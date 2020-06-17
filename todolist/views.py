"""Views"""
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Category, List

# Create your views here.

def todolist(request):
    """Index"""
    lists = List.objects.filter(done_date__lte=timezone.now()).order_by('done_date')
    categories = Category.objects.all()

    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["title"]
            category = request.POST["category_slide"]
            content = request.POST["content"]
            date = request.POST["date"]
            todo = List(title=title, content=content, due_date=date,
                        category=Category.objects.get(name=category))
            todo.save()
            return redirect("/")

        if "taskDelete" in request.POST:
            checked = request.POST["checkbox"]

            for list_id in checked:
                todo = List.objects.get(id=int(list_id))
                todo.delete()

        if "taskConclude" in request.POST:
            checked = request.POST["checkbox"]

            for list_id in checked:
                todo = List.objects.get(id=int(list_id))
                todo.conclude()
    return render(request, 'index.html', {'lists' : lists}, {'categories' : categories})
