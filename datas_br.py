from _datetime import datetime, timedelta
class Data_Br:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_cadastro = [
            "Janeiro","Feveiro" , "Março","abril",
            "maio", "junho", "julho" ,"agosto",
            "setembro","outubro", "novembro", "dezembro"
        ]
        mes_castro = self.momento_cadastro.month
        return meses_cadastro[mes_castro-1]

    def dia_semana(self):
        dias_da_semana = [
            "Segunda","Terça","Quarta","Quinta","Sexta","Sabado","Domingo"
            ]
        dia_semana = self.momento_cadastro.weekday()
        return  dias_da_semana[dia_semana]

    def format_br(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y  %H:%M")
        return data_formatada
    def __str__(self):
        return self.format_br()

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() +timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro