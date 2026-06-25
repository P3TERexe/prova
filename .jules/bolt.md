## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2024-06-25 - Pyodide SymPy Evaluation Blocking Main Thread
**Learning:** Pyodide executes synchronous Python code on the frontend main thread. Redundant heavy calculations like `sp.factor` or `sp.diff` block the UI and unnecessarily reduce perceived performance.
**Action:** When generating Python scripts for Pyodide, evaluate expensive SymPy operations once at the top of the script, cache their results in variables, and reuse them across different output formatting blocks. Wrap these calls in `try/except Exception:` with fallback values (e.g., the original expression for factor, `0` for diff) to ensure the rest of the script continues executing.
