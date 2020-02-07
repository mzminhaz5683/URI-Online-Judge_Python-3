take2 = raw_input().split(' ')
A, B, C = float(take2[0]), float(take2[1]), float(take2[2])

print("""TRIANGULO: {0:.3f}
CIRCULO: {1:.3f}
TRAPEZIO: {2:.3f}
QUADRADO: {3:.3f}
RETANGULO: {4:.3f}""".format(((1.0 / 2) * A * C),   (3.14159 * C * C), (((A + B) / 2) * C), (B * B), (A * B)))