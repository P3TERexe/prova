## 2024-11-02 - Vectorized Pyodide function evaluation implemented
**Learning:** Pyodide evaluating lambdified SymPy functions point-by-point via list comprehensions is a severe performance bottleneck. It's much faster to vectorize.
**Action:** Vectorized NumPy array evaluation (`ys = fn(xs)`) was added to `eq-solver.html` `sfn` function as the primary execution path.
