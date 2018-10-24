import random 
from django.db import models
from django.urls import reverse
from django.utils import timezone


def generate_filename(instance, filename):
	""" generate filename for upload files to db """    
	filename = instance.slug + '.jpg'
	return '{}'.format(instance.id_tick) + "/" + '{}'.format(filename)

def dir_images(instance, filename):
	return '{}'.format(instance.dir_img) + "/" + '{}'.format(filename)

def prop_id_generate():
	id_tick = ''.join([random.choice(list('1234567890')) for x in range(5)])
	return id_tick

add_id_prop = prop_id_generate()

class TravelTicket(models.Model):
	""" Main class of travel toure """
	id_tick     = models.CharField(
			max_length=150,
			verbose_name=u'id объекта/папки',
			default=add_id_prop,
			blank=True,
			null=True
		)
	category    = models.ForeignKey('Category', verbose_name=u'категория')
	country     = models.ForeignKey('Country', verbose_name=u'категория')
	city        = models.ForeignKey('City', verbose_name=u'категория')
	
	title       = models.CharField(max_length=400, verbose_name=u'заголовк')
	description = models.TextField(verbose_name=u'статья')
	target_link = models.URLField()
	date        = models.DateTimeField(verbose_name=u'дата публикации')
	slug        = models.SlugField()
	price    	= models.PositiveIntegerField(default=0, verbose_name=u'стоимость')
	image       = models.ImageField(
			upload_to=generate_filename,
			verbose_name=u'заглавное изображение',
			blank=True,
			null=True
		)

	def get_absolute_url(self):
		return reverse('ticket-detail', kwargs={'category': self.category.slug, 'slug': self.slug})

	def __str__(self):
		return "{}, категория: {}".format(
			self.title, self.category.name
		)

	class Meta:
		verbose_name = 'записи'
		verbose_name_plural = 'запись'


class Country(models.Model):
	name = models.CharField(max_length=150, verbose_name=u'названия страны')
	slug = models.SlugField()

	def __str__(self):
		return "{}, {}".format(
				self.name, self.slug
			)
	
	class Meta:
		verbose_name = 'страны'
		verbose_name_plural = 'страна'


class City(models.Model):
	name = models.CharField(max_length=150, verbose_name=u'названия города')
	slug = models.SlugField()

	def __str__(self):
		return "{}, {}".format(
				self.name, self.slug
			)

	class Meta:
		verbose_name = 'города'
		verbose_name_plural = 'город'



class Images(models.Model):
	""" images class """
	album    = models.ForeignKey(TravelTicket)
	images   = models.ImageField(upload_to=dir_images, verbose_name=u'изображеня', blank=True, null=True)
	dir_img  = models.CharField(max_length=50, default=add_id_prop, verbose_name=u'название папки')
	
	def __str__(self):
		return "Объект:{}, категория: {}".format(
			self.album.title, self.album.category.name)

	class Meta:
		verbose_name = 'изображение'
		verbose_name_plural = 'изображения'



class Category(models.Model):
	name  = models.CharField(max_length=250, verbose_name=u'название категории')
	slug  = models.SlugField()
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('category-detail', kwargs={'slug': self.slug})

	class Meta:
		verbose_name = 'категорию'
		verbose_name_plural = 'категории'

