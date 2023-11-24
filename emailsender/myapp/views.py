from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.mail import send_mail

# Create your views here.
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
        

            send_mail(subject, message, 'taruntiwari.mighty4113@gmail.com', [to_email])

            return redirect('success')
    else:
        form = EmailForm()
    return render(request,'myapp/send_email.html',{'form':form})


def success(request):
    return render(request,'myapp/success.html')

def home_view(request):
    return render(request, 'myapp/home.html')