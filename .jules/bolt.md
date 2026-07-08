## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2024-07-08 - Pyodide SymPy Factorization Performance
**Learning:** `sp.factor(expr)` is a computationally expensive operation in SymPy that was being called multiple times on the same expression within the Pyodide environment. Unlike `sp.diff`, which is fast, redundant `sp.factor` calls cause noticeable performance degradation.
**Action:** When working with expensive SymPy operations like `sp.factor` in Pyodide, evaluate them once immediately after parsing the expression and cache the result in a variable (e.g., `cached_factor`) for reuse. Wrap the evaluation in a `try/except Exception:` block with an appropriate fallback (e.g., `expr`) to ensure safety. Avoid caching fast operations like `sp.diff` to prevent unnecessary regression risks.
