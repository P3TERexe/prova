## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.
## 2024-06-27 - Caching SymPy Operations in Pyodide
**Learning:** To prevent main thread blocking during Pyodide execution in `eq-solver.html`, expensive SymPy operations like `sp.factor` and `sp.diff` are a bottleneck when evaluated redundantly.
**Action:** Compute expensive operations once at the start of the generated Python script and cache them in variables (`cached_factor`, `cached_diff`) for reuse across different execution blocks. Wrap them in `try/except Exception:` blocks with appropriate fallbacks.
