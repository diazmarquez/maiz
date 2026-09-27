"""Build the dependency-free Maíz editorial site.

Run `python site.py` after changing page content. Generated HTML lives in dist/.
"""

from pathlib import Path
from html import escape

ROOT = Path(__file__).parent / "dist"
ROOT.mkdir(exist_ok=True)

URLS = {
    "colombia": "colombia.html",
    "venezuela": "venezuela.html",
    "plain": "plain-arepas.html",
    "native": "indigenous-recipes.html",
    "ancestral": "ancestral.html",
    "history": "history.html",
}


def header(active="overview"):
    links = [("overview", "Overview", "index.html"), ("colombia", "Colombia", URLS["colombia"]),
             ("venezuela", "Venezuela", URLS["venezuela"]), ("plain", "Plain arepas", URLS["plain"]),
             ("native", "Indigenous recipes", URLS["native"]),
             ("ancestral", "Ancestral cake", URLS["ancestral"]),
             ("history", "History", URLS["history"])]
    nav = "".join(f'<a href="{url}"' + (' aria-current="page"' if key == active else '') + f'>{label}</a>'
                  for key, label, url in links)
    return f'''<header class="site-header"><div class="wrap header-inner">
      <a class="brand" href="index.html" aria-label="Maíz overview">Maíz<span>Recipes &amp; histories</span></a>
      <nav class="nav" aria-label="Main navigation">{nav}</nav>
    </div></header>'''


