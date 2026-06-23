## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.
## 2024-05-24 - Cached Expensive Pyodide SymPy computations
**Learning:** Repetitive SymPy computations like `sp.factor` and `sp.diff` within the dynamically generated Pyodide python script (`eq-solver.html`'s `buildCode`) can block the main thread unnecessarily. Executing them multiple times in different analysis blocks is a performance bottleneck.
**Action:** Always compute expensive symbolic operations once at the start of generated Pyodide scripts, cache their results in variables (`cached_factor`, `cached_diff`), and reuse these variables across subsequent blocks to reduce execution time and avoid main-thread blocking.
