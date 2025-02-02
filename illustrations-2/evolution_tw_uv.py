import matplotlib.pyplot as plt
import numpy as np
 
time_steps = np.arange(0, 10)
tw_uv_initial = np.ones_like(time_steps) 
 
tw_uv_step1 = tw_uv_initial.copy()
tw_uv_step1[3:6] = 0 
 
tw_uv_step2 = tw_uv_step1.copy()
tw_uv_step2[7:] = 0  
 
plt.figure(figsize=(10, 4))
plt.step(time_steps, tw_uv_initial, where='post', label="Initial", linestyle='--')
plt.step(time_steps, tw_uv_step1, where='post', label="Étape 1", linestyle='-.')
plt.step(time_steps, tw_uv_step2, where='post', label="Étape 2", linestyle='-')
 
plt.scatter([3, 4, 5], [0, 0, 0], color='red', label="Instants supprimés (Étape 1)")
plt.scatter([7, 8, 9], [0, 0, 0], color='orange', label="Instants supprimés (Étape 2)")
 
plt.title("Évolution de $Tw(u, v)$")
plt.xlabel("Temps")
plt.ylabel("Inclus dans $Tw(u, v)$")
plt.legend()
plt.grid()
plt.show()