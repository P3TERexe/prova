## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2026-07-03 - Pyodide SymPy Factor/Diff Performance
**Learning:** Evaluating heavy SymPy operations like `sp.factor` and `sp.diff` multiple times synchronously blocks the Pyodide main thread and hurts application responsiveness.
**Action:** Expensive SymPy operations should be evaluated once at the top of the generated Python script and cached in variables for reuse across execution blocks. Wrap them in `try/except Exception:` with appropriate fallbacks to prevent pipeline failures.
