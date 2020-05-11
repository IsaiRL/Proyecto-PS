from django.template import Template, Context
from django.shortcuts import render, redirect
from bd import models
import Fron_end.back_end as back_end

#def get_client_ip(request):
#	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#	if x_forwarded_for:
#		ip = x_forwarded_for.split(',')[0]
#	else:
#		ip = request.META.get('REMOTE_ADDR')
#	return ip

def login(request):
	t = 'loggin.html'
	if request.method == 'GET':
		#t = 'loggin.html'
		return render(request, t)
	elif request.method == 'POST':
		if back_end.dejar_pasar_peticion_login(request):
			return render(request, t, {'errores': 'Todo ok'})
		else:
			return render(request, t, {'errores': 'muchos intentos fallidos'})
#		ip = get_client_ip(request)
#		timestamp = datetime.datetiem.now()
#		try:
#			registros = models.IPs.objects.get(ip=ip)
#		except:
