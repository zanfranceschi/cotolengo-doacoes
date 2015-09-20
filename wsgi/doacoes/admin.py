from django.contrib import admin
from .models import *
from cotolengo.settings import STATIC_URL
import os
import sys

class IntencaoDoacaoAdmin(admin.ModelAdmin):
	list_display=['doacao', 'cadastro', 'unidade', 'foto_tag_thumb']
	exclude = ['foto',]
	search_fields = [
		'doacao', 
		'doador__endereco__cidade',
		'doador__endereco__logradouro',
		'doador__email',
		'doador__nome',
		'doador__telefone',
		]

	readonly_fields=['unidade', 'doacao', 'foto_tag', 'doador', 'observacoes', 'endereco']

	def endereco(self, obj):
		return obj.doador.endereco

	def foto_tag_thumb(self, obj):
		if (obj.foto):
			return "<img src='{url}' style='height: 42px;' class='admin-foto' />".format(url=os.path.join(STATIC_URL, obj.foto.url))
		else:
			return ""

	def foto_tag(self, obj):
		if (obj.foto):
			return "<img src='{url}' />".format(url=os.path.join(STATIC_URL, obj.foto.url))
		else:
			return "sem foto"
	
	foto_tag.short_description = "foto"
	foto_tag.allow_tags = True

	foto_tag_thumb.short_description = "foto"
	foto_tag_thumb.allow_tags = True

	def get_queryset(self, request):
		qs = super(IntencaoDoacaoAdmin, self).get_queryset(request)
		try:
			return qs.filter(unidade=request.user.administrador.unidade)
		except:
			return qs


admin.site.register(Endereco)
admin.site.register(Doador)
admin.site.register(IntencaoDoacao, IntencaoDoacaoAdmin)
admin.site.register(Unidade)
admin.site.register(AdministradorUnidade)