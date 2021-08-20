## News Article Classifier
Classify News Articles into different 14 categories.
The data was taken from Kaggle which contained only title and categories so we Scraped that data to include article contents. The data can be found here:

### DataSet
The dataset contains mainly columns about, *category*, *title* and *body*. The category column contains the category the article, title contains the title of the article and body contains the contents of the article. There are total of 6877 data samples of 14 categories: ARTS & CULTURE, BUSINESS, COMEDY, CRIME, EDUCATION, ENTERTAINMENT, ENVIRONMENT, MEDIA, POLITICS, RELIGION, SCIENCE, SPORTS, TECH, WOMEN.
### Model Accuracies
![image](https://github.com/TimilsinaBimal/News-Article-Classifier/blob/Main/figures/accuracy.png)


**Selected Model**: Logistic Regression    
**Model Accuracy (test)**: 79.57%

### Logistic Regression

#### Confusion Matrix:
![image](https://github.com/TimilsinaBimal/News-Article-Classifier/blob/Main/figures/confusion_matrix_lg.png)

### How to run the project
1. Clone the repository into your local machine.
```
git clone https://github.com/TimilsinaBimal/News-Article-Classifier.git
```
2. Inside Main Directory create a virtual environment.
```
python -m venv <venv_name>
```
3. Install all the dependencies.
```
pip install -r requirements.txt
```
4. Go to `src/api/` and run
```
uvicorn main:app --reload
```

5. Go to `src/web/` and run into your local machine `index.html` file.
6. Head to Chrome or any browser and go to your local server and follow the instructions
7. To Run in CLI, Go to `src/api/` and  run
```
python make_predictions.py
```

## Enjoy!
