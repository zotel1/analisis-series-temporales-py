import pandas as pd
diet.index = pd.to_datetime(diet.index)

#Plot the entire time series diet and show gridlines
diet.plot(grid=True)
plt.show()