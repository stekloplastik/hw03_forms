#  импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView

#  функция reverse_lazy позволяет получить URL по параметру
# "name" функции path()
#  берём, тоже пригодится
from django.urls import reverse_lazy

#  импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm

from django.core.mail import send_mail


send_mail(
    'Тема письма',
    'Текст письма.',
    'from@example.com',  # Это поле "От кого"
    ['to@example.com'],  # Это поле "Кому" (можно указать список адресов)
    fail_silently=False,  # Сообщать об ошибках («молчать ли об ошибках?»)
)


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("signup")
    template_name = "signup.html"
