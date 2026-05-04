from classe.funcionarios import clt, freelancer, estagiario


funcionarios = {
    "CLT": {
        "101": clt("Ana Silva", "101", 3500.0, 500.0),
        "102": clt("Bruno Souza", "102", 4000.0, 600.0),
        "103": clt("Carla Dias", "103", 3200.0, 300.0),
        "104": clt("Diego Lins", "104", 2800.0, 450.0),
        "105": clt("Elena Vaz", "105", 5500.0, 1200.0),
    },
    "Freelancer": {
        "201": freelancer("Fabio Araujo", "201", 1200.0, 3),
        "202": freelancer("Gisele Reis", "202", 1500.0, 2),
        "203": freelancer("Helio Neto", "203", 900.0, 5),
        "204": freelancer("Igor Gomes", "204", 2500.0, 1),
        "205": freelancer("Julia Mello", "205", 1100.0, 4),
    },
    "Estagiário": {
        "301": estagiario("Kauan Lima", "301", 1200.0, 50.0),
        "302": estagiario("Larissa Paz", "302", 1200.0, 0.0),
        "303": estagiario("Moacyr Luz", "303", 1000.0, 25.0),
        "304": estagiario("Nara Costa", "304", 1400.0, 80.0),
        "305": estagiario("Otavio Pires", "305", 1150.0, 30.0),
    }
}

def adicionar_funcionario(categoria, novo_funcionario):

    if categoria in funcionarios:
        funcionarios[categoria][novo_funcionario.cpf] = novo_funcionario
        print(f"Sucesso: {novo_funcionario.nome} adicionado em {categoria}.")
    else:
        print(f"Erro: Categoria {categoria} não existe.")

def listar_funcionarios():
    print("\n--- Listagem Completa ---")
    
    for categoria in funcionarios:
        print(f"\n>> {categoria}")
        grupo = funcionarios[categoria]
        for cpf in grupo:
            funcionario = grupo[cpf]
            funcionario.exibir_dados()

def calcular_salario_todos():
    print("\n--- Detalhamento de Pagamento ---")
    for categoria in funcionarios:
        grupo = funcionarios[categoria]
        for cpf in grupo:
            funcionario = grupo[cpf]
            valor = funcionario.calcular_salario()
            print(f"[{categoria}] {funcionario.nome}: R$ {valor:.2f}")

def calcular_folha_salarial():

    total_folha = 0

    for categoria in funcionarios:
        grupo = funcionarios[categoria]
        for cpf in grupo:
            total_folha += grupo[cpf].calcular_salario()

    print(f"\nValor total da folha de pagamento: R$ {total_folha:.2f}")
