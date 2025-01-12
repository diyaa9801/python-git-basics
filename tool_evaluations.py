import tools

#testing output
students_lod = [
    {"name": "Robin", "github_name": "ProgrammingGod42"},
    {"name": "Kim", "github_name": "CodingKim"},
    {"name": "Jesse", "github_name": "JavascriptJesse"},
]

students_dol = {
    "name": ["Robin", "Kim", "Jesse"],
    "github_name": ["ProgrammingGod42", "CodingKim", "JavascriptJesse"],
}


dol = tools.convert_lod_to_dol(students_lod)
print('Row to column conversion output', dol)

print('Check create_markdown_table function for dol object')
tools.create_markdown_table(dol)

lod = tools.convert_dol_to_lod(students_dol)
print('Column to Row conversion output', lod)

print('Check create_markdown_table function for lod object')
tools.create_markdown_table(lod)
