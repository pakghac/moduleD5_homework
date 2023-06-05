from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from .models import Post
from .filters import PostFilter
from .forms import PostForm


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['numPost'] = len(Post.objects.all())
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('newspaperapp.add_post',)
    template_name = 'post_create.html'
    form_class = PostForm


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('newspaperapp.change_post',)
    template_name = 'post_edit.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newspaperapp.delete_post',)
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


