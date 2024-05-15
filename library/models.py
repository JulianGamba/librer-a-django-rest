from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    
    def __str__(self):
        return self.name + " " + self.last_name
    
class Book(models.Model):
    NOVELA = 'NO'
    ENSAYO = 'EN'
    POESIA = 'PO'
    CIENCIA_FICCION = 'CF'

    GENERO_CHOICES = [
        (NOVELA, 'Novela'),
        (ENSAYO, 'Ensayo'),
        (POESIA, 'Poesía'),
        (CIENCIA_FICCION, 'Ciencia Ficción'),
    ]

    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.PositiveIntegerField()
    genre = models.CharField(choices=GENERO_CHOICES)