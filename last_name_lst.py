# give me a list of only the last names of the author string

authors = """Audre Lorde,Gabriela Mistral,Jean Toomer,
An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,
Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"""

author_name = authors.split(",")

author_last_name = []
for name in author_name:
    author_last_name.append(name.split()[-1])
print(author_last_name)
