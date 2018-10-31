__author__ = 'harsha'
import Tkinter as tk                # python 3
# from Tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
import random
import time
from itertools import islice

from coinmarketcap import Market

def getCoinMarket():
    coinmarketcap = Market()
    while True:
        print coinmarketcap.stats()
        print coinmarketcap.ticker( limit=4, convert='EUR')
        time.sleep(1)   # Delays for 5 seconds. You can also use a float value.


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.geometry(self, '600x450+512+151')
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.configure(width=200)
        # container.place(relx=0.0, rely=0.0, relheight=0.989, relwidth=0.992)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.scores = []
        self.products = {'Protine Shake':4,
                         'Protine Bar':5,
                         'Creatine': 8,
                         'Omega3':6}

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def passLabelValue(self, val):
        self.scores.append(val)

    def getPassLabel(self):
        return self.scores[-1]

    def emptyList(self):
        del self.scores[:]

    def printList(self):
        print(self.scores)

    def getProtineProducts(self):
        t = 'This is your whole product list' \
            '-------------------------------' \
            '-------------------------------'
        products = {'Protine Shake':2,
                    'Protine Bar':1,
                    'Creatine': 2,
                    'Omega3':2}
        return t+str(products)


    def getCountableKeyValue(self):
        return self.products

    def getCountableKeyValueTop(self):
        # n_items = list(islice(self.products.iteritems(), 1))[0]
        for k in self.products:
            # print k + ' asss'
            return k+ " x " + str(self.products[k])




