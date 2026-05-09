## 2024-05-18 - Optimize localStorage Synchronous Updates
**Learning:** In a single-page HTML application relying on `localStorage` for state management, synchronous reads/writes (like `JSON.parse(localStorage.getItem(...))` and `localStorage.setItem(...)`) can block the main thread and impact frontend performance, especially when triggered repeatedly.
**Action:** Use an in-memory variable to track the state, load it once from `localStorage` on initialization, and update `localStorage` lazily using `setTimeout` (debouncing) when the state changes.
