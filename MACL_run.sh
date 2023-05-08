# create virutal environment
python3 -m venv top_five_similar_venv

# activate virtual environment
source ./top_five_similar_venv/bin/activate

# install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# run the program
python3 ./src/top_five_similar.py

# deactivate virtual environment
deactivate