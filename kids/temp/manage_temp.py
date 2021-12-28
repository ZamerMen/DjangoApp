django -admin start project name_project
# into the dir where is manage.py
py manage.py srartapp name_app

подключаем приложение в settings APP
подключаем локальные урлы в общие через urls через include

создаем миграционный файл
py manage.py makemigrations

вносим изменения в базу
py manage.py migrate

p = Post.objects.create('title'='new post'...)
objects - атрибут - менеджер модели который управляет
все операция crud через него
p = Post.objects.all() - объект queryset типа списка но с кучей методов
p = Post.objects.get(slug='someslug') - возвращает конкретный экземпляр
для упрощения поиска в джанго есть лукапы slug__iexact - нечуствительный к регистру точное совпадение
(insensetive exact)
p = Post.objects.filter(slug__contains='someslug')

Form
класс Form для каждого своего поля генерит html тег в терминологии джанго это виджеты
title = forms.CharField(max_length=50) - в данном случае поля инпут(чарфилд)
клас форм проводит валидацию и очистку введенных данных клин методами
все данные из формы в базу берем из словаря cleaned_data
у экземпляра класса формы есть атрибуты
is_bound - были ли переданы данные(связана ли форма с данными)
is_valid - валидные ли данные были переданы
errors - если были ошибки данных то тут отобразятся
после передачи данных в метод is_valid появляестя cleaned_data

для связывания форм и модели используется подкласс Meta
где определяем model = Tag
и определяем поля через fields = ['asdf',...] или [__all__] если все
и переопределить классы для виджетов
