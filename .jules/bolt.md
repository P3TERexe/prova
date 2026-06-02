## 2024-06-02 - Pyodide Lambdify Evaluation Bottleneck
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Always use vectorized NumPy array evaluation (e.g., `ys = np.asarray(fn(xs), dtype=float)`). If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.
