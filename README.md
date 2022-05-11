# exe2png

Convert executables (or any other file) into an image

## Installation

### From PyPI

```sh
pip3 install exe2png
```

### From GitHub

```sh
pip3 install git+https://github.com/donno2048/exe2png
```

## Usage

```sh
exe2png -h
usage: exe2png [-h] (-e | -d) [-c] [-H HEIGHT] -f FILE [-o OUTPUT]

Encode or decode a file to or from a PNG image.

optional arguments:
  -h, --help            show this help message and exit
  -e, --encode          encode a file to a PNG image
  -d, --decode          decode a PNG image to a file
  -c, --color           encode or decode a color image
  -H HEIGHT, --height HEIGHT
                        height of the image
  -f FILE, --file FILE  the file to encode or decode
  -o OUTPUT, --output OUTPUT
                        the file to output to
```

For example, we can encode my [snake executable](https://github.com/donno2048/snake) to a greyscale PNG image:

```sh
wget https://github.com/donno2048/snake/releases/download/v14/snake.com
exe2png -e -H 15 -f snake.com -o snakeL.png
```

and get this:

![greyscale image](snakeL.png)

and we can decode the image back to a file:

```sh
exe2png -d -f snakeL.png -o snake.com
```

or we can encode a color image:

```sh
exe2png -e -c -H 9 -f snake.com -o snakeRGB.png
```

and get this:

![color image](snakeRGB.png)

and we can decode the image back to a file:

```sh
exe2png -d -c -f snakeRGB.png -o snake.com
```

Here is python itself encoded into a PNG image:

![python image](python.png)
