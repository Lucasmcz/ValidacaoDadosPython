from validate_docbr import CNPJ#PYPI
from cpf_cnpj import Documento

#cpf_um = Cpf(12354367996)
#print(cpf_um)

exe = "35379838000112"
exe_cpf = "44506596005"#5

documento = Documento.criar_documento(exe)
documento2 = Documento.criar_documento(exe_cpf)

print("O CNPJ: {}".format(documento))
print("O CPF: {}".format(documento2))