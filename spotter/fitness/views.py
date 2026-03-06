from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django .contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect
from datetime import datetime
from .models import Post
from .models import BodybuildingPlan
from .models import MuscleGainPlan
from .models import WeightLossPlan
from .models import ExerciseVideo
from .models import Exercise
from .models import Diet
from .models import WeightLifting
from .models import PowerLifting
from .models import BodyBuilding
from .models import StrongMan
from .models import TrackField
from .models import Gymnastics
from .models import UserData
from .models import User_Plan
from .models import Course
from .models import Contact


# Create your views here.
def index(request):
    guide=Course.objects.all()
    all_blogs = Post.objects.all().order_by('-posted_at')
    if all_blogs:
        img_blogs = Post.objects.exclude(image__isnull=True).exclude(image__exact='').order_by('-posted_at')
    return render(request,'index.html',{
        'guide':guide,
        'img_blogs': img_blogs,
        })

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # if email , password & username are equal login 
            if User.objects.filter(email=email).exists() & User.objects.filter(username=username).exists():
                messages.info(request,"Sign-In")
                return redirect('/')
            elif User.objects.filter(email=email).exists() | User.objects.filter(username=username).exists():
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Username Already Exists")
                    return redirect('signup')
                else:
                    messages.info(request,"E-mail Already Exists")
                    return redirect('signup')
            else:
                user= User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('signin')
        else:
            messages.info(request,"Password Didn't Match")
            return redirect('signup')
    else:
        return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate (username=username,password=password)
        if user is not None:
            auth.login(request,user)
            
            if request.user.is_authenticated:
                current_user = request.user.username
                return redirect('/',{'current_user':current_user})
            elif user.last_login == request.user.date_joined and request.user.is_authenticated:
                return redirect('calorie')
            else:
                return HttpResponse("The User is Not Authorized")
        else:
            messages.info(request,"Invalid User !Please Sign Up")
            return redirect('signup')
    else:
        return render (request,'signin.html')
    
def signout(request):
        auth.logout(request)
        return redirect ('/')


