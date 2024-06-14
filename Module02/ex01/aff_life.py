import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load

def main():
	"""Program that calls the load function from the previous exercise, loads the file
	life_expectancy_years.csv, and displays the country information of your campus."""

	df_life = load("life_expectancy_years.csv")
	
	if df_life is None or df_life.empty:
		print("Failed to load data")
		return

	country = df_life[df_life["country"]== "Finland"]

	if country is None:
		print("No data for this country")
		return

	life_expectancy = country.iloc[0, 1:].astype(float)
	life_expectancy = life_expectancy.to_numpy()
	
	years = df_life.columns[1:]
	years = pd.to_numeric(years)
	years = years.to_numpy()
	
	fig, ax = plt.subplots()
	
	ax.set_title("Finland Life expectancy Projections")
	ax.set_xlabel('Year')
	ax.set_ylabel('Life expectancy')
	ax.plot(years, life_expectancy)

	plt.xticks(np.arange(min(years), max(years)+1, 40))
	plt.yticks(np.arange(10, 90+1, 10))
	plt.show()
	
if __name__ == "__main__":
	main()