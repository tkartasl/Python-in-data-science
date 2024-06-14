import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load

def convert_capita(pop_str):
	"""Convert K to thousands."""
	pop_str = pop_str.strip().upper()
	if 'K' in pop_str:
		return float(pop_str.replace('K', '')) * 1e3
	else:
		return float(pop_str)

def main():
	"""Program that calls the load function from the first exercise, loads the files "income_per_person_gdppercapita_ppp_inflation_adjusted.csv" and "life_expectancy_years.csv",
	and displays the projection of life expectancy in relation to the gross national product of
	the year 1900 for each country."""

	df_capita = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
	if df_capita is None or df_capita.empty:
		print("Failed to load data")
		return

	for col in df_capita.columns[1:]:
		df_capita[col] = df_capita[col].apply(convert_capita)

	df_life = load("life_expectancy_years.csv")
	if df_life is None or df_life.empty:
		print("Failed to load data")
		return

	capita = df_capita.reindex(columns = ['1900']).to_numpy()
	life = df_life.reindex(columns = ['1900']).astype(float).to_numpy()

	fig, ax = plt.subplots()
	
	ax.set_title("1900")
	ax.set_xlabel('Gross domestic product')
	ax.set_ylabel('Life Expectancy')
	ax.plot(capita, life, marker='o')
	plt.xticks(np.aragne(20, 55+1, 5))
	plt.yticks(np.arange(0, 10000+1, 1000))
	plt.show()
if __name__ == "__main__":
	main()