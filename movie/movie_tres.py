#movie_tres

#configura a cor do lapis
def pencil_color(color):
    print('color')

#configura o desenho de um círculo
def draw_circle(x, y, radius):
    print('draw_circle')

#configura o desenho de um retângulo
def draw_rectangle(x, y, width, height):
    print('draw_rectangle')

#configura o desenho de uma linha
def draw_line(x1, y1, x2, y2, width):
    print('draw_line')

#configura a velocidade da animação
def time():
    for i in range(1, 101):
        print(f'Tempo: {i}')

draw_circle(50, 70, 10)
pencil_color('black')
draw_rectangle(50, 40, 20, 40)
pencil_color('blue')
draw_line(60, 50, 80, time(), 5)
draw_line(20, 100 - time(), 40, 50, 5)
