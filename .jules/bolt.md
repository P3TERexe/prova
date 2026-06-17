## 2024-05-24 - Pyodide SymPy Plotting Performance
**Learning:** Evaluating lambdified SymPy functions point-by-point via list comprehensions in Pyodide is a severe performance bottleneck.
**Action:** Vectorized NumPy array evaluation (e.g., `ys = fn(xs)`) should always be used as the primary execution path. If the result is a 0-dimensional scalar (e.g., for constant functions), broadcast it to an array using `np.full_like(xs, ys, dtype=float)`.

## 2024-05-24 - Pyodide SymPy Template Syntax Errors and Caching
**Learning:** In JS template strings building Python code for Pyodide, conditional logic or formatting errors can introduce orphaned `except: pass` statements, leading to static analysis SyntaxErrors that break execution. Furthermore, repetitive expensive SymPy operations (like `sp.simplify`, `sp.factor`, `sp.diff`) during execution cause main thread blocking and severely degrade performance.
**Action:** Always compute expensive SymPy operations once at the start of the script and cache them in variables. Periodically verify the syntax of the fully-injected Python template using `ast.parse` to ensure conditional blocks are well-formed and avoid unexpected `SyntaxError`s.
