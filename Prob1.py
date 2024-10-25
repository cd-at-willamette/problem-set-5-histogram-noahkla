from pgl import *

#1a
def create_histogram_array(data):
    h = [0]*10
    for d in data:
        h[d] += 1
    return h

#1b
def print_histogram(hist):
    for i in range(len(hist)):
        print(str(i) + ': ' + hist[i]*'*')

#1c
def graph_histogram(hist, width, height) -> None:
    gw = GWindow(width, height)
    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)
    w = width/10
    u = 400/max(hist)
    for i in range(10):
        my_rect(i*w, height-hist[i]*u, w, hist[i]*u, 'Red')

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test

