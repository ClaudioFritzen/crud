from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    print(pessoas)
    print("chegamos auqui]")
    return render(request, "index.html", {"pessoas": pessoas})