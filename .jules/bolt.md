## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2026-07-04 - Pyodide SymPy Blocking Main Thread
**Learning:** Repetitive and expensive SymPy operations (like `sp.factor` and `sp.diff`) block the main thread during Pyodide execution in `eq-solver.html`, acting as a significant performance bottleneck.
**Action:** Always compute these expensive operations once upfront within the generated Python script and cache them in variables (e.g., `cached_factor`, `cached_diff`) for reuse. Wrap them in `try/except Exception:` blocks to prevent catching system-level exceptions like `KeyboardInterrupt`, using fallbacks instead.
