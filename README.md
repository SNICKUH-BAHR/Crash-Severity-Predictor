# Crash Severity Prediction with LightGBM
*My first machine learning project!*

## Installation
To install required libraries, run:
~~~
"pip install -r requirements.txt"
~~~

## Project Summary
This project uses a LightGBM model trained on 20,000+ data points using 8 selected features to predict crash outcomes, including the number of casualties and accident severity. This involved:
- Selecting about 40,000 points from an approximately 240,000-point dataset spanning the years <a href=https://catalog.data.gov/dataset/allegheny-county-crash-data>2004 - 2021</a>
- Cleaning the data and splitting it into training, validation, and testing sets
- Identifying impactful features using feature importance: `VEHICLE_COUNT`, `PED_COUNT`, `COLLISION_TYPE`, `CRASH_MONTH`, `DEC_LAT`, `DEC_LONG`, `TIME_OF_DAY`, `WEATHER`
- Training and validating a LightGBM model
- Evaluating the model's performance on a test set

## Results
The LightGBM model made predictions for four target columns: FATAL_COUNT (regression), INJURY_COUNT (regression), TOT_INJ_COUNT (regression), MAX_SEVERITY_LEVEL (classification but treated as regression). 

### Training and Validation Loss

Column             |  Train MSE    |  Validation MSE
-------------------|---------------|----------------
FATAL_COUNT	       |  0.007	       |  0.008
INJURY_COUNT	     |  0.683	       |  0.553
TOT_INJ_COUNT	     |  0.681	       |  0.554
MAX_SEVERITY_LEVEL |  2.167	       |  2.132

> See `train_model.ipynb` for training and validation loss plots.  
> **Note:** *The train and validation MSE will vary slightly every time the notebook code is run*.

**Note:** The MSE calculation for the `MAX_SEVERITY_LEVEL` output column is technically invalid, as it is a classification output. However, predictions were made using a regression model because of a class imbalance during training when using a classification model, as the model had only been exposed to 3 out of the 5 possible classes. A larger training set would have resolved this, but due to time constraints, the regression output was rounded to the nearest integer as a workaround.

### Testing Loss

Column          | Test Metric
----------------|------------
FATAL_COUNT	    |  MSE: 0.083
INJURY_COUNT	  |  MSE: 0.752
TOT_INJ_COUNT	  |  MSE: 0.753
MAX_SEVERITY_LEVEL | Accuracy: 4.09%

> See `test_model.ipynb` for:  
> - **Confusion matrix** (`MAX_SEVERITY_LEVEL`)
> - **Predicted vs. Actual** plots (`FATAL_COUNT`, `INJURY_COUNT`, and `TOT_INJ_COUNT` output columns)

## Discussion
### Regression (`FATAL_COUNT`, `INJURY_COUNT`, and `TOT_INJ_COUNT`)
Despite relatively low MSE values across training, validation, and test datasets the regression model performed poorly in practice. The **Predicted vs. Actual** plots (see `test_model.ipynb`) reveal that the model frequently predicted near-zero values, especially for the `FATAL_COUNT` column, which contained an abundance of zeros (due a low number of recorded fatalities). While this minimized the model's MSE, it failed to accurately predict any non-zero values. In a future iteration of this project, this problem could be addressed using a zero-inflated regressor, such as the zero-inflated Poisson model.
### Classification (`MAX_SEVERITY_LEVEL`)
The classification performance for the `MAX_SEVERITY_LEVEL` column was also poor, with only **4.09% accuracy**. This was an expected outcome, as a regressor was used to predict classification output. A classification model was initially attempted but failed due to class imbalance as the training set only contained 3 out the 5 severity classes. As a result, the classifier was unable to handle the unseen classes encountered on the test set. Imprvoing this outcome in the future would involve expanding the training set to include all 5 classes or applying resampling techniques to mitigate the class imbalance.
