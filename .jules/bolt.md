## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2026-06-20 - Pyodide SymPy Block Caching
**Learning:** In the eq-solver application, redundant heavy SymPy calls (like `sp.factor` and `sp.diff`) in different parts of the generated Pyodide script unnecessarily block the main thread and degrade performance.
**Action:** Extract expensive and frequently reused operations to the top of the generated Python script, wrap them in `try...except` blocks with safe fallbacks, and reuse these cached variables (`cached_factor`, `cached_diff`) throughout the rest of the script.
