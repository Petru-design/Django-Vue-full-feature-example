from django.db import models


# Create your models here.
class Coach(models.Model):
    first_name = models.CharField('First name', default="", max_length=200)
    last_name = models.CharField('Last name', default="", max_length=200)
    description = models.TextField()

    expertise_choices = (('math', 'Math'),
                         ('arts', 'Arts'),
                         ('other', 'Other'))

    expertise = models.CharField('First name',
                                 default="",
                                 max_length=200,
                                 choices=expertise_choices)
    rate = models.IntegerField()


class Message(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    message = models.TextField()
    email = models.EmailField()
# class Component(models.Model):
#     name = models.CharField('Component name', default="", unique=True)
#     template = models.TextField()
#     script = models.TextField()
#     style = models.TextField()


# class VuexModule(models.Model):
#     name = models.CharField('Module name', default="", unique=True)
#     state = models.TextField()
#     mutations = models.TextField()
#     actions = models.TextField()
#     getters = models.TextField()
#     modules = models.ManyToManyField('self')
