import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

#Load the CSV file into a DataFrame
df = pd.read_csv('data/rating_vs_score.csv')

#Split the data into features (X) and target variable (y)
X = df[['Rating']]
y = df['Score']

#Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Create a linear regression model
model = LinearRegression()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#Plot the results
plt.scatter(X_test, y_test, color='green', alpha = 0.5, label='Actual data')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Linear regression line')
plt.xlabel('Ratings')
plt.ylabel('Anime Score')
plt.legend()
plt.title('Linear Regression: Anime Score Prediction based on Ratings')
plt.savefig("figures/score_based_on_rating.pdf")
plt.show()