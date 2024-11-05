def list_languages():
    return ["Python", "Java", "C++", "JavaScript"]

def build_statement(language):
    return f"{language} is a popular programming language."

languages = list_languages()
for language in languages:
    print(build_statement(language))
