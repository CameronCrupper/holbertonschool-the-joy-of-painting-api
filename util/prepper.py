"""helper function"""


def replace_char(file: str) -> None:
    with open(file, 'r') as f:
        text = f.read()
        text = text.replace(',', '')
        text = text.replace('"', '')
        text = text.replace(' (', ',')
        text = text.replace(')', ',')
    with open('../data/TJOP-Episode_Dates.txt', 'w') as f:
        f.write(text)


if __name__ == '__main__':
    replace_char('../data/TJOP-Episode_Dates.txt')
