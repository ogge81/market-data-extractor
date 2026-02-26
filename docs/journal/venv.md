
Created `.vscode/settings.json` so the workspace uses your project’s `.venv` as the default Python interpreter. That should make Cursor/VS Code pick it automatically for notebooks.

**What to do:**

1. **Reload the window** – `Ctrl+Shift+P` → “Developer: Reload Window” (or close and reopen the project).
2. **Ensure ipykernel is installed** – If `.venv` still doesn’t appear as a kernel:
   ```bash
   source .venv/bin/activate
   pip install ipykernel
   ```
   (or `pip install -r requirements-dev.txt`)

3. **Select the kernel once** – After reloading, choose the `.venv` kernel once. It should then be remembered for this workspace.

If it still doesn’t stick, you can register the venv as a named kernel so it’s easier to find:

```bash
source .venv/bin/activate
python -m ipykernel install --user --name=market-extractor --display-name=".venv (market-extractor)"
```