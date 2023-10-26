#movie_seis

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

draw_circle(50, 70, 10)
pencil_color('blue')
draw_rectangle(50, 40, 20, 40)
pencil_color('blue')
draw_line(80, ((range(1, 101) - 50) / 5) ** 2, 60, 50, 5)
pencil_color('blue')
draw_line(20, 100 - range(1, 101), 40, 50, 5)
draw_line(100 - range(1, 101), 0, 60, 20, 5)
draw_line(range(1, 101), 0, 40, 20, 5)
draw_circle(20, 100 - range(1, 101), 5)
draw_circle((80, ((range(1, 101) - 50) / 5) ** 2, 5)
            