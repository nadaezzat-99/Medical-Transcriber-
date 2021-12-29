
# from asrecognition import ASREngine
from asrecognition import ASREngine
from fastapi import UploadFile
import soundfile as sf
from fpdf import FPDF
import librosa
import os


asr = ASREngine("en", model_path="facebook/wav2vec2-base-960h")


# Trancribe the audio file , user uploaded 
def predict(audio_file: UploadFile):
      audio,sr=librosa.load(audio_file.file , sr =None)
      sf.write('Audio_to_transcribe.wav', audio, sr)
      audio_path=['Audio_to_transcribe.wav']
      transcriptions = asr.transcribe(audio_path)
      text=transcriptions[0]['transcription']
      os.remove("Audio_to_transcribe.wav")
      return(text)
      
def Generate_report(text:"str",destination):
    # save FPDF() class into a variable pdf
    pdf = FPDF()
 
    # Add a page
    pdf.add_page()
 
   # set style and size of font
   # that you want in the pdf
    pdf.set_font("Arial", size = 16)

    # create a cell
    pdf.cell(200, 10, txt = text, ln = 1, align = 'C')
 
    # save the pdf with name .pdf
    pdf.output("Report.pdf",dest=destination) 
