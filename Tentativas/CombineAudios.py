from pydub import AudioSegment
Silence = AudioSegment.from_file("C:/Users/Raul/Downloads/Silence.wav", format="wav")
sound2 = AudioSegment.from_file("C:/Users/Raul/Desktop/Mudança_PC/IPCA/Mestrado/1Ano/2Semestre/"
                                "TP_LAB22/TP/data/recordings/train/Vale_Ben_u_ron_26.wav", format="wav")


# sound1 6 dB louder
louder = Silence + 6


# sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
combined =  Silence+sound2
combined1 =  sound2 +Silence
combined2 =  Silence+sound2 + Silence
# simple export
file_handle = combined2.export("output/Vale_Ben_u_ron_76.wav", format="wav")
