from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)



class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 100

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        return context


# дженерик для получения деталей о товаре
class PostDetailView(DetailView):
    template_name = 'sample_app/post_detail.html'
    queryset = Post.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(CreateView):
    template_name = 'sample_app/post_create.html'
    form_class = PostForm
    success_url = '/news/'


# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'sample_app/post_create.html'
    form_class = PostForm
    success_url = '/news/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'sample_app/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


