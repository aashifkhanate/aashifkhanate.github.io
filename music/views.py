from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, ListView, DetailView
from .forms import LoginForm, RegisterForm
from django.db.models import Q


class SearchView(ListView):
    template_name = 'music/search.html'
    context_object_name = 'all_songs'
    def get_queryset(self):
        queryset_list = Song.objects.all()
        print(self.request)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(song_title__icontains=query)
            )
        return queryset_list



class IndexView(ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class SongList(ListView):
    template_name = 'music/songs.html'
    context_object_name = 'all_songs'
    def get_queryset(self):
        return Song.objects.all()

class DetailView(DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('index')

class SongCreate(CreateView):
    model = Song
    fields = ['album', 'song_title', 'song_file']

class RegisterView(View):
    form_class = RegisterForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})

class LoginView(View):
    form_class = LoginForm
    template_name = 'music/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')
