To Run the project
1. create virtual environment
`python -m pipenv venv`

2. Activate virtual environment
	'venv/Scripts/activate'
3. Run all dependencies:
	pip install -r requirements.txt

4. Go to src/api/
5. RUN: (API)
		`uvicorn main:app --reload`
6. or predict by running make_prediction.py file