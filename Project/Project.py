from tkinter import *
from tkinter import Button
from tkinter.ttk import Frame
from textblob import TextBlob
import tkinter.messagebox
import tweepy, re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import time


class Welcome(Frame):
    def __init__(self, master):
        super().__init__()

        self.master = master
        # self.master.geometry('999x530')
        self.master.title('Welcome Page')
        width = 1000
        height = 600
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.master.resizable(width=False, height=False)

        self.image1 = PhotoImage(file="file path to projectpic2.png")
        background_label = Label(self.master, image=self.image1).pack(side=TOP, expand=True, fill=BOTH)

        self.btn = Button(background_label, text="Run Tweet Sentiment", height=1, activebackground="#34CDFA",
                          activeforeground="White"
                          , bg="White", fg="#34CDFA", width=20, font=('SansSerif 20 bold'), command=self.start, ).place(
            x=350, y=450)

        self.menubar = Menu(self.master)
        self.subm2 = Menu(self.menubar)
        self.menubar.add_cascade(label="About", menu=self.subm2)
        self.subm2.add_command(label="About App", command=self.app)
        self.subm2.add_command(label="About Contributors", command=self.con)
        self.master.config(menu=self.menubar)

        tkinter.messagebox.showinfo("Greetings",
                                    'Welcome To Twitter Sentiment Analysis Application!!\n\nTo get more info,Go to About Menu')

    def closee(self):
        self.master.destroy()

    def exittt(self):
        self.master.destroy()

    def hel(self):
        help(tkinter)

    def con(self):
        tkinter.messagebox.showinfo("S/W Contributors", '\n Names\n ___Version 1.0___')

    def app(self):
        tkinter.messagebox.showinfo("App Info",'\n1.Twitter Sentiment Analysis is a text mining technique for analyzing the underlying sentiment of people regarding certain topic via tweets.\n2.Twitter sentiment or opinion expressed through it may be positive, negative or neutral.\n3.Click Run to start the Analyzer ')

    def start(self):
        self.master1 = Toplevel(self.master)
        width = 500
        height = 500

        x = (self.master1.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master1.winfo_screenheight() // 2) - (height // 2)
        self.master1.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        # self.master1.geometry('500x450')
        self.master1.title('Input Page')
        # self.master1.resizable(width=False,height=False)

        self.tweets = []
        self.tweetText = []
        self.tweetTextp = []
        self.tweetTextn = []

        self.positive = 0
        self.negative = 0
        self.neutral = 0
        self.polarity = 0

        framem = Frame(self.master1)
        framem.pack(fill=BOTH)

        frame1 = Frame(framem, borderwidth=10)
        frame1.pack(fill=X)

        self.image2 = PhotoImage(file="file path to tbac2.png")
        background_label1 = Label(frame1, image=self.image2, relief=FLAT).pack(fill=X)

        self.searchTerm1 = StringVar()
        self.NoOfTerms1 = StringVar()

        frame2 = Frame(framem, borderwidth=10, relief=RAISED)
        frame2.pack(fill=X)
        lab1 = Label(frame2, text='Enter Keyword/HashTag to search about:', font=("Sans 10 bold")).pack(side=LEFT,
                                                                                                        padx=5, pady=5)
        ent1 = Entry(frame2, textvar=self.searchTerm1, bg="light grey", font=("Sans 10 bold")).pack(side=RIGHT, fill=X,
                                                                                                    padx=5, expand=True)

        frame3 = Frame(framem, relief=RAISED, borderwidth=10)
        frame3.pack(fill=X)
        lab2 = Label(frame3, text='Enter how many tweets to analyze:         ', font=("Sans 10 bold")).pack(side=LEFT,
                                                                                                            padx=5,
                                                                                                            pady=5,
                                                                                                            anchor=W)
        ent2 = Entry(frame3, bg="light grey", textvar=self.NoOfTerms1, font=("Sans 10 bold")).pack(side=RIGHT, fill=X,
                                                                                                   padx=5, expand=True)

        frame4 = Frame(framem, borderwidth=10)
        frame4.pack(fill=Y)
        btn1 = Button(frame4, text="See Results", command=self.analysis, height=1, width=20, bg="#55ADEE", fg="white",
                      font=("Sans 10 bold")).pack(pady=25)
        btn2 = Button(frame4, text="Cancel", command=self.exitt, height=1, width=20, bg="#55ADEE", fg="white",
                      font=("Sans 10 bold")).pack(pady=44)

        consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        access_token ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

        self.auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

        self.master.withdraw()
        self.master.lift()
        self.master1.protocol("WM_DELETE_WINDOW", self.delete_window)
        self.master1.mainloop()

    def analysis(self):


        def inputss():
            self.searchTerm1.get()

        def inputn():
            if self.NoOfTerms1.get() == '':
                self.NoOfTerms = 0
            else:
                self.NoOfTerms = int(self.NoOfTerms1.get())

        inputss()
        inputn()

        if self.searchTerm1.get() == '' and self.NoOfTerms1 == 0:
            tkinter.messagebox.showerror("Error", "Please Input the Values!!")
            inputss()
            inputn()

        elif self.searchTerm1.get() == '':
            tkinter.messagebox.showerror("Error", "Please Input a keyword/Hastag to get sentiment!!")
            inputss()

        elif self.NoOfTerms1== 0:
            tkinter.messagebox.showerror("Error", "Please Input the No. of tweets to analyze!")
            inputn()


        self.tweets = tweepy.Cursor(self.api.search, q=self.searchTerm1.get(), lang="en").items(self.NoOfTerms)

        count = 0
        self.neutral = 0
        self.positive = 0
        self.negative = 0
        self.polarity = 0

        for tweet in self.tweets:
            # print(tweet.text)

            analysis = TextBlob(tweet.text)
            self.polarity += analysis.sentiment.polarity

            if (analysis.sentiment.polarity == 0.00):
                self.neutral += 1
            elif (analysis.sentiment.polarity < 0.00):
                self.negative += 1
            elif (analysis.sentiment.polarity > 0.00):
                self.positive += 1
            count += 1
            if count % 100 == 0:
                time.sleep(1.0)



        if  self.neutral > self.positive and self.neutral > self.negative:
            tkinter.messagebox.showinfo("Result", "People are reacting on " + self.searchTerm1.get() + ": Neutrally")

        elif self.negative > self.positive and self.negative > self.neutral:
            tkinter.messagebox.showinfo("Result", "People are reacting on " + self.searchTerm1.get() + ": Negatively")

        elif self.positive > self.negative and self.positive > self.neutral:
            tkinter.messagebox.showinfo("Results", "People are reacting on " + self.searchTerm1.get() + ": Positively")

        elif self.positive == self.negative and self.positive == self.neutral:
            tkinter.messagebox.showinfo("Results","People are reacting on " + self.searchTerm1.get() + ": with Mixed Thoughts")

        self.positive = self.percentage(self.positive, self.NoOfTerms)
        self.neutral = self.percentage(self.neutral, self.NoOfTerms)
        self.negative = self.percentage(self.negative, self.NoOfTerms)
        self.polarity = self.percentage(self.polarity, self.NoOfTerms)

        self.top1 = Toplevel(self.master1)
        # self.top1.geometry('1000x530')
        self.top1.title('Graph')
        width = 1000
        height = 570
        # self.master1.update_idletasks()
        x = (self.top1.winfo_screenwidth() // 2) - (width // 2)
        y = (self.top1.winfo_screenheight() // 2) - (height // 2)
        self.top1.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        frame = Frame(self.top1)
        frame.pack(fill=X, side=BOTTOM)

        button = Button(frame, text="ReInput Values", command=self.quitt, height=2, width=15, bg="#55ADEE", fg="white",
                        font=("Sans 9 bold"))
        # button.place(x=700,y=540)
        button.pack(side=RIGHT, padx=25)

        btn5 = Button(frame, text="See Tweets", command=self.tweet, height=2, width=15, bg="#55ADEE", fg="white",
                      font=("Sans 9 bold"))
        # btn5.place(x=850,y=540)
        btn5.pack(side=LEFT, padx=25)

        f = plt.figure(figsize=(5, 5), dpi=100)
        labels = ['Positive [' + str(self.positive) + '%]', 'Neutral[' + str(self.neutral) + '%]',
                  'Negative [' + str(self.negative) + '%]']
        sizes = [self.positive, self.neutral, self.negative]
        colors = ['yellowgreen', 'lightgreen', 'darkgreen']
        explode = list()
        for k in labels:
            explode.append(0.1)
        plt.pie(sizes, labels=labels, colors=colors, explode=explode, startangle=90, shadow=True)
        f.suptitle('How people are reacting on ' + self.searchTerm1.get() + ': Analyzing by ' + str(
            self.NoOfTerms) + ' Tweets.')
        canvas = FigureCanvasTkAgg(f, self.top1)

        canvas.get_tk_widget().pack(side=LEFT, expand=True, fill=BOTH)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, self.top1)
        toolbar.update()
        canvas.get_tk_widget().pack(side=BOTTOM, expand=True, fill=BOTH)

        self.master1.withdraw()
        self.top1.lift()
        self.top1.protocol("WM_DELETE_WINDOW", self.delete_window2)
        self.top1.mainloop()

    def tweet(self):

        top2 = Toplevel(self.top1)
        # top2.geometry('1000x530')
        top2.title("Tweet Page")
        width = 1000
        height = 570
        # self.master1.update_idletasks()
        x = (self.top1.winfo_screenwidth() // 2) - (width // 2)
        y = (self.top1.winfo_screenheight() // 2) - (height // 2)
        top2.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        sb = Scrollbar(top2)
        sb.pack(side=RIGHT, fill=Y)
        T = Text(top2, yscrollcommand=sb.set, height=100, width=200)
        T.tag_configure('color', foreground='#476042')
        T.tag_configure('color1', foreground='blue')
        T.tag_configure('color2', foreground='purple')
        tweetss = tweepy.Cursor(self.api.search, q=self.searchTerm1.get(), lang="en").items(self.NoOfTerms)
        count = 0
        # self.tweetTextp.append("\n\n")
        self.tweetTextn.append("\n\n\n")
        self.tweetTextn.append(
            "-------------------------------------------------------------------------------------------------------------------")
        self.tweetTextn.append("\n\n")
        self.tweetTextn.append("Negative Tweets")
        self.tweetTextn.append("\n\n")
        self.tweetTextn.append(
            "--------------------------------------------------------------------------------------------------------------------")
        self.tweetTextn.append("\n\n")

        self.tweetText.append("\n\n")
        self.tweetText.append(
            "---------------------------------------------------------------------------------------------------------------------")
        self.tweetText.append("\n\n")
        self.tweetText.append("Neutral Tweets")
        self.tweetText.append("\n\n")
        self.tweetText.append(
            "----------------------------------------------------------------------------------------------------------------------")
        self.tweetText.append("\n\n")

        self.tweetTextp.append(
            "---------------------------------------------------------------------------------------------------------------------")
        self.tweetTextp.append("\n\n")
        self.tweetTextp.append("Positive Tweets")
        self.tweetTextp.append("\n\n")
        self.tweetTextp.append(
            "----------------------------------------------------------------------------------------------------------------------")
        self.tweetTextp.append("\n\n")
        for tweet in tweetss:

            analysis = TextBlob(tweet.text)

            if (analysis.sentiment.polarity == 0.00):
                self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
                self.tweetText.append("\n\n\n")
            elif (analysis.sentiment.polarity < 0.00):
                self.tweetTextn.append(self.cleanTweet(tweet.text).encode('utf-8'))
                self.tweetTextn.append("\n\n\n")
            elif (analysis.sentiment.polarity > 0.00):
                self.tweetTextp.append(self.cleanTweet(tweet.text).encode('utf-8'))
                self.tweetTextp.append("\n\n\n")

            count += 1
            if count % 100 == 0:
                time.sleep(1.0)

        T.insert(END, self.tweetTextp, 'color')
        T.insert(END, self.tweetTextn, 'color1')
        T.insert(END, self.tweetText, 'color2')

        T.pack(side=LEFT, expand=True, fill=Y)
        sb.config(command=T.yview)
        top2.lift()
        top2.mainloop()

    def quitt(self):
        self.top1.quit()
        self.top1.destroy()
        self.master1.update()
        self.master1.deiconify()
        self.clear()

    def exitt(self):
        self.master1.destroy()
        self.master.update()
        self.master.deiconify()

    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    def clear(self):
        self.searchTerm1.set('')
        self.NoOfTerms1.set('')
        self.positive = 0
        self.negative = 0
        self.neutral = 0
        self.polarity = 0
        self.tweetText = []
        self.tweetTextp = []
        self.tweetTextn = []
        # self.top1.destroy()
        # self.top2.destroy()

    def delete_window(self):
        self.master1.destroy()
        # self.master.update()
        # self.master.deiconify()
        self.master.destroy()

    def delete_window2(self):
        self.top1.destroy()
        self.master.update()
        self.master.deiconify()
        self.master1.destroy()
        # self.master.destroy()
        self.clear()

    def cleanTweet(self, tweet):
        # return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S + { })", " ", tweet).split())
        return ' '.join(re.sub("([^0-9A-Za-z \t]) | (\w +:\ / \ / \S + { })", " ", tweet).split())
        # return ''.join([i if ord(i)<128 else ' ' for i in tweet])


def main():
    root = Tk()
    w1 = Welcome(root)
    root.mainloop()


if __name__ == '__main__':
    main()