class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # self.Frame1 = Frame(top)
        tk.Frame.place(self, relx=0.0, rely=0.0, relheight=0.989, relwidth=0.992)
        # tk.Frame.configure(relief=GROOVE)
        tk.Frame.configure(self, borderwidth="2")
        # tk.Frame.configure(relief=GROOVE)
        tk.Frame.configure(self, background="#FFFFFF")
        tk.Frame.configure(self, width=595)

        button1 = tk.Button(self, command=lambda: controller.show_frame("PageOne"))
        button1.place(relx=0.017, rely=0.112, height=27, width=59)
        button1.configure(activebackground="#8ed87b")
        button1.configure(text='''Login''')

        button2 = tk.Button(self, command=lambda: controller.show_frame("PageTwo"))
        button2.place(relx=0.874, rely=0.112, height=27, width=68)
        button2.configure(activebackground="#6cd87a")
        button2.configure(text='''Logout''')

        Label1 = tk.Label(self)
        Label1.place(relx=0.0, rely=-0.022, height=49, width=596)
        Label1.configure(text='''Scan badge and press login to start''')
        Label1.configure(width=596)
        # button1.pack()
        # button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # label = tk.Label(self, text="This is page 1", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)
        # button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller.show_frame("StartPage"))
        # button.pack()

        tk.Frame.place(self, relx=-0.017, rely=0.0, relheight=1.033, relwidth=1.025)
        # tk.Frame.configure(relief=GROOVE)
        tk.Frame.configure(self, borderwidth="2")
        # tk.Frame.configure(relief=GROOVE)
        tk.Frame.configure(self, background="#ffffff")
        tk.Frame.configure(self, width=615)
        tk.Frame.bind(self, '<Return>', lambda event: self.clearLabelAndGoLast(controller, event))
        tk.Frame.focus_set(self)
        # tk.Frame.bind('<Enter>', command=lambda: controller.show_frame("PageTwo"))
        # button2 = tk.Button(self, command=lambda: controller.show_frame("PageTwo"))


        label1 = tk.Label(self)
        label1.place(relx=0.016, rely=0.0, height=69, width=606)
        label1.configure(background="#2b2b2b")
        label1.configure(foreground="#e8e8e8")
        label1.configure(text='''Scan invoice''')
        label1.configure(width=606)

        self.s = tk.StringVar()
        label2 = tk.Label(self, textvariable=self.s)
        label2.place(relx=0.39, rely=0.495, height=29, width=156)
        label2.configure(width=156)


        button1 = tk.Button(self)
        button1.place(relx=0.732, rely=0.086, height=27, width=67)
        button1.configure(activebackground="#d9d9d9")
        button1.configure(background="#d2d82d")
        button1.configure(text='''Button''')
        button1.bind('<Button-1>', lambda event: self.comp_s(event, controller))
        # button1.bind('<Enter>', lambda event: controller.show_frame("PageTwo"))


        button2 = tk.Button(self, command=lambda: controller.show_frame("StartPage"))
        button2.place(relx=0.878, rely=0.086, height=27, width=65)
        button2.configure(activebackground="#d9d9d9")
        button2.configure(background="#d81139")
        button2.configure(text='''RESET''')

    def comp_s(self, event, controller):
        randNo = 'SO000%g' % random.randint(0,9)
        self.s.set(randNo) # construct string
        controller.passLabelValue(randNo)
        controller.printList()

    def clearLabelAndGoLast(self, controller, event):
        self.s.set('')
        tk.Frame.unbind(self, '<space>')
        controller.show_frame("PageTwo")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # label = tk.Label(self, text="This is page 2", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)
        # button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller.show_frame("StartPage"))
        # button.pack()

        tk.Frame.place(self, relx=-0.017, rely=0.0, relheight=1.033, relwidth=1.025)
        # tk.Frame.configure(relief=GROOVE)
        tk.Frame.configure(self, borderwidth="2")
        # tk.Frame.configure(relief=GROOVE)
        tk.Frame.configure(self, background="#ffffff")
        tk.Frame.configure(self, width=615)
        # tk.Frame.unbind_all(self, '<space>')
        tk.Frame.bind_all(self, '<space>', lambda event: self.scanAndVarifyProduct(controller, event))
        # tk.Frame.bind(self, '<Return>', lambda event: self.clearLabelAndGoLast(controller, event))
        tk.Frame.focus_set(self)


        label1 = tk.Label(self)
        label1.place(relx=0.016, rely=0.0, height=69, width=606)
        label1.configure(background="#2b2b2b")
        label1.configure(foreground="#e8e8e8")
        label1.configure(text='''Scan products''')
        label1.configure(width=606)
        # label1.bind(self, '<Button-1>', lambda event: self.scanAndVarifyProduct(event))


        self.s2 = tk.StringVar()
        self.s2.set(controller.getCountableKeyValueTop())
        # label2 = tk.Label(self, textvariable=self.s)
        # label2.place(relx=0.39, rely=0.495, height=29, width=156)
        # label2.configure(width=156)

        label2 = tk.Message(self, textvariable=self.s2)
        label2.place(relx=0.286, rely=0.374, relheight=0.314
                            , relwidth=0.462)
        label2.configure(background="#a2c2d8")
        label2.configure(text='''Message''')
        label2.configure(width=275)


        button1 = tk.Button(self)
        button1.place(relx=0.732, rely=0.086, height=27, width=67)
        button1.configure(activebackground="#d9d9d9")
        button1.configure(background="#d2d82d")
        button1.configure(text='''Button''')
        button1.bind('<Button-1>', lambda event: self.comp_s(event, controller))

        button2 = tk.Button(self)
        button2.bind('<Button-1>', lambda event: self.goingBackToIntial(controller, event))

        button2.place(relx=0.878, rely=0.086, height=27, width=65)
        button2.configure(activebackground="#d9d9d9")
        button2.configure(background="#d81139")
        button2.configure(text='''RESET''')

    def comp_s(self, event, controller):
        self.s2.set('%s' % controller.getPassLabel()) # construct string

    def goingBackToIntial(self, controller, event):
        controller.emptyList()
        print('After empty --->' + str(controller.getProtineProducts()))
        controller.printList()
        self.s2.set('')
        controller.show_frame("StartPage")

    def scanAndVarifyProduct(self, controller, event):

        print('Scan a product...')
        prod = controller.getCountableKeyValue()
        print(self.s2.get())
        currntProd = self.s2.get().split('x')[0].strip()
        currntAmount = self.s2.get().split('x')[1].strip()
        print(currntProd+ '  ---------------  ' +currntAmount)
        cnt = 0

        loopcount = 0
        for k, v in prod.iteritems():
            print k + ' **** ' + str(v)
            loopcount += 1
            if cnt == 1:
                currntProd = k
                currntAmount = v
                break
            if k == currntProd and int(currntAmount) == 0:
                cnt = 1
                if len(prod) == loopcount:
                    # self.s2.set('') #this is the place we set empty to the text
                    # self.refresh()
                    self.restart()
                    return

        if int(currntAmount) > 0:
            self.s2.set(currntProd + " x " + str(int(currntAmount)-1))

    def restart(self):
        # self.refresh()
        self.controller.show_frame("StartPage")
        self.s2.set(self.controller.getCountableKeyValueTop())

    def refresh(self):
        self.label2.config(state='normal')
        # self.weight_entry.delete(0,tk.END)
        self.label2.delete("1.0", "end")


def printLabel(event):
    print('Hello guys....')

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()






