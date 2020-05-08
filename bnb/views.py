from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
	)
from .models import BNB


class BNBListView(ListView):
	model = BNB
	template_name = 'bnb/bnb.html'
	context_object_name = 'posts'
	ordering = ['-start_date']

class BNBDetailView(DetailView):
	model = BNB

class BNBCreateView(LoginRequiredMixin, CreateView):
	model = BNB
	fields = ['name', 'rooms', 'price', 'start_date', 'end_date', 'amenities', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class BNBUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = BNB
	template_name = 'bnb/bnb_update.html'
	fields = ['name', 'rooms', 'price', 'start_date', 'end_date', 'amenities', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class BNBDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = BNB
	success_url = '/bnb/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False