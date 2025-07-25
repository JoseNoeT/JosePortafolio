from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=255)
    long_desc = models.TextField()
    technologies = models.CharField(max_length=200)
    github_url = models.URLField()
    demo_url = models.URLField(blank=True, null=True)

    # Este es el nuevo campo
    image = models.ImageField(upload_to='proyectos/img/', blank=True, null=True)

    def __str__(self):
        return self.title
