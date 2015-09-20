from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from utils import salvar_foto
from cotolengo.settings import MEDIA_ROOT

def escolher_unidade(request):
	unidades = Unidade.objects.all()
	if (len(unidades) == 1):
		unidade = unidades[0]
		return redirect('formulario', unidade.sigla)
	return render(request, 'escolher_unidade.html', { "unidades" : Unidade.objects.all() })

def obrigado(request, sigla_unidade):
	try:
		unidade = Unidade.objects.get(sigla__iexact=sigla_unidade)
		return render(request, 'obrigado.html', { "unidade" : unidade })
	except Unidade.DoesNotExist, e:
		return redirect('escolher_unidade')

def formulario(request, sigla_unidade):
	if request.method == 'POST':
		return _cadastrar_doacao(request, sigla_unidade)
	else:
		return _exibir_formulario(request, sigla_unidade)


def _exibir_formulario(request, sigla_unidade):
	try:
		unidade = Unidade.objects.get(sigla__iexact=sigla_unidade)
		return render(request, 'formulario.html', { "unidade" : unidade })	
	except Unidade.DoesNotExist, e:
		return escolher_unidade(request)

def _cadastrar_doacao(request, sigla_unidade):
	#try:

	unidade = Unidade.objects.get(sigla__iexact=sigla_unidade)

	doador_nome = request.POST['doador_nome']
	doador_email = request.POST['doador_email']
	doador_telefone = request.POST['doador_telefone']

	endereco_logradouro = request.POST['endereco_logradouro']
	endereco_complemento = request.POST['endereco_complemento']
	endereco_bairro = request.POST['endereco_bairro']
	endereco_cep = request.POST['endereco_cep']
	endereco_cidade = request.POST['endereco_cidade']
	endereco_referencia = request.POST['endereco_referencia']
	
	doacao_doacao = request.POST['doacao_doacao']
	doacao_observacoes = request.POST['doacao_observacoes']
	
	endereco = Endereco(
		logradouro=endereco_logradouro,
		complemento=endereco_complemento,
		bairro=endereco_bairro,
		cep=endereco_cep,
		cidade=endereco_cidade,
		referencia=endereco_referencia
		)

	endereco.save()

	doador = Doador(
		nome=doador_nome,
		email=doador_email,
		telefone=doador_telefone,
		endereco=endereco
		)

	doador.save()

	intencao_doacao = IntencaoDoacao(
		unidade=unidade,
		doador=doador,
		doacao=doacao_doacao,
		observacoes=doacao_observacoes,
		)

	intencao_doacao.save()

	if ('doacao_foto' in request.FILES):
		intencao_doacao.foto = request.FILES['doacao_foto']
		intencao_doacao.save()

	return render(request, 'obrigado.html', { "unidade" : unidade })
	#except:
	#		return redirect('escolher_unidade')
