from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect #можем указать рандомную ссылку куда сайт направит 
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Task_post
from .forms import PostForm, RegisterUserForm
from django.views.generic import CreateView



def page(request):
     return render(request, 'tasks/main_page.html')

def profile(request):
    return render(request, 'tasks/profile.html')

def task_view(request):
    tasks = Task_post.objects.all()  
    return render(request, 'tasks/tasks.html', {'posts': tasks})

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


def delete_post(request, pk):
    post = get_object_or_404(Task_post, pk=pk)
    post.delete()
    return redirect('tasks')

def task_add_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.published_date = timezone.now()
            task.save()
            messages.success(request,'Ваш пост был добавлен!' )
            return redirect('task_add')  
    else:
        form = PostForm()
    return render(request, 'tasks/add.html', {'form': form})


def task_list_view(request):
    category = request.GET.get('category', None)

    if category:
        tasks = Task_post.objects.filter(category=category)

    else:
        tasks = Task_post.objects.all()

    return render(request, 'tasks/tasks.html', {'posts': tasks, 'selected_category': category})
    

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

    

class RegisterUser(CreateView):
    form_class = RegisterUserForm  
    template_name = 'registration/register.html' 
    success_url = reverse_lazy('login') 

    def form_valid(self, form):
        user = form.save()  
        login(self.request, user)  
        return super().form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация" 
        return context
    
