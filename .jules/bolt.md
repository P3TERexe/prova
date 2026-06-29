## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2024-05-24 - Pyodide SymPy Caching
**Learning:** Duplicate SymPy calls (like `sp.factor` and `sp.diff`) in Pyodide cause severe performance bottlenecks on the main thread.
**Action:** Expensive SymPy operations must be cached in variables at the top of the execution block for reuse across different execution blocks. Wrap them in `try/except Exception:` blocks with appropriate fallbacks to prevent errors.
