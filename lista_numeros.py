import random

regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv', 'patín', 'balón', 'reloj', 'bicicleta', 'anillo']

for sorteo in range(5):
    regalo = regalos[random.randint(0, 9)]
    print('Sorteo', sorteo + 1, ':', regalo)