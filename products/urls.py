﻿from django.conf.urls.defaults import *

urlpatterns = patterns('products.views',
    (r'^$', 'home'),
    (r'^id(?P<id>\d+)$','productid'),
)