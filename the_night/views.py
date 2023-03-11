from django.shortcuts import render

# Create your views here.
def knight(request):
    return render(request,'knight.html')