print('-' * 30)
print('Sistema de Login')
print('-' * 30)

usuarios = ['Caio', 'Felipe', 'Manuela', 'Paula', 'Daniel', 'Camila']

while True:
    try:
        user = input('\nLogin: ')
        if user.title() in usuarios:
            print('\033[32mAcesso permitido!\033[m\n')
            break
        else:
            print('\033[31mAcesso negado!\033[m\n')
            raise NameError('Não cadastrado!')
            continue
    except Exception as e:
        print('Erro!')