def about(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    guide=Course.objects.all()
    all_blogs = Post.objects.all().order_by('-posted_at')
    if all_blogs:
        img_blogs = Post.objects.exclude(image__isnull=True).exclude(image__exact='').order_by('-posted_at')
    return render(request,'about.html',{
        'guide':guide,
        'img_blogs': img_blogs,
        })
        

def blog_details(request,):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment = request.POST.get('comment')
            #Blogs.objects.create(comment=comment)
            name = request.POST.get('name')
            #Blogs.objects.create(name=name)
            image = request.FILES.get('image')
            title = request.POST.get('title')

            if name and comment and title:
                if image:
                    Post.objects.create(name=name, comment=comment, title=title, image=image)
                else :
                    Post.objects.create(name=name, comment=comment, title=title)
                return redirect('blog_details')
            
            else:
                messages.error(request, "Title, Name and Blog are need to be Required.")
                return redirect('blog_details')
        img_blogs = Post.objects.all().order_by('-posted_at')
        #img_blogs = Post.objects.filter(image__icontains='.').order_by('-posted_at')
        paginator = Paginator(img_blogs, 6) 
            
         # 3. Get the current page number from the URL (e.g., ?page=2)
        page_number = request.GET.get('page')
            
        # 4. Extract the specific 5 blogs for that page
        page_obj = paginator.get_page(page_number) 
        return render(request, 'blog_details.html',
                      {
                          'all_blogs':img_blogs,
                          'img_blogs':page_obj, 
                      }
                      )
      
    else:
        messages.info(request,"!Please Log In")
        return redirect('/')
    
    

def blog(request):
    if request.user.is_authenticated:
        all_blogs = Post.objects.all().order_by('-posted_at')
        if all_blogs:
            img_blogs = Post.objects.exclude(image__isnull=True).exclude(image__exact='').order_by('-posted_at')
            #img_blogs = Post.objects.filter(image__icontains='.').order_by('-posted_at')
            paginator = Paginator(img_blogs, 5) 
            
            # 3. Get the current page number from the URL (e.g., ?page=2)
            page_number = request.GET.get('page')
            
            # 4. Extract the specific 5 blogs for that page
            page_obj = paginator.get_page(page_number)

        return render(request,'blog.html',
                      {
                          'all_blogs' :all_blogs,
                         
                          'img_blogs': page_obj,  
                      }
                      )
    else:
        messages.info(request,"!Please Log In")
        return redirect('/')
    

def diets(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')

        # 1. Set default values for initial load (GET request)
    food_category = "all"
    diet_list = Diet.objects.all()

    # 2. Check for button click (POST request)
    if request.method == 'POST':
        food_category = request.POST.get('food_category', 'all')
        
        # 3. Dynamic Filter: No need for 10 elifs!
        if food_category != 'all':
            diet_list = Diet.objects.filter(category=food_category)
        
        else:
            diet_list = Diet.objects.all()
        

    # 4. CRITICAL: This return must be aligned with the first 'if'
    # It handles both the initial load and the button clicks.
    return render(request, 'diets.html', {
        'diets': diet_list, 
        'food_category': food_category
    })
    

def exercises(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')

    # 1. Set default values for initial load (GET request)
    muscle_group = "all"
    exercises_list = Exercise.objects.all()

    # 2. Check for button click (POST request)
    if request.method == 'POST':
        muscle_group = request.POST.get('muscle_group', 'all')
        
        # 3. Dynamic Filter: No need for 10 elifs!
        if muscle_group == 'Chest':
            exercises_list = Exercise.objects.filter(order_index__in=[1, 2, 3])
        elif muscle_group == 'Back':
            exercises_list = Exercise.objects.filter(order_index__in=[14, 15, 16])
        elif muscle_group == 'Shoulders':
            exercises_list = Exercise.objects.filter(order_index__in=[4, 5, 6])
        elif muscle_group == 'Biceps':
            exercises_list = Exercise.objects.filter(order_index__in=[10, 11])
        elif muscle_group == 'Triceps':
            exercises_list = Exercise.objects.filter(order_index__in=[7, 8, 9])
        elif muscle_group == 'Quads':
            exercises_list = Exercise.objects.filter(order_index__in=[17, 18, 19, 20])
        elif muscle_group == 'Abs':
            exercises_list = Exercise.objects.filter(order_index__in=[12, 13])
        
        else:
            exercises_list = Exercise.objects.all()
        

    # 4. CRITICAL: This return must be aligned with the first 'if'
    # It handles both the initial load and the button clicks.
    return render(request, 'exercises.html', {
        'exercises': exercises_list, 
        'default_muscle': muscle_group 
    })
    

def contact(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            #user_data=User.objects.filter(user=request.user).last()
            message=request.POST.get('message')
            name=request.POST.get('name')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            if message:
                if name:
                    if subject:
                        if email:
                            if email == request.user.email:
                                Contact.objects.create(message=message,name=name,email=email,subject=subject)
                                messages.info(request,"We will Contact you Soon")
                                return redirect("contact")
                            else:
                                messages.error(request,"Use Your Sign-In Email")
                        else:
                            messages.error(request,"E-Mail is need to be Required")
                    else:
                        messages.error(request,"Subject is need to be Required")
                else:
                    messages.error(request,"Name is need to be Required")
            else:
                messages.error(request,"Message is need to be Required")
                return redirect("contact")
            
        return render(request,'contact.html')
    else:
        messages.info(request,"!Please Log In")
        return redirect('/')
    

def courses(request):
    if request.user.is_authenticated:

        #Fetching Viedo DB
        fitness_edu=ExerciseVideo.objects.first()

        user_data=UserData.objects.filter(user=request.user).last()
        user_plan=User_Plan.objects.filter(user=request.user).last()

        if user_plan is None or user_data is None:
            guide=Course.objects.all()
            context = {
                
                'exercise' : fitness_edu,
                'guide':guide,
            }
            return render(request,'courses.html',context)

        workout_plan= user_plan.workout_plan.split('\n')
        diet_plan= user_plan.diet_plan.split('\n')
        guide=Course.objects.all()

        context = {
                
                'user_data': user_data,
                'workout_plan': workout_plan,
                'diet_plan': diet_plan,
                'exercise' : fitness_edu,
                'guide':guide,
            }
        return render(request,'courses.html',context)
    else:
        messages.info(request,"!Please Log In")
        return redirect('/')

def elements(request):
    if request.user.is_authenticated:
        return render(request,'elements.html')
    else:
        messages.info(request,"!Please Log In")
        return redirect('/')

def sport(request):
    if request.user.is_authenticated:
        return render(request,'sport.html')
    else:
        messages.info(request,"!Please Log In")
        return redirect('/')

def main(request):
    if request.user.is_authenticated:
        return render(request,'main.html')
    else:
        messages.info(request,"!Please Log In")
        return redirect('/')


def calorie(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    if request.method == 'POST':
        
        age_yo=request.POST.get('age')
        gender_val=request.POST.get('gender')
        weight_kg=request.POST.get('weight')
        height_cm=request.POST.get('height')
        activity_val=request.POST.get('activity')
        
        
        if age_yo and weight_kg and height_cm and activity_val and gender_val :
            age=int(age_yo)
            weight=float(weight_kg)
            height=float(height_cm)
            activity=float(activity_val)
            gender=str(gender_val)

            if 18<= age <=120:
                if 35<= weight <= 150:
                    if 90<= height <= 275:
                        # Mifflin-St Jeor Equation
                        bmr = (10 * weight) + (6.25 * height) - (5 * age)
                        if gender == 'Male':
                            bmr += 5
                        else:
                            bmr -= 161
        
                        tdee = bmr * activity
                        loss  = tdee - 500
                        gain = tdee + 500
                        user_target=request.POST.get('user_target')
                        UserData.objects.create(user=request.user,gender=gender,age=age,weight=weight,height=height,activity=activity,bmr=bmr, tdee=tdee, loss=loss, gain=gain,user_target=user_target)
                        #return render (request,'calorie_results.html')
                    
                        return redirect ('calorie_results')
                    else:       
                        messages.error(request, "Your Height is Execceded the Limit( 90 - 275 ).")
                else:
                    messages.error(request, "Your Weight is Execceded the Limit( 30 - 150 ).")
            else:
                messages.error(request, "Your Age is Execceded the Limit( 18 - 120 ).")
        else:
            messages.error(request, "All User Informations are required.")
            return render(request, 'calorie.html', {'error': 'Please update profile first'})
        
    return render (request,'calorie.html')

def calorie_results(request):
    #if request.method == "GET":
    workout_plan=[]
    diet_plan=[]

    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    
    user_data=UserData.objects.filter(user=request.user).last()

    #results=Cal_Result.objects.filter(user=request.user).values('bmr','tdee','loss','gain','user_target').last()
    #m_gain=MuscleGainPlan.objects.all()      
    # or not User_Plan.objects.filter(user=request.user).exists()

    if not UserData.objects.filter(user=request.user).exists():
        messages.error(request, "No User Data is Stored in DataBase")
        return redirect('calorie')
        

    else:
    
        # Converting User Experience
        if 1<= user_data.activity  and user_data.activity <=1.5:
            exp="Beginner"
        elif user_data.activity == 1.55:
            exp="Intermediate"
        else:
            exp="Advanced"

        # Converting Weight Range
        if 35<= user_data.weight <=55:
            weight_range="35-55kg"
        elif 55< user_data.weight <=80:
            weight_range="56-80kg"
        elif 80< user_data.weight <=110:
            weight_range="81-110kg"
        elif 110< user_data.weight <=150:
            weight_range="111-150kg"
        else:
            weight_range=""
        

        # Maintaining Body Chart
        if user_data.user_target == 'Maintenance':
            b_build=BodybuildingPlan.objects.filter(
                gender=user_data.gender,
                weight_range_kg=weight_range,
                experience=exp,
            ).first()

            if b_build is not None:
                workout_plan = b_build.full_week_routine.split('\n')
                diet_plan = b_build.diet_plan.split('\n')
            else:
                messages.error(request, "User Fetching Data is Not Stored in DataBase")
                return redirect('calorie_results')

        # Weight Loss Body Chart
        if user_data.user_target == 'Weight Loss':
            w_loss=WeightLossPlan.objects.filter(
                gender=user_data.gender,
                weight_range_kg=weight_range,
                experience=exp,
            ).first()

            if w_loss is not None:
                workout_plan = w_loss.full_week_routine.split('\n')
                diet_plan = w_loss.diet_plan.split('\n')
            else:
                messages.error(request, "User Fetching Data is Not Stored in DataBase")
                return redirect('calorie_results')
        # Muscle Gain Body Chart
        if user_data.user_target == 'Muscle Gain':
            m_gain=MuscleGainPlan.objects.filter(
                gender=user_data.gender,
                weight_range_kg=weight_range,
                experience=exp,
            ).first()

            if m_gain is not None:
                workout_plan = m_gain.full_week_routine.split('\n')
                diet_plan = m_gain.diet_plan.split('\n')
            else:
                messages.error(request, "User Fetching Data is Not Stored in DataBase")
                return redirect('calorie_results')
            
        User_Plan.objects.create(user=request.user,diet_plan=diet_plan,workout_plan=workout_plan)

        context = {
            
            'user_data': user_data,
            'workout_plan': workout_plan,
            'diet_plan': diet_plan
        }

        
        # Render the individual results page
        return render(request, 'calorie_results.html',context)

    # If GET, just show the empty form page
    #return redirect('calorie')


def workout_diet_plan(request):
        return render(request, )


def post(request ,pk):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    blog = get_object_or_404(Post,pk=pk)
    return render (request,"post.html",{
        'blog':blog,
        })



def gym_games(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    return render(request,"gym_games.html")

def weight_lifiting(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    w_lift=WeightLifting.objects.all()
    return render (request,"gym_games.html",{
        'gym_games' : w_lift,
    })

def power_lifiting(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    p_lift=PowerLifting.objects.all()
    return render (request,"gym_games.html",{
        'gym_games' : p_lift,
    })

def body_building(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    b_built=BodyBuilding.objects.all()
    return render (request,"gym_games.html",{
        'gym_games' : b_built,
    })

def strong_man(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    s_man=StrongMan.objects.all()
    return render (request,"gym_games.html",{
        'gym_games' : s_man,
    })

def track_field(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    t_feild=TrackField.objects.all()
    return render (request,"gym_games.html",{
        'gym_games' : t_feild,
    })

def gym_nastics(request):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    g_nast=Gymnastics.objects.all()
    return render (request,"gym_games.html",{
        'gym_games' : g_nast,
    })


def target(request,pk):
    if not request.user.is_authenticated:
        messages.info(request, "!Please Log In")
        return redirect('/')
    target=get_object_or_404(Course,pk=pk)
    return render (request,'target.html',{
        'target':target,
    })