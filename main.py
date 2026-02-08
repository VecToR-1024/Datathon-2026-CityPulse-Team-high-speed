import plotly.express as px
import numpy as np
import pandas as pd

df = pd.read_csv("GovernmentPriorityIndex.csv")
df = df.dropna()

long = df["geometry/coordinates/0"].to_numpy()
lat = df["geometry/coordinates/1"].to_numpy()
score = df["Score"].to_numpy()

minlat = lat.min()
maxlat = lat.max()
minlong = long.min()
maxlong = long.max()

# number of tiles horizontally
# determines the resolution
cols = 150  
squareSize = (maxlong - minlong) / cols
rows = int(np.ceil((maxlat - minlat) / squareSize))

data = np.zeros((rows, cols))

# creates weight values for areas in the weighted map
for i in range(long.shape[0]):
  la = long[i]
  lo = lat[i]
  rowIndex = int(np.floor((maxlat - lo) / squareSize)) 
  colIndex = int(np.floor((la - minlong) / squareSize))
  if (colIndex == cols):
    colIndex = cols-1
  if (rowIndex == cols):
    rowIndex = cols-1
  data[rowIndex, colIndex] += score[i]

# so that zero values are not colored
data[data == 0] = np.nan

#configures the heatmap
fig = px.imshow(data,
                labels=dict(color="Value"), color_continuous_scale='Plasma')

fig.update_layout(yaxis={'visible': False})
fig.update_layout(xaxis={'visible': False})

fig.show()
#fig.write_html("SquareMapEIG.html")