from validate_docbr import CPF#PYPI
from validate_docbr import CNPJ#PYPI

class Documento:

    @staticmethod
    def criar_documento(documento):
        if(len(documento) == 11):
            return DocCpf(documento)

        elif(len(documento) == 14):
            return DocCnpj(documento)
        else:
            raise ValueError("Invalio Documento")


class DocCpf:
    def __init__(self,documento):
        if(self.valida_cpf(documento)):
            self.cpf = documento
        else:
            raise ValueError("Its a Wrong CPF")

    def valida_cpf(self,documento):
        if(len(documento) == 11):
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("CPF Invalido")

    def fatiamento(self):#Fatiamente String do CPF
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.fatiamento()


class DocCnpj:
    def __init__(self,documento):
        if(self.valida_cnpj(documento)):
            self.cnpj = documento
        else:
            raise ValueError("Wrong CNPJ")

    def valida_cnpj(self,cnpj):
        if(len(cnpj)==14):
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise  ValueError("Wrong Cnpj!!!")

    def fatiamento2(self):#Fatiamento String do CNPJ
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.fatiamento2()

