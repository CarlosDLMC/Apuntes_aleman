import os
from PyPDF2 import PdfReader, PdfMerger

folder_path = "A1.1"


def get_order_nums(name):
    words = name.replace(".pdf", "").split("_")
    result = ""
    for word in words:
        if word.isnumeric():
            result += word
            continue
        break
    return int(result)


files = os.listdir(folder_path)
pdf_merger = PdfMerger()

for filename in sorted(files, key=get_order_nums):
    filepath = os.path.join(folder_path, filename)
    with open(filepath, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        pdf_merger.append(pdf_file)
        print(f"procesado {filename}!")

with open("merged.pdf", "wb") as merged:
    pdf_merger.write(merged)
