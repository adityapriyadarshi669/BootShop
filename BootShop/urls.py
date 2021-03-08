from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cart_checker, name='cartChecker'),
    path('home', views.home, name='home'),
    path('addProduct/<int:id>', views.add_product, name='addProduct'),
    path('removeProduct/<int:id>', views.remove_product, name='removeProduct'),
    path('decreaseItem/<int:id>', views.decrease_item, name='decreaseItem'),
    path('checkout', views.checkout, name='checkOut'), 
    path('pdf/<int:id>', views.convert_to_pdf, name='pdf'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
