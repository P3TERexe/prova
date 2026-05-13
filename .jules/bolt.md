## 2024-05-24 - Pyodide Vectorized Evaluation
**Learning:** Element-wise list comprehensions in Pyodide (`[fn(xi) for xi in xs]`) are a severe performance bottleneck for evaluating lambdified SymPy functions.
**Action:** Always use vectorized NumPy array evaluations (`fn(xs)`) as the primary execution path. Handle scalar broadcast edge-cases (`np.full_like`) and fallback to point-by-point execution only if vectorized fails.
