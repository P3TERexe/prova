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

# Test cases
exprs = [
    x**2,
    sp.sin(x),
    sp.Rational(5, 1) # constant
]

xs = np.linspace(-10, 10, 800)

for expr in exprs:
    f_lamb = sp.lambdify(x, expr, 'numpy')
    ys_old = sfn_old(f_lamb, xs)
    ys_new = sfn_new(f_lamb, xs)
    # They should be equal, except nan values where both are nan
    np.testing.assert_allclose(ys_old, ys_new, equal_nan=True)
    print(f"Passed for {expr}")
