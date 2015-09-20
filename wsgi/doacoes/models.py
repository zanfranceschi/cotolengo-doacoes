#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import os
import uuid


class Unidade(models.Model):
	class Meta:
		verbose_name = u"Unidade"
		verbose_name_plural=u"Unidades"

	sigla = models.CharField(max_length=5)
	nome = models.CharField(max_length=50)
	url_institucional = models.URLField(verbose_name="site da Unidade")

	def __unicode__(self):
		return self.nome


class Endereco(models.Model):
	class Meta:
		verbose_name = u"Endereço"
		verbose_name_plural = u"Endereços"

	logradouro = models.CharField(max_length=200)
	complemento = models.CharField(max_length=50)
	bairro = models.CharField(max_length=50)
	cep = models.CharField(max_length=10)
	cidade = models.CharField(max_length=50)
	referencia = models.TextField(null=True)
	
	def __unicode__(self):
		return "{logradouro} - {complemento} / {bairro}, {cep} / {cidade}".format(
			logradouro=self.logradouro,
			complemento=self.complemento,
			bairro=self.bairro,
			cep=self.cep,
			cidade=self.cidade
			)


class Doador(models.Model):
	class Meta:
		verbose_name = u"Doador"
		verbose_name_plural=u"Doadores"

	nome = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	telefone = models.CharField(max_length=15)
	endereco = models.ForeignKey(Endereco)

	def __unicode__(self):
		return "{nome} ({email}, {telefone})".format(nome=self.nome, email=self.email, telefone=self.telefone)

def nome_foto(instancia, nome_arquivo):
	ext = nome_arquivo.split('.')[-1]
	nome_arquivo = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('fotos', nome_arquivo)

class IntencaoDoacao(models.Model):
	class Meta:
		verbose_name = u"Intenção de Doação"
		verbose_name_plural=u"Intenções de Doação"

	unidade = models.ForeignKey(Unidade)
	cadastro = models.DateTimeField(auto_now_add=True)
	doador = models.ForeignKey(Doador)
	doacao = models.TextField()
	foto = models.ImageField(upload_to=nome_foto, null=True)
	observacoes = models.TextField(null=True)

	def __unicode__(self):
		return self.doacao


class AdministradorUnidade(models.Model):
	class Meta:
		verbose_name = u"Administrador de Unidade"
		verbose_name_plural=u"Administradores de Unidade"
	user = models.OneToOneField(User, related_name='administrador')
	unidade = models.ForeignKey(Unidade)

	def __unicode__(self):
		return "{user} / {unidade}".format(user=self.user, unidade=self.unidade.nome)
