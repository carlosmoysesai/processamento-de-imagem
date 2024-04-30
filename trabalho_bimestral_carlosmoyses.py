import cv2
import numpy as np
from tkinter import filedialog
from tkinter import *
from PIL import Image
from PIL import ImageTk

# Funções de Conversão de Cor
def bgr_to_gray(imagem):
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

def bgr_to_rgb(imagem):
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

def bgr_to_hsv(imagem):
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Funções de Filtros
def blur(imagem, kernel_size):
    kernel_size = kernel_size if kernel_size % 2 == 1 else kernel_size + 1
    return cv2.GaussianBlur(imagem, (kernel_size, kernel_size), 0)

def sharpen(imagem):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    return cv2.filter2D(imagem, -1, kernel)

# Funções de Binarização
def edge_detection(imagem, low, up):
    return cv2.Canny(imagem, low, up)

def threshold(imagem, threshold1, threshold2):
    return cv2.threshold(imagem, threshold1, threshold2, cv2.THRESH_BINARY)[1]

# Funções de Morfologia Matemática
def dilation(imagem, kernel):
    return cv2.dilate(imagem, kernel, iterations = 1)

def erosion(imagem, kernel):
    return cv2.erode(imagem, kernel, iterations = 1)

def opening(imagem, kernel):
    return cv2.morphologyEx(imagem, cv2.MORPH_OPEN, kernel)

def closing(imagem, kernel):
    return cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, kernel)

# Função para atualizar a imagem
def update_image():
    global panelB, image_orig
    global var_gray, var_hsv
    global var_blur, var_sharpen, var_edges #variveis para mode de filtros
    global var_threshold, var_dilation, var_erosion, var_opening, var_closing
    global scaleBlur, scaleThreshold1, scaleThreshold2, scaleKernelDilation
    global scaleKernelErosion, scaleKernelOpening, scaleKernelClosing
    global scale_border1, scale_border2 #variveis para tracking

    # Comece sempre com a imagem original
    image = image_orig.copy()

    # Aplicar conversao de cor
    if var_gray.get() == 1:
        image = bgr_to_gray(image)
    
    if var_hsv.get() == 1:
        image = bgr_to_hsv(image)
    
    # Aplicar filtros
    if var_blur.get() == 1:
        image = blur(image, scaleBlur.get())
    
    if var_sharpen.get() == 1:
        image = sharpen(image)
    
    if var_edges.get() == 1 and var_gray.get() == 1:
        image = edge_detection(image, scale_border1.get(), scale_border2.get())
    
    # Aplicar binarização
    if var_threshold.get() == 1:
        image = threshold(image, scaleThreshold1.get(), scaleThreshold2.get())
    
    # Aplicar morfologia matematica
    if var_dilation.get() == 1:
        image = dilation(image, np.ones((scaleKernelDilation.get(), scaleKernelDilation.get()), np.uint8))
    
    if var_erosion.get() == 1:
        image = erosion(image, np.ones((scaleKernelErosion.get(), scaleKernelErosion.get()), np.uint8))
    
    if var_opening.get() == 1:
        image = opening(image, np.ones((scaleKernelOpening.get(), scaleKernelOpening.get()), np.uint8))
    
    if var_closing.get() == 1:
        image = closing(image, np.ones((scaleKernelClosing.get(), scaleKernelClosing.get()), np.uint8))
    
    # Atualizar a imagem
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    if panelB is not None:
        panelB.configure(image=image)
        panelB.image = image

# Inicialização da webcam
cap = cv2.VideoCapture(0)
cap.release()  # Fechando a webcam inicialmente

def show_frames():
    global panelA, panelB, image_orig
    # Lendo o frame da webcam
    ret, frame = cap.read()

    if ret:
        # Exibir o vídeo original no panelA
        image_orig = frame.copy()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        if panelA is None or panelB is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.grid(row=0, column=0, padx=10, pady=10)

            panelB = Label(image=image)
            panelB.image = image
            panelB.grid(row=0, column=1, padx=10, pady=10)

        else:
            panelA.configure(image=image)
            panelB.configure(image=image)
            panelA.image = image
            panelB.image = image
            
        update_image()

        # Comece sempre com a imagem original
        image = frame.copy()
        
        # Atualizando os frames a cada 10ms
        root.after(10, show_frames)

# Função para abrir a webcam
def start_webcam():
    global cap
    cap = cv2.VideoCapture(0)  # Abrindo a webcam
    show_frames()

# Função para parar a webcam
def stop_webcam():
    global cap
    cap.release()  # Fechando a webcam


# Função para selecionar uma imagem
def select_image():
    global panelA, panelB, image_orig

    # Feche a webcam se estiver aberta
    stop_webcam()

    path = filedialog.askopenfilename()

    if len(path) > 0:
        image = cv2.imread(path)
        image_orig = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        if panelA is None or panelB is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.grid(row=0, column=0, padx=10, pady=10)

            panelB = Label(image=image)
            panelB.image = image
            panelB.grid(row=0, column=1, padx=10, pady=10)

        else:
            panelA.configure(image=image)
            panelB.configure(image=image)
            panelA.image = image
            panelB.image = image

