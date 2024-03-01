
grifinoria = 0
lufalufa = 0
sonserina = 0
ravenclaw = 0

print('O CHAPÉU SELETOR')

print('Q1. Você prefere o amanhecer ou escuridão?')
print('1 amanhecer')
print('2 escuridão')
resposta = int(input('Responda com 1 ou 2: '))

if resposta == 1:
  grifinoria += 1
  ravenclaw += 1

elif resposta == 2:
  lufalufa += 1
  sonserina += 1

else:
  print('resposta errada')

print('Q2. Quando eu morrer, quero ser lembrado por ter sido:')
print('1 o bom')
print('2 o grande')
print('3 o sábio')
print('4 o corajoso')

resposta = int(input('Responda de 1 a 4: '))
if resposta == 1:
  lufalufa += 2
elif resposta == 2:
  sonserina += 2
elif resposta == 3:
  ravenclaw += 2
elif resposta == 4:
  grifinoria += 2
else:
  print('resposta errada')

print('Q.3 Qual instrumento mais te agrada?')
print('1 violino')
print('2 trombeta')
print('3 piano')
print('4 tambor')

int(input('Responda de 1 a 4: '))

if resposta == 1:
  sonserina += 4
elif resposta == 2:
  lufalufa += 4
elif resposta == 3:
  ravenclaw += 4
elif resposta == 4:
  grifinoria += 4
else:
  print('resposta errada')

if grifinoria >= lufalufa and grifinoria >= sonserina and grifinoria >= ravenclaw:
  print('VC É GRIFINÓRIA 🦁')
elif lufalufa >= sonserina and lufalufa >= ravenclaw:
  print ('VC É LUFALUFA 🦨')
elif sonserina >= ravenclaw:
  print ('vc é sonserina 🐍')
else:
  print ('VC É RAVENCLAW !!')