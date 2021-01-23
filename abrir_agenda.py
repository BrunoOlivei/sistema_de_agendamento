import csv


def abre_agenda_do_dia(arquivo):  # Função para abrir arquivo CSV com a relação dos pacientes agendados no dia
    with open(arquivo, newline='') as agenda:
        reader = csv.reader(agenda, delimiter=';', quotechar='|')
        agenda = []
        for row in reader:
            agenda.append({row[1]: {'nome': row[3], 'telefone': row[6]}})
    return agenda