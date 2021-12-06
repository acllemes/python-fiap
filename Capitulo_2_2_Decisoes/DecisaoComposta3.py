nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_viral = input('Suspeita de COVID 19? ').upper()

if idade >= 65 and doenca_viral == 'SIM': #idade maior ou igual a 65 e com covid....
 print('Paciente será direcionado para sala AMARELA - COM prioridade')

elif idade < 65 and doenca_viral == "SIM": #idade menor de 65 anos e com covid...
  print('Paciente será direcionado para sala AMARELA - SEM prioridade')

elif idade >= 65 and doenca_viral == "NAO": #idade maior ou igual a 65 sem covid...
  print('Paciente será direcionado para sala BRANCA - COM prioridade')

elif idade < 65 and doenca_viral == 'NÃO': #idade menor que 65 e sem covid...
  print('Paciente será direcionado para sala BRANCA - SEM prioridade')

else:
 print('Responda a suspeita de doença infectocontagiosa com SIM ou NAO')
