nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_viral = input('Suspeita de COVID-19? ').upper() #converter para letras maiúscula
if idade >= 65:
    print('Paciente ' + nome + ' possui atendimento prioritario!')
elif doenca_viral == 'SIM':
    print('Paciente ' + nome + ' deve ser direcionado para sala de espera reservada.')
else:
    print('Paciente ' + nome + ' NÃO possui atendimento prioritário e pode aguardar na sala comum!')

