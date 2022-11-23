from django.shortcuts import render



def home(request):
	data = { }
	data['pessoa'] = ''
	return render(request, 'index.html', data)

def form(request):
	return render(request, 'form.html')




