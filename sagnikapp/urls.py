from django.contrib import admin
from django.urls import path,include
from sagnikapp import views


urlpatterns = [
    path('',views.index, name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('bmi',views.bmi,name="bmi"),
    path('bfp',views.body_fat,name="bfp"),
    path('calorie',views.calorie,name="calorie"),
    path('data',views.data,name="data"),
    path('diet_plan',views.diet_plan,name="diet_plan"),
    path('diet_input',views.diet_input,name="diet_input"),
    path('idealw',views.ideal_weight,name="idealw"),
    path('fba',views.fba,name="fba"),
    path('exercise',views.exercise,name="exercise"),
    path('arm',views.arm,name="arm"),
    path('chest',views.chest,name="chest"),
    path('leg',views.leg,name="leg"), 
    path('suryanamaskar',views.suryanamaskar,name="suryanamaskar"),    
    path('meditation',views.meditation,name="meditation"),    
    path('detox',views.detox,name="detox"),    
    path('MuscleGain',views.MuscleGain,name="MuscleGain"), 
    path('Cardio',views.Cardio,name="Cardio"), 
    path('loosebellyfat',views.loosebellyfat,name="loosebellyfat"),   
    path('beginner',views.beginner,name="beginner"),
    path('Intermidiate',views.Intermidiate,name="Intermidiate"),
    path('Advanced',views.Advanced,name="Advanced"),




]

