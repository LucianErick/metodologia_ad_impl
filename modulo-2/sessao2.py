#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd


# In[47]:


import numpy as np


# In[46]:


import seaborn as sb
import matplotlib.pyplot as plt


# In[5]:


data = pd.read_excel('./sheetset.xls')
data.head(5)


# In[92]:


imagem_1_1 = data.groupby(["imagem_1_1"])["imagem_1_1"].count()
imagem_1_2 = data.groupby(["imagem_1_2"])["imagem_1_2"].count()

bar_width = 0.25
tamanho_lista = 2

r1 = np.arange(2)
r2 = [x + bar_width for x in r1]

plt.bar(r1, imagem_1_1.values[0], width=bar_width, label="Direita", edgecolor="#b0b0b0")
plt.bar(r2, imagem_1_1.values[1], width=bar_width, label="Esquerda", edgecolor="#b0b0b0")

plt.xlabel("Questões", fontsize=12)
plt.xticks([r + (bar_width / 2) for r in range(tamanho_lista)], ["Conforto", "Preferência"])
plt.yticks(np.arange(0, 50, step=5))
plt.ylabel("Frequência", fontsize=12)
plt.title("Resultados da imagem 1", fontsize=15)

plt.legend(loc='upper center')
plt.show()



# In[93]:


imagem_2_1 = data.groupby(["imagem_2_1"])["imagem_2_1"].count()
imagem_2_2 = data.groupby(["imagem_2_2"])["imagem_2_2"].count()

bar_width = 0.25
tamanho_lista = 2

r1 = np.arange(2)
r2 = [x + bar_width for x in r1]

plt.bar(r1, imagem_2_1.values[0], width=bar_width, label="Direita", edgecolor="#b0b0b0")
plt.bar(r2, imagem_2_1.values[1], width=bar_width, label="Esquerda", edgecolor="#b0b0b0")

plt.xlabel("Questões", fontsize=12)
plt.xticks([r + (bar_width / 2) for r in range(tamanho_lista)], ["Conforto", "Preferência"])
plt.yticks(np.arange(0, 50, step=5))
plt.ylabel("Frequência", fontsize=12)
plt.title("Resultados da imagem 2", fontsize=15)

plt.legend(loc='upper center')
plt.show()


# In[89]:


imagem_3_1 = data.groupby(["imagem_3_1"])["imagem_3_1"].count()
imagem_3_2 = data.groupby(["imagem_3_2"])["imagem_3_2"].count()

bar_width = 0.25
tamanho_lista = 2

r1 = np.arange(2)
r2 = [x + bar_width for x in r1]

plt.bar(r1, imagem_3_1.values[0], width=bar_width, label="Direita")
plt.bar(r2, imagem_3_1.values[1], width=bar_width, label="Esquerda")

plt.xlabel("Questões", fontsize=12)
plt.xticks([r + (bar_width / 2) for r in range(tamanho_lista)], ["Amistosidade", "Preferência"])
plt.yticks(np.arange(0, 50, step=5))
plt.ylabel("Frequência", fontsize=12)
plt.title("Resultados da imagem 3", fontsize=15)

plt.legend(loc='upper center')
plt.show()


# In[94]:


imagem_4_1 = data.groupby(["imagem_4_1"])["imagem_4_1"].count()
imagem_4_2 = data.groupby(["imagem_4_2"])["imagem_4_2"].count()

bar_width = 0.25
tamanho_lista = 2

r1 = np.arange(2)
r2 = [x + bar_width for x in r1]

plt.bar(r1, imagem_4_1.values[0], width=bar_width, label="Direita", edgecolor="#b0b0b0")
plt.bar(r2, imagem_4_1.values[1], width=bar_width, label="Esquerda", edgecolor="#b0b0b0")

plt.xlabel("Questões", fontsize=12)
plt.xticks([r + (bar_width / 2) for r in range(tamanho_lista)], ["Conforto", "Preferência"])
plt.yticks(np.arange(0, 50, step=5))
plt.ylabel("Frequência", fontsize=12)
plt.title("Resultados da imagem 4", fontsize=15)

plt.legend(loc='upper center')
plt.show()


# In[95]:


imagem_5_1 = data.groupby(["imagem_5_1"])["imagem_5_1"].count()
imagem_5_2 = data.groupby(["imagem_5_2"])["imagem_5_2"].count()

bar_width = 0.25
tamanho_lista = 2

r1 = np.arange(2)
r2 = [x + bar_width for x in r1]

plt.bar(r1, imagem_5_1.values[0], width=bar_width, label="Direita", edgecolor="#b0b0b0" )
plt.bar(r2, imagem_5_1.values[1], width=bar_width, label="Esquerda", edgecolor="#b0b0b0")

plt.xlabel("Questões", fontsize=12)
plt.xticks([r + (bar_width / 2) for r in range(tamanho_lista)], ["Simplicidade", "Preferência"])
plt.yticks(np.arange(0, 50, step=5))
plt.ylabel("Frequência", fontsize=12)
plt.title("Resultados da imagem 5", fontsize=15)

plt.legend(loc='upper center')
plt.show()


# In[ ]:




