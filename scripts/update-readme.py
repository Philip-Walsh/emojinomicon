import json
import os


def slugify(name):
    return name.replace(':', '')


def get_root_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def append_to_readme(emoji, shortname):
    readme_path = os.path.join(get_root_dir(), 'README.md')
    with open(readme_path, 'a', encoding='utf-8') as readme:
        readme.write(
            f'\n{emoji} [:{shortname}:](https://raw.githubusercontent.com/Philip-Walsh/emojinomicon/main/src/{slugify(shortname)}.svg)\n')


def main():
    with open(os.path.join(get_root_dir(), 'emoji.json'), 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data['emojis']:
        emoji = item['emoji']
        shortname = item['shortname']
        append_to_readme(emoji, shortname)


if __name__ == '__main__':
    main()

