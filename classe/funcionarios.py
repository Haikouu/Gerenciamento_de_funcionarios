class Funcionarios:
    def __init__(self, nome, cpf, salario_base):
        self.nome = nome  
        self.cpf = cpf      
        self.salario_base = salario_base 

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valor):
        if not valor:
            raise ValueError("Erro: O CPF não pode ser vazio.")
        self.__cpf = valor

    @property
    def salario_base(self):
        return self.__salario_base
    
    @salario_base.setter
    def salario_base(self, valor):
        if valor < 0:
            raise ValueError("Erro: O salário não pode ser negativo.")
        self.__salario_base = valor 

    def calcular_salario(self):
        return self.salario_base
    
    def exibir_dados(self):
        print(f"Nome: {self.nome} | CPF: {self.cpf} | Salário Final: R$ {self.calcular_salario():.2f}")


class Clt(Funcionarios):
    def __init__(self, nome, cpf, salario_base, bonus):
        super().__init__(nome, cpf, salario_base)
        self.__bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.__bonus
    

class Freelancer(Funcionarios):
    def __init__(self, nome, cpf, valor_por_projeto, quantidade_projeto):
        super().__init__(nome, cpf, 0)
        self.__valor_por_projeto = valor_por_projeto
        self.__quantidade_projeto = quantidade_projeto

    def calcular_salario(self):
        return self.__valor_por_projeto * self.__quantidade_projeto
    

class Estagiario(Funcionarios):
    def __init__(self, nome, cpf, bolsa, desconto):
        super().__init__(nome, cpf, bolsa)
        self.__desconto = desconto

    def calcular_salario(self):
        return self.salario_base - self.__desconto

