from django.shortcuts import render, HttpResponse
from django.views.generic import View
# Create your views here. Sabado Sabado

class Sabado(View):
	def get(self,request):
		#return HttpResponse('Hail Mortal!')
		return render(request, 'hola.html')



