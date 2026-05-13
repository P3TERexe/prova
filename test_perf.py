import time
import numpy as np
import sympy as sp

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
            if np.isscalar(ys):
                ys = np.full_like(xs, ys, dtype=float)
            else:
                ys = np.asarray(ys, dtype=float)
        except Exception:
            try: ys = np.array([float(fn(xi)) for xi in xs], dtype=float)
            except: ys = np.zeros_like(xs)
    ys[np.abs(ys) > 50] = np.nan
    return ys

x = sp.Symbol('x')
expr = sp.sin(x) * x**2
f_lamb = sp.lambdify(x, expr, 'numpy')
xs = np.linspace(-10, 10, 800)

# Warmup
sfn_old(f_lamb, xs)
sfn_new(f_lamb, xs)

n_iters = 100

t0 = time.time()
for _ in range(n_iters):
    sfn_old(f_lamb, xs)
t_old = time.time() - t0

t0 = time.time()
for _ in range(n_iters):
    sfn_new(f_lamb, xs)
t_new = time.time() - t0

print(f"Old: {t_old:.4f}s")
print(f"New: {t_new:.4f}s")
print(f"Speedup: {t_old/t_new:.2f}x")
