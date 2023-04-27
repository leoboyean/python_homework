import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#########################################################################################################
###########              DONE            Forward Selection                DONE                 ##########
#########################################################################################################

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'



from sklearn.feature_selection import f_regression
from sklearn.linear_model import LinearRegression

housing = pd.read_csv(url, sep='\s+', header=None)
print(housing.columns)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Perform forward feature selection
n_features = 3  # number of features to select
estimator = LinearRegression()
selected_features = set()

for i in range(n_features):
    best_score = 0
    best_feature = None
    
    for feature in X.columns:
        if feature not in selected_features:
            selected_features.add(feature)
            X_selected = X[list(selected_features)]
            scores, _ = f_regression(X_selected, y)
            score = scores.mean()
            
            if score > best_score:
                best_score = score
                best_feature = feature
                
            selected_features.remove(feature)
            
    selected_features.add(best_feature)

print("Forward Selection")
print('Selected features:', list(selected_features))


#########################################################################################################
###########                              Chi Cuadrado                                          ##########
#########################################################################################################


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# Separate features and target variable
x = housing.iloc[:, :-1]  # features
x = x.astype('int') 
y = housing.iloc[:, -1]   # target variable
y = y.astype('int') 
# Apply chi-squared feature selection
k = 3  # number of top features to select
selector = SelectKBest(chi2, k=k)
selector.fit(x, y)

# Get the selected features
selected_features = x.columns[selector.get_support()]
print("Chi Cuadrado")
print('Selected features:', list(selected_features))


#########################################################################################################
###########                          ANOVA Feature Selection                                   ##########
#########################################################################################################

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
# Load the dataset

# Separate features and target variable
x = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable
x = x.astype('int')
y = y.astype('int')

# Apply ANOVA feature selection
k = 3  # number of top features to select
selector = SelectKBest(f_classif, k=k)
selector.fit(x, y)

# Get the selected features
selected_features = X.columns[selector.get_support()]
print("ANOVA Feature Selection")
print('Selected features:', list(selected_features))

#########################################################################################################
###########                              Correlation MAP                                       ##########
#########################################################################################################

import seaborn as sns
import matplotlib.pyplot as plt

# dataset of Housing
#iris = pd.read_csv(url, header=None)

#iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Compute the correlation matrix
corr = housing.corr()

# Plot the correlation matrix
sns.set (rc = {'figure.figsize':(9, 8)}, font_scale=0.5)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

# Perform feature selection based on correlation
threshold = 0.5
corr_features = set()
for i in range(len(corr.columns)):
    for j in range(i):
        if abs(corr.iloc[i, j]) > threshold:
            corr_features.add(corr.columns[i])

print('Selected features:', list(corr_features))

# Create a new dataframe with the selected features
selected_features_df = housing[list(corr_features)]

# Display the new dataframe
print('\nNew dataframe with selected features:')
print(selected_features_df.head(), "==*== Correlation-based feature selection ==*==")
