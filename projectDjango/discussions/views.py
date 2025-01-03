from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .models import Artiles, Comment
from .forms import ArtilesForm, CommentForm
from django.views.generic import DetailView, UpdateView, DeleteView


def discussions_home(request):
    discussions = Artiles.objects.order_by('-date')
    return render(request, 'discussions/discussions_home.html', {'discussions': discussions})


def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        article = comment.article  # Получаем статью, к которой привязан комментарий
        comment.delete()
        request.session['message'] = "Комментарий успешно удален!"
        request.session['type'] = "success"
    except Comment.DoesNotExist:
        request.session['message'] = "Комментарий не найден."
        request.session['type'] = "error"

    # Перенаправляем обратно на страницу статьи, где был удалён комментарий
    return redirect('discussions_detail', pk=article.id)



class DiscussionsDetailView(DetailView):
    model = Artiles
    template_name = 'discussions/details_view.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['comments'] = article.comments.all().order_by('-created_at')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object

            # Если пользователь авторизован, имя берется из профиля пользователя
            if request.user.is_authenticated:
                comment.author = request.user.username
            else:
                comment.author = request.POST.get('author', 'Аноним')

            comment.save()

            # Отправка email автору статьи
            if self.object.author.email:
                send_mail(
                    subject='Новый комментарий к вашему обсуждению',
                    message=(
                        f'К вашей статье "{self.object.title}" добавлен новый комментарий:\n\n'
                        f'Автор: {comment.author}\n\n'
                        f'Комментарий: {comment.content}'
                    ),
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[self.object.author.email],
                )

            return redirect(self.request.path_info)

        return self.render_to_response(self.get_context_data(form=form))



class DiscussionsUpdateView(UpdateView):
    model = Artiles
    template_name = 'discussions/create.html'
    form_class = ArtilesForm

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class DiscussionsDeleteView(DeleteView):
    model = Artiles
    success_url = '/discussions/'
    template_name = 'discussions/delete.html'


def create(request):
    error = ''
    # Данные отправляются из формы
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            # Создаём объект, но не сохраняем его в базе
            article = form.save(commit=False)
            # Устанавливаем автора
            article.author = request.user
            # Сохраняем объект
            article.save()
            return redirect('home')
        else:
            error = 'В форме была допущена ошибка!'

    form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'discussions/create.html', data)