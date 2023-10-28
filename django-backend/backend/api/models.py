from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    task = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task

# class Order(models.Model):
#     id = auto_id
#     created = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
#     finished = models.BooleanField(default = False, blank = True) # if the rent is finished or not
#     finalized = models.BooleanField(default = False, blank = True) # if the order itself is finalized so the user can't edit the order anymore
#     updated = models.DateTimeField(auto_now = True, blank = True) # if the order is being updated by the user
#     user = user.models
#     car = car.models
#     start_date = date
#     end_date = date
#     payment = integer
#     payment_method = choice
#     damage = boolean
#     damage_descriptions = text
#
#     def __str__(self):
#         return self.id

# class User(models.Model):
#     id = auto_id
#     created = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
#     name = string
#     email = email
#     date_of_birth = date
#     location = choice
#     profile_picture = image
#     order = order.models
#
#     def __str__(self):
#         return self.id

# class Car(models.Model):
#     id = auto_id
#     brand = choice
#     model = string
#     license_plate = string
#     rented_now = boolean
#     ordered = order.models
#
#     def __str__(self):
#         return self.id
