# DealDesk · Process journey (presentation)

A 16:9 slide deck, in one self-contained `index.html`, for the Futureproofing prototype challenge.
Fictional product, fictional data (Project Harbor). Nothing is sent.

- **Navigate:** arrow keys, space, click the arrows, swipe, or use "Contents".
- **Slides (8):** cover · customer and problem · assumptions and task flow · alternative and trade-off · final design walkthrough · checks · iteration, limits and next question · tools.
- **Process document:** https://docs.google.com/document/d/1ZfMwIYkjEEj_gUwjJjqtu9YYewYgbQLxrB49bfrzEMM/edit?usp=sharing

## Editing

`index.html` is generated. Edit the source and rebuild:

```bash
# edit src/deck.template.html (text, layout) or replace images in src/images/
python3 build.py
```

## Deploy (Cloudflare Pages)

No build step is needed on Cloudflare: publish the repo root, where `index.html` already lives.

## Credits

Brand icons from [Simple Icons](https://simpleicons.org) (CC0). Tool logos belong to their owners and are used only to name the tools used.
