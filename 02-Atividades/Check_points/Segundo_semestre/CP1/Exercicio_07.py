# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Exercício 7 — Classificador de tráfego: 
        Treine um RandomForestClassifier para distinguir tráfego normal de
        malicioso. Divida treino/teste (test_size=0.3, random_state=42),
        reporte a acurácia e classifique um caso novo.

        import numpy as np
        # Features: [bytes, porta, duracao]
        X = np.array([
            [500,80,0.1],[1200,80,0.5],[64,22,0.02],[64000,4444,10.0],[45000,8080,15.0],
            [60000,31337,20.0],[800,443,0.3],[300,53,0.05],[55000,9999,18.0],[200,25,0.2],
        ])
        y = np.array([0,0,0,1,1,1,0,0,1,0])
        caso_novo = [[58000, 4444, 16.0]]

        # Saída esperada:
        # Acurácia no teste: (imprime o valor, ex. 1.00)
        # Caso novo [58000,4444,16.0] -> Malicioso (1)
'''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np


arvores = 100
try:
    arvores = int(input("Indique a quantidade ded arvores para treino: "))
except Exception as e:
    print("Valor invalido: {}".format(e))
    print("Iniciando treino com valor padrão {}".format(arvores))
    print("")

finally:
    # Dados para utilizar no treino
    x = np.array([
        [500,80,0.1],[1200,80,0.5],[64,22,0.02],[64000,4444,10.0],[45000,8080,15.0],
        [60000,31337,20.0],[800,443,0.3],[300,53,0.05],[55000,9999,18.0],[200,25,0.2],
    ])
    try:
        y = np.array([0,0,0,1,1,1,0,0,1,0])
        caso_novo = [[58000, 4444, 16.0]]

        # divisões de treino
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.3, random_state=42)

        # importantdo modelo e passando parametros de treino
        modelo = RandomForestClassifier(n_estimators=arvores, random_state=42)
        modelo.fit(x_train, y_train)
    except Exception as e:
        print("Erro na execção do programa: {}".format(e))

    # Previsões e avaliasões
    previsoes = modelo.predict(x_test)
    print("\nAcurácia: {:.2f}".format(accuracy_score(y_test, previsoes)))
    print("{}".format(classification_report(y_test, previsoes)))

    # Verificando com novo dado
    caso_novo = [[58000, 4444, 16.0]]
    print("Malicioso" if modelo.predict(caso_novo)[0] == 1 else "Normal")
