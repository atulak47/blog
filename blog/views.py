from django.shortcuts import render,redirect
from .models import Blogpost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, BlogPostSerializer


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_list') 
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog_list') 
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('blog_list') 


@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_list') 
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog.html', {'form': form})

def blog_list(request):
    posts = Blogpost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})
@login_required(login_url='login')
def delete_blog(request,id):
    Blogpost.objects.get(id=id).delete()
    return redirect('blog_list')



#---------->2nd Versions Code (APIs using Android version 12.0.1)<-------------#################################

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        print(f"Received login request for username: {username}")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({'detail': 'Login successful','username':user.username})
        else:
            print(f"Authentication failed for username: {username}")
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer 

    def create(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)


class CreateBlogAPIView(generics.CreateAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogListAPIView(generics.ListAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogPostSerializer

