## 2024-06-04 - Pyodide SymPy Lambdify Evaluation Bottleneck
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck due to crossing the Python/JS bridge repeatedly or simply Python loop overhead in WebAssembly.
**Action:** Always use vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.
