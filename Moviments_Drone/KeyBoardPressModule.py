import pygame

def iniciar():
    pygame.init()
    janela = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    ChaveEntrada = pygame.key.get_pressed()
    minhaChave = getattr(pygame, f'K_{keyName}')
    if ChaveEntrada[minhaChave]:
        ans = True
    pygame.display.update()
    return ans

def main():
    print(getKey('a'))

if __name__ == '__main__':
    iniciar()
    while True:
        main()
