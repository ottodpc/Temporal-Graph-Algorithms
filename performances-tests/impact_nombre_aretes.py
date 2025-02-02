import matplotlib.pyplot as plt
import numpy as np
 
m_values = np.linspace(1000, 1e5, 10)  
time_rollernet = m_values / 1e4 + 10  
time_enron = m_values / 1e5 + 2  
 
plt.figure(figsize=(10, 6))
plt.plot(m_values, time_rollernet, marker='o', label="Rollernet (dense)", color="red")
plt.plot(m_values, time_enron, marker='x', label="Enron (clairsemé)", color="green")
 
plt.title("Impact du nombre d'arêtes (m) sur le temps de calcul")
plt.xlabel("Nombre d'arêtes (m)")
plt.ylabel("Temps de calcul (secondes)")
plt.legend()
plt.grid()
 
plt.savefig("impact_nombre_aretes.png")
plt.show()