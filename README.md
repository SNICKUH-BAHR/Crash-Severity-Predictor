# Crash Severity Prediction with LightGBM
*My first machine learning project!*

## Installation
To install required libraries, run:
~~~
"pip install -r requirements.txt"
~~~

## Project Summary
This project uses a LightGBM model trained on over 20,000 data points using 8 selected features to predict crash outcomes, including the number of casualties and accident severity. This involved:
- Selecting a ~40,000-point subset from a ~240,000-point dataset
- Cleaning the data and splitting it into training, validation, and testing sets
- Identifying impactful features using feature importance: `VEHICLE_COUNT`, `PED_COUNT`, `COLLISION_TYPE`, `CRASH_MONTH`, `DEC_LAT`, `DEC_LONG`, `TIME_OF_DAY`, `WEATHER`
- Training and validating a LightGBM
- Evaluating the model's performance on a test set

## Results
The LightGBM model made predictions for four target columns: FATAL_COUNT (regression), INJURY_COUNT (regression), TOT_INJ_COUNT (regression), MAX_SEVERITY_LEVEL (classification but treated as regression). 

#### Training and Validation Loss

Column             |  Train MSE    |  Validation MSE
-------------------|---------------|----------------
FATAL_COUNT	       |  0.007	       |  0.008
INJURY_COUNT	     |  0.681	       |  0.553
TOT_INJ_COUNT	     |  0.686	       |  0.553
MAX_SEVERITY_LEVEL |  2.171	       |  2.132

> See `train_model.ipynb` for training and validation loss plots.  
> **Note:** *The train and validation MSE will vary slightly every time the notebook code is run*

**Note:** The MSE calculation for the `MAX_SEVERITY_LEVEL` output column is technically invalid, as it is a classification output. However, predictions were made using a regression model because of a class imbalance during training when using a classification model, as the model had only been exposed to 3 out of the 5 possible classes. A larger training set would have resolved, but due to time constraints, the regression output was rounded to the nearest integer as a workaround.

#### Testing Loss

Column          | Test Metric
----------------|------------
FATAL_COUNT	    |  MSE: 0.007
INJURY_COUNT	  |  MSE: 0.567
TOT_INJ_COUNT	  |  MSE: 0.566
MAX_SEVERITY_LEVEL | Accuracy: 4.21%

> See `test_model.ipynb` for:  
> - Confusion matrix (`MAX_SEVERITY_LEVEL`)
> - Predicted vs. Actual plots (`FATAL_COUNT`, `INJURY_COUNT`, and `TOT_INJ_COUNT` output columns)

## Discussion
