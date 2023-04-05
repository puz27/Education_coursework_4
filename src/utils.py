sj_api_key = "v3.r.137436720.8c7f8aba97fa695bc8eb530e248876d05b91ac49.93eb1ab45d1127728b93d412484a5f08ae09f2c8"


def print_info(*args):
    for description in args:
        print(description)
    print("--------------------------------------")


def format_text(text: str):

    patterns = {
        1: ['<highlighttext>', ''],
        2: ['</highlighttext>', '']
    }

    if text is None or "null":
        return f"Данных нет"
    else:
        for i in patterns:
            text = text.replace(patterns[i][0], patterns[i][1])
        return text
