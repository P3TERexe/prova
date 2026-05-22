## 2024-05-22 - Pyodide Vectorized Evaluation
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck. Vectorized NumPy array evaluation is significantly faster.
**Action:** Always use vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.
