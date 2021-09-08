import requests#Chamar API IMPORTANTE 
class BuscaEndereco:

    def __init__(self,cep):
        cep = str(cep)
        if(self.cep_e_valido(cep)):
            self.cep = cep
        else:
            raise ValueError("CEP Invalido")

    def cep_e_valido(self,cep):
        if(len(cep) == 8):
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])
    def __str__(self):
        return self.acessa_viacep()

    def acessa_viacep(self):
        url = "https://viacep.com.br/ws/{}/json".format(self.cep)#Url de todas API do ViaCEP
        r = requests.get(url)
        dados = r.json()#metodo JSON(Dict)
        return(
            dados['bairro'],
            dados['localidade'],
            dados['uf'],


        )
