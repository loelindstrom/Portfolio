import tkinter as tk                # python 3
# import tkinter.ttk as tk
from tkinter import font as tkfont # python 3
import tkinter.ttk as ttk
from glosforhor import minaglosor


class GlosorApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Preparing the variables for the words and definitions:
        global minaglosor
        self.glosDict = minaglosor
        self.dataSetName = tk.StringVar("")
        self.words = []
        self.definitions = []

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="normal", slant="roman")
        self.title("Glosor")
        self.geometry("700x500")

        # Make window adjust when user resizes window:
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (DataSetMenu, WordView, DefinitionView):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

            cols, rows = frame.grid_size()
            for i in range(cols+1):
                frame.grid_columnconfigure(i, weight=1)
            for i in range(rows+1):
                frame.grid_rowconfigure(i, weight=1)



        # Style all widgets by default:
        for key in self.frames:
            for children in self.frames[key].winfo_children():
                children.configure(font=self.title_font)
                children.grid_configure(ipadx=10,
                                        ipady=10,
                                        padx=10,
                                        pady=10)

        # Show first menu:
        self.show_frame("DataSetMenu")

    def show_frame(self, page_name, oldFrame=None):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        if page_name == "DataSetMenu":
            if oldFrame.__class__.__name__ == "WordView":
                oldFrame.definition.set("")
            if frame.index:
                frame.dataSetsListbox.selection_set(frame.index)
        if page_name == "WordView":
            frame.words.set(self.words)
        if page_name == "DefinitionView":
            frame.definition.set(self.definitions[0])
            frame.showWordBtnLabel.set("Show word")
            frame.word.set("")
        frame.tkraise()


class DataSetMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.index = None

        # Create dataset menu items:
        dataSetList = []
        for key in controller.glosDict:
            dataSetList.append(key)

        # Open DataSetMenu-button
        openDataSetBtn = tk.Button(self, text="Data set-menu", highlightbackground="light steel blue")

        # Open WordView-button
        openWordViewBtn = tk.Button(self, text="Word-view",
                                     command=lambda: controller.show_frame("WordView"))

        # Open DefinitionsView-button
        openDefinitionsViewBtn = tk.Button(self, text="Definition-view",
                                           command=lambda: controller.show_frame("DefinitionView"))

        # Empty Label to fill out page (and make it fit with other menus)
        emptyLabel = tk.Label(self, text="Choose data set:", anchor="sw", width=50)

        # Datasets list
        dataSet = tk.StringVar(value=dataSetList)
        self.dataSetsListbox = tk.Listbox(self, listvariable=dataSet, width=50)
        self.dataSetsListbox.bind("<<ListboxSelect>>", self.onSelect)

        # Empty Label to fill out page (and make it fit with other menus)
        definitionMessage = tk.Label(self, text="   ",
                                     width=40, wraplength=600)

        # Layout via grid-method:
        openDataSetBtn.grid(column=0, row=0, columnspan=2, sticky="swe")
        openWordViewBtn.grid(column=0, row=1, sticky="nwe")
        openDefinitionsViewBtn.grid(column=1, row=1, sticky="nwe")
        emptyLabel.grid(column=0, row=2, columnspan=2, sticky="we")
        self.dataSetsListbox.grid(column=0, row=3, columnspan=2, sticky="nwe")
        definitionMessage.grid(column=0, row=4, columnspan=2, sticky="we")

    def onSelect(self, event):
        widget = event.widget
        try:
            self.index = int(widget.curselection()[0])
            key = widget.get(self.index)
            self.controller.dataSetName.set(str(key))
            self.controller.words = self.controller.glosDict[key][0]
            self.controller.definitions = self.controller.glosDict[key][1]
        except IndexError:
            return


