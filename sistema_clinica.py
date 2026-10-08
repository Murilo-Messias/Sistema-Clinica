fila_espera = []
historico_atendimentos = []
from datetime import datetime

while True :
  print('----Sistema Integrado de Clínica Médica----')
  print('1 - Cadastrar Paciente  ')
  print('2 - Atender Paciente  ')
  print('3 - Desfazer Último Atendimento ')
  print('4 - Relatório')
  print('5 - Sair ')

  ope = input('Digite a opção desejada: ')

  if ope == '1' :

   n = input('Insira o nome do paciente:')
   s = input('Informe o sintoma deste paciente:')
   nome_sintoma = (n, s)
   fila_espera.append(nome_sintoma)

  elif ope == '2' :

    if len(fila_espera) == 0:
            print('Não há pacientes na fila.')
    else:
        paciente = fila_espera.pop(0)
        nome = paciente[0]
        dh = datetime.now()
        historico_atendimentos.append((nome, dh))
        print(f'Paciente {nome} atendido em {dh.strftime("%d/%m/%Y %H:%M")}')

  elif ope == '3':

        if len(historico_atendimentos) == 0:
            print('Não há atendimentos para desfazer.')

        else:
            nome, data_hora = historico_atendimentos.pop()
            sintoma = input(f'Informe novamente o sintoma de {nome} para retornar à fila:')
            fila_espera.insert(0, (nome, sintoma))
            print(f'Atendimento de {nome} cancelado.')


  elif ope == '4':

        print('--- RELATÓRIO ---')
        print('Pacientes aguardando:')

        if len(fila_espera) == 0:
            print('Nenhum paciente na fila.')

        else:
            for nome, sintoma in fila_espera:
             print(f'- {nome} ({sintoma})')

        print(f'Total na fila: {len(fila_espera)}')
        print(f'Total atendidos: {len(historico_atendimentos)}')

  elif ope == '5':

        print('Fechando e encerrando o sistema de atendimento...')
        break

  else:
        print('Opção inválida! Digite apenas a opção na qual você quer, por exemplo: 1, 2, 3, 4 ou 5.')

