from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from .models import Paciente



def index(request):
    return render(request, 'siteafr/index.html')

def doacao(request):
    return render(request, 'siteafr/doacao.html')

def atendimento(request):
    return render(request, 'siteafr/atendimento.html')

def nossahistoria(request):
    return render(request, 'siteafr/nossahistoria.html')

def governanca(request):
    return render(request, 'siteafr/governanca.html')

def transparencia(request):
    return render(request, 'siteafr/transparencia.html')

def certificacoes(request):
    return render(request, 'siteafr/certificacoes.html')

def reabilitacao(request):
    return render(request, 'siteafr/reabilitação.html')

def cooperacao(request):
    return render(request, 'siteafr/cooperacao.html')

def sac(request):
    return render(request, 'siteafr/sac.html')

def visita(request):
    return render(request, 'siteafr/visita.html')

def trabalheconosco(request):
    return render(request, 'siteafr/trabalheconosco.html')

def voluntariado(request):
    return render(request, 'siteafr/voluntariado.html')

def unidadefluminense(request):
    return render(request, 'siteafr/unidadefluminense.html')

def unidadelisaura(request):
    return render(request, 'siteafr/unidadelisaura.html')

def afrmais(request):
    return render(request, 'siteafr/afrmais.html')

def depmedico(request):
    return render(request, 'siteafr/depmedico.html')

def oficinaorto(request):
    return render(request, 'siteafr/oficinaorto.html')

def fag(request):
    return render(request, 'siteafr/fag.html')

def editais(request):
    return render(request, 'siteafr/editais.html')

def captacao(request):
    return render(request, 'siteafr/parceiroscaptacao.html')

def imprensa(request):
    return render(request, 'siteafr/imprensa.html')

def guia(request):
    return render(request, 'siteafr/guia.html')

def privacidade(request):
    return render(request, 'siteafr/privacidade.html')

def sistema_restrito_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('sistema-restrito-crud')
        else:
            return render(request, 'siteafr/sistema-restrito-login.html', {'erro': 'Usuário ou senha inválidos'})

    return render(request, 'siteafr/sistema-restrito-login.html')

from django.shortcuts import render
from .models import Paciente


@login_required(login_url="/sistema-restrito-login/")
def sistema_restrito_crud(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        idade = request.POST.get('idade')
        telefone = request.POST.get('telefone')

        if nome and email and idade and telefone:
            Paciente.objects.create(nome=nome, email=email, idade=idade, telefone=telefone)
            return redirect('sistema-restrito-crud')

    pacientes = Paciente.objects.all()
    return render(request, "siteafr/sistema-restrito-crud.html", {"pacientes": pacientes})



@login_required(login_url="/sistema-restrito-login/")
def delete_paciente(request, pk):
    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, pk=pk)
        paciente.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Método não permitido.'})

@login_required(login_url="/sistema-restrito-login/")
def update_paciente(request, pk):
    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, pk=pk)
        paciente.nome = request.POST.get('nome', paciente.nome)
        paciente.email = request.POST.get('email', paciente.email)
        paciente.idade = request.POST.get('idade', paciente.idade)
        paciente.telefone = request.POST.get('telefone', paciente.telefone)
        paciente.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Método não permitido.'})

@login_required(login_url="/sistema-restrito-login/")
def gerar_relatorio_historico(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "Relatório de Pacientes")

    pacientes = Paciente.objects.all()

    y = 770
    p.setFont("Helvetica", 12)
    for paciente in pacientes:
        texto = f"ID: {paciente.id} | Nome: {paciente.nome} | Email: {paciente.email} | Idade: {paciente.idade} | Tel: {paciente.telefone}"
        p.drawString(50, y, texto)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800

    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_pacientes.pdf"'
    return response

def gerar_grafico(request):
    pacientes = Paciente.objects.all()

    faixas = {'0–18': 0, '19–30': 0, '31–50': 0, '51+': 0}

    for p in pacientes:
        idade = p.idade
        if idade <= 18:
            faixas['0–18'] += 1
        elif idade <= 30:
            faixas['19–30'] += 1
        elif idade <= 50:
            faixas['31–50'] += 1
        else:
            faixas['51+'] += 1

    categorias = list(faixas.keys())
    valores = list(faixas.values())

    plt.figure(figsize=(8, 6))
    plt.bar(categorias, valores, color='#c71b1f')
    plt.title('Distribuição por Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Número de Pacientes')
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagem_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()

    return render(request, 'siteafr/grafico.html', {'grafico': imagem_base64})