from django.contrib import admin
from django.urls import path
from root import settings
from django.conf.urls.static import static
from apps.views import IndexView, AboutView , ShopView , BlogDetailsView, BlogView , CheckoutView , contactview, ShopDetailView, ShoppingCartView, UserCreateView, UserSigninView, ShoppingCartCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name='about'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('blogdetails/', BlogDetailsView.as_view(), name= 'blogdetails'),
    path('blog/', BlogView.as_view(), name= 'blog'),
    path('checkout/', CheckoutView.as_view(), name= 'checkout'),
    path('contact/',contactview, name= 'contact'),
    path('shop/<int', ShopDetailView.as_view(), name='shop_detail'),
    path('shopping-cart/', ShoppingCartView.as_view(), name= 'shop_pingcart'),
    path('like/', ShoppingCartCreateView.as_view(), name='like'),


    path('singup/', UserCreateView.as_view(), name='user_create' ),
    path('signin/', UserSigninView.as_view(), name='signin'),
    path('logout/', UserSigninView.as_view(), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
