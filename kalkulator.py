import tkinter as tk

symbole = ['7','8','9','/','\u21BA','C','4','5','6','*', '(', ')', '1', '2', '3', '-', 'x^2', '\u221A', '0', ',','%','+']

COLOR = '#F2F4F7'

#Główne okno
def glowne_okno():
    root = tk.Tk()
    root.configure(bg=COLOR)
    root.geometry('410x400')
    root.title('Kalkulator')

    return root

#Okno podzielone na wiersze
def male_okna(root):

    okno = [
        tk.Label(root, bg='#9BA4B5', width=55, anchor = 'w', borderwidth = 2) 
            for i in range(3)
    ]

    for i in range(len(okno)):
        okno[i].grid(row = i, columnspan = 6, ipady = 15, ipadx = 1)
    
    return okno

def okno_dane(root, okno):
    pole_dane = tk.Entry(
        borderwidth=0,highlightcolor='white',highlightbackground='white'
    )

    pole_dane.grid(row = len(okno), columnspan = 6, ipadx=142, ipady=10)

    info = tk.Label(root, bg='white', width=55, anchor = 'w', borderwidth = 2)
    info.grid(row = len(okno) + 1, columnspan = 6, ipady = 15, ipadx = 1)

    return pole_dane, info

def pole_przyciski(root, okno):
    przyciski = [
        tk.Button(root, text = symbol, bg=COLOR, borderwidth = 0) 
        for symbol in symbole
    ]

    j = len(okno) + 2
    for i in range(len(przyciski)):
        if i % 6 == 0:
            j += 1

        margin = 21 if len(symbole[i]) == 1 else 10
        przyciski[i].grid(row = j, column = i % 6, ipady = 5, ipadx = margin)


        znak_ruwna = tk.Label(
            root, bg='#00BFFF',text = '=', borderwidth = 0
        )
        znak_ruwna.grid(row = len(okno) + 6, column = 4, columnspan = 2, ipady = 5, ipadx = 50)
                              
    return przyciski



if __name__ == '__main__':
    root = glowne_okno()
    okno = male_okna(root)
    pole_dane = okno_dane(root, okno)
    przyciski = pole_przyciski(root, okno)

    root.mainloop()