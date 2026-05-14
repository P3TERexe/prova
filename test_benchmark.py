import sympy as sp
import numpy as np
import time

var_sym = sp.Symbol('x')
expr = sp.sin(var_sym) * sp.exp(var_sym) / 2
f_lamb = sp.lambdify(var_sym, expr, 'numpy')
xs = np.linspace(-10, 10, 800)

def sfn_old(fn, xs):
    with np.errstate(divide='ignore', invalid='ignore'):
        try: ys = np.array([float(fn(xi)) for xi in xs], dtype=float)
        except: ys = np.zeros_like(xs)
    ys[np.abs(ys) > 50] = np.nan
    return ys

def sfn_new(fn, xs):
    with np.errstate(divide='ignore', invalid='ignore'):
        try:
            ys = np.asarray(fn(xs), dtype=float)
            if ys.ndim == 0:
                ys = np.full_like(xs, ys)
        except Exception:
            try: ys = np.array([float(fn(xi)) for xi in xs], dtype=float)
            except: ys = np.zeros_like(xs)
    ys[np.abs(ys) > 50] = np.nan
    return ys

t0 = time.time()
for _ in range(100):
    sfn_old(f_lamb, xs)
t1 = time.time()
print(f"Old time: {t1 - t0:.4f}s")

t0 = time.time()
for _ in range(100):
    sfn_new(f_lamb, xs)
t1 = time.time()
print(f"New time: {t1 - t0:.4f}s")
