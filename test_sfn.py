import numpy as np
import sympy as sp
import time

def sfn_old(fn, xs):
    with np.errstate(divide='ignore', invalid='ignore'):
        try: ys = np.array([float(fn(xi)) for xi in xs], dtype=float)
        except: ys = np.zeros_like(xs)
    ys[np.abs(ys) > 50] = np.nan
    return ys

def sfn_new(fn, xs):
    with np.errstate(divide='ignore', invalid='ignore'):
        try:
            ys = fn(xs)
            if np.isscalar(ys) or np.ndim(ys) == 0:
                ys = np.full_like(xs, float(ys), dtype=float)
            else:
                ys = np.asarray(ys, dtype=float)
        except:
            try: ys = np.array([float(fn(xi)) for xi in xs], dtype=float)
            except: ys = np.zeros_like(xs)
    ys[np.abs(ys) > 50] = np.nan
    return ys

x = sp.Symbol('x')
expr = sp.sin(x) * sp.exp(-x)
fn = sp.lambdify(x, expr, 'numpy')
xs = np.linspace(-10, 10, 800)

t0 = time.time()
for _ in range(100):
    sfn_old(fn, xs)
t1 = time.time()
print("Old:", t1 - t0)

t0 = time.time()
for _ in range(100):
    sfn_new(fn, xs)
t1 = time.time()
print("New:", t1 - t0)

expr2 = sp.sympify(5)
fn2 = sp.lambdify(x, expr2, 'numpy')

ys1 = sfn_old(fn2, xs)
ys2 = sfn_new(fn2, xs)

print("Const correct?", np.allclose(ys1, ys2))
