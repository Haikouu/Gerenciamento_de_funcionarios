import sistemas.sistema as sistema
from classe.funcionarios import Clt, Freelancer, Estagiario

def exibir_menu():
    
    while True:
        print("\n" + "="*35)
        print("   GESTOR DE FUNCIONÁRIOS")
        print("="*35)
        print("1 - Cadastrar Funcionário")
        print("2 - Listar Funcionários")
        print("3 - Mostrar Salário de Todos")
        print("4 - Mostrar Folha Salarial Total")
        print("5 - Excluir Funcionário")
        print("0 - Sair")
        print("="*35)

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n--- Novo Cadastro ---")
            nome = input("Nome: ")
            cpf = input("CPF: ")

            print("\nQual o regime de trabalho?")
            print("1. CLT")
            print("2. Freelancer")
            print("3. Estagiário")
            tipo = input("Opção: ")


            if tipo == "1":
                salario = float(input("Salário Base: R$ "))
                bonus = float(input("Bônus: R$ "))
                novo = Clt(nome, cpf, salario, bonus)
                categoria = "CLT"

            elif tipo == "2":
                valor_proj = float(input("Valor por Projeto: R$ "))
                qtd_proj = int(input("Quantidade de Projetos: "))
                novo = Freelancer(nome, cpf, valor_proj, qtd_proj)
                categoria = "Freelancer"

            elif tipo == "3":
                bolsa = float(input("Valor da Bolsa: R$ "))
                desconto = float(input("Valor do Desconto: R$ "))
                novo = Estagiario(nome, cpf, bolsa, desconto)
                categoria = "Estagiário"

            else:
                print("\n[!] Tipo inválido. Cadastro cancelado.")
                continue

            sistema.adicionar_funcionario(categoria, novo)

        elif opcao == "2":
            sistema.listar_funcionarios()
            input("\n[Pressione ENTER para voltar ao menu...]")

        elif opcao == "3":
            sistema.calcular_salario_todos()
            input("\n[Pressione ENTER para voltar ao menu...]")

        elif opcao == "4":
            sistema.calcular_folha_salarial()
            input("\n[Pressione ENTER para voltar ao menu...]")
            
        elif opcao == "5":
            print("\n--- Excluir Funcionário ---")
            cpf_alvo = input("Digite o CPF do funcionário que deseja excluir: ")
            sistema.excluir_funcionario(cpf_alvo)
            input("\n[Pressione ENTER para voltar ao menu...]")

        elif opcao == "0":
            print("\nEncerrando o sistema... Até mais!")
            break 

        else:
            print("\n[!] Opção inválida. Tente novamente.")
