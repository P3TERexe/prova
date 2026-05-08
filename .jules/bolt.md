## 2024-05-14 - [Vectorize lambdified plots in Pyodide]
**Learning:** Pyodide python is extremely slow for looping over arrays. When generating plots of functions containing lambdified Sympy expressions, utilizing numpy broadcasting directly (`ys = fn(xs)`) avoids list comprehensions (`[fn(xi) for xi in xs]`) and resulted in roughly 20x faster performance.
**Action:** Always prefer NumPy vectorized array operations over python loops when passing points into Pyodide lambdified graphs.
