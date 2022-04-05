from django.db import models
from django.urls import reverse
# Create your models here.
class Tasks(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    content = models.TextField('Контент', blank=True)
    serious_category = models.ForeignKey('SeriousCategory', on_delete=models.PROTECT, default=
    'Простая задача')
    is_finished = models.BooleanField('Закончено ?', default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('task_view', kwargs={'pk':self.pk})
    
    def get_color(self):
        d = {
            'Простая задача':'primary',
            'Средняя важность':'secondary',
            'Важно':'warning',
            'Очень важно':'danger',
        }
        if not self.is_finished:
            return d[str(self.serious_category)]
        else:
            return 'success'
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-serious_category']

class SeriousCategory(models.Model):
    name = models.CharField('Насколько важно?',max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория важности'
        verbose_name_plural = 'Категории важности'
