from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
	)
from .models import Post

def home(request):
	return render(request, 'blog/home.html')

def posts_home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/posts.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/posts.html'
	context_object_name = 'posts'
	ordering = ['-date']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['name', 'content', 'price', 'date', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	template_name = 'blog/post_update.html'
	fields = ['name', 'content', 'price', 'date', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/posts/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render(request, 'blog/about.html')