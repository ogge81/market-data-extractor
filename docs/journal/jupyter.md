
Here are practical ways to deal with a stuck or lagging kernel:

## Quick options (try in order)

1. **Interrupt** – Click the **Stop** (square) icon in the notebook toolbar, or `Ctrl+M I` (or `Cmd+M I` on Mac).
2. **Restart** – Click **Restart** in the toolbar, or `Ctrl+Shift+P` → “Notebook: Restart Kernel”.
3. **Select another kernel** – Use the kernel picker (top right) and choose a different kernel, then switch back to `.venv`. This often forces the old kernel to shut down.

## If it’s still stuck

4. **Close the notebook** – Close the tab. The kernel may keep running in the background.
5. **Shut down kernels** – `Ctrl+Shift+P` → “Jupyter: Shut Down All Jupyter Notebooks” (or “Jupyter: Shut Down Kernel” if available).
6. **Reload the window** – `Ctrl+Shift+P` → “Developer: Reload Window”. This restarts the Jupyter extension and usually kills stuck kernels.

## Nuclear option (force kill)

If nothing else works, kill the Python process in a terminal:

```bash
pkill -f "ipykernel"
```

Or, to target only this project’s kernel:

```bash
pkill -f "market-extractor.*ipykernel"
```

## Why it happens

Common causes:

- Heavy imports (pandas, sqlalchemy, etc.) making startup slow
- Memory pressure
- WSL + Jupyter sometimes being slow or flaky

## Mitigation

- Avoid restarting the kernel unless needed.
- Use “Interrupt” instead of “Restart” when a cell is stuck.
- If imports are slow, run them once and keep the kernel alive instead of restarting often.