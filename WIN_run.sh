# create virutal environment
python -m venv top_five_similar_venv

# activate virtual environment
source ./top_five_similar_venv/Scripts/activate

# install requirements
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# run the program
python ./src/top_five_similar.py

# deactivate virtual environment
deactivate