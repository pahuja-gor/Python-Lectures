import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

tips = sns.load_dataset("tips")
sns.relplot(x = "total_bill", y = "tip", col = "time", hue = "smoker", size = "size", data = tips)
plt.show()

dots = sns.load_dataset("dots")
sns.relplot(kind = "line", x = "time", y = "firing_rate", col = "align", hue = "choice", size = "coherence", legend = "full", data = dots)
plt.show()

fmri = sns.load_dataset("fmri")
sns.relplot(kind = "line", x = "timepoint", y = "signal", col = "region", hue = "event", style = "event", data = fmri)
plt.show()

sns.lmplot(x = "total_bill", y = "tip", col = "time", hue = "smoker", data = tips)
plt.show()

sns.catplot(x = "day", y = "total_bill", hue = "smoker", kind = "swarm", data = tips)
plt.show()

sns.catplot(x = "day", y = "total_bill", hue = "smoker", kind = "violin", split = True, data = tips)
plt.show()

iris = sns.load_dataset("iris")
sns.jointplot(x = "sepal_length", y = "petal_length", data = iris)
plt.show()