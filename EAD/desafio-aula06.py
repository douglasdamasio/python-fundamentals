class ContaCorrente():
    ''' Tentando abstrair uma conta corrente! '''
    def __init__(self, **kwargs):
        self.banco = kwargs['banco']
        self.agencia = kwargs['ag']
        self.conta = kwargs['conta']
        self.valor = kwargs['valor']

    def sacar(self, *args):
        self.valor -= args[0]

    def depositar(self, *args):
        self.valor += args[0]

    def transferir(self, **kwargs):
        self.sacar(kwargs['valor'])
        kwargs['conta'].depositar(kwargs['valor'])


class ContaPopunca(ContaCorrente):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.conta += '/500'
        self.juros = 0.005


    def render_juros(self):
        self.valor += self.valor * self.juros
        


conta_douglas = ContaCorrente(banco='Itau Unibanco', ag='6413', conta='18804-3', valor=500.00)
conta_guilherme = ContaPopunca(banco='Nubank', ag='0001', conta='90906-1', valor=500)
conta_douglas.sacar(20)
conta_douglas.depositar(50)
conta_douglas.transferir(valor=100, conta=conta_guilherme)
conta_guilherme.render_juros()
print(conta_guilherme.conta)

# conta_douglas.depositar(50)
# conta_douglas.transferir()

# conta_pop_douglas = ContaPopunca(banco='Itau Unibanco', ag='6413', conta='18804-3', valor=100)
# conta_pop_douglas.render_juros()

