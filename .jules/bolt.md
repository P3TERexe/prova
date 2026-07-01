## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2024-05-24 - Pyodide Main Thread Blocking
**Learning:** Calling expensive SymPy operations like `sp.factor` and `sp.diff` multiple times for the same expression causes significant main thread blocking in Pyodide.
**Action:** Pre-calculate and cache these expensive operations once at the start of the Python execution block, wrapping them in `try/except Exception:` blocks with appropriate fallback values to reuse them safely throughout the script.
