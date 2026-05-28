## 2024-05-24 - Pyodide Lambdify Evaluation Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck. Vectorized NumPy array evaluation (`ys = fn(xs)`) is significantly faster (4x-10x) but requires handling 0-dimensional scalar results (e.g. constant functions) by broadcasting them using `np.full_like`.
**Action:** Always prefer NumPy vectorized evaluations over Python loops/list comprehensions within Pyodide, ensuring fallback handling for scalars and functions that don't support vectorized inputs.
