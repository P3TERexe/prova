## 2024-05-24 - Pyodide List Comprehension Bottleneck
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck. Vectorized NumPy array evaluation is significantly faster in the Pyodide environment.
**Action:** Always use vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) as the primary execution path when evaluating functions in Pyodide, falling back to list comprehensions only if necessary.
