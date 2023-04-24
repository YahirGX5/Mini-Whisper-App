import whisper
import tkinter as tk
from tkinter import filedialog
from style import STYLE
import asyncio
import tkinter.messagebox as messagebox

#This class implements Whisper AI with a GUI of tkinter
class Using_Whisper_With_GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        "self.RecordingWidget = RecordingAudio()"

        #Initialize things we need, the whisper object, and configure some app estetics of the app
        self.title("Whisper mini app")
        self.Whisper = whisper.load_model("medium")
        self.configure(background="gray26")
        self.init_widgets()

    #Function that transcribe the audio using a thread of asyncio, for no freeze the app while is transcribing
    async def Transcribing(self, audio):
        try:
            text = await asyncio.to_thread(self.Whisper.transcribe, audio)
            return text

        except Exception as e:
            messagebox.showerror("Error", e)

    #This function open a window to choose a file, then process and transcribe it, finally showing the text in the label  
    def RunningWhisper(self):
        audio = filedialog.askopenfilename()
        text = asyncio.run(self.Transcribing(audio))

        self.Text.delete("1.0", tk.END)
        self.Text.insert(tk.END, text["text"])

    #This function initialize the neccesary widgets, like the text label and buttons    
    def init_widgets(self):
        self.Text = tk.Text(self, **STYLE)
        self.Text.pack(side="top")
        
        self.ButtonTranscribing = tk.Button(self, text="Transcript with file", command=self.RunningWhisper)
        self.ButtonTranscribing.place(x=340, y=600)

        self.StopButton = tk.Button(self, text="Salir", command=self.destroy)
        self.StopButton.place(x=390, y=700)

"""        
class RecordingAudio(tk.Frame):
    def __init__(self):
        super().__init__()

        #Initialize the buttons and assigns the event of press and release the buttons
        self.isrecording = False
        self.Whisper = whisper.load_model("medium")
        self.button = tk.Button(self, text='rec')
        self.button.bind("<Button-1>", self.startRecording)
        self.button.bind("<ButtonRelease-1>", self.stopRecording)
        self.button.pack(side="bottom")

    #The same thing than the fucntion of Using_Whisper_With_GUI class
    async def Transcribing(self, audio):
        text = await asyncio.to_thread(self.Whisper.transcribe, audio)
        return text

    #This record the audio of microphone and stores it in self.audio
    def record(self):
        while self.isrecording:
            tk.Label(self, 
                     text="Recording"
                     ).pack(side="bottom")
            
            self.audio = sd.rec(int(44100*10), 44100, channels=2)

    #This creates a thread for record the audio and not freeze the app
    def startRecording(self, event):
        self.isrecording = True
        thread = threading.Thread(target=self.record)
        thread.start()

    #This proccess and transcribe the audio, then shows it in Text label
    def stopRecording(self, event):
        self.isrecording = False
        text = asyncio.run(self.Transcribing(self.audio))
        self.Text.delete(1.0, tk.END)
        self.Text.insert(tk.END, text["text"])
        
    """ 

    
        

        
        
