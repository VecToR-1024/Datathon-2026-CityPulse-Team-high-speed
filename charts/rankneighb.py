import pandas as pd
import plotly.express as px

df = pd.read_csv("Access_to_Everyday_Life_Dataset.csv")

neighbor = df['properties/neighborhood'].value_counts().reset_index()
neighbor.columns = ['properties/neighborhood', 'access_point_count']
point_type = df['properties/label_type'].value_counts().reset_index()
point_type.columns = ['properties/label_type', 'access_point_count']

neighbor_sorted = neighbor.sort_values(by='access_point_count', ascending=False)

fig = px.bar(
    neighbor_sorted,
    x='properties/neighborhood',
    y='access_point_count',
    title='Number of Access Points per Neighborhood',
    labels={'properties/neighborhood': 'Neighborhood', 'access_point_count': 'Number of Access Points'}
)

fig.update_layout(xaxis_tickangle=-45)
fig.show()

point_type_sorted = point_type.sort_values(by='access_point_count', ascending=False)

fig = px.bar(
    point_type_sorted,
    x='properties/label_type',
    y='access_point_count',
    title='Number of Access Points per Label Type',
    labels={'properties/label_type': 'Label Type', 'access_point_count': 'Number of Access Points'}
)

fig.update_layout(xaxis_tickangle=-45)
fig.show()