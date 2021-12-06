nome = input('Digite o nome: ')
idade = int(input ('Digite a idade: '))
if idade >=65: #se idade for maior ou igual a 65 então...
    print('Paciente ' + nome + ' possui atendimento prioritário!')
else: #aqui só vai cair se a idade for menor que 65
    print('Paciente ' + nome + ' NÃO possui atendimento prioritário!')
