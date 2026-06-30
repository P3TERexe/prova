## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2026-06-30 - Caching SymPy Operations in Pyodide
**Learning:** Calling expensive SymPy operations like `sp.factor` and `sp.diff` multiple times inside the Pyodide Python script execution blocks the main thread unnecessarily and degrades application performance.
**Action:** These operations should be computed once at the start of the script execution and cached in variables (e.g., `cached_factor`, `cached_diff`) wrapped in proper `try/except Exception:` blocks with appropriate fallbacks to prevent performance regressions and unexpected failures.