root = Tk()
root.title("Processamento de Imagem")
panelA = None
panelB = None
image_orig = None

var_gray = IntVar()
var_hsv = IntVar()
var_hsvbgr = IntVar()

var_blur = IntVar()
var_sharpen = IntVar()

var_edges = IntVar()
var_threshold = IntVar()

var_dilation = IntVar()
var_erosion = IntVar()
var_opening = IntVar()
var_closing = IntVar()

frame = Frame(root)
frame.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

#Convert BGR to Gray
Label(frame, text="Gray").grid(row=0, column=0, sticky=W)
Checkbutton(frame, text="Ativar", variable=var_gray, onvalue=1, offvalue=0, command=update_image).grid(row=0, column=1)

#Convert BGR to HSV
Label(frame, text="HSV").grid(row=1, column=0, sticky=W)
Checkbutton(frame, text="Ativar", variable=var_hsv, onvalue=1, offvalue=0, command=update_image).grid(row=1, column=1)

#Gaussian Blur
Label(frame, text="Gaussian Blur").grid(row=2, column=0, sticky=W)
Checkbutton(frame, text="Ativar", variable=var_blur, onvalue=1, offvalue=0, command=update_image).grid(row=2, column=1)
scaleBlur = Scale(frame, from_=1, to=100, orient=HORIZONTAL, command=lambda x: update_image())
scaleBlur.grid(row=3, column=0)

#Sharpen
Label(frame, text="Sharpen").grid(row=4, column=0, sticky=W)
Checkbutton(frame, text="Ativar", variable=var_sharpen, onvalue=1, offvalue=0, command=update_image).grid(row=4, column=1)

#Edges
Label(frame, text="Canny").grid(row=5, column=0, sticky=W)
Checkbutton(frame, text="Ativar", variable=var_edges, onvalue=1, offvalue=0, command=update_image).grid(row=5, column=1)
scale_border1 = Scale(frame, from_=1, to=255, orient=HORIZONTAL, command=lambda x: update_image())
scale_border1.grid(row=6, column=0)
scale_border2 = Scale(frame, from_=1, to=255, orient=HORIZONTAL, command=lambda x: update_image())
scale_border2.grid(row=7, column=0)

#Threshold
Label(frame, text="Threshold").grid(row=8, column=0, sticky=W)
Checkbutton(frame, text="Ativar", variable=var_threshold, onvalue=1, offvalue=0, command=update_image).grid(row=8, column=1)
scaleThreshold1 = Scale(frame, from_=1, to=255, orient=HORIZONTAL, command=lambda x: update_image())
scaleThreshold1.grid(row=9, column=0)
scaleThreshold2 = Scale(frame, from_=1, to=255, orient=HORIZONTAL, command=lambda x: update_image())
scaleThreshold2.grid(row=10, column=0)

#Dilation
Label(frame, text="Dilation").grid(row=11, column=0, sticky=W)
Checkbutton(frame, text="Ativar", variable=var_dilation, onvalue=1, offvalue=0, command=update_image).grid(row=11, column=1)
scaleKernelDilation = Scale(frame, from_=1, to=100, orient=HORIZONTAL, command=lambda x: update_image())
scaleKernelDilation.grid(row=12, column=0)

#Erosion
Label(frame, text="Erosion").grid(row=13, column=0, sticky=W)
Checkbutton(frame, text="Ativar", variable=var_erosion, onvalue=1, offvalue=0, command=update_image).grid(row=13, column=1)
scaleKernelErosion = Scale(frame, from_=1, to=100, orient=HORIZONTAL, command=lambda x: update_image())
scaleKernelErosion.grid(row=14, column=0)

#Opening
Label(frame, text="Opening").grid(row=15, column=0, sticky=W)
Checkbutton(frame, text="Ativar", variable=var_opening, onvalue=1, offvalue=0, command=update_image).grid(row=15, column=1)
scaleKernelOpening = Scale(frame, from_=1, to=100, orient=HORIZONTAL, command=lambda x: update_image())
scaleKernelOpening.grid(row=16, column=0)

#Closing
Label(frame, text="Closing").grid(row=17, column=0, sticky=W)
Checkbutton(frame, text="Ativar", variable=var_closing, onvalue=1, offvalue=0, command=update_image).grid(row=17, column=1)
scaleKernelClosing = Scale(frame, from_=1, to=100, orient=HORIZONTAL, command=lambda x: update_image())
scaleKernelClosing.grid(row=18, column=0)

btn = Button(root, text="Selecione uma imagem", command=select_image)
btn.grid(row=20, column=2)

btn_webcam = Button(root, text="Abrir Webcam", command=start_webcam)
btn_webcam.grid(row=21, column=2)

root.mainloop()
