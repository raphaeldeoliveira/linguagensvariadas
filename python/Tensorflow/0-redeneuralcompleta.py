# Nesse codigo criamos, treinamos e extraimos parametros de uma rede neural

# import do Tensorflow e tf.keras
import tensorflow as tf
from tensorflow import keras

# Bibliotecas auxiliares
import numpy as np
import matplotlib.pyplot as plt

# Printa a versão pra ver se o TF ta instalado
print(tf.__version__)

# Importanto a base de dados (usada para criar e testar a rede neural)
fashion_mnist = keras.datasets.fashion_mnist

# Cria o array de treinamento (imagens e rotulos para dizer o que cada imagem é)
# e cria o array de teste e seus rotulos
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# pra mostra a forma do array
# saida: 60k imagens, 28x28
print(train_images.shape)

# pra inspecionar as imagens
plt.figure() # cria uma figura
plt.imshow(train_images[0]) # renderiza a imagem 0
plt.colorbar() # indices de cores
plt.grid(False)
plt.show() # mostra a imagem

# pra efeito computacional é melhor tranformar as cores pra ficarem numa escala de 0 a 1
# divide todas as imagens do array por 255.0 (itera o array - recurso do numpy)
train_images = train_images / 255.0
test_images = test_images / 255.0

# Definindo os nomes das classes (rótulos)
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# mostrando 25 fotos
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

# montando as camadas
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# compila o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# treina o modelo
model.fit(train_images, train_labels, epochs=10)

# avaliando a acurácia
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)
print('\nTeste Losss', test_loss)

# predições
predictions = model.predict(test_images)
predictions[0] 
np.argmax(predictions[0])
test_labels[0]

# se der acerto ele vai da azul, se der errado vai da vermelho
def plot_image(i, predictions_array, true_label, img):
    # extrai os dados para aquele elemento (i)
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    # limpa o grafico plotado (pra nao ficar linhas sobrepostas)
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    
    # exibe a imagem em cinza (cmap = mapa de cores)
    plt.imshow(img, cmap=plt.cm.binary)

    # pega o valor mais alto do vetor de previsões (o que ele acha que é)
    # se estiver correto conforme a label, ele pinta de azul senão vermelho
    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    # plota no grafico
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label], 100*np.max(predictions_array), class_names[true_label]), color=color)

# Faz o desenho do azul e vermelho em um grafico
def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks(range(10), class_names, rotation=90)
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

# blota a imagem e do lado um grafico com azul e vermelho
i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions, test_labels)
plt.show()
