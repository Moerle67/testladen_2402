from django.db import models

# Create your models here.

class Benutzer(models.Model):
    name = models.CharField(("Name"), max_length=50)
    vorname = models.CharField(("Vorname"), max_length=50)
    entgelt = models.IntegerField(("Gehalt"))
    aktiv = models.BooleanField(("Aktiv"))
    eintritt = models.DateField(("Mitarbeiter seit"), auto_now=False, auto_now_add=False)
    
    class Meta:
        verbose_name = ("Benutzer")
        verbose_name_plural = ("Benutzer")

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse("Benutzer_detail", kwargs={"pk": self.pk})

