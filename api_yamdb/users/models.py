
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'

USER_ROLE = (
    (USER, 'user'),
    (MODERATOR, 'moderator'),
    (ADMIN, 'admin'),
)


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        verbose_name='Логин',
        help_text='Укажите логин',
        unique=True,
        validators=([RegexValidator(regex=r'^[\w.@+-]+$')]))
    email = models.EmailField(max_length=254,
                              verbose_name='E-mail',
                              help_text='Укажите e-mail',
                              unique=True,
                              null=False)
    confirmation_code = models.CharField(max_length=40,
                                         blank=True,
                                         verbose_name='Проверочный код')
    first_name = models.CharField(max_length=150,
                                  verbose_name='Имя',
                                  help_text='Ваше Имя',
                                  blank=True)
    last_name = models.CharField(max_length=150,
                                 verbose_name='Фамилия',
                                 help_text='Ваша Фамилия',
                                 blank=True)
    bio = models.TextField(max_length=1000,
                           verbose_name='Биография',
                           help_text='Расскажите о себе',
                           blank=True,)
    role = models.CharField(max_length=100,
                            verbose_name='Роль',
                            choices=USER_ROLE,
                            default=USER,
                            help_text='Пользователь')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return self.is_staff or self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    def __str__(self):
        return self.username
    
    def validate_username(self):
        '''Проверка поля username.'''
        if self.username == 'me':
            raise ValidationError('Использовать имя me запрещено.')
