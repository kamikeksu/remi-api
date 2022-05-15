
from django.conf.urls import include, url
from . import handlers

urlpatterns = [
    url(r'^get$',          handlers.Get.as_view(),                name='product_get'),
    url(r'^get_test$',          handlers.GetTest.as_view(),                name='product_get'),
    url(r'^list$',         handlers.List.as_view(),               name='product_list'),
    url(r'^create$',       handlers.Create.as_view(),             name='product_create'),
    url(r'^update$',       handlers.Update.as_view(),             name='product_update'),
    url(r'^delete$',       handlers.Delete.as_view(),             name='product_delete'),
]
