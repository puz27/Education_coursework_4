superjob_api_key = "v3.r.137436720.8c7f8aba97fa695bc8eb530e248876d05b91ac49.93eb1ab45d1127728b93d412484a5f08ae09f2c8"

def print_info(*args):
    for description in args:
        print(description)
    print("--------------------------------------")

def convert_description(text: str):
    patterns = {
        "<highlighttext>": "",
        "</highlighttext>": ""
    }
    if text is None:
        return f"Нет данных"
    convert = text
    for i, j in patterns.items():
        convert = convert.replace(i, j)
    return convert
