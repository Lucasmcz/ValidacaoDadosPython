from cpf_cnpj import Documento


exe = "35379838000112"
exe_cpf = "44506596005"#5

documento = Documento.criar_documento(exe)
documento2 = Documento.criar_documento(exe_cpf)

print("O CNPJ: {}".format(documento))
print("O CPF: {}".format(documento2))
