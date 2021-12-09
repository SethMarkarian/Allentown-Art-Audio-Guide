from django.db import models

class Exhibit(models.Model):
    artist = models.CharField(max_length=30, default="Unknown")
    title = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=20, null=True, blank=True)
    lookup_number = models.IntegerField(null=True)
    accession_number = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    additional_lookup_number = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='exhibit_images')
    video = models.FileField(default='default.mp4', upload_to='videos')
    audio = models.FileField(default='default.mp3', upload_to='audio')

    # Determines how the exhibit will be displayed on the admin page
    def __str__(self):
        return f'{self.lookup_number} – {self.title}'