## 2024-05-18 - Pyodide graph plotting vectorization
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck. Vectorized NumPy array evaluation (`ys = fn(xs)`) is roughly ~15-20x faster.
**Action:** Always prefer NumPy vectorized array evaluation when plotting graphs. Ensure fallback options and correctly handle scalar values for constant functions.
