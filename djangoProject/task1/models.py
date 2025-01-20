from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


# QuerySet запросы:
# python manage.py shell
# from task1.models import Buyer, Game

# Buyer.objects.create(name='Anne', balance=500, age=16)
# Buyer.objects.create(name='Harry', balance=1000, age=21)
# Buyer.objects.create(name='Bob', balance=700, age=40)
# Buyer.objects.all()

# Game.objects.create(title='Subnautica 2', cost=3000, size=20, description='Описание 1', age_limited = False)
# Game.objects.create(title='S.T.A.L.K.E.R. 2', cost=5000, size=150, description='Описание 2', age_limited = True)
# Game.objects.create(title='Atomic Heart', cost=4500, size=90, description='Описание 3', age_limited = True)
# Game.objects.all()

# Game.objects.get(id=4).buyer.set((Buyer.objects.get(id=1), Buyer.objects.get(id=3)))
# Game.objects.get(id=5).buyer.set((Buyer.objects.get(id=2), Buyer.objects.get(id=3)))
# Game.objects.get(id=6).buyer.set((Buyer.objects.get(id=2), Buyer.objects.get(id=3)))
