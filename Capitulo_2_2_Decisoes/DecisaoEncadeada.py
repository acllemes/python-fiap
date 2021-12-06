nome = input ('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_viral = input('Suspeita de Covid-19? ').upper()

if idade >= 65: #idade maior ou igual a 65 anos....
    print('Paciente COM prioridade')
    if doenca_viral == 'SIM': #indica comparação
        print('Encaminhe o paciente para sala AMARELA')
    elif doenca_viral == 'NÃO': #indica comparação
        print('Encaminhe o paciente para sala BRANCA')
    else:
        print('Responda a suspeita de COVID-19 com SIM ou NÃO')
else:
    print('Paciente SEM prioridade')
    if doenca_viral == 'SIM': #indica comparação
        print('Encaminhe o paciente para sala AMARELA')
    elif doenca_viral == 'NÃO': #indica comparação
        print('Encaminhe o paciente para sala BRANCA')
    else:
        print('Responda a suspeita de COVID-19 com SIM ou NÃO')