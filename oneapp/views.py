from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Menu


def show(request):
   return render(request,"quater_master(1).html")

def gun(request):



    place=request.POST.get("p")
    number = request.POST.get("n")
    type = request.POST.get("t")
    description = request.POST.get("d")
    date= request.POST.get("dt")
    Contract_Service_Number = request.POST.get("sn")
    Electric_Meter_Number = request.POST.get("mn")
    # if a GET (or any other method) we'll create a blank form
    from pymongo import MongoClient
    client=MongoClient('localhost:27017')
    db=client
    posts=db.simple
    x={"Quaters_Place":place,"Quaters_Number":number,"Quaters_Type":type,"Quaters_Description":description,"Quaters_Date":date,"Contract_Service_Number":Contract_Service_Number,"Electric_Meter_Number":Electric_Meter_Number}
    posts.simple.insert(x)
    return render(request,"quater_master(1).html")
# # def destroy(request, Quaters_Number):
# #     employee = Menu.objects.get(Quaters_Number=Quaters_Number)
# #     from pymongo import MongoClient
# #     client = MongoClient('localhost:27017')
# #     db = client
# #     posts = db.simple
# #     x = { "Quaters_Number": employee}
# #     posts.delete(x)
#     return render(request,"quater_master(1).html")