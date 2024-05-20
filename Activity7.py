import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:\\Users\\mnced\\OneDrive\\Desktop\\tp test 1\\dataset - 2020-09-24.csv")
sns.set_theme()


# Setting different styles to compare
sns.set_style("whitegrid")
sns.lineplot(x="Appearances", y="Passes", data=df)
plt.title('Appearances vs Passes')
plt.show()

# Setting the style to dark
sns.set_style("dark")
sns.lineplot(x="Appearances", y="Tackles", data=df)
plt.title('Appearances vs Tackles')
plt.show()

# Setting the context to "talk" for larger plots suitable for presentations
sns.set_context("talk")
sns.lineplot(x="Appearances", y="Goals", data=df)
plt.title('Appearances vs Goals')
plt.show()

# Setting the context to "paper" for smaller plots suitable for papers
sns.set_context("paper")
sns.lineplot(x="Appearances", y="Interceptions", data=df)
plt.title('Appearances vs Interceptions')
plt.show()

# Distribution plot for Passes
sns.distplot(df['Passes'], kde=True)
plt.title('Distribution of Passes')
plt.show()

# KDE plot for Tackles
sns.kdeplot(data=df['Tackles'], shade=True)
plt.title('KDE of Tackles')
plt.show()

# Rug plot for Goals
sns.rugplot(df['Goals'])
plt.title('Rug Plot of Goals')
plt.show()

# Box plot for Goals by Position
sns.boxplot(x='Position', y='Goals', data=df)
plt.title('Goals by Position')
plt.show()

# Violin plot for Passes by Position
sns.violinplot(x='Position', y='Passes', data=df)
plt.title('Passes by Position')
plt.show()

# Swarm plot for Tackles by Position
sns.swarmplot(x='Position', y='Tackles', data=df)
plt.title('Tackles by Position')
plt.show()

# Pair plot for numerical columns with hue as Position
sns.pairplot(df[['Goals', 'Passes', 'Tackles', 'Interceptions']], hue='Position')
plt.title('Pair Plot for Numerical Columns by Position')
plt.show()

# Joint plot for Goals and Passes
sns.jointplot(x='Goals', y='Passes', data=df, kind='scatter')
plt.title('Joint Plot of Goals and Passes')
plt.show()