from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, category_list
from .forms import ProductCreateForm
from django.shortcuts import  redirect, render

class ProductCreateView(CreateView):
    template_name = 'beverage/product_create.html'
    form_class = ProductCreateForm
    # success_url = reverse_lazy('board:list') #class에서 sucessurl에서는 reverselazy써야함

    def get_success_url(self):
        return reverse('product:detail',args=[self.object.pk]) #self.object : insert한 모델객체


class ProductUpdateView(UpdateView):
    template_name = 'game/game_update.html'
    form_class = ProductCreateForm
    model = Product  #update는 create와 다르게 폼을 만들때 조회를 해야하기때문에 모델을 지정해주어야함

    def get_success_url(self):
        return reverse('product:detail',args=[self.object.pk]) #self.object : insert한 모델객체


def product_delete(request, pk):
    game = Product.objects.get(pk=pk) #조회
    game.delete()
    return redirect(reverse('product:list'))