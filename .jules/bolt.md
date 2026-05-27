## 2025-01-28 - Pyodide SymPy Plotting Performance Bottleneck
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Always use Vectorized NumPy array evaluation (e.g. `ys = np.asarray(fn(xs))`) and handle 0-dimensional scalar results for constant functions by broadcasting them using `np.full_like`.