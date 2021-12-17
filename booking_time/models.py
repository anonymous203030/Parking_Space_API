from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.


class BookTime(models.Model):
    floor = models.IntegerField(default=-1, validators=[MaxValueValidator(1), MinValueValidator(-5)])
    parking_space_id = models.IntegerField(unique=True)
    # In this test project i thought that parking spaces are selling by Date, so you cannot buy a place for an hour
    # If it could be possible the only thing to change would be to change 'DateField' to 'DateTimeField'
    booking_start_time = models.DateField()
    booking_end_time = models.DateField()

    def __str__(self):
        return f'{self.floor} | {self.parking_space_id}'

    # owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    class Meta:
        ordering = ['id']


class ReserveBookTime(models.Model):
    book_time = models.OneToOneField(BookTime, on_delete=models.CASCADE)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True, unique=True)

    class Meta:
        ordering = ['id']
