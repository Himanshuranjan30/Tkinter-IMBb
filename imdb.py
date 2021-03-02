import tkinter as tk
import requests
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()
canvas1.configure(bg='yellow')

label1 = tk.Label(root, text='IMDb Rating!')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter the Movie Name:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getrating ():
    
    x1 = entry1.get()
    movie=str(x1)
    print(movie)
    url="http://www.omdbapi.com/?t="+movie+"&apikey=4a62f6d8"
    r = requests.get(url = url)
    data = r.json() 
    
    if data["Response"]=="False":
         
         rating=movie+": No Such Movie Found"
    else:
         
         rating="The IMDb rating of "+movie+" is "+data["imdbRating"]+""
    print(rating)
    
  
    
    label4 = tk.Label(root, text= rating,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Get the Rating', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
