import pandas as pd 

master_season_dfs = list()
for year in range(1991,2019):
	master_season_dfs.append(pd.read_excel("Resources/" + str(year) + "/Master_" + str(year) + ".xlsx"))

standings_dfs = list()
for year in range(1991,2019):
	standings_dfs.append(pd.read_excel("Resources/" + str(year) + "/Standings_" + str(year) + ".xlsx"))

salary_dfs = list()
for year in range(1991,2019):
	master_season_dfs.append(pd.read_csv("Resources/" + str(year) + "/Salary_" + str(year) + ".csv"))

salary_cap_df = pd.read_excel("Resources/SalaryCap.xlsx")

#if the spreadsheets already exist, it will read them in and use this list.
seasons_PER_list = list()
for year in range(1991,2019):
	df = pd.read_excel('Resources/' + str(year) + "/Team_PER_" + str(year) + ".xlsx")
	seasons_PER_list.append(df)

#when constructing new PER spreadsheets, this list will be used. When updating the spreadsheets, it will still use the old ones when running
#analysis. Thus, run this file twice, once constructing sheets, and once analyzing. 
new_per_list = list()
for x in range(1,29):
	season_dict = dict()
	new_per_list.append(season_dict)


team_name_list = list()
team_name_list.append("ATL")
team_name_list.append("BKN")
team_name_list.append("BOS")
team_name_list.append("CHA")
team_name_list.append("CHI")
team_name_list.append("CLE")
team_name_list.append("DAL")
team_name_list.append("DEN")
team_name_list.append("DET")
team_name_list.append("GSW")
team_name_list.append("HOU")
team_name_list.append("IND")
team_name_list.append("LAC")
team_name_list.append("LAL")
team_name_list.append("MEM")
team_name_list.append("MIA")
team_name_list.append("MIL")
team_name_list.append("MIN")
team_name_list.append("NOP")
team_name_list.append("NYK")
team_name_list.append("OKC")
team_name_list.append("ORL")
team_name_list.append("PHI")
team_name_list.append("PHX")
team_name_list.append("POR")
team_name_list.append("SAC")
team_name_list.append("SAS")
team_name_list.append("TOR")
team_name_list.append("UTA")
team_name_list.append("WAS")
team_name_list.append("NJN")
team_name_list.append("SEA")
team_name_list.append("WSB")
team_name_list.append("VAN")
team_name_list.append("CHH")
team_name_list.append("PHO")
team_name_list.append("BRK")
team_name_list.append("CHO")
team_name_list.append("NOH")
team_name_list.append("NOK")

full_team_name_list = list()

full_team_name_list.append("Atlanta Hawks")
full_team_name_list.append("Brooklyn Nets")
full_team_name_list.append("Boston Celtics")
full_team_name_list.append("Charlotte Hornets")
full_team_name_list.append("Chicago Bulls")
full_team_name_list.append("Cleveland Cavaliers")
full_team_name_list.append("Dallas Mavericks")
full_team_name_list.append("Denver Nuggets")
full_team_name_list.append("Detroit Pistons")
full_team_name_list.append("Golden State Warriors")
full_team_name_list.append("Houston Rockets")
full_team_name_list.append("Indiana Pacers")
full_team_name_list.append("Los Angeles Clippers")
full_team_name_list.append("Los Angeles Lakers")
full_team_name_list.append("Memphis Grizzlies")
full_team_name_list.append("Miami Heat")
full_team_name_list.append("Milwaukee Bucks")
full_team_name_list.append("Minnesota Timberwolves")
full_team_name_list.append("New Orleans Pelicans")
full_team_name_list.append("New York Knicks")
full_team_name_list.append("Oklahoma City Thunder")
full_team_name_list.append("Orlando Magic")
full_team_name_list.append("Philadelphia 76ers")
full_team_name_list.append("Phoenix Suns")
full_team_name_list.append("Portland Trail Blazers")
full_team_name_list.append("Sacramento Kings")
full_team_name_list.append("San Antonio Spurs")
full_team_name_list.append("Toronto Raptors")
full_team_name_list.append("Utah Jazz")
full_team_name_list.append("Washington Wizards")
full_team_name_list.append("New Jersey Nets")
full_team_name_list.append("Seattle SuperSonics")
full_team_name_list.append("Washington Bullets")
full_team_name_list.append("Vancouver Grizzlies")
full_team_name_list.append("Charlotte Hornets")
full_team_name_list.append("Phoenix Suns")
full_team_name_list.append("Brooklyn Nets")
full_team_name_list.append("Charlotte Hornets")
full_team_name_list.append("New Orleans Hornets")
full_team_name_list.append("New Orleans/Oklahoma City Hornets")

abbr_to_names = dict(zip(team_name_list,full_team_name_list))

#calculates any metric for any team for any year. returns a number value.
def calculateTeamMetric(teamName, year, metric):
	df = getOneMasterSeason(year)
	df = df.loc[df['Tm'] == teamName]
	if(df.empty):
		return -1
	cumulative = 0
	numPlayers = 0
	for row in df.itertuples(index = True,name = 'Pandas'):
		value = getattr(row,metric)
		cumulative += value
		numPlayers += 1
	return cumulative / numPlayers

