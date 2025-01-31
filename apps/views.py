from django.shortcuts import render, redirect
from django.views.generic import ListView , TemplateView , DetailView, CreateView, FormView
from .models import Product, Category, Brand ,Banner, Blog, Saqlovchi, Users , ShoppingCart
from httpx import get
from django.contrib.auth import login, logout
from .forms import UserCreateForm, UserLoginForm
from .mixins import NotLoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
BOT_TOKEN = '7219637434:AAH97ltbR1SSTG8m1tPm-p7VJueKf5lBguo'

class IndexView(ListView):  
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        products = Product.objects.all()
        banner = Banner.objects.all()
        contex['products'] = products
        contex['banner'] = banner
        return contex


     
class AboutView(ListView):
    model = Product
    about_name = 'about.html' 
    context_object_name = 'about'



class ShopView(ListView):
    model = Product
    template_name = "shop.html"
    context_object_name = 'products'

    def get_context_data(self, * ,object_list=..., **kwargs):
        products = Product.objects.all()
        category = Category.objects.all()
        brands = Brand.objects.all()
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = products
        context['category'] = category
        context['brands'] = brands
        return context  


class BlogDetailsView(TemplateView):
    model =Blog
    template_name = 'blog-details.html'
    context_object_name = 'blog'


class BlogView(LoginRequiredMixin,ListView):
    model = Blog
    template_name = 'blog.html'  
    context_object_name = 'blogs'    



def send_message (chat_id, message) :
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': 8154542411,
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
{first_name}
{email}
BU YERGA QARANG:👉🫴👉 {message}
"""
        
        s = Saqlovchi.objects.create(   
            first_name=first_name,
            email = email,
            message=message
        )
        s.save()
        send_message(8154542411, text)

    return render(request, 'contact.html')    








class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class ContactView(TemplateView):
    template_name = 'contact.html'



class ShopDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop-details.html'


class ShoppingCartView(ListView):
    model = ShoppingCart
    template_name = 'shopping-cart.html'    
    context_object_name = 'like_list' 


    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)







class ShoppingCartCreateView(LoginRequiredMixin, View):
    login_url = 'login'



    def get(self,*args, **kwargs):
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
                wishlist = ShoppingCart.obejcts.filter(product=product).first()
                wishlist.delete()    
        return redirect('shop')


class UserCreateView(NotLoginRequiredMixin,CreateView):
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
        user = Users.objects.filter(username = username).first()
        # print(password, username , user)
        if user and user.check_password(password):
            login(self.request, user)
            return redirect('/')
        return super().form_valid(form)
    


class UserLogoutView(View):
    def get(self, request):
        logout(request.user)
        return redirect('/')
