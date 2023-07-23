import scipy.stats as stats

media = 12000
desvio_padrao = 800

probabilidade_12000 = stats.norm.cdf(12000, media, desvio_padrao)
probabilidade_13000 = stats.norm.cdf(13000, media, desvio_padrao)

probabilidade_entre_12000_e_13000 = probabilidade_13000 - probabilidade_12000

probabilidade_entre_12000_e_13000
