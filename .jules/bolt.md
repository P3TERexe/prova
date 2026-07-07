## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.
## 2024-07-07 - Pyodide SymPy Blocking Bottleneck
**Learning:** Repetitive calls to expensive SymPy functions like `sp.factor` and `sp.diff` block the main thread and significantly slow down execution when running in Pyodide on the frontend.
**Action:** Always compute expensive SymPy operations once at the start of the execution script and cache the results in variables (e.g., `cached_factor`, `cached_diff`). Wrap them in `try/except Exception:` with appropriate fallbacks to prevent breaking subsequent execution if the operation fails.
