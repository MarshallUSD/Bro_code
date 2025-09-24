# Python writing files (.txt, json, .csv)



txt_d="I like pizza"

file_path="output.txt"


with open(file=file_path, mode="w") as file:
    file.write(txt_d)
    print(f"txt data written to {file_path}")