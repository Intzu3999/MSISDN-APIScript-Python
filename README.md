# 🐍 PYTHON PANDA 🐼

# WHAT DOES THIS PROJECT DO
1) Processes msisdn list from csv asynchronously against API to extract payload data, flattens the data structure with Panda, and output the final result in excel table.

# PYTHON BEST PRACTICE
1) snake_case is preferred in Python (it is a ssssnake!)
2) We follow the Pythonic way of handling API responses and extracting data. The strategy is centered around Python dictionaries!

# TO SETUP
1) Install python3.exe x64-bit
 verify:
 python --version
 python -c "import platform; print(platform.architecture())" 
2) At root project create new virtual env: python -m venv venv 
3) Start Python's virtual env: venv\Scripts\activate
4) python.exe -m pip install --upgrade pip
5) pip install --upgrade setuptools wheel
6) pip install -r requirements.txt
 if panda failing it is most likely due to your venv setup.
 pip install --upgrade setuptools wheel meson ninja cython numpy (and any other missing/failed dependency installation based from your log)
 pip install --force-reinstall --no-cache-dir pandas
7) To close Python's virtual env: deactivate

# TO RUN TEST
1) python tests/test_script_name.test.py

# TO RUN DATA PROCESSING SCRIPT
1) python read_csv.py
2) python read_csv.py csvFileName --service service_name

# TO ADD / BUILD 
1) get_account_structure_api 
2) chain API calls

# TO LEARN AND IMPROVE
1) Strategy Pattern using Python's Registry and abc abstract method classes