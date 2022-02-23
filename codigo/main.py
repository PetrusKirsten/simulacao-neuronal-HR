import numpy as np


def lambdas(i):
    import sympy as sm

    # Parâmetros para o sistema
    a = 1
    b = 3
    c = 1
    d = 5
    r = 0.006
    s = 4
    xr = - 1.56

    x, y, z = sm.symbols('x, y, z')

    # O sistema dinâmico a ser simulado
    fx = y - a * x ** 3 + b * x ** 2 - z + i
    fy = c - d * x ** 2 - y
    fz = r * (s * (x - xr) - z)

    # Igualar as equações do sistema a zero
    eqx = sm.Eq(fx, 0)
    eqy = sm.Eq(fy, 0)
    eqz = sm.Eq(fz, 0)

    # Resolver o sistema
    pf1, pf2, pf3 = sm.solve([eqx, eqy, eqz])

    print(f'\nPF1: {pf1}'
          f'\nPF2: {pf2}'
          f'\nPF3: {pf3}')

    sistema = sm.Matrix([fx, fy, fz])                # Sistema de matrizes
    jacobiano_sistema = sistema.jacobian((x, y, z))  # Jacobiano das matrizes   |A*I - lambda| = 0

    # Substituir os pontos de equilibrio no sistema das matrizes jacobianas
    jacobiano_pf1 = jacobiano_sistema.subs([(x, pf1.get(x)), (y, pf1.get(y)), (z, pf1.get(z))])
    jacobiano_pf2 = jacobiano_sistema.subs([(x, pf2.get(x)), (y, pf2.get(y)), (z, pf2.get(z))])
    jacobiano_pf3 = jacobiano_sistema.subs([(x, pf3.get(x)), (y, pf3.get(y)), (z, pf3.get(z))])

    # Printar as soluções para os lambdas de cada função em cada intensidade I
    print(f'\n', f'*'*25, f'Lambdas para I = {i}', f'*'*25)
    print(f'Lambdas para o ponto fixo 1:')
    for x in jacobiano_pf1.eigenvals():
        print(f'{x}')
    print(f'\nLambdas para o ponto fixo 2:')
    for y in jacobiano_pf2.eigenvals():
        print(f'{y}')
    print(f'\nLambdas para o ponto fixo 3:')
    for z in jacobiano_pf3.eigenvals():
        print(f'{z}')


def sist_EDO(edo, t, i):
    # Função para nos retornar a matriz do sistema a ser resolvida pela função odeint

    # Parâmetros para o sistema
    a = 1
    b = 3
    c = 1
    d = 5
    r = 0.006
    s = 4
    xr = - 1.56

    # Retorna a matriz que representa o sistema de equações
    return np.array([edo[1] - a * edo[0] ** 3 + b * edo[0] ** 2 - edo[2] + i,  # x' = y - a*x^3 + b*x^2 - z + I
                     c - d * edo[0] ** 2 - edo[1],                             # y' = c - d*x^2 - y
                     r * (s * (edo[0] - xr) - edo[2])])                        # z' = r*[s*(x - xr) - z]


def sol_EDO(i):
    # Função para resolver o sistema dinâmico que é retornado pela função sist_EDO

    from scipy.integrate import odeint
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import figure

    plt.style.use('seaborn-poster')     # Estilo do plot
    tempo = np.arange(0, 1500, 0.01)    # Matriz para a iteração de tempo
    cond_inicial = np.array([0, 0, 0])  # Condições iniciais para o sistema

    # Usamos a função odeint para resolver o sistema de equações retornado pela função
    # sist_EDO utilizando o tempo e as condições iniciais e diferentes intensidades I
    solucao_edo = odeint(sist_EDO, cond_inicial, tempo, args=(i,))
    x = solucao_edo[:, 0]
    y = solucao_edo[:, 1]
    z = solucao_edo[:, 2]

    # Plot para as funções x, y e z em função do tempo
    figure(figsize=(15, 8), dpi=80)
    plt.xlabel('Tempo [s]')
    plt.ylabel('Variável')
    plt.xlim(0, 1000)
    plt.plot(tempo, x, label='x', linewidth=0.75)
    plt.plot(tempo, y, label='y', linewidth=0.75)
    plt.plot(tempo, z, label='z', linewidth=0.75)
    plt.legend(loc=4)
    plt.show()

    # Plot para o plano de fase de y vs. x
    figure(figsize=(15, 8), dpi=80)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x[36000:], y[36000:], linewidth=0.75)
    plt.show()

    # Plot para o plano de fase de z vs. x
    figure(figsize=(15, 8), dpi=80)
    plt.xlabel('x')
    plt.ylabel('z')
    plt.plot(x[36000:], z[36000:], linewidth=0.75)
    plt.show()

    # Plot para o plano de fase de z vs. y
    figure(figsize=(15, 8), dpi=80)
    plt.xlabel('z')
    plt.ylabel('y')
    plt.plot(y[36000:], z[36000:], linewidth=0.75)
    plt.show()

    # Plot para o plano de fase 3D
    figure(figsize=(15, 8), dpi=80)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x[36000:], y[36000:], z[36000:])
    ax.set_xlabel("Eixo x")
    ax.set_ylabel("Eixo y")
    ax.set_zlabel("Eixo z")
    ax.set_title("Atrator de Lorenz")
    plt.show()


if __name__ == '__main__':
    # Encontrar os autovalores lambdas para diferentes intensidades I
    lambdas(1.1)
    lambdas(1.2)
    lambdas(3.0)

    # Simular o sistema dinâmico para diferentes intensidades I
    sol_EDO(1.1)
    sol_EDO(1.2)
    sol_EDO(3.0)
