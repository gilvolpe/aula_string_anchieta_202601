'''
Criar 3 variaveis e armazenar as informacoes
de user, password e dominio
Depois apresentar as 3 variaveis
'''
nome = input('Qua o seu nome? ')
senha = input('Qua a sua senha? ')
dominio = input('Qua o seu dominio? ')
print('Ola ',nome, ', seja bem vindo ao meu mundo')
print('Sua senha é: ', senha)
print('O seu domínio é: ', dominio)


email = nome + '@' + dominio
print('Seu e-mail é :', email)

palavra = 'jaca'
#colocar a string como toda maiuscula
print('Colocando o texto em maiuscula: ',palavra.upper())

PALAVRA = 'JACA'
#colocar a string como toda minuscula
print('Colocando o texto em minuscula: ', PALAVRA.lower()) 

#contar caracter da string
palavra_contar = 'banana'
print('Contar a letra b', palavra_contar.count('b') )
print('Contar a letra a', palavra_contar.count('a') )
print('Contar a letra n', palavra_contar.count('n') )

x = palavra_contar.count('x')
print('A letra x foi contada ', x)


print(email)
a_c = email.count('a')
e_c = email.count('e')
i_c = email.count('i')
o_c = email.count('o')
u_c = email.count('u')
nova_senha = 'a' + str(a_c) + 'e'+ str(e_c) + 'i' + str(i_c) + 'o' + str(o_c) + 'u' + str(u_c)
print(nova_senha)

