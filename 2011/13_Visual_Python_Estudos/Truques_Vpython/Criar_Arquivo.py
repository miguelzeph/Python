from visual.filedialog import save_file
fd = save_file()
if fd:
    fd.write("This is a test.\nThis is only a test.")
    fd.close() # close the file (we're through with it)