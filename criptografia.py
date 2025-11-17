numero_para_mandar = 852369741

numero_Primario = 277
numero_Pequeno = 7

a_privado = 5
b_privado = 4

a_publico = ((numero_Pequeno ** a_privado)
             % numero_Primario)
b_publico = ((numero_Pequeno ** b_privado) 
             % numero_Primario)
print(f'{a_publico=}')
print(f'{b_publico=}')
a_publico=187
b_publico=185
segredos_juntos_a = ((b_publico ** a_privado) 
                     % numero_Primario)
segredos_juntos_b = ((a_publico ** b_privado) 
                     % numero_Primario)
print(f'{segredos_juntos_a=}')
print(f'{segredos_juntos_b=}')

segredos_juntos_a=57
segredos_juntos_b=57

encrypto = (((segredos_juntos_a - 1) 
             ** numero_Primario)
             * numero_para_mandar)
print(f'{encrypto=}')

descrypto = ((encrypto // 
            ((segredos_juntos_b - 1)
            ** numero_Primario)))
print(f'{descrypto=}')




