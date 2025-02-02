import matplotlib.pyplot as plt
import numpy as np
 
tau_values = np.linspace(5000, 1e6, 10)  
execution_times = np.log(tau_values) * 10 + 5  
 
plt.figure(figsize=(10, 6))
plt.plot(tau_values, execution_times, marker='o', label="Temps de calcul (MLEI)")
 
plt.title("Dépendance logarithmique du temps de calcul en fonction de τ")
plt.xlabel("Longueur de l'historique (τ)")
plt.ylabel("Temps de calcul (secondes)")
plt.legend()
plt.grid()
 
plt.savefig("dependance_logarithmique_tau.png")
plt.show()