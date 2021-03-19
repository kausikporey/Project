import tkinter
import cv2
import PIL.Image,PIL.ImageTk

SET_WIDTH = 650
SET_HEIGHT = 368

window = tkinter.Tk()
window.title("DRS Review System")
cv_img = cv2.cvtColor(cv2.imread("laxmi.png"),cv2.COLOR_BAYER_BG2BGR)
canvas = tkinter.Canvas(window,width = SET_WIDTH,height = SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image = photo)
canvas.pack()

window.mainloop()