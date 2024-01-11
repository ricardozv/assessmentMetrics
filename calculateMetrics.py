# Definição dos valores para a matriz de confusão
verdadeiros_positivos = 100  # VP
falsos_negativos = 50        # FN
falsos_positivos = 30        # FP
verdadeiros_negativos = 120  # VN

# Cálculo da Sensibilidade (ou Recall)
sensibilidade = verdadeiros_positivos / (verdadeiros_positivos + falsos_negativos)

# Cálculo da Especificidade
especificidade = verdadeiros_negativos / (verdadeiros_negativos + falsos_positivos)

# Cálculo da Acurácia
total_elementos = verdadeiros_positivos + verdadeiros_negativos + falsos_positivos + falsos_negativos
acuracia = (verdadeiros_positivos + verdadeiros_negativos) / total_elementos

# Cálculo da Precisão
precisao = verdadeiros_positivos / (verdadeiros_positivos + falsos_positivos)

# Cálculo do F-score
f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

# Impressão das métricas calculadas
print(f'Sensibilidade (Recall): {sensibilidade:.2f}')
print(f'Especificidade: {especificidade:.2f}')
print(f'Acurácia: {acuracia:.2f}')
print(f'Precisão: {precisao:.2f}')
print(f'F-score: {f_score:.2f}')
