from visual.filedialog import get_file
fd = get_file()
if fd:
    data = fd.read() # or fd.readlines()
    fd.close() # close the file (we're through with it)
    print(data)