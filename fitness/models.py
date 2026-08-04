from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.



"""class Blog_Post(models.Model):
    comment=models.CharField(max_length=1000000)
    name = models.CharField(max_length=100)
    posted_at = models.DateTimeField(default=datetime.now,blank=True)
    class Meta:
        managed = True"""

class UserData(models.Model):
    #GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    #LEVEL_CHOICES = [ ('Weight Loss', 'Weight Loss'), ('Maintenance', 'Maintenance'), ('Muscle Gain', 'Muscle Gain')]
    #ACTIVITY_CHOICES=[('Sedentary (No exercise)', 'Sedentary (No exercise)'), ('Light (1-2 days/week)', 'Light (1-2 days/week)'), ('Moderate (3-5 days/week)', 'Moderate (3-5 days/week)'), ('Active (6-7 days/week)', 'Active (6-7 days/week)'), ('Elite (Athlete/Pro)', 'Elite (Athlete/Pro)')]
   

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    gender=models.CharField()
    #experience = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    age=models.IntegerField()
    height=models.FloatField()
    weight=models.FloatField()
    activity=models.FloatField()
    
    bmr=models.FloatField()
    tdee=models.FloatField()
    loss=models.FloatField()
    gain=models.FloatField()
    user_target=models.CharField()
    

class User_Plan(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    diet_plan=models.CharField()
    workout_plan=models.CharField()


class Post(models.Model):
    comment=models.CharField(max_length=1000000)
    title=models.CharField(max_length=500,null=True,blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_posts',null=True,blank=True)
    posted_at = models.DateTimeField(default=datetime.now,blank=True)


class FitnessPlanBase(models.Model):
    # Using choices to match your PostgreSQL ENUMs
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    LEVEL_CHOICES = [('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')]
    plan_id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    weight_range_kg = models.CharField(max_length=20)
    experience = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    full_week_routine = models.TextField()
    diet_plan = models.TextField()

    class Meta:
        abstract = True  # This ensures no table is created for this base class

class MuscleGainPlan(FitnessPlanBase):
    def __str__(self):
        return f"{self.gender} - {self.weight_range_kg} ({self.experience})"
    class Meta:
        db_table = 'muscle_gain_plan'  # Maps exactly to your SQL table name
        managed = False

class WeightLossPlan(FitnessPlanBase):
    def __str__(self):
        return f"{self.gender} - {self.weight_range_kg} ({self.experience})"
    class Meta:
        db_table = 'weight_loss_plan'
        managed = False

class BodybuildingPlan(FitnessPlanBase):
    def __str__(self):
        return f"{self.gender} - {self.weight_range_kg} ({self.experience})"
    class Meta:
        db_table = 'bodybuilding_plan'
        managed = False

# Exercise and Diet

class Exercise(models.Model):
    # The unique row name
    target_muscle = models.CharField(
        max_length=100, 
        primary_key=True, 
        help_text="The specific muscle group being targeted."
    )
    
    # Equipment types as the column headers
    order_index=models.IntegerField(default=0, null=True, blank=True)
    dumbbell = models.CharField(max_length=255, verbose_name="Dumbbell Exercise")
    barbell = models.CharField(max_length=255, verbose_name="Barbell Exercise")
    machine_cable = models.CharField(max_length=255, verbose_name="Machine/Cable Exercise")
    bodyweight_other = models.CharField(max_length=255, verbose_name="Bodyweight/Other Exercise")
    exercise1_image = models.ImageField(upload_to='exercise_pics/', null=True, blank=True)
    exercise2_image = models.ImageField(upload_to='exercise2_pics/', null=True, blank=True)
    exercise3_image = models.ImageField(upload_to='exercise3_pics/', null=True, blank=True)
    exercise4_image = models.ImageField(upload_to='exercise4_pics/', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Exercises"
        ordering = ['order_index']

    def __str__(self):
        return self.target_muscle
    
class Diet(models.Model):

    category = models.CharField(max_length=50) # Veg, Non-Veg, etc.
    protein = models.TextField(default="—")
    carbs = models.TextField(default="—")
    fiber = models.TextField(default="—")
    fats = models.TextField(default="—")
    vitamins_minerals = models.TextField(default="—")
    p_image = models.ImageField(upload_to='p_pics/', null=True, blank=True)
    c_image = models.ImageField(upload_to='c_pics/', null=True, blank=True)
    fa_image = models.ImageField(upload_to='fa_pics/', null=True, blank=True)
    fi_image = models.ImageField(upload_to='fi_pics/', null=True, blank=True)
    vm_image = models.ImageField(upload_to='vm_pics/', null=True, blank=True)

    def __str__(self):
        return self.category

# Media Uploader 
class ExerciseVideo(models.Model):
    video_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    # Videos will be saved in media/workout_videos/
    video_file = models.FileField(upload_to='workout_videos/')


class WeightLifting(models.Model):
    lifting_sport = models.CharField(max_length=20,default='Weight Lifting')
    game =models.CharField(max_length=100,primary_key=True)
    game_img =models.ImageField(upload_to='weight_lifting/',null=True,blank=True)
    description=models.CharField(max_length=100000,null=True,blank=True)
    

class PowerLifting(models.Model):
    lifting_sport = models.CharField(max_length=20,default='Power Lifting')
    game=models.CharField(max_length=100,primary_key=True)
    game_img=models.ImageField(upload_to='power_lifting/',null=True,blank=True)
    description=models.CharField(max_length=100000,null=True,blank=True)

class BodyBuilding(models.Model):
    lifting_sport = models.CharField(max_length=20,default='Body Building')
    game=models.CharField(max_length=100,primary_key=True)
    game_img=models.ImageField(upload_to='body_building/',null=True,blank=True)
    description=models.CharField(max_length=100000,null=True,blank=True)

class StrongMan(models.Model):
    lifting_sport = models.CharField(max_length=20,default='Strong Man')
    game=models.CharField(max_length=100,primary_key=True)
    game_img=models.ImageField(upload_to='strong_man/',null=True,blank=True)
    description=models.CharField(max_length=100000,null=True,blank=True)

class TrackField(models.Model):
    lifting_sport = models.CharField(max_length=20,default='Track & Field')
    game=models.CharField(max_length=100,primary_key=True)
    game_img=models.ImageField(upload_to='track_field/',null=True,blank=True)
    description=models.CharField(max_length=100000,null=True,blank=True)

class Gymnastics(models.Model):
    lifting_sport = models.CharField(max_length=20,default='Gymnastics')
    game=models.CharField(max_length=100,primary_key=True)
    game_img=models.ImageField(upload_to='gymnastics/',null=True,blank=True)
    description=models.CharField(max_length=100000,null=True,blank=True)

class Course(models.Model):
    
    body_target=models.CharField(max_length=20)
    info=models.CharField(max_length=1000)
    purpose=models.CharField(max_length=1000)
    planning=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='target/')

class Contact(models.Model):
    message=models.CharField(max_length=100000)
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=1000)