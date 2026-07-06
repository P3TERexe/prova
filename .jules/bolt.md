## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.
## 2026-07-06 - Pyodide SymPy Operations Blocking Main Thread
**Learning:** Redundant, expensive SymPy operations (like `sp.factor(expr)` and `sp.diff(expr, var_sym)`) executed multiple times in the generated Pyodide Python script severely block the browser's main thread and degrade performance.
**Action:** Compute expensive operations once at the start of the execution block, cache them in variables (e.g., `cached_factor`, `cached_diff`) inside `try/except Exception:` blocks with appropriate fallbacks, and reuse these cached variables throughout the script.
