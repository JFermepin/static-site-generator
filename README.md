# Static Site Generator

A Python static site generator with no external dependencies as a [boot.dev](https://boot.dev) project. Write content in Markdown, run a single command, and get a ready-to-deploy HTML site.

## Features

- Converts Markdown files to HTML with support for headings, bold, italic, code, links, and images
- Recursive content directory processing — mirrors your `content/` folder structure into `docs/`
- HTML templating via `template.html`
- GitHub Pages–ready output (configurable basepath)
- Zero external dependencies — pure Python 3

## Project structure

```
content/      # Markdown source files
static/       # CSS, images, and other assets (copied as-is)
docs/         # Generated HTML output (GitHub Pages root)
template.html # Page template (injects title and content)
src/          # Generator source code and tests
```

## Usage

```bash
# Generate site and serve locally at http://localhost:8888
./main.sh

# Build for GitHub Pages (sets basepath to /static-site-generator/)
./build.sh
```

## Adding content

1. Create a `.md` file anywhere under `content/`. It must start with a `# H1` heading — this becomes the page `<title>`.
2. Run `./main.sh` to regenerate the site.

## Running tests

```bash
./test.sh
# or
python3 -m unittest discover -s src
```