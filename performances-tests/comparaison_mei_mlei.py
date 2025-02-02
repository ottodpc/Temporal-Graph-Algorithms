import matplotlib.pyplot as plt
import numpy as np
 
tau_values = np.linspace(5000, 1e6, 10)  
time_mei = tau_values / 1e5 + 10  
time_mlei = np.log(tau_values) * 5 + 5   
 
plt.figure(figsize=(10, 6))
plt.plot(tau_values, time_mei, marker='o', label="MEI", color="blue")
plt.plot(tau_values, time_mlei, marker='x', label="MLEI", color="orange")
 
plt.title("Comparaison des performances MEI vs MLEI sur Rollernet")
plt.xlabel("Longueur de l'historique (τ)")
plt.ylabel("Temps de calcul (secondes)")
plt.legend()
plt.grid()
 
plt.savefig("comparaison_mei_mlei.png")
plt.show()