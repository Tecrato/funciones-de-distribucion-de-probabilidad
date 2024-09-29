# este archivo pa a contener las funciones de distribucion de probabilidades
# las funciones de distribucion de probabilidades son las que se utilizan para
# calcular la probabilidad de un valor o caso particular
# Las funciones son las siguientes:
# func_distribucion_binomial
# func_distribucion_normal
# func_distribucion_exponencial
# func_hypergeometrica
# func_poisson

from scipy import stats

def func_distribucion_binomial(n, p, k):
    # Calcular la probabilidad de que un número de experimentos de binomial tenga k éxitos
    return stats.binom(n, p).pmf(k)

def func_distribucion_normal(x, mu, sigma):
    # Calcular la probabilidad de que una variable normal tenga un valor x
    return stats.norm(mu, sigma).cdf(x)

def func_distribucion_normal_range(limite_superior, limite_inferior, mu, sigma):
    # Calcular la probabilidad de que una variable normal tenga un valor x dentro del rango
    probabilidad = stats.norm(mu, sigma).cdf(limite_superior) - stats.norm(mu, sigma).cdf(limite_inferior)
    return probabilidad
    
def func_distribucion_exponencial(x, lam):
    # Calcular la probabilidad de que una variable exponencial tenga un valor x
    return stats.expon(scale=1/lam).cdf(x)

def func_hypergeometrica(n, k, N):
    # Calcular la probabilidad de que una variable de números aleatorios de una distribución de Hypergeometrica tenga k éxitos
    return stats.hypergeom(k, N, n).pmf(k)

def func_distribucion_poisson(x, lam):
    # Calcular la probabilidad de que una variable de números aleatorios de una distribución de Poisson tenga k éxitos
    return stats.poisson(lam).pmf(x)