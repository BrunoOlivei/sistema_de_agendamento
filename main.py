from abrir_agenda import abre_agenda_do_dia
import selenium

print("Sistema de confirmação de consulta")

for linha in abre_agenda_do_dia("agenda_25_01_2021.csv"):
    for hora in linha.keys():
        horario_agendado = hora
    for agendado in linha:
        paciente = linha[agendado]
        nome_paciente = paciente['nome']
        tel_paciente = paciente['telefone']

print(tel_paciente)