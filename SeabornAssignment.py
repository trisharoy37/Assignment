# %% [markdown]
# Que 1: Name any five plots that we can plot using the Seaborn library. Also, state the uses of each plot.

# %% [markdown]
# We can plot :
# 1. Scatter plot: Shows the relationship between two continuous variables. Reveals trends, correlations, and clusters. Helps understand how one variable changes with another.
# 2. Distribution Plot : Shows the distribution of a single variable, highlighting its shape, central tendency, and spread. Useful for understanding data properties and outliers.
# 3. Line Plot: Visualizes trends and changes over time or a continuous variable. Useful for showing how a variable evolves, identifies peaks, valleys, and overall patterns.
# 4. Joint Plot: Combines a scatter plot with marginal histograms, offering a comprehensive view of the relationship between two variables and their individual distributions.
# 5. Pairplot: Creates a matrix of scatter plots, visualizing relationships between all pairs of numerical variables in a dataset. Useful for exploring data quickly, identifying potential correlations, and spotting outliers.

# %% [markdown]
# Que 2: Load the "fmri" dataset using the load_dataset function of seaborn. Plot a line plot using x =
# "timepoint" and y = "signal" for different events and regions.

# %%
import seaborn as sns
df=sns.load_dataset('fmri')
df

# %%
sns.lineplot(x="timepoint",y="signal",data=df,style="event",hue="region")

# %% [markdown]
# Que 3: Load the "titanic" dataset using the load_dataset function of seaborn. Plot two box plots using x =
# 'pclass', y = 'age' and y = 'fare'.

# %%
df1=sns.load_dataset("titanic")
df1

# %%
sns.boxplot(x="pclass",y="age",showmeans=True,data=df1)

# %%
sns.boxplot(x="pclass",y="fare",showmeans=True,data=df1)

# %% [markdown]
# Que 4: Use the "diamonds" dataset from seaborn to plot a histogram for the 'price' column. Use the hue
# parameter for the 'cut' column of the diamonds dataset.

# %%
df2=sns.load_dataset("diamonds")
df2.head()

# %%
sns.histplot(x="price",hue='cut',data=df2)

# %% [markdown]
# Que 5: Use the "iris" dataset from seaborn to plot a pair plot. Use the hue parameter for the "species" column
# of the iris dataset.

# %%
df3=sns.load_dataset("iris")
df3.head()

# %%
sns.pairplot(hue='species',data=df3)

# %% [markdown]
# Que 6: Use the "flights" dataset from seaborn to plot a heatmap.

# %%
df4=sns.load_dataset("flights")
df4=df4.iloc[:30,:]

# %%
import pandas as pd


# %%
df4

# %%
#pivot_table = pd.pivot_table(df4, values="passengers", index=["month", "year"], aggfunc="mean")
g=df4.groupby(['month','year'])

# %%
k=g.mean()
k

# %%
sns.heatmap(k, annot=True, fmt=".2f", cmap="YlGnBu")


