from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("C:/Users/Raul/PycharmProjects/VoiceRecognition/Audios/Raul_Ben_u_ron.wav", "wav")
chunk_length_ms = 8000  # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms)  # Make chunks of one sec
for i, chunk in enumerate(chunks):
    chunk_name = "output/audio/{0}.wav".format(i)
    print("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")