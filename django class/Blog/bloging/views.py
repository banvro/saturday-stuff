from django.shortcuts import render, redirect
from bloging.models import contactUs
from django.contrib import messages
# Create your views here.

def homepage(request):
    return render(request, "home.html")

def aboutuspage(request):
    return render(request, "about.html")

def servicesuspage(request):
    return render(request, "services.html")

def contactuspage(request):
    return render(request, "contact.html")


def savingdata(request):
    if request.method == "POST":
        name = request.POST.get("fname")
        email = request.POST.get("email")
        number = request.POST.get("mob")
        messg = request.POST.get("msg")

        data = contactUs(name = name, user_email = email, phon_nmbr = number, message = messg)

        data.save()

        messages.success(request, "your form data saved sucessfullyy in database...!")

        return redirect("contact")



def showingdata(request):
    data = contactUs.objects.all()

    return render(request, "showingForm.html", {"all_data" : data})


def deletethis(request, card_id):
    data = contactUs.objects.get(id = card_id)
    data.delete()

    messages.warning(request, "you record deleteed sucessfully from database....")

    return redirect("show")


def updatedata(request, myid):
    data = contactUs.objects.get(id = myid)

    return render(request, "updatecontact.html", {"data" : data})



def updatedatanow(request, myid):
    data = contactUs.objects.get(id = myid)
    if request.method == "POST":
        name = request.POST.get("fname")
        email = request.POST.get("email")
        number = request.POST.get("mob")
        messg = request.POST.get("msg")

        data.name = name 
        data.user_email = email
        data.phon_nmbr = number
        data.message = messg

        data.save()

        messages.success(request, "data update sucessfully in database...!")

        return redirect("show")