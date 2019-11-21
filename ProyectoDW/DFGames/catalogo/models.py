from django.db import models
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


	#Create your models here.
class Genre(models.Model):
    #Model representing a book genre."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
		

class Juego(models.Model):
    
	title = models.CharField(max_length=200)
	company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True) #compañia del juego
	fecha_lanzamiento = models.DateField(null=True, blank=True)
	platform = models.ForeignKey('Platform', on_delete=models.SET_NULL, null=True)	   
	descripcion = models.TextField(max_length=1000)
	idgame = models.CharField('IDGAME', max_length=13)
	genre = models.ManyToManyField(Genre)
	
    
	def __str__(self):
		return self.title
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('juego-detail', args=[str(self.id)])
		
class Platform(models.Model):
	"""Model representing an company."""
	plataforma = models.CharField(max_length=100) #nombre de la plataforma
	
	class Meta:
		ordering = ['plataforma']

	def get_absolute_url(self):
		return reverse('Platform-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.plataforma}'	
		
class Company(models.Model):
	"""Model representing an company."""
	name = models.CharField(max_length=100) #nombre de la compañia
	
	class Meta:
		ordering = ['name']

	def get_absolute_url(self):
		return reverse('Company-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.name}'	
		
		