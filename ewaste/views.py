from django.shortcuts import render
from ewaste.models import Contact
# Create your views here.
def home(request):
    return render(request, "home.html")

def about_us(request):
    return render(request, "about_us.html")

def contact(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone_no=request.POST.get("phone_no")
        description=request.POST.get("description")

        Contact.objects.create(
            name=name,
            email=email,
            phone_no=phone_no,
            description=description
        )
        return render(request, "contact.html", {"message": "Form submitted successfully"})

    return render(request, "contact.html")
