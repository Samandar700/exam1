from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, TemplateView, DetailView,
    CreateView, FormView,
)
from .models import (
    Product, Category, Brand, Banner,
    Size, Color, Tags, Blog, Contact,
    Users, ShoppingCart
)
from httpx import get
from django.contrib.auth import login,logout
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .mixins import NotLoginRequiredMixin

BOT_TOKEN = '8185100923:AAFAFpnOtfcjVFcL3hYy8TJJL0lyCAwSs2g'


class IndexView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        products = Product.objects.all()
        banner = Banner.objects.all()
        contex['products'] = products
        contex['banner'] = banner
        return contex


class ShopView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    ordering = ['-created_at']

    def get_context_data(self, *, object_list=..., **kwargs):
        products = Product.objects.all()
        category = Category.objects.all()
        brands= Brand.objects.all()
        size = Size.objects.all()
        color = Color.objects.all()
        tags = Tags.objects.all()
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = products
        context['category'] = category
        context['brands'] = brands
        context['size'] = size
        context['color'] = color
        context['tags'] = tags
        return context


# class ContactView(TemplateView):
#     template_name = 'contact.html'

def send_message (chat_id, message) :
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = get(url, params=params)
   
    # print(response.text, response.status_code)


def contactview(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        email = data.get('email')
        message = data.get('message')
        text = f"""
Foydalanuvchi ismi: {first_name}
Foydalanuvchi email: {email}
Foydalanuvchining habari: {message}
"""
        data = Contact.objects.create(
            name = first_name,
            email = email,
            message = message
        )
        data.save()
        send_message(1038185913, text)
    return render(request, 'contact.html')

    

class BlogView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    login_url = 'login'


class ShopingCartView(ListView):
    model = ShoppingCart
    template_name = 'shopping-cart.html'
    context_object_name = 'like_list'

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)


class ShoppingCartCreateView(LoginRequiredMixin, View):
    # model = ShoppingCart
    # template_name = 'shop.html'
    login_url = 'login'

    def get(self, *args, **kwargs):
        user = self.request.user
        pk = self.kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if user and pk:
            if not ShoppingCart.objects.filter(product=product).exists():
                ShoppingCart.objects.create(
                    user=user,
                    product=product
                )
            else:
                wishlist = ShoppingCart.objects.filter(product=product).first()
                wishlist.delete()
        return redirect('shop')


class ShopDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop-details.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog-details.html'
    context_object_name = 'blog'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class UserCreateView(NotLoginRequiredMixin, CreateView):
    model = Users
    form_class = UserCreateForm
    template_name = 'register.html'
    success_url = '/'


class UserSigninView(FormView):
    form_class = UserLoginForm
    template_name = 'signin.html'
    success_url = '/'


    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = Users.objects.filter(username=username).first()
        # print(username, password, user)
        if user and user.check_password(password):
            login(self.request, user)
            return redirect('/')
        return super().form_valid(form)


class UserLogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')



