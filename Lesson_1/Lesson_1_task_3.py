# 3) По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.

def draw_line(x1, y1, x2, y2):
    k = (y1 - y2)/(x1 - x2)
    b = y2 - k*x2
    return f'y={k:.2f}x + {b:.2f}'


if __name__ == '__main__':
    print(
        draw_line(
            float(input(f'Enter x1: ')),
            float(input(f'Enter y1: ')),
            float(input(f'Enter x2: ')),
            float(input(f'Enter y2: '))
        )
    )
