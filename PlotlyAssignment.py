# %% [markdown]
# Q1. Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
# scatter plot for age and fare columns in the titanic dataset.

# %%
import seaborn as sns

# %%
df=sns.load_dataset('titanic')
df

# %%
import plotly.graph_objects as go

# %%
fig=go.Figure()
fig.add_trace(go.Scatter(x=df.age,y=df.fare,mode='markers'))

# %% [markdown]
# Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express.

# %%
df1=sns.load_dataset('tips')
df1

# %%
import plotly.express as px

# %%
fig = px.box(df1, y="total_bill",x="tip")
fig.show()

# %% [markdown]
# Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
# the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
# column with the color parameter.

# %%
fig=go.Figure()
color_map = {"Thur": "blue", "Fri": "orange", "Sat": "green", "Sun": "red"}
pat_map = {"No": "\\", "Yes": "+"}
fig.add_trace(go.Histogram(x=df1["total_bill"], marker_color=df1["day"].map(color_map),marker_pattern_shape=df1['smoker'].map(pat_map), name="Total Bill"))

# %% [markdown]
# Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
# the color parameter.

# %%
df2=sns.load_dataset('iris')
df2

# %%
fig=px.scatter_matrix(df2,dimensions=['sepal_width','sepal_length','petal_width','petal_length'],color='species')
fig.show()

# %% [markdown]
# Q5. What is Distplot? Using Plotly express, plot a distplot.
# 
# A distplot, short for distribution plot, visualizes the distribution of a single numerical variable in your data. It typically combines a histogram, kernel density estimation (KDE) line, and rug plot to offer a comprehensive view of the data's spread and shape.

# %%
import plotly.express as px
fig = px.histogram(df1, x="tip")  # Correct function name

# Customize as needed (e.g., title, color, etc.)
fig.update_layout(title="Distribution of Total Bill")

fig.show()


