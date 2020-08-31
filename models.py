from django.db import models

class Account(models.Model):
    account_id = models.BigIntegerField(db_index=True)

    class Meta:
        abstract = True

class Recipe(models.Model):
    recipe_id = models.BigIntegerField(db_index=True)

    class Meta:
        abstract = True