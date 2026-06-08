## 2024-06-12 - Vectorized Pyodide function evaluation
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck. Vectorized NumPy array evaluation is much faster.
**Action:** Always use vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) as the primary execution path for Pyodide function evaluations. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.