class WordView(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Open Data set menu-button
        openDataSetBtn = tk.Button(self, text="Data set-menu",
                                   command=lambda: controller.show_frame("DataSetMenu", oldFrame=self))

        # Open DefinitionsView-button
        openDefinitionsViewBtn = tk.Button(self, text="Definition-view",
                                           command=lambda: controller.show_frame("DefinitionView"))

        # Open WordView-button
        openWordViewBtn = tk.Button(self, text="Word-view", highlightbackground="light steel blue")

        # Label with Data set name:
        dataSetLabel = tk.Label(self, textvariable=self.controller.dataSetName, width=50)

        # Listbox with list-variable:
        self.words = tk.StringVar()
        self.wordsLB = tk.Listbox(self, listvariable=self.words)
        self.wordsLB.bind("<<ListboxSelect>>", self.onSelect)


        # Label with definition
        self.definition = tk.StringVar()
        self.definition.set("")
        definitionMessage = tk.Label(self, textvariable=self.definition,
                                     width=40, wraplength=600)

        # Layout via grid-method:
        openDataSetBtn.grid(column=0, row=0, columnspan=2, sticky="swe")
        openWordViewBtn.grid(column=0, row=1, sticky="nwe")
        openDefinitionsViewBtn.grid(column=1, row=1, sticky="nwe")

        dataSetLabel.grid(column=0, row=2, columnspan=2, sticky="we")
        self.wordsLB.grid(column=0, row=3, columnspan=2, sticky="nwe")
        definitionMessage.grid(column=0, row=4, columnspan=2, sticky="we")

    def onSelect(self, event):
        widget = event.widget
        try:
            index = int(widget.curselection()[0])
            self.definition.set(self.controller.definitions[index])
        except IndexError:
            return


class DefinitionView(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Index to know where in the definitionlist we are:
        self.index = 0

        # Open Data set menu-button:
        openDataSetMenuBtn = tk.Button(self, text="Data set-menu",
                           command=lambda: controller.show_frame("DataSetMenu"))

        # Open WordView-button
        openWordViewBtn = tk.Button(self, text="Word-view",
                                    command=lambda: controller.show_frame("WordView"))

        # Open DefinitionsView-button
        openDefinitionsViewBtn = tk.Button(self, text="Definition-view", highlightbackground="light steel blue")

        # Label with Data set name:
        dataSetLabel = tk.Label(self, textvariable=self.controller.dataSetName, width=50)

        # Label with definition within a LabelFrame
        definitionLabelFrame = tk.LabelFrame(self, text="Definition", width=250)
        self.definition = tk.StringVar("")
        definitionLabel = tk.Label(definitionLabelFrame,
                                     textvariable=self.definition,
                                     width=25, wraplength=200)
        definitionLabel.grid(column=0, row=0, sticky="w")

        # Show word-button
        self.showWordBtnLabel = tk.StringVar("")
        self.showWordBtnLabel.set("Show word")
        showWordBtn = tk.Button(self, textvariable=self.showWordBtnLabel,
                                    command=self.showWord)

        # Label with word within a LabelFrame
        wordLabelFrame = tk.LabelFrame(self, text="Word")
        self.word = tk.StringVar("")
        wordLabel= tk.Label(wordLabelFrame, textvariable=self.word,
                            width=25, wraplength=200)
        wordLabel.grid(column=0, row=0, sticky="w")

        # Next definition-button
        nextDefinitionBtn = tk.Button(self, text="Next definition",
                                      command=self.nextDefinition)

        # Layout via grid-method:
        openDataSetMenuBtn.grid(column=0, row=0, columnspan=2, sticky="swe")
        openWordViewBtn.grid(column=0, row=1, sticky="nwe")
        openDefinitionsViewBtn.grid(column=1, row=1, sticky="nwe")
        dataSetLabel.grid(column=0, row=2, columnspan=2, sticky="we")
        definitionLabelFrame.grid(column=0, row=3, sticky="nwe")
        wordLabelFrame.grid(column=1, row=3, sticky="nwe")
        showWordBtn.grid(column=1, row=4, sticky="we")
        nextDefinitionBtn.grid(column=1, row=6, sticky="we")

    def showWord(self):
        '''
        If showWord-button is pressed the word will show
        and the button will instead say "Hide word".

        If the button is pressed again the word will be hidden
        and the button will again say "Show word".
        '''
        if self.showWordBtnLabel.get() == "Show word":
            self.word.set(self.controller.words[self.index])
            self.showWordBtnLabel.set("Hide word")
        else:
            self.word.set("")
            self.showWordBtnLabel.set("Show word")
        return

    def nextDefinition(self):
        self.index += 1
        if self.index == len(self.controller.definitions) - 1:
            self.index = 0
        self.word.set("")
        self.showWordBtnLabel.set("Show word")
        self.definition.set(self.controller.definitions[self.index])
        return


if __name__ == "__main__":
    app = GlosorApp()
    app.mainloop()