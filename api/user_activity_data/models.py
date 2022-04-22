from django.db import models


class UserActivityData(models.Model):
    id = models.IntegerField(primary_key=True)
    activity_type = models.TextField()
    value = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()
    points = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'user_activity_data'



class UserPoints(models.Model):
    id = models.IntegerField(primary_key=True)
    total_points = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'user_points'