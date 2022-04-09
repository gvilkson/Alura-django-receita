from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def cadastro(request):
	if request.method == 'POST':
		nome = request.POST['nome']
		email = request.POST['email']
		senha = request.POST['password']
		senha2 = request.POST['password2']

		if not nome.strip():
			print('O campo nome não pode ficar em branco!')
			return redirect('cadastro')

		if not email.strip():
			print('O campo email não pode ficar em branco!')
			return redirect('cadastro')

		if not senha.strip():
			print('O campo senha não pode ficar em branco!')
			return redirect('cadastro')

		if User.objects.filter(email=email).exists():
			print('Usuário já cadastrado no sistema!')
			return redirect('cadastro')

		user = User.objects.create_user(username=nome, email=email, password=senha)
		user.save()

		print(f'Usuário:{nome} cadastrado com sucesso')
		return redirect('login')
	else:
		return render(request, 'usuarios/cadastro.html')

def login(request):
	return render(request, 'usuarios/login.html')

def logout(request):
	pass

def dashboard(request):
	pass