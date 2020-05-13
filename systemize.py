import os

def createIfNotExit(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

if __name__ == "__main__":
    files = os.listdir()
    files.remove("systemize.py")
    print("Files Available in this Folder :")
    print(*files, sep = ", ")
    print("Total files = ",len(files))

    createIfNotExit('Images')
    createIfNotExit('Docs')
    createIfNotExit('Videos')
    createIfNotExit('Audios')
    createIfNotExit('Archives')
    createIfNotExit('Exes')
    createIfNotExit('Pdfs')
    createIfNotExit('Texts')
    createIfNotExit('Htmls')
    createIfNotExit('Cpps')
    createIfNotExit("Others")

    imgExts = [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", 
                ".png", ".bpg", "svg",".heif", ".psd"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    print("Total Image file moved = ",len(images))

    docExts = [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                    ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                    ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                    ".pptx"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    print("Total Doc file moved = ",len(docs))

    videoExts = [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
			    ".qt", ".mpg", ".mpeg", ".3gp"]
    video = [file for file in files if os.path.splitext(file)[1].lower() in videoExts]
    print("Total Video files moved = ",len(video))

    audioExts = [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
			    ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"]
    audio = [file for file in files if os.path.splitext(file)[1].lower() in audioExts]
    print("Total Audio files moved = ",len(audio))

    archiveExts = [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
				    ".dmg", ".rar", ".xar", ".zip"]
    archives = [file for file in files if os.path.splitext(file)[1].lower() in archiveExts]
    print("Total Archive files moved = ",len(archives))

    exeExts = [".exe"]
    exes = [file for file in files if os.path.splitext(file)[1].lower() in exeExts]
    print("Total Exe files moved = ",len(exes))

    pdfExts = [".pdf"]
    pdfs = [file for file in files if os.path.splitext(file)[1].lower() in pdfExts]
    print("Total PDF files moved = ",len(pdfs))

    plaintextExts = [".txt", ".in", ".out"]
    plaintexts = [file for file in files if os.path.splitext(file)[1].lower() in plaintextExts]
    print("Total Text files moved = ",len(plaintexts))

    htmlExts = [".html5", ".html", ".htm", ".xhtml"]
    htmls = [file for file in files if os.path.splitext(file)[1].lower() in htmlExts]
    print("Total HTML files moved = ",len(htmls))

    cppExts = [".cpp"]
    cpps = [file for file in files if os.path.splitext(file)[1].lower() in cppExts]
    print("Total C++ files moved = ",len(cpps))


    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in videoExts) and (ext not in cppExts) and (ext not in plaintextExts) and (ext not in htmlExts) and (ext not in docExts) and (ext not in pdfExts) and (ext not in imgExts) and (ext not in exeExts) and (ext not in archiveExts) and (ext not in audioExts)  and os.path.isfile(file):
            others.append(file)
    print("Total others file moved = ",len(others))

    
    move("Images",images)
    move("Docs",docs)
    move("Videos",video)
    move("Audios",audio)
    move("Archives",archives)
    move("Exes",exes)
    move("Pdfs",pdfs)
    move("Texts",plaintexts)
    move("Htmls",htmls)
    move("Cpps",cpps)
    move("Others",others)
    
    g = input("Press Enter to Exit")