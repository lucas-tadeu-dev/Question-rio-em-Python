print()
print('Abaixo teremos alguns execícios básicos de matemática para quem está na primeira série: ')

perguntas = {
   'Pergunta 1': {
    'pergunta': 'Quanto é 2+2?',
    'respostas':{
      'a': '1',
      'b': '4',
      'c': '6',
      'd': '5',
      'e': '2'
    },
    'resposta_certa': 'b',
   },

   'Pergunta 2': {
    'pergunta': 'Quanto é 4*5?',
    'respostas':{
      'a': '30',
      'b': '16',
      'c': '9',
      'd': '20',
      'e': '10'
    },
    'resposta_certa': 'd',
   },
   'Pergunta 3': {
    'pergunta': 'Quanto é 0/6?',
    'respostas':{
      'a': '0',
      'b': '7',
      'c': '6',
      'd': '0.6',
      'e': '10'
    },
    'resposta_certa': 'a',
   },
   'Pergunta 4': {
    'pergunta': 'Quanto é 10/2?',
    'respostas':{
      'a': '3',
      'b': '4',
      'c': '10',
      'd': '2',
      'e': '5'
    },
    'resposta_certa': 'e',
   },
   'Pergunta 5': {
    'pergunta': 'Quanto é 10*80?',
    'respostas':{
      'a': '200',
      'b': '160',
      'c': '800',
      'd': '80',
      'e': '400'
    },
    'resposta_certa': 'c',
   },    
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
  print(f'{pk}: {pv["pergunta"]}')
  
  print('Respostas: ')
  for rk, rv in pv['respostas'].items():
    print(f'[{rk}]:{rv}')
  
  resposta_usuario = input('Sua Resposta: ')

  if resposta_usuario == pv['resposta_certa']:
    print('EHHHHH!!! Você acertou!!!')
    respostas_certas += 1
  else:
    print('IXII!!! Você ERROUU!!!')


  print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas/ qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')