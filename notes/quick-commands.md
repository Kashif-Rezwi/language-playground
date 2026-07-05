# Quick Commands Reference

This document serves as a quick reference for important terminal commands, their use cases, and explanations of why they are used.

---

## Python Virtual Environments

### Activate Virtual Environment

* **Command:**
  ```bash
  source .venv/bin/activate
  ```

* **Use Case:**
  Activate the Python virtual environment located in the `.venv` directory.

* **Why we use it:**
  1. **Dependency Isolation:** It isolates your project's libraries (packages installed via `pip`) from the global system Python installation. This ensures that different projects with conflicting requirements do not interfere with each other.
  2. **Consistent Environment:** When activated, running `python` or `pip` will resolve to the binaries inside the virtual environment rather than the system's global binaries. This guarantees you are using the correct Python version and packages.
  3. **No Root Permissions Needed:** Since the packages are installed inside the project's folder (`.venv/`), you do not need administrative/root privileges (`sudo`) to install libraries.

* **Under the Hood (`source`):**
  The `source` command (or `.` in shell scripting) runs the activation script within the context of your *current* terminal process. If you ran it without `source`, the environment variables (like `PATH`) would only change inside a temporary subshell, which would immediately exit and leave your active terminal unaffected.

* **Verification:**
  Once activated, your terminal prompt will be prefixed with `(.venv)`, indicating that any python execution is now sandboxed within this environment:
  ```bash
  (.venv) user@machine language-playground %
  ```

---

## General CLI Diagnostics

### Check Active Python Path

* **Command:**
  * macOS/Linux: `which python` or `which python3`
  * Windows (PowerShell): `Get-Command python`
* **Use Case:**
  Verify which Python interpreter is currently active in the session.
* **Why we use it:**
  Ensures that the terminal is correctly pointing to your virtual environment's Python (`.venv/bin/python`) rather than the system default.
