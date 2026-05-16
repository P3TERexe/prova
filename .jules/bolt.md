## 2024-05-18 - Pyodide Function Evaluation Bottleneck
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck due to crossing the Python/JavaScript/C boundary for every single point evaluated during plotting.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = np.asarray(fn(xs))`) should always be used as the primary execution path for lambdified functions. Only use list comprehensions as a fallback when vectorization fails.
