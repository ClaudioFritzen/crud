from django.shortcuts import render, redirect
from .models import Pessoa

# importações para mensagens do bootstrap
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    if request.method == "GET":
        pessoas = Pessoa.objects.all()
        return render(request, "index.html", {"pessoas": pessoas})
    elif request.method == "POST":
        vnome = request.POST.get("nome")
        
        pessoas = Pessoa.objects.filter(nome=vnome)
        print(vnome)
        if pessoas.exists():
            messages.add_message(request, constants.ERROR, 'Nome já existe')
            return redirect(home)
        else:
            messages.add_message(request, constants.SUCCESS, "Nome cadastrato")
            vnome = Pessoa.objects.create(nome=vnome)
            return redirect(home)
            #return render (request, "Index.html", {"pessoa": pessoas})

    #       
    
def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {'pessoa': pessoa})

def update(request, id):
    vnome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.save()
    messages.add_message(request, constants.INFO, 'Dados Atualizado com sucesso.')
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    messages.add_message(request, constants.WARNING, 'Dados excluido com sucesso')
    return redirect(home)
    