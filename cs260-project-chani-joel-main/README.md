## CS260 Project: Lab Notebook
Notebook Logs:

### 12/1/2023: Chani and Joel (2 hrs)

- explored the dataset to see what we wanted to analyze

- decided to focus on genre, rating, licensors, source, episodes length

- Looked over/quality checked original best feature and partition code from lab 6 to make sure it still works

- Realized we need to change csv data to arff


### 12/4/2023: Chani and Joel (3 hrs)

- Figured out how to change csv to arff

- Finished cleaning up data(removed blanks, deleted feature columns not being used, converted score column to 'class' and made it 1 or 0 depending on the bop or flop threshold, split up genres to individual genre features with 1 or 0 as the value, converted episodes # into short: <= 50, medium: 50-150, long: > 150)


### 12/9/2023: Joel and Chani (1.5 hrs)

- Added naive bayes algorithim

- Sorted and displayed log probabilities 

- Started working on presentation


### 12/10-11/2023: Joel and Chani (2 hrs)

- Continued presentation work with data


### 12/12/2023: Chani and Joel (1 hr)

- Coded up the plots for info gain for each feature and then showed all three info gains plots for each threshold on one figure

- Finished presentation

### 12/14/2023: Chani and Joel (1 hr)

- Implemented linear regression to show the relationship between rating and anime score
- Convert rating values to 0-4 corresponding with the maturity/graphic content level of the rating. In order from 0-4 as follows G-All ages, PG-Children, PG-13 Teens 13 or older, R-17+ violence and profanity, R+ mild nudity.


## Results :

#### Threshold 6

Best Info Gain: 0.04257198126204281

Best Feature:  Licensors

Best Feature by Accuracy:  Episodes


##### Naive Bayes:

Training Set Class Counts -->    1: 2364    0: 198

Accuracy: 0.9282371294851794

Confusion Matrix:
[[  4  39]
 [  7 591]]


##### Top Features with their Avg_Log_Prob:

Episodes_Short :                          -1.947901

Rating_PG-13_Teens_13_or_older :         -2.485326

Action :                                 -2.697384

Comedy :                                 -2.888725

Source_Manga :                           -2.925987


#### Threshold 7.5

Best Info Gain: 0.06017373441896101

Best Feature:  Licensors

Best Feature by Accuracy:  Licensors


##### Naive Bayes:

Training Set Class Counts -->  0:  1814    1: 748

Accuracy: 0.717628705148206

Confusion Matrix:
[[399  51]
 [130  61]]


##### Top Features with their Avg_Log_Prob:

Episodes_Short :                          -1.953012

Rating_PG-13_Teens_13_or_older :          -2.385665

Action :                                  -2.758425

Source_Manga :                            -2.772713

Comedy :                                  -2.880632


#### Threshold 7.5

Best Info Gain: 0.04365848251052562

Best Feature:  Licensors

Best Feature by Accuracy:  Licensors


##### Naive Bayes:

Training Set Class Counts --> 0:    2269     1:     293

Accuracy: 0.8876755070202809

Confusion Matrix:
[[561  13]
 [ 59   8]]

##### Top Features with their Avg_Log_Prob:

Episodes_Short :                          -1.970090

Rating_PG-13_Teens_13_or_older :          -2.436054

Source_Manga :                            -2.713243

Action :                                  -2.785111

Comedy :                                  -2.991189



#### Threshold 8 & No Licensor

Best Info Gain: 0.0284639187449085

Best Feature:  Source

Best Feature by Accuracy:  Source

##### Naive Bayes:

Accuracy: 0.9968798751950078

Confusion Matrix:
[[572   2]
 [  0  67]]

##### Top Features with their Avg_Log_Prob:

Episodes_Short :                          -1.873712

Rating_PG-13_Teens_13_or_older :          -2.339675

Source_Manga :                            -2.616865

Action :                                  -2.688733

Comedy :                                  -2.894810


## Reference:

Sajid Uddin. (2023). Anime Dataset 2023. https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset.