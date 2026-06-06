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
        except Exception as e:
            print("fallback", e)
            try: ys = np.array([float(fn(xi)) for xi in xs], dtype=float)
            except: ys = np.zeros_like(xs)
    try:
        ys[np.abs(ys) > 50] = np.nan
    except:
        pass
    return ys

x = sp.Symbol('x')

# test 1: vectorized
expr1 = x**2 + sp.sin(x)
fn1 = sp.lambdify(x, expr1, 'numpy')

# test 2: constant
expr2 = sp.Integer(5)
fn2 = sp.lambdify(x, expr2, 'numpy')

xs = np.linspace(-10, 10, 800)

t0 = time.time()
r1_old = sfn_old(fn1, xs)
t1 = time.time()
r1_new = sfn_new(fn1, xs)
t2 = time.time()
print(f"fn1: old {t1-t0:.5f}s, new {t2-t1:.5f}s, equal={np.allclose(np.nan_to_num(r1_old), np.nan_to_num(r1_new))}")

t0 = time.time()
r2_old = sfn_old(fn2, xs)
t1 = time.time()
r2_new = sfn_new(fn2, xs)
t2 = time.time()
print(f"fn2: old {t1-t0:.5f}s, new {t2-t1:.5f}s, equal={np.allclose(np.nan_to_num(r2_old), np.nan_to_num(r2_new))}")
