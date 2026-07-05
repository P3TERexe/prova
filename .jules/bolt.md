## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2024-05-24 - Pyodide SymPy Caching Optimization
**Learning:** Calling expensive SymPy operations like `sp.factor` and `sp.diff` multiple times for the same expression causes unnecessary main thread blocking in Pyodide.
**Action:** Cache the results of these operations at the start of the execution block, wrapping them in `try/except Exception:` to prevent failures on complex expressions, and reuse the variables throughout the script.
