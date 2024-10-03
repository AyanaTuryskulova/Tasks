from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect #можем указать рандомную ссылку куда сайт направит 
from django.utils import timezone
from .models import Task_post
from .forms import PostForm

def page(request):
     return render(request, 'tasks/main_page.html')


def task_view(request):
    posts = Task_post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'tasks/tasks.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Task_post, pk=pk)
    return render(request, 'tasks/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'tasks/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Task_post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'tasks/post_edit.html', {'form': form})  




def user_login(request):   
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('main_page')
    return render(request, 'registration/login.html')
#принимает пост нэйм=нэйм


def user_logout(request):
    logout(request)
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm({
            'username': request.POST['username'],
            'password1': request.POST['password1'],
            'password2': request.POST['password2']
        })  
        if form.is_valid():
            user = form.save()  
            login(request, user) 
            return redirect('tasks') 
    else:
        form = UserCreationForm()  
    return render(request, 'registration/register.html', {'form': form})
