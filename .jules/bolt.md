## 2024-06-12 - [Pyodide Array Evaluation Bottleneck]
**Learning:** List comprehensions for point-by-point evaluation of lambdified SymPy functions in Pyodide are a major performance bottleneck due to crossing the Python iteration layer, taking ~7ms for 800 points.
**Action:** Always attempt vectorized evaluation `fn(xs)` first. This leverages NumPy's optimized C backend within Pyodide, reducing evaluation time to ~0.3ms (a ~22x speedup). Fall back to list comprehensions only when vectorized evaluation fails (e.g., when the function does not support it).
