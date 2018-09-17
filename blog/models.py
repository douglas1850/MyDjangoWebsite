from django.db import models

#contains classes. Each class is like a table in the database,
# each variable in the class is like a column

class Post(models.Model) :
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title