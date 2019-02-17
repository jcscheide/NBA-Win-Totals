import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
import numpy as np

df = pd.read_excel("master_with_age.xlsx")

wins = df.pop('num_wins').values

y = wins
X = df.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

linreg = LinearRegression().fit(X_train,y_train)
linreg_y_pred = linreg.predict(X_test)
print("LinReg: " + str(mean_absolute_error(y_test, linreg_y_pred)))
print(linreg.coef_)

plt.scatter(linreg_y_pred, y_test, color='black', label='LinReg')

svr = SVR().fit(X_train,y_train)
svr_y_pred = svr.predict(X_test)
print("SVR: " + str(mean_absolute_error(y_test, svr_y_pred)))
print(svr.support_vectors_)


plt.scatter(svr_y_pred, y_test, color='blue', label = 'SVR')

x = np.linspace(5,80)
plt.plot(x,x)

plt.xticks(np.arange(5,80,step=5))
plt.yticks(np.arange(5,80,step=5))
plt.xlabel('Predicted wins')
plt.ylabel('Actual wins')
plt.title('Predicted wins vs Actual wins')
plt.legend(loc='upper left')
plt.text(55,25,"LinReg MAE: " + str(round(mean_absolute_error(y_test, linreg_y_pred), 2)))
plt.text(55,20,"SVR MAE: " + str(round(mean_absolute_error(y_test, svr_y_pred), 2)))

plt.show()