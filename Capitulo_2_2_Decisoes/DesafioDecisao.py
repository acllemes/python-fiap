print('ADM para administrador')
print('USR para usuario')
print('GUEST para visitantes')
nivel = input('Digite o nível de acesso: ').upper()
if nivel == 'ADM' or nivel == 'USR':
    genero = input('Digite o seu gênero: ').upper()
    if nivel == 'ADM':
        if genero == 'FEMININO':
            print('Olá administradora')
        else:
            print('Olá administrador')
elif nivel == 'GUEST':
    print('Olá visitante')
else:
    print('Olá desconhecido(a')
