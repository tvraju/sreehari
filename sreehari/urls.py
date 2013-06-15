from django.conf.urls import patterns, include, url
from cms import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sreehari.views.home', name='home'),
    # url(r'^sreehari/', include('sreehari.sreehari.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    #login Screen
    url(r'^login/', views.login, name='login'),

    url(r'^$', views.index, name='index')

    
)
