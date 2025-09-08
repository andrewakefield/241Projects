lst = [1, 2, 3, 'Andy', 'other']
indices = [i for i in range(len(lst)) if lst[i] == 'Andy'] # essentially the first i means append i to this indice; if it didnt exist a syntax error would occur
print(indices)