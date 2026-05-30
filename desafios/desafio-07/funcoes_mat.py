import math

def area_circulo(raio):
    """
    Calcula a área de um círculo.
    
    Parâmetro:
    raio (float): raio do círculo
    
    Retorna:
    float: área do círculo
    """
    return math.pi * raio**2


def volume_esfera(raio):
    """
    Calcula o volume de uma esfera.
    
    Parâmetro:
    raio (float): raio da esfera
    
    Retorna:
    float: volume da esfera
    """
    return (4/3) * math.pi * raio**3


def hipotenusa(cateto1, cateto2):
    """
    Calcula a hipotenusa de um triângulo retângulo.
    
    Parâmetros:
    cateto1 (float): primeiro cateto
    cateto2 (float): segundo cateto
    
    Retorna:
    float: valor da hipotenusa
    """
    return math.sqrt(cateto1**2 + cateto2**2)