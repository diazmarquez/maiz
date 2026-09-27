# Maíz: arepas and their histories

A six-page, source-linked ChatGPT Site: an overview, Colombian arepa’e huevo, Venezuelan Reina Pepiada, a side-by-side comparison of two plain arepas, an evidence-based reconstruction of a whole-maize cake, and a history of maize-cake propagation in northern South America.

## Pages

- `dist/index.html` — overview and navigation
- `dist/colombia.html` — Luruaco arepa’e huevo
- `dist/venezuela.html` — Caracas Reina Pepiada
- `dist/plain-arepas.html` — unfilled Antioquian and Venezuelan arepas, recipe by recipe
- `dist/ancestral.html` — Indigenous whole-maize cake reconstruction
- `dist/history.html` — independent crop and corn-cake timelines, their evidence intersection, and documented multicultural exchange

The site is plain static HTML/CSS. Edit the overview and featured recipes in `site.py`; the plain comparison lives in `plain_page.py`, and the history text and claim-level references live in `history_page.py`. Run `python site.py` to regenerate the pages. Serve `dist/` locally with `python -m http.server 8000 -d dist`.

## Historical method

The ancestor recipe is a **modern kitchen reconstruction** from contact-era accounts. It does not claim to preserve exact preconquest quantities. The history page separates the crop's origin and movement from evidence for a formed food. Its dates label the material actually dated: a layer or charcoal, a person, a maize specimen, a genetic model, or a written account. El Saladero links maize starch with a ceramic cooking surface, but does not preserve a cake. The 1548 Riohacha document is a surviving written usage listed by the historical dictionary, not a proof of invention there. Each page links directly to its sources and notes where its recipe is adapted.

## Image credits

- `arepa-de-huevo.webp`: [Jdvillalobos, *Arepa de huevo*](https://commons.wikimedia.org/wiki/File:Arepa_de_huevo.jpg), [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). Resized and displayed with responsive cropping.
- `reina-pepiada.webp`: [USDA Food and Nutrition Service, Reina Pepiada](https://commons.wikimedia.org/wiki/File:MyPlate_gov_Cultural_Food_(20241025-USDA-FNS-UNK-0024).jpg), U.S. government public domain. Resized and displayed with responsive cropping.
- `metate.webp`: [Fecive, grinding stones from San Agustín](https://commons.wikimedia.org/wiki/File:Metate_y_mano_de_moler_encontrados_en_San_Agustin_Huila.jpg), CC0. Resized and displayed with responsive cropping; the object is illustrative, not proof of use for the reconstructed cake.
- `arepas-itagui.jpg`: [Eddy Milfort, arepas in Itagüí](https://commons.wikimedia.org/wiki/File:Arepas_%28Itag%C3%BC%C3%AD%29.jpg), [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/). Original image displayed with a CSS crop to show plain rounds; illustrative, not the cited recipe's batch.
- `arepas-venezolanas.jpg`: [Periodismodepaz, plain Venezuelan arepas](https://commons.wikimedia.org/wiki/File:Arepas_venezolanas.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Original displayed on the comparison page; illustrative, not the cited recipe's batch.

The original source and license links also appear on the corresponding site pages.
