from django.shortcuts import render, redirect

def cadastro(request):
	if request.method == 'POST':
		nome = request.POST['nome']
		email = request.POST['email']
		senha = request.POST['password']
		senha2 = request.POST['password2']
		print(f'{nome}\n{email}\n{senha}\n{senha2}')
		return redirect('login')
	else:
		return render(request, 'usuarios/cadastro.html')

def login(request):
	return render(request, 'usuarios/login.html')

def logout(request):
	pass

def dashboard(request):
	pass