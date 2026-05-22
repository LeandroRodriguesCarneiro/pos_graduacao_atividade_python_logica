import getpass

from cls import Drink, VendingMachine, Money
from .suport import pagination, get_number_value

def admin_menu(machine):
    while True:
        print('\n' + '=' * 40)
        print('      MODO ADMINISTRADOR')
        print('=' * 40)

        print(
            '\n1 - Listar produtos'
            '\n2 - Cadastrar produto'
            '\n3 - Editar produto'
            '\n4 - Remover produto'
            '\n5 - Listar estoque de moedas/notas'
            '\n0 - Voltar'
        )

        option = input('\nEscolha uma opção: ')

        match option:

            case '1':
                machine.show_drinks()
                pagination()

            case '2':
                code = int(get_number_value('Código: '))
                name = input('Nome: ')
                price = int(
                    float(input('Preço (ex: 5.50): ')) * 100
                )
                stock = int(get_number_value('Quantidade em estoque: '))

                product = Drink(code, name, price, stock)
                machine.add_drink(product)

                print('\nProduto cadastrado com sucesso!')
                pagination()

            case '3':
                print('\n')
                machine.show_drinks()
                code = int(get_number_value('Digite o código do produto: '))

                product = machine.get_drink(code)

                if not product:
                    print('\nProduto não encontrado!')
                    continue

                print('\nDeixe vazio para manter o valor atual.')

                name = input(f'Nome ({product.name}): ')
                price = input(
                    f'Preço ({product.price/100:.2f}): '
                )
                stock = input(
                    f'Estoque ({product.stock}): '
                )

                if name:
                    product.name = name

                if price:
                    product.price = int(
                        float(price.replace(',', '.')) * 100
                        )

                if stock:
                    product.stock = int(stock)

                print('\nProduto atualizado!')
                pagination()

            case '4':
                machine.show_drinks()
                code = int(get_number_value('Digite o código do produto: '))

                if machine.remove_drink(code) is None:
                    print('\nProduto removido!')
                else:
                    print('\nProduto não encontrado!')
                pagination()

            case '5':
                machine.show_money()
                pagination()

            case '0':
                pagination()
                return

            case _:
                print('\nOpção inválida!')
                pagination()

def sales_menu(machine):
    while True:

        print('\n' + '=' * 40)
        print('      MÁQUINA DE BEBIDAS')
        print('=' * 40)

        machine.show_drinks()

        print('\n0 - Voltar')

        code = input('\nDigite o código do produto: ')

        if code == '0':
            pagination()
            return

        product = machine.get_drink(int(code))

        if not product:
            print('\nProduto inválido!')
            continue

        machine.buy_drink(product)
        pagination()

def start(machine: VendingMachine):

    while True:

        print('\n' + '=' * 40)
        print('     SISTEMA VENDING MACHINE')
        print('=' * 40)

        print(
            '\n1 - Entrar como administrador'
            '\n2 - Acessar terminal de vendas'
            '\n0 - Sair'
        )

        option = input('\nDigite uma opção: ')

        match option:

            case '1':

                user = input('\nUsuário: ')
                password = getpass.getpass('Senha: ')

                if user == 'admin' and password == 'admin':
                    admin_menu(machine)
                else:
                    print('\nUsuário ou senha inválidos!')

            case '2':
                sales_menu(machine)

            case '0':
                print('\nEncerrando sistema...')
                return

            case _:
                print('\nOpção inválida!')