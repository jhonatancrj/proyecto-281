# -*- coding: utf-8 -*-
"""primer codigo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x8lnnYzifym4ys7FywpDznk5OFBBAPlp
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Cargar los datos balanceados
from scipy.io.arff import loadarff
file_path = '/content/drive/MyDrive/datos/diabetes_datos_balanceados.arff'

data, meta = loadarff(file_path)
df = pd.DataFrame(data)

# Decodificar variables categóricas (si aplica)
for col in df.select_dtypes([object]).columns:
    df[col] = df[col].str.decode('utf-8')

# Separar características (X) y etiqueta objetivo (y)
X = df.drop('Diabetes', axis=1)
y = df['Diabetes'].astype(int)  # Convertir la etiqueta objetivo a numérico

# Función para realizar múltiples ejecuciones y calcular la mediana de accuracy
def evaluate_split(split_ratio, n_runs=100):
    accuracies = []
    for _ in range(n_runs):
        # Dividir los datos
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1-split_ratio, random_state=None)

        # Entrenar el modelo
        clf = RandomForestClassifier(random_state=42)
        clf.fit(X_train, y_train)

        # Evaluar el modelo
        y_pred = clf.predict(X_test)
        accuracies.append(accuracy_score(y_test, y_pred))

    # Calcular la mediana de accuracy
    return np.median(accuracies)

# Configuración Académica: 80/20
median_accuracy_academic = evaluate_split(split_ratio=0.8, n_runs=100)
print(f"Mediana de confiabilidad (80/20 Académico): {median_accuracy_academic:.4f}")

# Configuración Investigación: 50/50
median_accuracy_research = evaluate_split(split_ratio=0.5, n_runs=100)
print(f"Mediana de confiabilidad (50/50 Investigación): {median_accuracy_research:.4f}")