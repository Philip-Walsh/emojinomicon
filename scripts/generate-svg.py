import json
import os


def get_svg(emoji):
    return f'''
<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50">
  <text y="32" font-size="32">{emoji}</text>
</svg>
'''


def slugify(name):
    return name.replace(':', '')


def get_script_dir():
    return os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(get_script_dir(), 'emoji.json'), 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data['emojis']:
        emoji = item['emoji']
        shortname = item['shortname']
        slug = slugify(shortname)

        with open(os.path.join(get_script_dir(), 'src', f'{slug}.svg'), 'w', encoding='utf-8') as svg_file:
            svg_file.write(get_svg(emoji))


if __name__ == '__main__':
    main()

