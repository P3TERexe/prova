
## 2024-05-18 - Pyodide SymPy Evaluation Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Always use vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) as the primary execution path, with fallback and scalar broadcast when appropriate.
