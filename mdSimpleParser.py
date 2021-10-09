import pypandoc

# With an input file: it will infer the input format from the filename
output = pypandoc.convert_file('mdFiles/markdown-cheat-sheet.md', 'json')


output = pypandoc.convert_file('mdFiles/markDownForDummies.txt', 'json', format='md')

print("json:", output)

