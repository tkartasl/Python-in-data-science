import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd
from load_csv import load

def convert_to_millions(x, pos):
    """Convert numbers to Millionformat"""
    return f'{x * 1e-6:.0f}M'

def convert_population(pop_str):
	"""Convert K to thousands, M to millions  and B to billions"""
	pop_str = pop_str.strip().upper()
	if 'K' in pop_str:
		return float(pop_str.replace('K', '')) * 1e3
	elif 'M' in pop_str:
		return float(pop_str.replace('M', '')) * 1e6
	elif 'B' in pop_str:
		return float(pop_str.replace('B', '')) * 1e9
	else:
		return float(pop_str)

def main():
	"""program that calls the load function from the first exercise, loads the file
	population_total.csv, and displays the country information of your campus versus other
	country of your choice."""

	df_population = load("population_total.csv")

	if df_population is None or df_population.empty:
		print("Failed to load data")
		return
	
	for col in df_population.columns[1:]:
		df_population[col] = df_population[col].apply(convert_population)

	finland = df_population[df_population["country"]== "Finland"]
	if finland is None:
		print("No data for Finland")
		return
	italy = df_population[df_population["country"]== "Italy"]
	if italy is None:
		print("No data for Italy",)
		return

	population_fin = finland.iloc[0, 1:252].to_numpy()
	population_it = italy.iloc[0, 1:252].to_numpy()
	years = df_population.columns[1:252].astype(int).to_numpy()
	fig, ax = plt.subplots()

	ax.set_title("Population Projections")
	ax.set_xlabel('Year')
	ax.set_ylabel('Population')
	ax.plot(years, population_fin, label='Finland')
	ax.plot(years, population_it, label='Italy')
	ax.legend(loc='lower right')

	ax.yaxis.set_major_formatter(FuncFormatter(convert_to_millions))
	plt.xticks(np.arange(min(years), max(years)+1, 40))
	plt.yticks(np.arange(0, max(population_it.max(), population_fin.max()) + 1, 2e6 * 10))
	plt.show()
if __name__ == "__main__":
	main()