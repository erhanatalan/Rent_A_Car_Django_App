from django.db import models
from django.contrib.auth.models import User


# FixModel
class FixModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# CarModel
from django.core.validators import MinValueValidator
class Car(FixModel):
    GEAR=(
        (1, 'Auto'),
        (0, 'Manual')
    )

    plate = models.CharField(max_length=16, unique=True)
    brand = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    year = models.PositiveSmallIntegerField()
    gear = models.BooleanField(choices=GEAR, default=0)
    rent_per_day = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(1)],
    )
    availabilty = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.brand} {self.model} {self.plate}'

# Resevation

class Reservation(FixModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.user} {self.car} {self.start_date} {self.end_date}'


    # https://docs.djangoproject.com/en/4.2/ref/models/constraints/
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'start_date', 'end_date'], name='user_rent_date'
            )
        ]