def document(title, description, body, active="overview"):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="description" content="{escape(description, quote=True)}"><title>{escape(title)} · Maíz</title>
    <link rel="stylesheet" href="assets/site.css"></head><body>
    <a href="#main" class="skip-link" style="position:absolute;left:-10000px;top:auto;z-index:10;background:#fff;padding:10px" onfocus="this.style.left='10px'" onblur="this.style.left='-10000px'">Skip to content</a>
    {header(active)}<main id="main">{body}</main><footer class="footer"><div class="wrap footer-inner">
      <span>Maíz · Arepa recipes and their shared history</span><span><a href="index.html">Overview</a> · <a href="history.html">Evidence &amp; sources</a></span>
    </div></footer></body></html>'''


def sources(items, intro="These links identify the recipe, historical, and image sources used on this page."):
    rows = "".join(f'<li id="source-{i}"><a href="{url}" target="_blank" rel="noopener noreferrer">{name} ↗</a><p>{note}</p></li>'
                   for i, (name, url, note) in enumerate(items, 1))
    return f'''<section class="sources" id="sources"><div class="wrap"><span class="eyebrow">Trace the account</span>
      <h2>Sources &amp; credits</h2><p>{intro}</p><ol class="source-list">{rows}</ol></div></section>'''


def picture(file, alt, caption):
    return f'<figure class="picture wrap"><img src="assets/{file}" alt="{escape(alt, quote=True)}" loading="eager"><figcaption>{caption}</figcaption></figure>'


def recipe_page(key, title, kicker, dek, pills, file, alt, caption, ingredients, method, callout, refs, next_key, next_title):
    pill_html = "".join(f'<span class="pill">{p}</span>' for p in pills)
    ing_html = "".join(f'<h3>{heading}</h3><ul>' + "".join(f'<li>{item}</li>' for item in items) + '</ul>'
                       for heading, items in ingredients)
    steps_html = "".join(f'<li><div><strong>{heading}</strong><p>{body}</p></div></li>' for heading, body in method)
    body = f'''<section class="detail-intro wrap"><a class="breadcrumb" href="index.html">← Overview</a>
      <div class="eyebrow">{kicker}</div><h1>{title}</h1><p class="dek">{dek}</p><div class="pills">{pill_html}</div></section>
      {picture(file, alt, caption)}
      <div class="wrap recipe-layout"><aside class="ingredients"><h2>Ingredients</h2>{ing_html}</aside>
      <section class="method"><span class="eyebrow">Cook it</span><h2>Method</h2><ol class="steps">{steps_html}</ol>
      <div class="callout">{callout}</div></section></div>
      {sources(refs)}<nav class="wrap next-links" aria-label="More Maíz pages"><a href="index.html">← Back to overview</a><a href="{URLS[next_key]}">Next: {next_title} →</a></nav>'''
    return document(title, dek, body, key)


overview = '''<section class="hero"><div class="wrap hero-inner"><div><span class="eyebrow" style="color:var(--maize)">A maize inheritance</span>
  <h1>One grain.<br>Many kitchens.</h1><p class="lead">Meet three distinctive corn cakes, compare plain Colombian and Venezuelan arepas, then follow the evidence of how Indigenous maize traditions, colonial contact, migration, and modern kitchens shaped them.</p>
  <a class="jump" href="#explore">Explore the recipes ↓</a></div><div class="hero-side"><strong>Read the evidence with the food.</strong>
  <p>The ancient cake is a reconstruction. The Colombian and Venezuelan recipes are documented modern expressions. Each page links to its sources.</p></div></div></section>
  <section class="section" id="explore"><div class="wrap"><div class="section-head"><div><span class="eyebrow">The table</span><h2>Three featured cakes</h2></div>
  <p>Begin with a dish or start before the present borders. Every card opens a full recipe with context and source notes.</p></div>
  <div class="grid">
   <a class="feature" href="ancestral.html"><img src="assets/metate.webp" alt="Two maize grinding stones displayed in San Agustín, Colombia" loading="eager"><div class="body"><span class="label">Before modern nations · reconstruction</span><h3>Whole maize on a griddle</h3><p>A cookable interpretation of Indigenous maize processing described in sixteenth-century accounts.</p><span class="read">Read the ancestral cake ↗</span></div></a>
   <a class="feature" href="colombia.html"><img src="assets/arepa-de-huevo.webp" alt="A group of golden fried arepas de huevo" loading="eager"><div class="body"><span class="label">Colombia · Luruaco, Atlántico</span><h3>Arepa’e huevo</h3><p>The Caribbean coast’s puffed, fried maize pocket with an egg inside.</p><span class="read">Cook the Colombian arepa ↗</span></div></a>
   <a class="feature" href="venezuela.html"><img src="assets/reina-pepiada.webp" alt="Chicken and avocado filled Venezuelan arepas" loading="eager"><div class="body"><span class="label">Venezuela · Caracas</span><h3>Reina Pepiada</h3><p>A griddled arepa filled with chicken and avocado, named in the 1950s.</p><span class="read">Cook the Venezuelan arepa ↗</span></div></a>
  </div><a class="compare-band" href="plain-arepas.html"><div><span class="eyebrow">Back to the base</span><h2>Plain arepas, side by side</h2></div>
  <p>Make an Antioquian arepa from dehulled maize kernels and a Venezuelan one from precooked flour, without fillings or toppings. See exactly where the two sourced methods differ. <strong>Compare the recipes ↗</strong></p></a>
  <a class="native-band" href="indigenous-recipes.html"><div><span class="eyebrow">Living kitchens · recorded sources</span><h2>Indigenous recipes of the region</h2></div>
  <p>Read Zenú and Wayúu corn-cake methods in their documented form, with the community or cook credited on each card. A Warao account is identified separately where the record is incomplete. <strong>See the recipes ↗</strong></p></a>
  <a class="history-band" href="history.html"><div><span class="eyebrow">Two evidence trails</span><h2>Two histories behind the arepa</h2></div>
  <p>Trace maize from its Mexican origin through Colombia and Venezuela. Separately, follow the evidence for cooking surfaces, corn cakes, colonial accounts, and later recipes. Each claim links to its source. <strong>Read the history ↗</strong></p></a></div></section>'''
(ROOT / "index.html").write_text(document("Overview", "Three featured corn cakes, two plain arepas compared side by side, and an evidence-led history of maize across Colombia and Venezuela.", overview), encoding="utf-8")


colombia = recipe_page(
    "colombia", "Arepa’e huevo", "Colombia / Luruaco, Atlántico",
    "A thin maize round rises in hot oil. The cook opens the hollow crust, slips in a raw egg, seals it, and fries it again. Luruaco is a celebrated center of this Caribbean dish; the exact place of invention is not established.",
    ["Makes 4", "About 35 minutes", "Fried · egg-filled"], "arepa-de-huevo.webp",
    "Several golden fried arepas de huevo on a plate",
    'Photograph: <a href="https://commons.wikimedia.org/wiki/File:Arepa_de_huevo.jpg" target="_blank" rel="noopener noreferrer">Jdvillalobos / Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener noreferrer">CC BY 3.0</a>. Cropped and resized for this site.',
    [("For the dough", ["1 cup precooked maize flour (masarepa)", "1 cup warm water", "½ tsp salt", "½ tsp sugar", "Vegetable oil for deep-frying"]),
     ("For the centers", ["4 eggs", "A little dough reserved from each portion for sealing"])],
    [("Mix and rest", "Combine masarepa, salt, and sugar. Add warm water and knead to a smooth dough. Rest 5 minutes. Divide into 4 equal portions; pinch off a tiny bit from each for its seal."),
     ("Shape and puff", "Press each portion between sheets of parchment into a round about 1 cm (½ in) thick. Heat oil to 175°C / 350°F. Fry one at a time, turning once, for about 3 minutes until puffed. Spoon hot oil over the top if needed to help the skin lift."),
     ("Open and fill", "Drain briefly. When safe to handle, cut a short slit into the hollow edge without cutting across the cake. Crack one egg into a small cup and pour it into the pocket. Close the slit with its reserved dough."),
     ("Fry again", "Return carefully to hot oil for about 4 minutes, turning as needed, until the egg is cooked to your preference. Drain and serve warm.")],
    '<strong>What is traditional here?</strong><p>Colombia’s Ministry of Culture documents the puff–slit–egg–seal–fry technique in Luruaco. This four-serving home formula follows Erica Dinho’s accessible masarepa recipe; the Governor of Atlántico also records a whole-maize-dough version from cook María del Socorro Castillo Montero. The precooked flour is a convenience, not a claim about an ancient formula. <a href="#sources">See sources</a>.</p>',
    [("Colombia Ministry of Culture · Mi Atlántico SABE, p. 13", "https://patrimonio.mincultura.gov.co/SiteAssets/Paginas/Publicaciones-biblioteca-cocinas/Atl%C3%A1ntico.pdf", "Documents a Luruaco cook’s method and describes Indigenous and African traditions in the area."),
     ("Gobernación del Atlántico · Atlántico sabe rico, pp. 142–144", "https://www.atlantico.gov.co/images/stories/capital/Adultos/PalabrasMayores/atlanticosaberico82-192.pdf", "Records María del Socorro Castillo Montero’s egg arepa and its local standing."),
     ("Erica Dinho · Arepa de Huevo", "https://www.mycolombianrecipes.com/es/arepa-de-huevo/", "Ingredient quantities and practical timing for this four-arepa home adaptation."),
     ("Jdvillalobos · Arepa de huevo photograph", "https://commons.wikimedia.org/wiki/File:Arepa_de_huevo.jpg", "CC BY 3.0 photograph; resized for this site.")],
    "venezuela", "Reina Pepiada")
(ROOT / URLS["colombia"]).write_text(colombia, encoding="utf-8")


venezuela = recipe_page(
    "venezuela", "Reina Pepiada", "Venezuela / Caracas, 1955",
    "A warm griddled arepa becomes a pocket for chicken and avocado. The Álvarez family’s Caracas creation acquired its name after Susana Duijm won Miss World in 1955. This is a modern home version, not an exact replica of the shop’s original dough.",
    ["Makes 4", "About 40 minutes", "Griddled · chicken & avocado"], "reina-pepiada.webp",
    "Venezuelan arepas filled with chicken and avocado on a table",
    'Photograph: <a href="https://commons.wikimedia.org/wiki/File:MyPlate_gov_Cultural_Food_(20241025-USDA-FNS-UNK-0024).jpg" target="_blank" rel="noopener noreferrer">USDA Food and Nutrition Service / Wikimedia Commons</a>, U.S. government public domain. Cropped and resized for this site.',
    [("For four arepas", ["2 cups (about 290 g) precooked maize flour", "2¼ cups (about 510 ml) warm water", "1 tsp salt", "2 tbsp oil, divided"]),
     ("Chicken and avocado filling", ["300 g cooked, shredded chicken", "1 ripe avocado (about 300 g)", "3 tbsp mayonnaise", "1 tbsp lemon juice", "1 small garlic clove, crushed", "1 small onion, finely chopped", "2 cilantro sprigs, chopped", "1 tbsp olive oil", "Salt to taste"]),
     ("Optional historical nod", ["A spoonful of cooked green peas per serving"])],
    [("Make the dough", "Stir salt and 1 tablespoon oil into the warm water. Gradually work in the precooked maize flour until smooth and pliable. Rest a few minutes, then divide into 4 equal balls and flatten into thick discs."),
     ("Griddle", "Brush a skillet with the remaining oil. Cook the discs over medium heat, covered, about 5 minutes on each side, until a crust forms and the centers are cooked. Rest briefly."),
     ("Mix the filling", "Reserve a quarter of the avocado as slices. Mash the rest with mayonnaise and lemon. Fold in the cooked chicken, onion, garlic, cilantro, olive oil, and salt. Taste and adjust."),
     ("Open and serve", "Split the warm arepas to make pockets. Spoon in the filling and add avocado slices. Add cooked peas if you want a nod to the early Álvarez version.")],
    '<strong>Original and adaptation</strong><p>A published interview with an Álvarez family descendant documents chicken, avocado, mayonnaise, mustard, Worcestershire sauce, ají dulce, and a green-pea garnish in the early filling. The family ground maize for its dough. This cookable version adapts Jani Díaz’s recipe with precooked flour and consistently makes four arepas. It does not claim to recreate every 1955 ingredient. <a href="#sources">See sources</a>.</p>',
    [("Álvarez family account · Arepas Around the World, p. 37", "https://historiadelaarepa.com/downloads/arepas-around-the-world%28en%29.pdf", "Interview-based account of the shop, original filling, name, and whole-maize preparation."),
     ("Jani Díaz · Arepa Reina Pepiada", "https://www.laylita.com/recetas/arepa-reina-pepiada/", "Quantities and technique behind this practical home adaptation. Its published yield and dough division disagree; four are used consistently here."),
     ("USDA Food and Nutrition Service · Reina Pepiada photograph", "https://commons.wikimedia.org/wiki/File:MyPlate_gov_Cultural_Food_(20241025-USDA-FNS-UNK-0024).jpg", "U.S. government public-domain image; resized for this site.")],
    "ancestral", "Whole-maize cake")
(ROOT / URLS["venezuela"]).write_text(venezuela, encoding="utf-8")


ancestral = recipe_page(
    "ancestral", "Whole-maize cake on a griddle", "Indigenous inheritance / evidence-based reconstruction",
    "A simple, flat cake made from cooked whole maize, water, and a hot surface. Early descriptions from northern South America record stone-ground maize dough and round griddled cakes. The measurements and timings below are modern choices—not a recovered preconquest recipe.",
    ["Makes 4 small cakes", "Overnight soak + about 2 hours", "Whole grain · griddled"], "metate.webp",
    "Grinding stone and handstone from San Agustín, Colombia, displayed in a museum",
    'Grinding stones from San Agustín, Colombia: <a href="https://commons.wikimedia.org/wiki/File:Metate_y_mano_de_moler_encontrados_en_San_Agustin_Huila.jpg" target="_blank" rel="noopener noreferrer">Fecive / Wikimedia Commons</a>, CC0. Photograph resized; this object is illustrative, not evidence it was used for the exact cake below.',
    [("Minimal ingredients", ["1 cup dried whole maize kernels (field corn, white or yellow; not popcorn)", "Water for soaking and simmering", "A few tablespoons of warm water if the ground dough needs it"]),
     ("Equipment", ["A stone grinder or food processor", "A griddle or seasoned skillet (a kitchen substitute for a clay budare)"])],
    [("Soak", "Cover the dry whole maize generously with water and soak overnight. Drain. This soak is a modern practical step; it is not specified in the contact-era descriptions."),
     ("Cook and grind", "Simmer in fresh water until the kernels are fully tender, roughly 60–90 minutes depending on the maize. Drain and grind while warm to a cohesive, slightly coarse dough. Add warm water a spoonful at a time only if needed."),
     ("Shape", "Divide into 4 and pat into round cakes about 1 cm thick. Keep edges together with damp hands. No salt, cheese, or packaged flour is required for this deliberately spare version."),
     ("Griddle", "Cook on a hot seasoned griddle over medium heat, turning until both faces have browned and the centers are hot and set, roughly 6–8 minutes a side. Serve warm.")],
    '<strong>What can we actually trace?</strong><p>Oviedo’s 1526 account describes wet stone-grinding and leaf-roasted maize dough in Tierra Firme; that bread was a <em>bollo</em>, not explicitly a flat arepa. Galeotto Cey’s 1539–1553 account describes thick round cakes turned on a greased griddle. A Venezuelan cultural account describes cooked maize ground between stones and shaped on a clay <em>budare</em>. These are related observations, not a single intact ancient recipe. The exact sequence and quantities above are editorial reconstruction. <a href="#sources">See sources</a>.</p>',
    [("Gonzalo Fernández de Oviedo · Sumario, ch. IV (1526)", "https://www.biblioteca-antologica.org/es/wp-content/uploads/2018/03/FERNANDEZ-DE-OVIEDO-Sumario-de-la-Natural-Historia-de-las-Indias.pdf", "Contact-era description of Indigenous wet grinding and leaf-roasted maize bread; a related form, not this flat cake."),
     ("Galeotto Cey · 1539–1553 passage via IberCultura Viva", "https://iberculturaviva.org/es/sabores-migrantes-2021-mildred-najera-najera-y-las-arepas-de-maiz-cariaco-morado/", "Published transcription of thick round maize cakes cooked on both sides on a griddle."),
     ("Venezuela Ministry of Culture · La arepa y sus variantes", "https://www.mincultura.gob.ve/noticias/la-arepa-y-sus-variantes-en-el-territorio-venezolano/", "Describes cooked maize, stone grinding, and a clay aripo or budare."),
     ("Fecive · Grinding stones, San Agustín", "https://commons.wikimedia.org/wiki/File:Metate_y_mano_de_moler_encontrados_en_San_Agustin_Huila.jpg", "CC0 photograph; illustrative object, not a claim about the specific cakes in this recipe.")],
    "history", "How the cakes changed")
(ROOT / URLS["ancestral"]).write_text(ancestral, encoding="utf-8")


from history_page import build_history
from plain_page import build_plain_page
from native_page import build_native_page

(ROOT / URLS["history"]).write_text(build_history(document, sources), encoding="utf-8")
(ROOT / URLS["plain"]).write_text(build_plain_page(document, sources), encoding="utf-8")
(ROOT / URLS["native"]).write_text(build_native_page(document, sources), encoding="utf-8")

print("Built:", ", ".join(str(p.relative_to(ROOT)) for p in sorted(ROOT.glob("*.html"))))
