### Create Virtual environemnt
```bash
python -m venv venv
.\venv\Scripts\activate    # Windows
```
source venv/bin/activate   # Linux/macOS
pip install -r requirements.txt

## 👨‍💻 Standard Developer Workflow (per project)
Let’s say you're working on:

C:\Users\km443\Projects\
│
├── aws-dashboard/        ← Flask app 1
├── ssh-firewall-monitor/ ← Flask app 2
├── django-api/           ← Django project
├── static-site/          ← Tailwind site
🧱 Step 1: Create project folders
You keep each project in its own folder.

## 🐍 Step 2: Create virtual environment inside each

cd C:\Users\km443\Projects\ssh-firewall-monitor
python -m venv venv
Creates ssh-firewall-monitor/venv/ which holds all packages just for that project.

## 🛠 Step 3: Activate virtual env & install tools

.\venv\Scripts\activate
pip install flask python-dotenv
Now your flask, python, etc. refer to this local venv.

## 📁 Step 4: Create .env for project settings

FLASK_APP=app.py
FLASK_ENV=development
Keeps environment variables clean and project-specific.

## 💡 Step 5: Use VS Code per project
Open only one project folder at a time
It remembers the right Python interpreter (your local venv)
Set in VS Code:
Ctrl+Shift+P → Python: Select Interpreter
Choose .venv\Scripts\python.exe

## 🧪 Bonus: Use a requirements.txt per project
Save your project dependencies:

pip freeze > requirements.txt
Now you can recreate the environment later:


