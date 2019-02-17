import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm 

master_df = pd.read_excel("Master.xlsx")

X = master_df[['PER','last_year_wins','continuity']]
Y = master_df['num_wins']

regr = linear_model.LinearRegression()
regr.fit(X,Y)

print('Intercept: \n', regr.intercept_)
print('Coeffecients: \n', regr.coef_)

pred_PER = 0
pred_last_year_wins = 0
pred_continuity = 0

print('Predicted wins: \n', 
	regr.predict([[pred_PER, pred_last_year_wins, pred_continuity]]))

X = sm.add_constant(X)

model = sm.OLS(Y,X).fit()
predictions = model.predict(X)
print_model = model.summary()
print(print_model)