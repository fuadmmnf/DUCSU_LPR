from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    def __str__(self):
        return self.name

class Tag(models.Model):
    word = models.CharField(max_length=200)

    def __str__(self):
        return self.word

class Article(models.Model):
    TYPE = (
        ('B', 'Blog'),
        ('J', 'Journal'),
        ('R', 'Book Review'),
        ('L', 'DUThinks'),
        ('N', 'LPRNews'),
    )
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    article_type = models.CharField(max_length=1, choices=TYPE)
    created_date = models.DateTimeField(default=timezone.now)
    pdf = models.URLField(max_length=500, null=True, blank=True)
    image_link = models.URLField(max_length=500, null=True, blank=True)
    youtube_link = models.URLField(max_length=1000, null=True, blank=True)
    authors = models.ManyToManyField(Author, through='Article_Author')
    tags = models.ManyToManyField(Tag, through='Article_Tag')

    def __str__(self):
        return self.title

class Article_Author(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.name+"_"+ self.article.title

class Article_Tag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag.word+"_"+ self.article.title