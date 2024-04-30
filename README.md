# Processamento de Imagem com Python, OpenCV e Tkinter

Este código demonstra processamento de imagem em Python utilizando as bibliotecas OpenCV, Tkinter e Pillow. Ele oferece uma interface gráfica do usuário (GUI) para interagir com o usuário e visualizar as imagens processadas.

## Pré-requisitos

* Python 3.x instalado
* OpenCV (`pip install opencv-python`)
* Tkinter (já incluso na maioria das distribuições Python)
* Pillow (`pip install Pillow`)

## Baixando o Código

1. Salve o código a seguir como `processamento_imagem.py` em uma pasta no seu computador.

## Estrutura do Código

O código define várias funções para realizar diferentes tarefas de processamento de imagem:

* **Conversão de cor:** Converte imagens entre diferentes espaços de cores (BGR, HSV, Cinza).
* **Filtros de imagem:** Aplica filtros como Desfoque Gaussiano e Nitidez.
* **Binarização:** Aplica a técnica de Limiar para criar imagens binárias.
* **Morfologia Matemática:** Realiza operações de Dilatação, Erosão, Abertura e Fechamento.
* **Atualização da imagem:** Atualiza a imagem na GUI de acordo com as transformações selecionadas.
* **Funções de inicialização:** Inicializa a webcam (opcionalmente).

A GUI utiliza Tkinter para criar elementos como labels, botões e sliders para interagir com o usuário e controlar as transformações.

## Executando o Código

1. Abra um terminal ou prompt de comando e navegue até a pasta onde salvou o código.
2. Execute o seguinte comando:

```
python processamento_imagem.py
```

## Interface Gráfica do Usuário (GUI)

A GUI possui duas áreas de visualização:

* **Painel A:** Exibe a imagem original ou a imagem com as alterações aplicadas.
* **Painel B:** Exibe a imagem após a aplicação de todas as transformações selecionadas pelo usuário.

O lado direito da GUI contém controles para configurar as diferentes opções de processamento de imagem:

* **Conversão de Cor:** Selecione a conversão de cor desejada (Cinza, HSV).
* **Filtros:** Ative e ajuste os parâmetros para os filtros Desfoque Gaussiano e Nitidez.
* **Binarização:** Ative e ajuste os parâmetros para o algoritmo de binarização Threshold.
* **Morfologia Matemática:** Ative e ajuste o tamanho do kernel para as operações de Dilatação, Erosão, Abertura e Fechamento.
* **Selecionar Imagem:** Carregue uma imagem do computador.
* **Abrir Webcam:** Abra a webcam para processamento em tempo real (opcional).

## Desenvolvimento do Código

Você pode modificar o código para adicionar novas funcionalidades de processamento de imagem, como:

* Outros filtros (por exemplo, Sobel, média)
* Técnicas de segmentação de imagem
* Detecção de objetos

Você também pode personalizar a GUI para atender às suas necessidades específicas. Certifique-se de documentar as alterações feitas no código para facilitar a compreensão e reutilização do código no futuro.

## Recursos Adicionais

* Documentação OpenCV: https://opencv.org/
* Tutoriais Tkinter: https://realpython.com/tutorials/gui/
* Documentação Pillow: https://readthedocs.org/projects/pillow/

Este roteiro fornece um guia básico para executar e desenvolver o código. Para um entendimento mais profundo do código, é recomendável analisar as funções e variáveis ​​individuais e consultar a documentação das bibliotecas utilizadas. Sinta-se à vontade para adaptar e modificar o código de acordo com suas necessidades e objetivos específicos.
