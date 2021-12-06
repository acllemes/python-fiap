nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
prioridade = 'NÃO'
if idade >=65: #se idade for maior ou igual a 65 anos então...
    prioridade = 'SIM'
print('O paciente ' + nome + ' possui atendimento prioritário? ' + prioridade)