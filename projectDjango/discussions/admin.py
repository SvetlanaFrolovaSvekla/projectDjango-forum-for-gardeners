from django.contrib import admin
from .models import Artiles, Comment, Tag
from modeltranslation.admin import TranslationAdmin



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
# Register your models here.
# В Django ModelAdmin — это класс, который предоставляет настройки и функционал для отображения,
# редактирования и управления моделью в административной панели. Этот класс позволяет разработчику
# настраивать поведение и внешний вид админки для конкретной модели.
class ArtilesAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке статей
    list_display = ('title', 'anons', 'date', 'image_display', 'author')
    # По каким полям можно искать
    search_fields = ('title', 'anons', 'full_text')
    # Фильтрация по дате публикации
    list_filter = ('date', 'tags')
    # Поля, которые можно редактировать прямо в списке
    list_editable = ('anons',)
    # Сортировка статей
    ordering = ('-date',)

    filter_horizontal = ('tags',)  # Удобное добавление тегов в админке

    # Группировка полей на странице редактирования
    fieldsets = (
        (None, {
            'fields': ('title', 'anons', 'full_text', 'tags')  # Добавили поле tags
        }),
        ('Дополнительные параметры', {
            'fields': ('date', 'image')
        }),
    )
    # Поля, доступные только для чтения
    readonly_fields = ('date',)

    # Метод для отображения изображения в админке
    def image_display(self, obj):
        if obj.image:
            return f"🖼️ {obj.image.url.split('/')[-1]}"
        return "Нет изображения"
    image_display.short_description = "Изображение"

# Регистрация модели с кастомным классом админки
admin.site.register(Artiles, ArtilesAdmin)


admin.site.register(Comment)
