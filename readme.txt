Project Outline

Forecasting win-loss records

The purpose of this project is to create a model which predicts regular season win totals using data only
available before the season tips off. 
modeling. The project deliverable is a method which produces the lowest error in forecasting wins for a
season. 

Imagine that a GM asks you to evaluate two trade proposals before the start of the 2018-19
season. The GM assures you that both deals provide positive value for the organization and any
outgoing assets will not have an effect on the upcoming season. Using takeaways from your
model, describe how you would advise the GM in selecting between the following two offers:
  a. The more favorable unprotected 1st round pick from either the Los Angeles Clippers or
Detroit Pistons in the 2019 NBA draft
  b. The unprotected 1st round pick from the Cleveland Cavaliers in the 2019 NBA draft


Trade Proposal

1.	The more favorable unprotected 1st round pick from either the Los Angeles Clippers or Detroit Pistons in the 2019 NBA Draft.

Predicting LAC2019:
Last year wins: 42	Continuity: 0.4080	Average age: 27.24
Model: 0.6061 * last_year_wins + 11.3776 * continuity + -0.4617 * avg_age + 21.7312
Predicted wins = 39

Predicting DET2019:
Last year wins: 39	Continuity: 0.5363	Average age: 26.29
Predicted wins = 38

The more favorable of the two picks is likely to be the Detroit pick, but both are very similar. 

2.	The unprotected 1st round pick from the Cleveland Cavaliers in the 2019 NBA Draft. 

Predicting CLE2019:
Last year wins: 50	Continuity: 0.3866	Average age: 27.13
Predicted wins: 44

I would recommend accepting the trade proposal for the best of the Clippers/Pistons pick for two reasons: firstly, the model predicts that both teams will win less games than the Cavaliers. Secondly, having a best-pick swap is ideal because it mitigates the error of the model by essentially doubling the chance one of the teams has a bad season. 
