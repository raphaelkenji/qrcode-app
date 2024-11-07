# qrcode-app

This is a "simple" QR code generator app I've made to practice Python using FastAPI and Streamlit.

### Setup
1. Clone repository
```bash
git clone https://github.com/raphaelkenji/qrcode-app.git
```
2. Create Python environment
```bash
cd project_folder
python -m venv .venv
```
3. Activate Python environment
```bash
# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```
4. Install dependencies
```bash
pip install -r /path/to/requirements.txt
```
### Running
- Frontend (Streamlit)
```
cd frontend
streamlit run app.py
```
- Backend (FastAPI & Uvicorn)
```
cd backend
py main.py
```
