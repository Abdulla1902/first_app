from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
def abdulla(request):
    return render(request, 'abdulla.html')
