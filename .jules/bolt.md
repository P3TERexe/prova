## 2024-06-26 - Pyodide Main Thread Blocking
**Learning:** Repetitive expensive SymPy operations (like `factor` and `diff`) in Pyodide block the main thread. Caching them once at the start of the execution script prevents significant performance degradation across different mathematical analysis blocks.
**Action:** When building Python execution strings for Pyodide, always precompute expensive operations with a `try/except Exception:` block and reuse the cached variables to avoid redundant computation and main thread blocking.
