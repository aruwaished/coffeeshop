from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('mycoffee.urls', namespace="mycoffee")),
    url(r'^cart/', include('cart.urls', namespace="cart")),
    ]