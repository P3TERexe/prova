## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2024-06-24 - Pyodide SymPy Caching Redundant Calculations
**Learning:** Calling computationally heavy SymPy operations like `sp.factor` and `sp.diff` redundantly across different processing steps within the generated Python script causes severe Pyodide execution bottlenecks.
**Action:** Always compute expensive operations once, wrap them in `try/except Exception:` blocks with appropriate fallbacks, and reuse cached variables across different visualization blocks to avoid redundant evaluations.
