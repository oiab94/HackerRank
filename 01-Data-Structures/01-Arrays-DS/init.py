'''
  Un arreglo es un tipo de estructura de datos en la que almacena elementos del 
  mismo tipo en bloques contiguos de memoria. En un arreglo A, de tamaño N, cada 
  locación de memoría contiene un unico índice, i (donde 0 <= i < N), eso es 
  referenciado como A[i].
'''

# ----------------- # 
# Invierta un array #
# ------------------#
def reverseArray(a):      # a: Parámetro INTEGER_ARRAY
  arr = []

  for i in reversed(a):
    arr.append(i);

  return arr              # Retorna el INTEGER_ARRAY


# -------------- #
# Prueba función #
# -------------- #
arr = [10, 20, 30]
print(reverseArray(arr))