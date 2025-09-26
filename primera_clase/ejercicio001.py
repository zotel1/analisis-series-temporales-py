import pandas as pd
diet.index = pd.to_datetime(diet.index)


"""
cortamos el conjunto de datos diet para conservar solo slkos valores de 2012, asignandolos a diet2012
- traza rl diet2012, creando de nuevo lineas de cuadricula con el argumento grid
"""
# Slice the dataset to keep only 212
diet2012 = diet['2012']

#Plot the entire time series diet and show gridlines
diet.plot(grid=True)
plt.show()