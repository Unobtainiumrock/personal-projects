import re

def replace_keywords(text, replacements):
    pattern = re.compile("|".join(map(re.escape, replacements.keys())))

    return pattern.sub(lambda match: replacements[match.group(0)], text)

text = "Coca cola international wishes to partner with Apple. However, Apple already has plans in the pipeline to collaborate with Pepsi which could to conflicting interests."

replacements = {
    "Coca cola": "party A",
    "Apple": "party B",
    "Pepsi": "party C",
}

new_text = replace_keywords(text, replacements)

print(new_text)