from tqdm import tqdm
import time
import os

def customFileSizeGenerator():
    sec = 0
    file_name = str(input("File Name: "))
    file_form = str(input("File Form(txt, py, json...): "))
    file_size = int(input("File Size: "))
    file = f"{file_name}.{file_form}"
    f = open(file,"wb")
    for i in tqdm (range (100),
                   desc="Loading…",
                   ascii=False, ncols=75):
        time.sleep(0.01)
        f.seek(int(file_size)-1)
        f.write(b"\0")
    print("Completed.")
    f.close()

customFileSizeGenerator()
