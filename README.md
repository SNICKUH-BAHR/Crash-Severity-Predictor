# Crash Severity Prediction with LightGBM
My first machine learning project!

## Installation of Required Libraries
Run "pip install -r requirements.txt"

## Project Summary
A LightGBM model was trained on 20,000+ data points using 8 feature columns from a crash dataset in order to predict the number of casualties and severity of the accident. This involved the following:
- Selecting a ~40,000 point subset from a ~240,000 point dataset
- Cleaning the data and splitting it into a training, validation, and testing set
- Using feature importance to select the most impactful features: VEHICLE_COUNT, PED_COUNT, COLLISION_TYPE, CRASH_MONTH, DEC_LAT, DEC_LONG, TIME_OF_DAY, WEATHER
- Training and validating a LightGBM model with the training and validation set
- Testing the LightGBM on the testing set

## Results
The LightGBM model made 4 predictions: FATAL_COUNT, INJURY_COUNT, TOT_INJ_COUNT, MAX_SEVERITY_LEVEL. The first 3 columns were regression outputs and the last column was a classification output. Below is the training, validation, and testing loss for each column.

#### Training and Validation Loss

Column             |  Train MSE    |  Validation MSE
-------------------|---------------|----------------
FATAL_COUNT	       |  0.007	       |  0.008
INJURY_COUNT	     |  0.681	       |  0.553
TOT_INJ_COUNT	     |  0.686	       |  0.553
MAX_SEVERITY_LEVEL |  2.171	       |  2.132

(See "train_model.ipynb" for loss plots)
(The train and validation MSE will vary slightly every time the notebook code is run)

**Note:** *The MSE calculation for the* `MAX_SEVERITY_LEVEL` *output column is technically invalid, as it is a classification output. However, a higher MSE is expected for this column compared to the other three regression output columns, since a regression model was used to predict all outputs. The reason a regression model was used in place of a classification model was because of a class mismatch error that occurred during validation, as the model had only been exposed to 3 out of the 5 possible classes in the training data. Ideally, the model would have been trained on a larger portion of the dataset to ensure it encountered all 5 classes. However, due to time constraints, using a regression model and then rounding its output for that column to the nearest integer was the quickest option.*

#### Testing Loss

Column          | Test MSE
----------------|----------
FATAL_COUNT	    |  0.007
INJURY_COUNT	  |  0.567
TOT_INJ_COUNT	  |  0.566

MAX_SEVERITY_LEVEL Accuracy: 4.21%

(See "test_model.ipynb" for the confusion matrix for the `MAX_SEVERITY_LEVEL` output column and predicted vs. actual plots for the `FATAL_COUNT`, `INJURY_COUNT`, and `TOT_INJ_COUNT` output columns)

## Discussion
