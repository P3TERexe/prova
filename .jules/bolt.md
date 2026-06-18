## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2026-06-18 - Pyodide SymPy Caching
**Learning:** Repetitive SymPy operations (`sp.diff`, `sp.factor`) across multiple execution blocks block the main thread and impact Pyodide script execution performance in `eq-solver.html`.
**Action:** Compute expensive operations once at the start of the script and cache the results in variables for reuse across subsequent code blocks.
