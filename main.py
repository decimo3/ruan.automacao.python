# coding: utf8

import sapHandler

class main:
  print("Programa de automação de rotinas do Mestre Ruan")
  print("===============================================")
  print("")
  print("Digite o comando abaixo que deseja executar ou AJUDA para mostrar as opções disponíveis.")
  print("")
  while True:
    resposta = input("> ")
    resposta = resposta.lower()
    argumentos = resposta.split(' ')
    if argumentos[0] == "sair":
      break
    if argumentos[0] == "ajuda":
      print("")
      print("RELATORIO [0-9]")
      print("\tAutomatiza o relatório de uma semana se nenhum argumento for informado")
    if argumentos[0] == "relatorio":
      try:
        sapHandler.sap.relatorio(int(argumentos[1]))
      except:
        sapHandler.sap.relatorio()