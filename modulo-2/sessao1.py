#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

data = pd.read_excel('./sheetset.xls')

# Gerando gráfico de barras para parâmetro populacional de idade

subset = data["idade"]
subset.describe(), str("Mediana: {}".format(subset.median()))

idade = data.groupby("idade")["idade"].count()

plt.title("Idades", fontsize=15)
plt.xlabel("Idade", fontsize=12)
plt.ylabel("Frequência", fontsize=12)
plt.xticks(np.arange(0, 50, step=2))
plt.bar(idade.index, idade.values, color=['#c21d1d',"#ccad00","#36cc00", "#96d4cc", "#41a6c4", "#6641c4"], alpha=0.75)
plt.show()


# Gerando gráfico de barras para parâmetro populacional sobre conhecimento de UX

conhece_ux = data.groupby("conhece_ux")["conhece_ux"].count()

plt.title("Frequência de conhecedores de UX", fontsize=15)
plt.ylabel("Frequência", fontsize=12)
plt.xlabel("Resposta", fontsize=12)
plt.bar(conhece_ux.index, conhece_ux.values,color=['#a31a1a','#0029cc'], edgecolor="#a1a1a1", alpha=0.75)
plt.show()


# Gerando gráfico de barras para parâmetro populacional sobre conhecimento a respeito de desenvolvimento web

nivel_conhecimento = data.groupby("nivel_conhecimento")["nivel_conhecimento"].count()
nivel_conhecimento.index = ["Nenhum", "Graduação relacionada", "Conhecimento técnico"]

plt.title("Nível de conhecimento em desenvolvimento de sistemas", fontsize=15)
plt.ylabel("Nível", fontsize=12)
plt.xlabel("Frequência", fontsize=12)
plt.xticks(np.arange(0, 50, step=2))
plt.barh(nivel_conhecimento.index, nivel_conhecimento.values, color=['#c21d1d',"#ccad00","#36cc00"], alpha=0.75)
plt.show()


# Gerando gráfico de barras para parâmetro populacional sobre experiência com projeto de interfaces gráficas

subset = data["experiencia_design"]
subset.describe(), str("Mediana: {}".format(subset.median()))

experiencia_design = data.groupby("experiencia_design")["experiencia_design"].count()
experiencia_design.index = ["Nenhuma", "Pouca", "Razoável", "Boa", "Muito alta"]
plt.title("Níveis de experiência design de interfaces", fontsize=15)
plt.xlabel("Frequência", fontsize=12)
plt.xticks(np.arange(0, 25, step=2))
plt.ylabel("Nível de conhecimento", fontsize=12)
plt.barh(experiencia_design.index, experiencia_design.values, color=['#cc0e00',"#ccad00","#36cc00","#00becc", '#0029cc'], alpha=0.75, edgecolor="#a1a1a1")
plt.show()


# Gerando gráfico de barras para parâmetro populacional sobre importância dada ao design de UX durante projeto

subset = data["importancia_ux"]
subset.describe(), str("Mediana: {}".format(subset.median()))

importancia_ux = data.groupby("importancia_ux")["importancia_ux"].count()
importancia_ux.index = ["Irrelevante", "Pouco relevante", "Razoável", "Relevante", "Indispensável"]

plt.title("Importância de pensar em UX no projeto", fontsize=15)
plt.xlabel("Frequência", fontsize=12)
plt.ylabel("Nível de importância", fontsize=12)
plt.barh(importancia_ux.index, importancia_ux.values, color=['#cc0e00',"#ccad00","#36cc00","#00becc", '#0029cc'], alpha=0.75, edgecolor="#a1a1a1")
plt.show()


# Gerando gráfico de barras para parâmetro populacional sobre quantidade de recursos que deveriam ser disponibilizados para design UX

subset = data["qtd_recursos"]
subset.describe(), str("Mediana: {}".format(subset.median()))

qtd_recursos = data.groupby("qtd_recursos")["qtd_recursos"].count()
qtd_recursos.index = ["Muito pouco", "Pouco", "Razoável", "Grande", "Muito grande"]
plt.title("Quantidade de recursos alocados para UX", fontsize=15)
plt.xlabel("Frequência", fontsize=12)
plt.ylabel("Quantidade de recursos", fontsize=12)
plt.barh(qtd_recursos.index, qtd_recursos.values, color=['#cc0e00',"#ccad00","#36cc00","#00becc", '#0029cc'], alpha=0.75, edgecolor="#a1a1a1")
plt.show()


# Gerando gráfico de barras para parâmetro populacional sobre quantidade de profissionais especializados

subset = data["qtd_profissionais"]
subset.describe(), str("Mediana: {}".format(subset.median()))

Frequência_profissionais = data.groupby("qtd_profissionais")["qtd_profissionais"].count()
Frequência_profissionais.index = ["Poucos", "Razoáveis", "Muitos"]

plt.title("Quantidade de profissionais qualificados", fontsize=15)
plt.ylabel("Frequência", fontsize=12)
plt.xlabel("Quantidade de profissionais", fontsize=12)
plt.bar(Frequência_profissionais.index, Frequência_profissionais.values, color=['#cc0e00',"#ccad00","#36cc00"], alpha=0.75, edgecolor="#a1a1a1")
plt.show()


# Gerando gráfico de barras para parâmetro populacional sobre percepção de quantidade de vagas disponíveis no mercado

subset = data["mercado_vagas"]
subset.describe(), str("Mediana: {}".format(subset.median()))

vagas = data.groupby("mercado_vagas")["mercado_vagas"].count()
vagas.index = ["Muito Vago", "Há bastante vagas", "Razoável", "Há poucas vagas", "Saturado"]

plt.title("Mercado de vagas", fontsize=15)
plt.xlabel("Frequência", fontsize=12)
plt.ylabel("Nível", fontsize=12)
plt.xticks(np.arange(0, 25, step=2))
plt.barh(vagas.index, vagas.values, color=['#cc0e00',"#ccad00","#36cc00","#00becc", '#0029cc'], alpha=0.75, edgecolor="#a1a1a1")
plt.show()