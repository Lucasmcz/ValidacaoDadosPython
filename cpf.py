from validate_docbr import CPF#PYPI
class Cpf:
    def __init__(self,documento):
        documento = str(documento)
        if(self.valida_cpf(documento)):
            self.cpf = documento
        else:
            raise ValueError("CPF Invalido!!!")
    def valida_cpf(self,documento):
        if(len(documento) == 11):
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("CPF Invalido")


    def fatiamento(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.fatiamento()
