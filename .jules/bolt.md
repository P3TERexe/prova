## 2024-05-24 - Pyodide Vectorization Bottleneck
**Learning:** In the `eq-solver.html` architecture, which uses Pyodide in the browser, evaluating dynamically lambdified functions using point-by-point list comprehensions (`[fn(xi) for xi in xs]`) incurs massive overhead due to repeated boundary crossings between JS and Python.
**Action:** Always prefer NumPy vectorized evaluations (`ys = fn(xs)`) first when evaluating functions in Pyodide, catching any scalar edge cases, and using the list comprehension only as a fallback.
