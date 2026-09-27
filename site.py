"""Build the five-page, dependency-free Maíz editorial site.

Run `python site.py` after changing page content. Generated HTML lives in dist/.
"""

from pathlib import Path
from html import escape

ROOT = Path(__file__).parent / "dist"
ROOT.mkdir(exist_ok=True)

URLS = {
    "colombia": "colombia.html",
    "venezuela": "venezuela.html",
    "ancestral": "ancestral.html",
    "history": "history.html",
}


def header(active="overview"):
    links = [("overview", "Overview", "index.html"), ("colombia", "Colombia", URLS["colombia"]),
             ("venezuela", "Venezuela", URLS["venezuela"]), ("ancestral", "Ancestral cake", URLS["ancestral"]),
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
      <span>Maíz · Three recipes and their shared history</span><span><a href="index.html">Overview</a> · <a href="history.html">Evidence &amp; sources</a></span>
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
    body = f'''<section class="detail-intro wrap"><a class="breadcrumb" href="index.html">← All four stories</a>
      <div class="eyebrow">{kicker}</div><h1>{title}</h1><p class="dek">{dek}</p><div class="pills">{pill_html}</div></section>
      {picture(file, alt, caption)}
      <div class="wrap recipe-layout"><aside class="ingredients"><h2>Ingredients</h2>{ing_html}</aside>
      <section class="method"><span class="eyebrow">Cook it</span><h2>Method</h2><ol class="steps">{steps_html}</ol>
      <div class="callout">{callout}</div></section></div>
      {sources(refs)}<nav class="wrap next-links" aria-label="More Maíz pages"><a href="index.html">← Back to overview</a><a href="{URLS[next_key]}">Next: {next_title} →</a></nav>'''
    return document(title, dek, body, key)


overview = '''<section class="hero"><div class="wrap hero-inner"><div><span class="eyebrow" style="color:var(--maize)">A maize inheritance</span>
  <h1>One grain.<br>Many kitchens.</h1><p class="lead">Meet three very different corn cakes, then follow the evidence of how Indigenous maize traditions, colonial contact, migration, and modern kitchens shaped the arepas we know.</p>
  <a class="jump" href="#explore">Explore the recipes ↓</a></div><div class="hero-side"><strong>Read the evidence with the food.</strong>
  <p>The ancient cake is a reconstruction. The Colombian and Venezuelan recipes are documented modern expressions. Each page links to its sources.</p></div></div></section>
  <section class="section" id="explore"><div class="wrap"><div class="section-head"><div><span class="eyebrow">The table</span><h2>Three cakes, three moments</h2></div>
  <p>Begin with a dish or start before the present borders. Every card opens a full recipe with context and source notes.</p></div>
  <div class="grid">
   <a class="feature" href="ancestral.html"><img src="assets/metate.webp" alt="Two maize grinding stones displayed in San Agustín, Colombia" loading="eager"><div class="body"><span class="label">Before modern nations · reconstruction</span><h3>Whole maize on a griddle</h3><p>A cookable interpretation of Indigenous maize processing described in sixteenth-century accounts.</p><span class="read">Read the ancestral cake ↗</span></div></a>
   <a class="feature" href="colombia.html"><img src="assets/arepa-de-huevo.webp" alt="A group of golden fried arepas de huevo" loading="eager"><div class="body"><span class="label">Colombia · Luruaco, Atlántico</span><h3>Arepa’e huevo</h3><p>The Caribbean coast’s puffed, fried maize pocket with an egg inside.</p><span class="read">Cook the Colombian arepa ↗</span></div></a>
   <a class="feature" href="venezuela.html"><img src="assets/reina-pepiada.webp" alt="Chicken and avocado filled Venezuelan arepas" loading="eager"><div class="body"><span class="label">Venezuela · Caracas</span><h3>Reina Pepiada</h3><p>A griddled arepa filled with chicken and avocado, named in the 1950s.</p><span class="read">Cook the Venezuelan arepa ↗</span></div></a>
  </div><a class="history-band" href="history.html"><div><span class="eyebrow">The fourth story</span><h2>How the cake traveled and changed</h2></div>
  <p>Follow maize through Indigenous exchange, read the first surviving descriptions of arepas, and see how new ingredients and migration shaped regional identities. <strong>Read the history ↗</strong></p></a></div></section>'''
(ROOT / "index.html").write_text(document("Overview", "Three sourced corn-cake recipes and an evidence-led history of arepas in Colombia and Venezuela.", overview), encoding="utf-8")


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


history_refs = [
    ("Matsuoka et al. · maize domestication genetics (2002)", "https://doi.org/10.1073/pnas.052125199", "Genetic comparison of maize and teosinte identifies the Balsas region of southwestern Mexico as the principal domestication origin, around 9,000 years ago."),
    ("Piperno et al. · Xihuatoxtla, Mexico (2009)", "https://repository.si.edu/items/0cedfac1-0d93-4b11-8573-de64560518d3", "Starch on tools and maize phytoliths in deposits place maize in the Central Balsas by about 8,700 cal BP."),
    ("Dickau, Ranere & Cooke · Panama (2007)", "https://repository.si.edu/items/6f64557a-1132-4520-91b5-06acf79fb7ba", "Maize starch on stone tools in central Pacific Panama by 7,800–7,000 cal BP, with local roots and other plants; proposed exchange of planting material."),
    ("Pagán-Jiménez et al. · southern Caribbean (2015)", "https://www.sciencedirect.com/science/article/pii/S0277379115300445", "Starch residues on grinding stones at St. John, Trinidad, in a site sequence reaching at least 7,790 cal BP; the proposed coastal dispersal path remains a hypothesis."),
    ("Aceituno & Loaiza · Middle Cauca (2014)", "https://doi.org/10.1016/j.quascirev.2013.12.013", "Early maize starch reported on Colombian grinding tools from dated archaeological contexts; this is not a directly dated maize cob or an arrival date."),
    ("Kistler et al. · South American maize genomes (2018)", "https://wrap.warwick.ac.uk/id/eprint/110238/", "Genomic model places movement into South America around 6,500 BP and finds further improvement and multiple dispersal waves there; chronology differs from some early microfossil reports."),
    ("Archila et al. · Checua, Colombia (2021)", "https://doi.org/10.1016/j.quaint.2020.07.040", "Maize starch on tools and in human dental calculus at Checua; a sampled human is directly dated to 5,720–5,600 cal BP."),
    ("Delgado · Bogotá savanna diets (2018)", "https://sedici.unlp.edu.ar/handle/10915/137548", "Carbon and nitrogen isotope study of 134 people finds a mixed C3/C4 diet around 4,000 cal BP and a clearer C4 crop, interpreted as maize, by about 3,500 cal BP."),
    ("Zucchi · western Venezuelan llanos (1973)", "https://www.cambridge.org/core/journals/american-antiquity/article/prehistoric-human-occupations-of-the-western-venezuelan-llanos/6C5B63799144F342BDC6F0662A75286A", "Excavation interprets maize farming alongside hunting and fishing at Hato de la Calzada during an occupation spanning 920 BCE–500 CE."),
    ("Jaimes et al. · Cueva La Capilla, Venezuela (2026)", "https://www.cambridge.org/core/journals/latin-american-antiquity/article/late-holocene-maize-diversity-and-cultural-remains-from-the-northern-neotropics-the-site-of-cueva-la-capilla-venezuelan-andes/8B53C5EBE29FEC7F351C163DFA4ACB7E", "Direct radiocarbon dates on maize rachises support a modeled cultural phase of 395–460 CE; distinct morphologies suggest several maize forms in use."),
    ("Perry · Middle Orinoco starch analysis (2002)", "https://ve.scielo.org/scielo.php?pid=S0378-18442002001100010&script=sci_arttext", "Maize starch on all five analyzed grater flakes from Pozo Azul Norte-1, with other plants and griddle fragments. Published radiocarbon dates for the context are uncalibrated."),
    ("Ciofalo et al. · Caribbean griddles (2019)", "https://link.springer.com/article/10.1007/s10816-019-09421-1", "Maize residues, including heat-altered starch, on clay griddles at El Flaco, Hispaniola, in a thirteenth–fifteenth-century settlement; different nearby sites used other plants."),
    ("Fernández de Oviedo · Sumario, ch. IV (1526)", "https://www.biblioteca-antologica.org/es/wp-content/uploads/2018/03/FERNANDEZ-DE-OVIEDO-Sumario-de-la-Natural-Historia-de-las-Indias.pdf", "Wet grinding and leaf-roasted maize bread described in Tierra Firme; the form is a bollo, not a documented flat arepa."),
    ("Galeotto Cey · 1539–1553 passage via IberCultura Viva", "https://iberculturaviva.org/es/sabores-migrantes-2021-mildred-najera-najera-y-las-arepas-de-maiz-cariaco-morado/", "Published transcription of thick, round maize cakes turned on a greased griddle."),
    ("RAE/ASALE · historical dictionary: arepa", "https://temporalweb.asale.org/dhle/arepa", "Cumanagoto etymology and a 1548 Riohacha judicial record, with later excerpts dated 1590 and 1653. The date is a written attestation, not an invention date."),
    ("Saldarriaga · Alimentación e identidades, ch. IV", "https://patrimonio.mincultura.gov.co/SiteAssets/Paginas/Publicaciones-biblioteca-cocinas/biblioteca%205.pdf", "Archival study, pp. 195–200, of Indigenous and Black women's maize-bread labor in colonial New Granada, Spanish adoption, and coercive production."),
    ("Colombia Ministry of Culture · Mi Atlántico SABE", "https://patrimonio.mincultura.gov.co/SiteAssets/Paginas/Publicaciones-biblioteca-cocinas/Atl%C3%A1ntico.pdf", "Luruaco egg-arepa cooking and its Indigenous and African traditions, p. 13; it does not establish one inventor."),
    ("Álvarez family account · Arepas Around the World", "https://historiadelaarepa.com/downloads/arepas-around-the-world%28en%29.pdf", "Interview-based account of the Reina Pepiada's 1955 Caracas creation and filling."),
    ("Rafael Cartay · comparative arepa study", "https://www.academiaculinaria.org/index.php/gastronomia-cocina/article/download/34/64/289?inline=1", "Regional forms and movement of Colombian egg arepas into Venezuela's Zulia."),
    ("FAO · Maize in human nutrition: Arepas", "https://www.fao.org/4/t0395e/T0395E05.htm", "Traditional processing and time saved through precooked flour, section 'Arepas'."),
]


def history_source(number, label):
    """Put the primary provenance beside each claim, not only in the bibliography."""
    return f'<a class="source-ref" href="{history_refs[number - 1][1]}" target="_blank" rel="noopener noreferrer">{label} [{number}] ↗</a>'


history = f'''<section class="history-intro"><div class="wrap detail-intro"><a class="breadcrumb" href="index.html">← All four stories</a>
  <div class="eyebrow">History / movement &amp; exchange</div><h1>How maize cakes traveled and changed</h1>
  <p class="dek">The maize in Colombian and Venezuelan arepas began with Indigenous domestication in Mexico. Archaeology and genetics trace its spread and local change across the isthmus and South America, while much later records describe the cakes. These are different kinds of evidence, with real gaps between them.</p>
  <div class="history-summary">Maize starch on a tool shows processing. A dietary signal shows consumption. A griddle can suggest a cooking practice. None alone reveals a complete preconquest arepa recipe.</div></div></section>
  <section class="wrap section"><span class="eyebrow">Three strands</span><h2>What propagated?</h2><div class="strand-grid">
  <div class="strand"><h3>The plant</h3><p>Indigenous cultivators transformed teosinte in Mexico; planting material moved through Central America, then underwent more selection in South America. {history_source(1, 'Genetic origin')} · {history_source(6, 'South American genomes')}</p></div>
  <div class="strand"><h3>Ways of preparing it</h3><p>Communities used maize beside roots and other local plants. Residues document grinding and grating; a neighboring Caribbean study identifies maize on griddles. {history_source(3, 'Panama tools')} · {history_source(11, 'Orinoco tools')} · {history_source(12, 'Caribbean griddles')}</p></div>
  <div class="strand"><h3>People and new forms</h3><p>Indigenous and Black women sustained colonial maize-bread production, often under coercion. Regional cooks and migration later shaped distinctive arepas. {history_source(16, 'Colonial labor')} · {history_source(19, 'Regional exchange')}</p></div></div></section>
  <section class="wrap history-evidence" aria-labelledby="before-1500"><div class="period-heading"><span class="eyebrow">Before the written word “arepa”</span><h2 id="before-1500">Before 1500: the evidence trail</h2>
  <p>Dates below are approximate. <strong>cal BP</strong> means calibrated years before 1950; 7,500 cal BP is about 5550 BCE, not 7500 BCE. A date may belong to an excavated layer, a human remain, or a maize fragment, and those distinctions matter.</p></div>
  <div class="timeline" aria-label="Pre-1500 evidence timeline">
   <article class="timeline-entry"><div class="date">c. 7050–6750 BCE<br><small>9,000–8,700 cal BP</small></div><div><span class="evidence">Genetics + starch and phytoliths · southwestern Mexico</span><h3>Maize begins in the Balsas region</h3><p>Genetic comparison links cultivated maize to Balsas teosinte (<em>Zea mays</em> ssp. <em>parviglumis</em>). This was a long process of Indigenous selection, beginning around 9,000 years ago. At Xihuatoxtla in the Central Balsas, maize starch on tools and maize phytoliths in deposits document use by about 8,700 cal BP.</p><p class="evidence-limit">This is maize’s origin and an early archaeological anchor—not a date for a flat cake.</p><div class="provenance">Provenance: {history_source(1, 'Matsuoka et al.')} · {history_source(2, 'Piperno et al.')}</div></div></article>
   <article class="timeline-entry"><div class="date">c. 5850–5050 BCE<br><small>7,800–7,000 cal BP</small></div><div><span class="evidence">Starch on tools · Panama and southern Caribbean</span><h3>Maize travels with other plants</h3><p>Maize starch on stone tools in central Pacific Panama belongs to contexts dated 7,800–7,000 cal BP; western Panamanian sites also yield maize and root-crop starch in later overlapping contexts. Grinding stones at St. John, Trinidad, preserve maize in a plant-use sequence reaching at least 7,790 cal BP. The Panama study suggests exchange of planting material, and the Trinidad authors consider coastal movement.</p><p class="evidence-limit">The sites show early processing at more than one location. They do not trace one continuous journey or identify a maize cake.</p><div class="provenance">Provenance: {history_source(3, 'Dickau et al.')} · {history_source(4, 'Pagán-Jiménez et al.')}</div></div></article>
   <article class="timeline-entry"><div class="date">Early Colombian reports<br><small>c. 6050–5550 BCE contexts</small></div><div><span class="evidence">Microfossils versus genomes · Middle Cauca</span><h3>An early arrival date remains contested</h3><p>Maize starch has been reported on tools at El Jazmín and La Pochola in archaeological contexts placed around 8,000–7,600 cal BP. These are dates for contexts, not direct dates on maize kernels. A later genomic reconstruction models movement into South America at roughly 6,500 BP, followed by further improvement and multiple dispersals within the continent.</p><p class="evidence-limit">Different materials and methods yield different chronologies. We cannot turn one early residue into a settled date for first arrival in Colombia.</p><div class="provenance">Provenance: {history_source(5, 'Aceituno & Loaiza')} · {history_source(6, 'Kistler et al.')}</div></div></article>
   <article class="timeline-entry"><div class="date">c. 3770–3650 BCE<br><small>5,720–5,600 cal BP</small></div><div><span class="evidence">Starch in teeth and on tools · Checua, Colombia</span><h3>Maize enters a highland foodway</h3><p>At Checua on the Bogotá savanna, researchers identified maize starch on stone tools and in human dental calculus. A sampled human from the excavation is directly dated to 5,720–5,600 cal BP. The study also identifies other plants, showing a mixed pattern of food use rather than a maize-only diet.</p><p class="evidence-limit">Starch in calculus supports consumption; it does not tell us whether the maize was eaten as a cake, drink, or another preparation.</p><div class="provenance">Provenance: {history_source(7, 'Archila et al.')}</div></div></article>
   <article class="timeline-entry"><div class="date">c. 2050–1550 BCE<br><small>4,000–3,500 cal BP</small></div><div><span class="evidence">Human dietary isotopes · Bogotá savanna</span><h3>Maize becomes more visible in diets</h3><p>Analysis of 134 people’s bone chemistry finds a shift toward mixed C3/C4 foods around 4,000 cal BP. By about 3,500 cal BP, the study sees a clearer C4 crop signal interpreted as maize. Its longer sequence suggests intensive agriculture became established later, during the last two millennia before 1950.</p><p class="evidence-limit">Isotopes describe broad diet patterns; they cannot recover the dish or its cooking method.</p><div class="provenance">Provenance: {history_source(8, 'Delgado')}</div></div></article>
   <article class="timeline-entry"><div class="date">920 BCE–500 CE<br><small>site occupation span</small></div><div><span class="evidence">Excavated farming settlement · western Venezuela</span><h3>Maize joins hunting and fishing</h3><p>At Hato de la Calzada in the western Venezuelan llanos, Zucchi interprets the Caño del Oso occupation as maize farming alongside hunting and fishing. The published 920 BCE–500 CE range describes the mound’s occupation.</p><p class="evidence-limit">The beginning of that occupation is not a directly dated first maize harvest, much less a cake.</p><div class="provenance">Provenance: {history_source(9, 'Zucchi')}</div></div></article>
   <article class="timeline-entry"><div class="date">395–460 CE<br><small>modeled phase</small></div><div><span class="evidence">Directly dated maize remains · Lara, Venezuela</span><h3>Several forms of maize are in use</h3><p>Researchers directly radiocarbon dated maize rachises from Cueva La Capilla in the Venezuelan Andes; their chronological model places the cultural event at 395–460 CE. The remains’ distinct shapes suggest multiple maize forms. They also report a masticated maize stem and plants from different environments, consistent with exchange or varied cultivation.</p><p class="evidence-limit">The dated remains prove maize was present in this context, not how its kernels were cooked.</p><div class="provenance">Provenance: {history_source(10, 'Jaimes et al.')}</div></div></article>
   <article class="timeline-entry"><div class="date">First millennium CE<br><small>uncalibrated context dates</small></div><div><span class="evidence">Starch on grater flakes · Middle Orinoco</span><h3>One tool processed several plants</h3><p>At Pozo Azul Norte-1, maize starch appeared on all five analyzed quartz grater flakes, along with starch from other plants such as arrowroot and yam. The flakes came from a context with ceramic griddle fragments; reported radiocarbon measurements center on 430, 720, and 740 CE but are <em>uncalibrated</em>.</p><p class="evidence-limit">The residues establish maize processing. They cannot establish that these griddles cooked maize, or what shape the finished food took.</p><div class="provenance">Provenance: {history_source(11, 'Perry')}</div></div></article>
   <article class="timeline-entry"><div class="date">13th–15th centuries CE<br><small>neighboring Caribbean</small></div><div><span class="evidence">Starch on clay griddles · Hispaniola</span><h3>A closer trace of maize cooking</h3><p>At El Flaco in present-day Dominican Republic, researchers found maize starch—some altered by heat—on clay griddles. Their comparison shows neighboring sites favoring different plants on similar cooking surfaces. This helps explain a varied Caribbean food network near the continental coast.</p><p class="evidence-limit">El Flaco is outside today’s Colombia and Venezuela. Even this direct cooking residue cannot identify a flat arepa recipe or prove a particular route between communities.</p><div class="provenance">Provenance: {history_source(12, 'Ciofalo et al.')}</div></div></article>
  </div><div class="history-summary history-caution"><strong>The remaining gap:</strong> no cited excavation preserves a complete pre-1500 arepa recipe. Maize presence, diet, processing, and even griddle residue become progressively closer clues; the first surviving descriptions of recognizable cakes come from the contact era below.</div></section>
  <section class="wrap history-evidence" aria-labelledby="after-1500"><div class="period-heading"><span class="eyebrow">Written accounts and reinvention</span><h2 id="after-1500">After 1500: cakes enter the record</h2></div><div class="timeline" aria-label="Written evidence timeline">
   <article class="timeline-entry"><div class="date">1526–1553</div><div><span class="evidence">Contact-era written descriptions</span><h3>Several maize breads, one regional inheritance</h3><p>Oviedo described women wet-grinding maize on stones and roasting leaf-wrapped dough in Tierra Firme. Cey later described thick round maize cakes cooked on a griddle and turned on both sides. The first is a related <em>bollo</em>; the second resembles the griddled arepa. The accounts record practices during contact, rather than a verbatim preconquest recipe.</p><div class="provenance">Provenance: {history_source(13, 'Oviedo')} · {history_source(14, 'Cey passage')}</div></div></article>
   <article class="timeline-entry"><div class="date">1548</div><div><span class="evidence">Earliest surviving word in the historical dictionary</span><h3><em>Arepa</em> appears in a Riohacha record</h3><p>A judicial account of Indigenous pearl-fishery workers’ mistreatment names the scant maize cakes given to them <em>arepas</em>. The historical dictionary derives the word from Cumanagoto <em>erepa</em>, “maize.” The record establishes written use; it cannot locate the first cook or first cake.</p><div class="provenance">Provenance: {history_source(15, 'RAE/ASALE')}</div></div></article>
   <article class="timeline-entry"><div class="date">16th–17th centuries</div><div><span class="evidence">Archival and colonial accounts</span><h3>Labor, adaptation, and regional difference</h3><p>In New Granada, Indigenous and Black women ground, kneaded, and heated maize dough while colonial demand often made their labor coercive. Spaniards adopted maize bread and introduced other ingredients and methods. Acosta wrote in 1590 that ground-maize cakes were called arepas in some places; Cobo in 1653 contrasted thinner New Spain tortillas with finger-thick arepas of Tierra Firme. These records describe multiple kitchens, not one standardized formula.</p><div class="provenance">Provenance: {history_source(16, 'Saldarriaga')} · {history_source(15, 'Historical dictionary')}</div></div></article>
   <article class="timeline-entry"><div class="date">Colonial to modern coast</div><div><span class="evidence">Regional culinary history</span><h3>Inherited forms acquire local additions</h3><p>Colombia’s Ministry of Culture places Luruaco’s egg arepa in a region shaped by Indigenous and African traditions. The association does not isolate who invented the fried pocket or egg insertion. The living dish reflects regional cooking and work over time.</p><div class="provenance">Provenance: {history_source(17, 'Colombian Ministry of Culture')}</div></div></article>
   <article class="timeline-entry"><div class="date">1950s–today</div><div><span class="evidence">Documented modern adaptation</span><h3>Stuffing, mobility, and quick maize flour</h3><p>The Álvarez family’s Reina Pepiada in Caracas layered chicken, avocado, mayonnaise, and other ingredients onto the maize cake in 1955. Comparative culinary research describes Colombian egg arepas crossing into Venezuela’s Zulia. Precooked maize flour shortened labor: FAO summarizes a change from a traditional 7–12 hours to roughly 30 minutes of preparation. These are particular, traceable changes rather than a single straight line from one country to another.</p><div class="provenance">Provenance: {history_source(18, 'Álvarez family')} · {history_source(19, 'Cartay')} · {history_source(20, 'FAO')}</div></div></article>
  </div></section>'''
history += sources(history_refs, "Every timeline entry links directly to its underlying study or historical record. Source notes identify the material dated and the limits of each inference.")
history += '<nav class="wrap next-links" aria-label="More Maíz pages"><a href="index.html">← Back to overview</a><a href="ancestral.html">Cook the reconstructed cake →</a></nav>'
(ROOT / URLS["history"]).write_text(document("How maize cakes traveled and changed", "An evidence-led history of Indigenous maize, colonial and African influences, regional recipes, and modern adaptation.", history, "history"), encoding="utf-8")

print("Built:", ", ".join(str(p.relative_to(ROOT)) for p in sorted(ROOT.glob("*.html"))))
