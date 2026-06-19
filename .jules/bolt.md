## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.
## 2024-05-25 - Redundant SymPy Operations Optimization
**Learning:** Calling heavy SymPy operations (`sp.factor`, `sp.diff`) multiple times on the same expression blocks the main thread unnecessarily during Pyodide execution.
**Action:** Always compute heavy SymPy operations once, cache them in variables, and reuse them across different execution blocks to improve execution time.
