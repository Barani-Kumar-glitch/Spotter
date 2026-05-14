from django.contrib import admin
#from .models import Blog_Post
from .models import Post
from .models import BodybuildingPlan
from .models import MuscleGainPlan
from .models import WeightLossPlan
from .models import UserData
from .models import User_Plan
from .models import ExerciseVideo
from .models import Exercise
from .models import Diet
from .models import WeightLifting
from .models import PowerLifting
from .models import BodyBuilding
from .models import StrongMan
from .models import TrackField
from .models import Gymnastics
from .models import Course
from .models import Contact


# Register your models here.
#admin.site.register(Blog_Post)
admin.site.register(Post)
admin.site.register(BodybuildingPlan)
admin.site.register(WeightLossPlan)
admin.site.register(MuscleGainPlan)
admin.site.register(UserData)
admin.site.register(User_Plan)
admin.site.register(ExerciseVideo)
admin.site.register(Exercise)
admin.site.register(Diet)
admin.site.register(WeightLifting)
admin.site.register(PowerLifting)
admin.site.register(BodyBuilding)
admin.site.register(StrongMan)
admin.site.register(TrackField)
admin.site.register(Gymnastics)
admin.site.register(Course)
admin.site.register(Contact)