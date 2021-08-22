#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_excel('./sheetset.xls')

imagem_1_2 = data.groupby(["imagem_1_2"])["imagem_1_2"].count()
imagem_2_2 = data.groupby(["imagem_2_2"])["imagem_2_2"].count()
imagem_3_2 = data.groupby(["imagem_3_2"])["imagem_3_2"].count()
imagem_4_2 = data.groupby(["imagem_4_2"])["imagem_4_2"].count()
imagem_5_2 = data.groupby(["imagem_5_2"])["imagem_5_2"].count()

labels = ["Imagem 1", "Imagem 2", "Imagem 3", "Imagem 4", "Imagem 5"]

def calc_percentual(dataset):
    return round((dataset.values[0] / (dataset.values[0] + dataset.values[1])) * 100, 2)

porcentagens = [calc_percentual(imagem_1_2), calc_percentual(imagem_2_2), calc_percentual(imagem_3_2), calc_percentual(imagem_4_2), calc_percentual(imagem_5_2)]


plt.barh(labels, porcentagens, color="#0032e8", alpha=0.75)

plt.xlabel("Questões", fontsize=12)
plt.xticks([50, 75, 85, 90, 95])
plt.ylabel("Porcentagem", fontsize=12)
plt.title("Nível de 'conversão' de designs com UX elaborados", fontsize=15)
plt.gcf().set_size_inches(5, 5)

plt.show()