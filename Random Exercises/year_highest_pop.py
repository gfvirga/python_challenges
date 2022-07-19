birth_death_years = [[2000,2010],[1975,2005],[1975,2003],[1803,1809],[1750,1869],[1840,1935],[1803,1921],[1894,1921]]

population = {}


lowest_year = min(b for b,d in birth_death_years)
lowest_year = max(b for b,d in birth_death_years)

for birth, death in birth_death_years:
  if birth in population.keys():
    population[birth] += 1
  else:
    population[birth] = 1

  if death+1 in population.keys():
    population[death+1] -= 1
  else:
    population[death+1] = -1

largest = 0
current = 0
# for year in sorted(population.keys()):


print(population)