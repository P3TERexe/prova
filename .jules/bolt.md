## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.
## 2024-05-24 - Pyodide SymPy Operations Caching
**Learning:** Redundant calls to expensive SymPy operations (like `sp.factor` and `sp.diff`) in the generated Pyodide script block the main thread and degrade performance.
**Action:** Compute these expensive symbolic operations once at the top of the evaluation script and cache them in Python variables (e.g., `factored_expr`, `diff_expr`) to be reused across different mathematical interpretation blocks.
