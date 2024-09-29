from pydantic import BaseModel

class binomial_input(BaseModel):
    n: int
    p: float
    k: int

class normal_input(BaseModel):
    x: float
    mu: float
    sigma: float

class normal_range_input(BaseModel):
    limite_superior: float
    limite_inferior: float
    mu: float
    sigma: float

class exponencial_input(BaseModel):
    x: float
    lam: float

class hypergeometrica_input(BaseModel):
    n: int
    k: int
    N: int

class poisson_input(BaseModel):
    x: int
    lam: float
