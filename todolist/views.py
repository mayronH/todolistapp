"""Views"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Category, List
from .forms import SingUpForm


def index(request):
    """Index"""
    return render(request, 'index.html')

# Create your views here.


@login_required
def todolist(request):
    """TodoList View"""
    user = request.user
    list_conclude = List.objects.filter(
        done_date__lte=timezone.now(), user=user).order_by('done_date')
    lists = List.objects.filter(
        done_date__isnull=True, user=user).order_by('created_date')
    categories = Category.objects.all()

    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["txtTitle"]
            category = request.POST["optCategory"]
            content = request.POST["txtContent"]
            date = request.POST["txtDate"]
            todo = List(title=title, content=content, due_date=date, user=user,
                        category=Category.objects.get(name=category))
            todo.save()
            return redirect("/todolist")

        if "taskDelete" in request.POST:
            checked = []
            if request.POST.getlist('taskCheckbox'):
                checked = request.POST.getlist('taskCheckbox')
            elif request.POST.getlist('taskCheckboxConclude'):
                checked = request.POST.getlist('taskCheckboxConclude')

            for list_id in checked:
                todo = List.objects.get(id=int(list_id))
                todo.delete()

        if "taskConclude" in request.POST:
            checked = request.POST.getlist("taskCheckbox")
            for list_id in checked:
                todo = List.objects.get(id=int(list_id))
                todo.conclude()
    return render(request, 'tasks.html', {"list_conclude": list_conclude,
                                          "categories": categories, "lists": lists, })


def singup(request):
    """User Sing Up"""
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SingUpForm()
    return render(request, 'registration/singup.html', {'form': form})
