import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
 
data = {
    "tau": np.linspace(5000, 1e6, 10), 
    "time_MEI": np.random.uniform(1, 100, 10), 
    "time_MLEI": np.random.uniform(1, 50, 10), 
}

df = pd.DataFrame(data)
 
plt.figure(figsize=(10, 6))
sns.lineplot(x="tau", y="time_MEI", data=df, label="MEI", marker="o")
sns.lineplot(x="tau", y="time_MLEI", data=df, label="MLEI", marker="x")
 
plt.title("Comparaison des performances MEI vs MLEI en fonction de τ")
plt.xlabel("Longueur de l'historique (τ)")
plt.ylabel("Temps d'exécution (secondes)")
plt.legend()
plt.grid()
 
plt.savefig("comparaison_MEI_MLEI.png")
plt.show()