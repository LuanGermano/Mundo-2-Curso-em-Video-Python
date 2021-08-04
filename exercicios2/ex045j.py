import random
valores = {
    'pedra': {
        'ganha': 'tesoura',
        'perde': 'papel'
    },
    'papel': {
        'ganha': 'pedra',
        'perde': 'tesoura'
    },
    'tesoura': {
        'ganha': 'papel',
        'perde': 'pedra'
    }
}

chaves = list(valores.keys())

inputusr = str(input('jogada: ')).lower().strip()

maquina = random.randint(0,2)

if valores[inputusr]:
  if valores[inputusr].get('ganha', '') == chaves[maquina]:
    print('ganhou')
  elif inputusr == chaves[maquina]:
    print('empate')
  else:
    print('perdeu')
else:
   print('invalido')