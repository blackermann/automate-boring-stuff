import webbrowser, sys, pyperclip

sys.argv # 

#check if commandline elements were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870','Valencia', 'St.'] -> '870 Valencia St."
    ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste
webbrowser.open('https://www.google.com/maps/place/' + address)
