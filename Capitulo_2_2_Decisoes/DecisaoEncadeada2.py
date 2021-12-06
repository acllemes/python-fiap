nome = input ('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_viral = input('Suspeita de Covid-19? ').upper()

#PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_viral == 'SIM':
    print('Encaminhe o paciente para sala AMARELA')
elif doenca_viral == 'NÃO':
    print('Encaminhe o paciente para sala BRANCA')
else:
    print('Responda a suspeita de COVID-19 com SIM ou NÃO')

#SEGUNDO PROBLEMA A SER RESOLVIDO

if idade >= 65:
    print('Paciente COM prioridade')
else:
    genero = input('Digite o gênero do paciente: ').upper()
    if genero == 'FEMININO' and idade > 15:
        gravidez = input('A paciente está grávida? ').upper()
        if gravidez == 'SIM':
            print('Paciente COM prioridade')
        else:
            print('Paciente SEM prioridade')
    else:
        print('Paciente SEM prioridade')
