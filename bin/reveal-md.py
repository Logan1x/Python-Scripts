# Generating presentation from markdown

import json
import argparse
from os import listdir
from os.path import isfile, join, isdir

# Parsing command line args
parser = argparse.ArgumentParser(
    description='Convert your markdown to presentation')

parser.add_argument('-dir', metavar='-d', type=str,
                    nargs='+', help='Directory of your markdown files')
parser.add_argument('-config', metavar='-c', type=str,
                    nargs='+', help='Config file')

args = parser.parse_args()
config = json.load(open('reveal.default.config.json'))

# Replacing default config with user defined config
if args.config:
    try:
        config = json.load(open(args.config[0]))
    except:
        print('Please check if config file exist or it is a json')

# Read all files in the directory
if args.dir:
    if isdir(args.dir[0]):
        file_names = [file for file in listdir(
            args.dir[0]) if isfile(join(args.dir[0], file))]

        all_file_content = ""
        html = """
          <html>
            <head>
              <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/css/reveal.min.css">
              <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/css/theme/black.min.css">
            </head>
          <body>
            <div class="reveal">
            <div class="slides">"""

        for file in file_names:
            with open(join(args.dir[0], file)) as f:
                data = f.read()

            all_file_content = '<section data-markdown><textarea data-template>' + \
                data + '</textarea></section>'

            html += all_file_content

        html += """</div>
                    </div>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/js/reveal.min.js"></script>
                    <script>
                    Reveal.initialize(""" + str(json.dumps(config, ensure_ascii=False)) + """);
                    </script>
                    </body>
                    </html>
                    """

        html_file = open('output.html', 'w')
        html_file.write(html)
        html_file.close()
    else:
        print('Please make sure directory exist or if it is a directory')