#given a year, will save the values stored in the PER_list to an excel file
def savePERtoExcel(year):
	teamAbbrList = list(new_per_list[year-1991].keys())
	teamMetricList = list(new_per_list[year-1991].values())
	metric_oneyear = [('Team', teamAbbrList),
				('PER', teamMetricList)]
	df = pd.DataFrame.from_items(metric_oneyear)
	writer = pd.ExcelWriter('Resources/' + str(year) + '/Team_PER_' + str(year) + '.xlsx')
	df.to_excel(writer, 'Sheet1')
	writer.save()

#calculates team PER for every team from 1991-2018 and saves them into excel spreadsheets. 
def createPERSpreadsheets():
	for year in range(1991,2019):
		numOfTeams = 0
		year_dict = new_per_list[year-1991]
		for teamAbbr in team_name_list:
			PER = calculateTeamMetric(teamAbbr,year,"PER")
			if (PER == -1):
				continue
			numOfTeams +=1
			year_dict[teamAbbr] = PER
		print("Number of teams in year " + str(year) + ": " + str(numOfTeams))
		savePERtoExcel(year)


def getOneSeasonPER_DF(year):
	return seasons_PER_list[year-1991]

def getOneSeasonStandings_DF(year):
	return standings_dfs[year-1991]

def getOneMasterSeason(year):
	return master_season_dfs[year-1991]

def sortSeasonPERDF(year):
	df = getOneSeasonPER_DF(year)
	df = df.sort_values(by=['PER'], ascending = False)
	return df

def parseRecordStrings(standings_df):
	record_string_list = list()
	for row in standings_df.itertuples(index = True, name = 'Pandas'):
		record_string = getattr(row, 'Overall')
		wins_and_losses = parseRecordString(record_string)
		record_string_list.append(wins_and_losses)
	return record_string_list

def parseRecordString(string):
	return string.split('-')

def calculateAverageAge(short_team,predicting_year):
	df1 = getOneMasterSeason(predicting_year-1)
	df1 = df1.loc[df1['Tm'] == short_team]
	age = 0
	numPlayers = 0
	for row in df1.itertuples(index = True, name = 'Pandas'):
		age += getattr(row,'Age')
		numPlayers += 1
	return age/numPlayers

def calculateContinuity(short_team,predicting_year):
	df1 = getOneMasterSeason(predicting_year-1)
	df1 = df1.loc[df1['Tm'] == short_team]
	df2 = getOneMasterSeason(predicting_year)
	df2 = df2.loc[df2['Tm'] == short_team]
	minutes = 0
	totalMinutesInSeason = 19680
	for row in df1.itertuples(index = True, name = 'Pandas'):
		PID = getattr(row, 'PID')
		for row2 in df2.itertuples(index = True, name = 'Pandas'):
			PID2 = getattr(row2,'PID')
			if(PID != PID2):
				continue
			minutes += getattr(row, 'MP') * getattr(row, 'G')
	return minutes / totalMinutesInSeason


#Start code


#Each column is stored in a list.


short_name_list = list()
long_name_list = list()
predicting_year_list = list()
PER_list = list()
num_wins_list = list()
continuity_list = list()
last_year_wins_list = list()
avg_age_list = list()

for year in range (1991,2018):
	#sort PER's.
	PER_df = sortSeasonPERDF(year)
	last_year_wins_df = getOneSeasonStandings_DF(year)
	standings_df = getOneSeasonStandings_DF(year+1)
	count = 0

	#loop through teams in descending order PER
	for PER_row in PER_df.itertuples(index = True, name = 'Pandas'):
		#find the standing row corresponding to the team using the lookup dict
		df = standings_df.loc[standings_df['Team'] == abbr_to_names[getattr(PER_row,'Team')]]
		last_year_df = last_year_wins_df.loc[last_year_wins_df['Team'] == abbr_to_names[getattr(PER_row,'Team')]]
		for standings_row in df.itertuples(index = True, name = 'Pandas'):
			#get all metrics
			short_name = getattr(PER_row, 'Team')
			long_name = getattr(standings_row,'Team')
			predicting_year = year+1
			PER = str(getattr(PER_row, 'PER'))
			record = getattr(standings_row, 'Overall')
			for last_year_row in last_year_df.itertuples(index = True, name = 'Pandas'):
				last_year_record = getattr(last_year_row, 'Overall')
			num_wins = parseRecordString(record)[0]
			last_year_num_wins = parseRecordString(last_year_record)[0]
			continuity = calculateContinuity(short_name, predicting_year)
			avg_age = calculateAverageAge(short_name,predicting_year)
			
			#add to lists
			short_name_list.append(short_name)
			long_name_list.append(long_name)
			predicting_year_list.append(predicting_year)
			PER_list.append(PER)
			num_wins_list.append(num_wins)
			continuity_list.append(continuity)
			last_year_wins_list.append(last_year_num_wins)
			avg_age_list.append(avg_age)
			break

master = [('short_name', short_name_list),
			('long_name', long_name_list),
			('predicting_year', predicting_year_list),
			('PER', PER_list),
			('num_wins', num_wins_list),
			('last_year_wins', last_year_wins_list),
			('continuity',continuity_list),
			('avg_age', avg_age_list)]

master_df = pd.DataFrame.from_items(master)
writer = pd.ExcelWriter('Master_with_age.xlsx')
master_df.to_excel(writer, 'Sheet1')
writer.save()


