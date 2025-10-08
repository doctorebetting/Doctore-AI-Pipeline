# Doctore AI Pipeline - Scaffold

This repository scaffold provides starter code, configuration, and scripts to
build the Doctore AI pipeline: fetch ESPN data, preprocess, train Spread & Totals
models, compute SHAP explanations, and generate dashboard-ready JSON.

## Quick start (local)

1. Unzip the scaffold and `cd` into the folder.
2. Create a Python virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS / Linux
   .\venv\Scripts\activate  # Windows (PowerShell)
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run a test fetch (this will save raw JSON under `data/raw/`):

   ```bash
   python scripts/fetch_data.py --sport basketball.nba
   ```

5. Preprocess the saved raw file:

   ```bash
   python scripts/preprocess.py --sport basketball.nba
   ```

6. Train models (will look for processed CSV in `data/processed/`):

   ```bash
   python scripts/train_models.py
   ```

7. Generate SHAP explanations:

   ```bash
   python scripts/explain.py
   ```

8. Generate dashboard JSON:

   ```bash
   python scripts/generate_dashboard.py
   ```

## For beginners: push to GitHub (step-by-step)

1. Create a new repository on GitHub via the web UI named `Doctore-AI-Pipeline`.
2. Locally, add & commit the scaffold and push:

   ```bash
   git init
   git add .
   git commit -m "Initial scaffold for Doctore AI Pipeline"
   git branch -M main
   git remote add origin <PASTE_YOUR_GIT_REMOTE_URL>
   git push -u origin main
   ```

## Notes
- This scaffold is intentionally minimal and safe: scripts include checks and clear TODOs
  where you will wire in project-specific logic (feature calculations, model tuning).
- Do **not** commit large raw data or model files to the repo. Keep them in external
  storage or use Git LFS if necessary.
