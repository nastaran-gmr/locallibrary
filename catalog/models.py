from django.db import models

# Create your models here.
class Author (models.Model):
    name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    date_of_birth=models.DateField('birth',null=True,blank=True)
    date_of_death=models.DateField('death',null=True,blank=True)


    def __str__(self) -> str:
        return '%s,%s'%(self.name , self.last_name)
    

class Gener (models.Model):
    name=models.CharField(max_length=100,help_text='enter book gener')

    def __str__(self) -> str:
        return self.name    

class Book (models.Model):
    author =models.ForeignKey(Author,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    isbn=models.CharField('ISBN',max_length=13,null=True,blank=True,help_text="13 character <a href='https://isbn/'>in this site</a>")
    gener=models.ManyToManyField(Gener ,help_text='select gener of this book')
    summery=models.CharField(max_length=300 ,help_text='enter a brife description of the book')

    def display_gener(self):
       return' ,'.join([gener.name for gener in self.gener.all()])
    display_gener.short_description='gener'

  
    def __str__(self) -> str:
        return self.title

import uuid
class Bookinstance (models.Model):

    id=models.UUIDField(primary_key=True ,default=uuid.uuid4)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    due_back=models.DateField(null=True,blank=True)
    status_onlone=(
        ('r','reserved'),
        ('m','maintenance'),
        ('a','on lone'),
        ('a','available'),
    )

    status=models.CharField(max_length=1,choices=status_onlone ,default='m',blank=True, help_text='book status')

    class meta:
        ordering={"due_back"}

    
    def __str__(self) -> str:
        return '%s,(%s)'%(self.id,self.book.title)