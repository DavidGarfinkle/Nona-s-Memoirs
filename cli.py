import sys
import os
import click

@click.group()
def cli():
    """
    Top level command group
    """

@cli.command()
@click.argument('source_dir')
def fmt(source_dir):
    from fmt import newline_by_sentence

    print("Formatting {} with newlines...".format(source_dir))

    for fl in os.listdir(source_dir):
        print("{:>10}".format(fl))
        file_path = os.path.join(source_dir, fl)

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        formatted_text = newline_by_sentence(text)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(formatted_text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translate_english.py dest_dir fr|he")

    dest_dir = sys.argv[1]
    language = sys.argv[2]

if __name__ == "__main__":
    cli()
