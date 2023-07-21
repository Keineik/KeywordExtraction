f = open('webSearch.bat', 'w', encoding="utf-8")
writeString = "https://www.google.com/search?q="
for kw in keywords:
    writeString += str(kw[0]) + ' '
    writeString = "start " + writeString.replace(' ', '+')
    f.write(writeString)