#! python 3

# Regex Example Program: Phone and Email Scraper
# manually copy the phone directory from the pdf to the clipboard by ctrl-a & ctrl-c; pyperclip does this

import re, pyperclip

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# per Al's example:
# types of phone numbers: 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?    # area code (optional); two groups both are optional ?
(\s | -)    # first separator, space or dash, in a group
\d\d\d    # first 3 digits
-   # separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s) |x)     # extension word part (optional)
(\d{2,5}))?    # extenssion number part, two to five digits
)
''', re.VERBOSE)


# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d){2,5}))?.com

[a-zA-Z0-9_.+]+    # name part, character class, + at the end is we'll be looking for one or more of them

@    # @ symbol
[a-zA-Z0-9_.+]+    # domain name part
''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# capture the phone numbers from the first tuple and the e-mails
allPhoneNumbers = [] # create an empty list (square brackets)
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0]) # 0 is the position of the first item tuple, append to the list

# TODO: Copy the extracted email/phone to the clipboare
# use the join method to join the phone numbers with a new line so you get a column of phone numbers and emails
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

print(results)



#print(text)
#print(allPhoneNumbers)
#print(extractedPhone)
#print(extractedEmail)
