from django.shortcuts import render

# Create your views here.
def my_views(request):
    myName="Mohammed Azhar"
    favPlayer="Hashim Amla"
    favAnimal="Wolf"
    favSubject="Python"
    d={"name":myName,"player":favAnimal,"animal":favAnimal,"subject":favSubject}
    return render (request,"myApp/1.html",d)