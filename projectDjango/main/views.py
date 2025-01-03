from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import locale

from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from news.models import Artiles as NewsArtiles, Tag as NewsTag
from discussions.models import Tag as DiscussionsTag, Artiles as DiscussionsArtiles

from .forms import RegisterForm


def index(request):
    # Устанавливаем локаль на русский язык
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    today = datetime.today()

    # Месяцы и их склонения
    months = {
        1: "января",
        2: "февраля",
        3: "марта",
        4: "апреля",
        5: "мая",
        6: "июня",
        7: "июля",
        8: "августа",
        9: "сентября",
        10: "октября",
        11: "ноября",
        12: "декабря",
    }

    day = today.day
    month_number = today.month  # Получаем номер месяца (1-12)
    month = months[month_number]  # Получаем склоненную форму месяца
    # Получаем новости
    news = NewsArtiles.objects.order_by('-date')[:8]
    data = {
        'title': 'Главная страница!!!',
        'values': ['Some', 'Hello', '123'],
        'dataTime': {
            'day': day,
            'month': month
        },
        'news': news,  # Передача новостей в шаблон
    }

    return render(request, 'main/index.html', data)

@login_required
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("main:profile")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def news_by_tag(request, tag_id):
    tag = get_object_or_404(NewsTag, id=tag_id)
    news = NewsArtiles.objects.filter(tags=tag).order_by('-date')
    return render(request, 'news/news_home.html', {'news': news, 'selected_tag': tag})

def discussions_by_tag(request, tag_id):
    tag = get_object_or_404(DiscussionsTag, id=tag_id)
    discussions = DiscussionsArtiles.objects.filter(tags=tag).order_by('-date')
    return render(request, 'discussions/discussions_home.html', {'discussions': discussions, 'selected_tag': tag})
