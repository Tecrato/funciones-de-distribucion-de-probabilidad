from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse


from funciones_de_distribucion import (
    func_distribucion_binomial,
    func_distribucion_normal,
    func_distribucion_normal_range,
    func_distribucion_exponencial,
    func_hypergeometrica,
    func_distribucion_poisson,
)
from modelos import (
    binomial_input,
    normal_input,
    normal_range_input,
    exponencial_input,
    hypergeometrica_input,
    poisson_input,
)

app = FastAPI()

@app.get("/")
def read_root() -> RedirectResponse:
    return RedirectResponse(url="/docs")

@app.get("/api/binomial")
def api_binomial(input: binomial_input) -> JSONResponse:
    return JSONResponse(content=func_distribucion_binomial(input.n, input.p, input.k))

@app.get("/api/normal")
def api_normal(input: normal_input) -> JSONResponse:
    return JSONResponse(content=func_distribucion_normal(input.x, input.mu, input.sigma))

@app.get("/api/normal_range")
def api_normal_range(input: normal_range_input) -> JSONResponse:
    return JSONResponse(content=func_distribucion_normal_range(input.limite_superior, input.limite_inferior, input.mu, input.sigma))

@app.get("/api/exponencial")
def api_exponencial(input: exponencial_input) -> JSONResponse:
    return JSONResponse(content=func_distribucion_exponencial(input.x, input.lam))

@app.get("/api/hypergeometrica")
def api_hypergeometrica(input: hypergeometrica_input) -> JSONResponse:
    return JSONResponse(content=func_hypergeometrica(input.n, input.k, input.N))

@app.get("/api/poisson")
def api_poisson(input: poisson_input) -> JSONResponse:
    return JSONResponse(content={"result":func_distribucion_poisson(input.x, input.lam)})

@app.exception_handler(404)
async def custom_404_handler(_, __) -> HTMLResponse:
    return HTMLResponse(content="<h1>404 Not Found</h1>", status_code=404)

@app.exception_handler(405)
async def custom_405_handler(_, __) -> HTMLResponse:
    return HTMLResponse(content="<h1>405 Method Not Allowed</h1>", status_code=405)

@app.exception_handler(500)
async def custom_500_handler(_, __) -> HTMLResponse:
    return HTMLResponse(content="<h1>500 Internal Server Error</h1>", status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    