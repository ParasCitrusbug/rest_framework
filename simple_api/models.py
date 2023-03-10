from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


# Create your models here.
class Students(models.Model):
    """student models"""

    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    roll_number = models.IntegerField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippets(models.Model):
    """Snippet Models"""

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=25, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=25
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=25)

    class Meta:
        ordering = ["created"]
