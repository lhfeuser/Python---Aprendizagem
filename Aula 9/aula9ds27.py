nome = str(input('Digite seu nome: ')).strip()
n = nome.split()

print('Prazer em te conhecer, {}'.format(nome))
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu útimo nome é {}'.format(n[len(n)-1]))