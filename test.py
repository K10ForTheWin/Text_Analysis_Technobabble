import os

want_names = [
    "0'BRIEN.txt",
    "CARDASSIAN 2.txt",
    "DAMAR.txt",
    "JAKE.txt",
    "KURN.txt",
    "PICARD.txt",
    "ALEXANDER.txt",
    "CARDASSIAN 3.txt",
    "DATA.txt",
    "JANEWAY.txt",
    "LAFORGE.txt",
    "PULASKI.txt",
    "ALIEN.txt",
    "CARDASSIAN.txt",
    "DUKAT.txt",
    "JEM'HADAR.txt",
    "LENARA.txt",
    "Q.txt",
    "ALKAR.txt",
    "CASSIE.txt",
    "EDDINGTON.txt",
    "JENNIFER.txt",
    "LWAXANA.txt",
    "REED.txt",
    "AMANDA.txt",
    "CHAKOTAY.txt",
    "EZRI.txt",
    "JONATHAN.txt",
    "MARTOK.txt",
    "RIKER.txt",
    "ARCHER.txt",
    "CHANCELLOR.txt",
    "FOUNDER.txt",
    "KEEVAN.txt",
    "MCCOY.txt",
    "RO.txt",
    "BARCLAY.txt",
    "CHAPEL.txt",
    "GARAK.txt",
    "K'EHLEYR.txt",
    "MOLLY.txt",
    "SCOTT.txt",
    "BASHIR.txt",
    "CHEKOV.txt",
    "GOWRON.txt",
    "KEIK.txt",
    "MORIARTY.txt",
    "SESKA.txt",
    "BEJAL.txt",
    "COMPUTER.txt",
    "GUINAN.txt",
    "KES.txt",
    "NEELIX.txt",
    "SHAKAAR.txt",
    "B'ETOR.txt",
    "CRUSHER.txt",
    "HAYES.txt",
    "KHAN.txt",
    "NOG.txt",
    "BILBY.txt",
    "CULLUH.txt",
    "HOSHI.txt",
    "KOLOS.txt",
    "O'BRIEN.txt",
    "BRIEN.txt",
    "CURZON.txt",
    "ILIANA.txt",
    "KOLOTH.txt",
    "ODO.txt"]

for file in os.listdir('data_char_lines_top_100'):
    if file in want_names:
        print(f'[INFO] Detected {file}')
        if file not in os.listdir('wordclouds'):
            pass

somestring = "I do]^_n't kn/:;<ow"
import string
list(string.punctuation)


breakpoint

