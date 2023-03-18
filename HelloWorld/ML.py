# We used Jupyter for it (won't work here)
# If you can't load Jupyter from the terminal
# Then just search it and press Jupyter Notebook and it will launch the server
# The working code is saved in ThisPC -> Users -> Python ML

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split # For testsing
from sklearn.metrics import accuracy_score

music_data = pd.read_csv('music.csv')
# Input data set, we use a capital X
X = music_data.drop(columns=['genre']) #Creates a new table without the genre column
#X #To print the result
# Output data set, we use an input data set
y = music_data['genre'] #Creates a new table with just the genre column
#y #To print the result

#For testing our data
# We're allocationg 20% of our data for testing
# It returns a tuple, so we can unpack it into 4 variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# For training our model
model = DecisionTreeClassifier()
# We pass in the training input and output data
model.fit(X_train, y_train)
predictions = model.predict(X_test) # For making predictions we pass in the testing data
predictions

#For testing the accuracy of our model
#We pass in the expected values and the actual values
score = accuracy_score(y_test, predictions)
score