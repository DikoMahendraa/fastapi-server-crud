# Setting Up Python Environment and Installing Packages

## Step-by-Step Guide

### 1. Ensure Your Python Version

Make sure your Python version is either **3.12** or higher (**3.7+ is also supported**).

To verify your Python version, run this command in your terminal:

```bash
python3 --version
```

---

### 2. Download and Install Python 3.12

If your Python version is outdated, download and install the latest version of Python 3.12 from the official Python website:

[Download Python 3.12.8](https://www.python.org/downloads/release/python-3128/)

---

### 3. Replace Your Virtual Environment

To create and replace your virtual environment:

1. **Create a new virtual environment** using Python 3.12:

   ```bash
   python3.12 -m venv your_env_name
   ```

2. **Deactivate your current virtual environment** (if any):

   ```bash
   deactivate
   ```

3. **Activate your new virtual environment**:
   ```bash
   source your_env_name/bin/activate
   ```

---

### 4. Install Required Packages

Navigate to the `src` folder where your `requirements.txt` file is located and run:

```bash
pip install -r requirements.txt
```

This command installs all the dependencies listed in the `requirements.txt` file.

---

### 5. Run Your Application

Finally, run your application using:

```bash
python run.py
```

---

## Notes

1. Always ensure your virtual environment is activated when running `pip install` or `python run.py`. You'll know it's activated if your terminal prompt shows something like `(your_env_name)`.
2. If you face issues with permissions or installations, consider running the commands with `python3.12` explicitly instead of just `python`.

source: https://www2.cs.sfu.ca/CourseCentral/120/alavergn/Python_Instructions_MACOS.pdf
