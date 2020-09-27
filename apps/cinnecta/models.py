from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Texts(Base):
    title = models.CharField(max_length=20)
    text = models.TextField(blank=True, default='')
    file = models.FileField(blank=False, null=False)

    class Meta:
        verbose_name = 'Texts'
        ordering = ['id']

    def __str__(self):
        return self.title


