from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^songs/$', views.SongList.as_view(), name = 'songs'),
    url(r'^search/$', views.SearchView.as_view(), name = 'search'),
    url(r'^register/$', views.RegisterView.as_view(), name = 'register'),
    url(r'^login/$', views.LoginView.as_view(), name = 'login'),
    url(r'^logout/$', views.LogoutView.as_view(), name = 'logout'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name = 'album-add'),
    url(r'^songs/add/$', views.SongCreate.as_view(), name = 'song-add'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name = 'album-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name = 'album-delete'),
]
