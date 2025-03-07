from django.urls import path
from shopapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('singup/',views.singup,name='singup'),
    path('get_product/',views.get_product,name='get_product'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('product_order/',views.product_order, name='product_order'),
    path('order_view/',views.order_view,name='order_view'),
    

    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""   path('admin_page/',views.admin_page,name='admin_page'),
    path('show_prodct/',views.show_prodct,name='show_prodct'),"""