# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Exercício 8 — Detecção de anomalias:
        Use IsolationForest para sinalizar comportamentos anômalos em métricas
        de acesso. Liste quais amostras foram marcadas como anomalia.

        import numpy as np
        # [requisicoes_min, conexoes_simultaneas]
        trafego = np.array([
            [100,5],[120,6],[110,5],[105,4],[50000,500],[109,5],[111,6],[45000,450],
        ])
        # Dica: IsolationForest(contamination=0.25, random_state=42); -1 = anomalia

        # Saída esperada:
        # Amostra 4: [50000, 500] -> ANOMALIA
        # Amostra 7: [45000, 450] -> ANOMALIA
        # Demais -> Normal
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import numpy as np
from sklearn.ensemble import IsolationForest

# Dados para estudo
# [requisicoes_min, conexoes_simultaneas]
trafego = np.array([
    [100,5],
    [120,6],
    [110,5],
    [105,4],
    [50000,500],
    [109,5],
    [111,6],
    [45000,450]
])

# Importação do modelo e definição da contaminação (estimativa de ataques/anomalias)
detetive = IsolationForest(contamination=0.25, random_state=42)
resultados = detetive.fit_predict(trafego)

# Iterando sobre o trafego, aprendendo e definindo anomalias (investigando)
for i, (amostra, r) in enumerate(zip(trafego, resultados)):
    status = "Belezinha" if r == 1 else "ANOMALIA"
    print("Amostra {}: {} -> {}".format(i, amostra, status))
