""" 
Chani and Joel
12/1/23
Implement naive bayes and find/sort/print log probability values
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


data = pd.read_csv('data/anime-dataset_7.5.csv')

#Separate features and labels
X = data.drop('class', axis=1)
y = data['class']

class_counts = y.value_counts()
print("Class Counts:")
print(class_counts)

#One-hot encode categorical features
X_encoded = pd.get_dummies(X, columns=['Episodes', 'Licensors', 'Source','Rating'])

#Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

train_class_counts = y_train.value_counts()
print("Training Set Class Counts:")
print(train_class_counts)

clf = MultinomialNB()
clf.fit(X_train, y_train)

#Make predictions on the test set
predictions = clf.predict(X_test)

#Evaluate the accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy}')

#Calculate confusion matrix
conf_matrix = confusion_matrix(y_test, predictions)
print("Confusion Matrix:")
print(conf_matrix)

feature_log_probs = clf.feature_log_prob_
feature_names = X_encoded.columns

#Calculate the average log probability for each feature across classes
avg_log_probs = np.mean(feature_log_probs, axis=0)

feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Avg_Log_Prob': avg_log_probs})
sorted_feature_importance = feature_importance_df.sort_values(by='Avg_Log_Prob', ascending=False)
print(sorted_feature_importance)


