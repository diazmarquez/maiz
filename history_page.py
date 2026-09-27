"""The two evidence trails behind the Maíz history page.

Keep claim-level provenance beside each timeline entry.  Dates for a layer,
person, ceramic object, and maize remain are deliberately distinguished.
"""

from html import escape


REFERENCES = [
    ("matsuoka", "Matsuoka et al. · maize domestication genetics (2002)", "https://doi.org/10.1073/pnas.052125199", "Genetic comparison of maize and teosinte places the principal domestication origin in the Balsas region of southwestern Mexico, beginning around 9,000 years ago."),
    ("piperno", "Piperno et al. · Xihuatoxtla, Mexico (2009)", "https://repository.si.edu/items/0cedfac1-0d93-4b11-8573-de64560518d3", "Maize starch on stone tools and maize phytoliths in deposits in the Central Balsas by about 8,700 cal BP."),
    ("aceituno", "Aceituno & Loaiza · Middle Cauca (2014)", "https://doi.org/10.1016/j.quascirev.2013.12.013", "Reports maize starch on grinding tools from El Jazmín and La Pochola in early dated contexts. The maize particles themselves were not radiocarbon dated."),
    ("cauca_dates", "Dickau et al. · Middle Cauca chronology (2015)", "https://doi.org/10.1016/j.quaint.2014.12.025", "Revisits the radiocarbon chronology of Middle Cauca occupations. The association between particular microfossils and dated levels requires care."),
    ("panama", "Dickau, Ranere & Cooke · Panama (2007)", "https://repository.si.edu/items/6f64557a-1132-4520-91b5-06acf79fb7ba", "Maize starch on stone tools in central Pacific Panama in contexts spanning roughly 7,800–7,000 cal BP, alongside other plants."),
    ("trinidad", "Pagán-Jiménez et al. · southern Caribbean (2015)", "https://doi.org/10.1016/j.quascirev.2015.07.005", "Maize starch on grinding stones at St. John, Trinidad, in a site sequence reaching at least 7,790 cal BP. A coastal movement route is proposed, not demonstrated end to end."),
    ("checua", "Archila et al. · Checua, Colombia (2021)", "https://doi.org/10.1016/j.quaint.2020.07.040", "Tables 1 and 6: individual 10's bone dates to 6,786–6,662 cal BP (95.4%); one maize starch grain was identified in that person's dental calculus. The grain itself was not dated."),
    ("peru", "Vallebueno-Estrada et al. · ancient maize from Peru (2023)", "https://doi.org/10.7554/eLife.83149", "A burned maize husk/shank fragment attached to a cob from Paredones was directly dated to 6,775–6,504 cal BP; ancient genomes indicate domesticated maize in coastal Peru by then."),
    ("kistler", "Kistler et al. · South American maize genomes (2018)", "https://wrap.warwick.ac.uk/id/eprint/110238/", "Genomic model for a secondary South American improvement center and multiple dispersals, with a movement estimate around 6,500 BP. Earlier reported Middle Cauca residues and later ancient-genome interpretations complicate a single simple account."),
    ("aguazuque", "Ziegler et al. · Aguazuque dietary isotopes (2025)", "https://doi.org/10.1016/j.isci.2024.111624", "An individual's isotope value around 4,400–4,200 cal BP is consistent with C4 foods, plausibly maize; it does not establish population-wide reliance or identify the plant and dish by itself."),
    ("zucchi", "Zucchi · western Venezuelan llanos (1973)", "https://www.cambridge.org/core/journals/american-antiquity/article/prehistoric-human-occupations-of-the-western-venezuelan-llanos/6C5B63799144F342BDC6F0662A75286A", "Interprets maize farming alongside hunting and fishing at Hato de la Calzada; 920 BCE–500 CE is an occupation span, not a directly dated first maize harvest."),
    ("capilla", "Jaimes et al. · Cueva La Capilla, Venezuela (2026)", "https://www.cambridge.org/core/journals/latin-american-antiquity/article/late-holocene-maize-diversity-and-cultural-remains-from-the-northern-neotropics-the-site-of-cueva-la-capilla-venezuelan-andes/8B53C5EBE29FEC7F351C163DFA4ACB7E", "Six directly dated maize rachises underpin a modeled 395–460 CE phase. A chewed stem dates to 1450–1619 CE and was excluded as an outlier from that early model."),
    ("malambo", "Friedemann & Arocha · Malambo synthesis (1982; digital ed. 2016)", "https://siise.bibliotecanacional.gov.co/BBCC/Documents/View/284", "Herederos del jaguar y la anaconda reports flat clay budares at Malambo on the lower Magdalena around 1130 BCE and notes their ambiguous use. A cooking surface does not establish which plant or food shape was prepared on it."),
    ("saladero", "Oliver · El Saladero, lower Orinoco (2014), pp. 97–112", "https://ro.scribd.com/document/475413692/Actas-del-3er-Encuentro-Internacional-de-pdf", "Published chapter: maize starch in eight samples from six ceramic sherds, including Saladero-style budare fragments; associated charcoal supports a component around 800–500 BCE. Implausibly old food-crust dates were rejected."),
    ("saladero_dates", "Oxford ORAU · El Saladero radiocarbon register", "https://intchron.org/ref/oliver2014naa", "Independent chronological register for Oliver's charcoal measurements and rejected soot or food-crust samples; the maize residue was not directly dated."),
    ("perry", "Perry · Middle Orinoco starch analysis (2002)", "https://ve.scielo.org/scielo.php?pid=S0378-18442002001100010&script=sci_arttext", "Maize starch on five quartz grater flakes at Pozo Azul Norte-1, with other plants and associated griddle sherds. The cited context dates are uncalibrated; the griddles did not yield proven maize residue."),
    ("ciofalo", "Ciofalo et al. · Caribbean griddles (2019)", "https://link.springer.com/article/10.1007/s10816-019-09421-1", "Maize starch on clay griddles at El Flaco, Hispaniola, in a thirteenth–fifteenth-century settlement. Heat alteration and a food's final shape require cautious interpretation."),
    ("oviedo", "Fernández de Oviedo · Historia general, book VII, ch. 1 (1535)", "https://ems.kcl.ac.uk/print/e026.html", "Contact-era account of wet-ground maize dough formed as leaf-wrapped bollos and either boiled in water or roasted by embers. This is a related bread, not a documented flat arepa."),
    ("cey", "Galeotto Cey · 1539–1553 passage via IberCultura Viva", "https://iberculturaviva.org/es/sabores-migrantes-2021-mildred-najera-najera-y-las-arepas-de-maiz-cariaco-morado/", "Published transcription of thick, round maize cakes turned on a greased griddle; 1539–1553 is the span of his travels, not a precisely dated observation."),
    ("rae", "RAE/ASALE · historical dictionary: arepa", "https://temporalweb.asale.org/dhle/arepa", "Cumanagoto erepa etymology; excerpts from a 1548 Riohacha judicial file, Acosta (1590), Cobo (1653), and Alcedo (1789). Written attestations are not invention dates."),
    ("saldarriaga", "Saldarriaga · Alimentación e identidades, ch. IV", "https://patrimonio.mincultura.gov.co/SiteAssets/Paginas/Publicaciones-biblioteca-cocinas/biblioteca%205.pdf", "Archival analysis, pp. 196–203, of Indigenous and Black women's maize-bread labor in colonial New Granada, Spanish adoption, coercion, and later vending."),
    ("santa", "Serra (Fray Juan de Santa Gertrudis) · Maravillas de la naturaleza", "https://patrimonio.mincultura.gov.co/SiteAssets/Paginas/Publicaciones-biblioteca-cocinas/biblioteca%204.pdf", "Ministry of Culture anthology, p. 129: travel observations in 1757–1767 contrasting a leaf-wrapped bollo with maize dough flattened and roasted on a callana, called arepa. Manuscript written later."),
    ("ministry", "Colombia Ministry of Culture · Mi Atlántico SABE", "https://patrimonio.mincultura.gov.co/SiteAssets/Paginas/Publicaciones-biblioteca-cocinas/Atl%C3%A1ntico.pdf", "Presents the Luruaco egg arepa and traditions of the area in an illustrated cultural account, p. 13; it does not establish a dated origin or inventor."),
    ("alvarez", "Álvarez family account · Arepas Around the World", "https://historiadelaarepa.com/downloads/arepas-around-the-world%28en%29.pdf", "Interview-based account of the Reina Pepiada's 1955 Caracas creation and filling."),
    ("cartay", "Cartay · comparative arepa study", "https://academiaculinaria.org/index.php/gastronomia-cocina/article/download/34/63/288", "Documents regional forms and recent Colombian migration associated with egg arepas in Venezuela's Zulia."),
    ("polar", "Cartay · El maíz en Venezuela, chapter 8", "https://bibliofep.fundacionempresaspolar.org/media/1378248/libro-el-maiz-cap-8.pdf", "Historical synthesis, pp. 446–447, describes the 1960 commercial precooked-flour launch and changes in household preparation time; the maker's institutional perspective is identified."),
]

INDEX = {key: n for n, (key, *_) in enumerate(REFERENCES, 1)}


def cite(key, label=None):
    row = REFERENCES[INDEX[key] - 1]
    return (f'<a class="source-ref" href="{escape(row[2], quote=True)}" target="_blank" '
            f'rel="noopener noreferrer">{escape(label or row[1])} [{INDEX[key]}] ↗</a>')


def entry(date, kind, title, account, limit, keys):
    provenance = " · ".join(cite(key) for key in keys)
    return f'''<article class="timeline-entry">
      <div class="date">{date}</div><div><span class="evidence">{kind}</span>
      <h3>{title}</h3><p>{account}</p><p class="evidence-limit">{limit}</p>
      <div class="provenance">Evidence: {provenance}</div></div></article>'''


def build_history(document, sources):
    crop = [
        entry("c. 7050–6750 BCE<br><small>origin estimate ~9,000 years ago;<br>archaeology by 8,700 cal BP</small>",
              "Genetic origin + archaeological microfossils",
              "The crop begins in southwestern Mexico",
              "Indigenous cultivators selected maize from Balsas teosinte (<em>Zea mays</em> ssp. <em>parviglumis</em>) over generations. Genetic comparison places the principal domestication origin in the Balsas region around 9,000 years ago. At Xihuatoxtla, maize starch on tools and phytoliths in deposits provide an archaeological anchor by about 8,700 cal BP.",
              "The genetic estimate and archaeological context are different measures. Neither dates an arepa or a route into South America.",
              ["matsuoka", "piperno"]),
        entry("c. 6050–5650 BCE<br><small>about 8,000–7,600 cal BP</small>",
              "Maize starch in dated contexts · Middle Cauca",
              "Early Colombian reports need careful dating",
              "At El Jazmín and La Pochola in Colombia’s Middle Cauca, researchers report maize starch on grinding tools in early archaeological contexts. Their dates come from associated occupation deposits and charcoal; later chronology work examines the sequence and its associations.",
              "These are reported early occurrences, not directly dated maize kernels. A dated layer cannot establish the exact first arrival of the crop or a continuous migration path.",
              ["aceituno", "cauca_dates"]),
        entry("c. 5840–5050 BCE<br><small>7,790–7,000 cal BP</small>",
              "Maize starch on stone tools · Panama and Trinidad",
              "More than one corridor shows maize use",
              "Central Pacific Panama has maize starch on tools in contexts spanning roughly 7,800–7,000 cal BP, alongside roots and other plants. St. John, Trinidad, has maize starch on grinding stones in a sequence reaching at least 7,790 cal BP. Researchers propose exchange of planting material and possible coastal movement.",
              "The sites document use in different places; no single excavated trail joins Mexico, Panama, Colombia, and Trinidad. The proposed routes remain hypotheses.",
              ["panama", "trinidad"]),
        entry("c. 4850–4550 BCE<br><small>6,786–6,504 cal BP</small>",
              "A dated person and directly dated maize",
              "The evidence becomes more specific",
              "At Checua on the Bogotá savanna, a bone from individual 10 dates to 6,786–6,662 cal BP; one maize starch grain was found in that person’s dental calculus. At Paredones on Peru’s coast, a burned maize husk/shank fragment attached to a cob dates to 6,775–6,504 cal BP. These nearly overlapping observations use different kinds of dating.",
              "Checua dates the person, not the starch grain. The Peruvian specimen directly dates maize, but does not define the plant’s first arrival in Colombia or Venezuela.",
              ["checua", "peru"]),
        entry("Around 4550 BCE<br><small>about 6,500 BP · model estimate</small>",
              "Genomic reconstruction · South America",
              "A model of later adaptation is debated",
              "One genomic model places a major movement into South America around 6,500 BP, followed by local improvement and multiple dispersals. Reported Middle Cauca microfossils are earlier; Paredones ancient genomes suggest that maize reaching Peru was already domesticated. Models differ about where particular traits were fixed.",
              "A genetic model estimates population history. The Paredones date sits near, rather than decisively before, that model’s rounded arrival estimate. No single route or date explains every regional lineage.",
              ["kistler", "aceituno", "peru"]),
        entry("c. 2450–2250 BCE<br><small>about 4,400–4,200 cal BP</small>",
              "Human dietary isotopes · Aguazuque, Colombia",
              "An early dietary signal appears",
              "One Aguazuque person’s bone chemistry points to C4 food consumption around this time, interpreted by the researchers as likely maize. It adds a dietary clue to the changing highland food economy well before colonial descriptions.",
              "A single person does not establish population-wide reliance. C4 isotope values cannot on their own identify maize rather than every possible C4 plant, nor recover a cake, porridge, or drink.",
              ["aguazuque"]),
        entry("920 BCE–500 CE<br><small>site occupation span</small>",
              "Excavated settlement · western Venezuela",
              "Cultivation joins local foodways",
              "At Hato de la Calzada in the Venezuelan llanos, Zucchi interprets the Caño del Oso occupation as maize farming alongside hunting and fishing. This is a regional settlement account, not a claim that people abandoned other foods.",
              "The 920 BCE–500 CE range dates the occupation, not its first maize harvest or a cake.",
              ["zucchi"]),
        entry("395–460 CE<br><small>modeled early phase</small>",
              "Six directly dated maize rachises · Venezuelan Andes",
              "Several maize forms are present",
              "Six directly radiocarbon-dated maize rachises at Cueva La Capilla support a modeled 395–460 CE phase. Their differing shapes point to maize diversity. A chewed maize stem from the site dates much later, 1450–1619 CE, and the researchers exclude it as an outlier from the early model.",
              "The early maize remains establish the crop’s presence, not the way its kernels were cooked; the late stem cannot be used to describe the early phase.",
              ["capilla"]),
    ]

    cakes = [
        entry("Around 1130 BCE<br><small>reported context · lower Magdalena</small>",
              "Flat clay cooking surfaces · Malambo",
              "A budare is a clue, not a menu",
              "A Colombian archaeological synthesis reports flat clay <em>budares</em> at Malambo. Such surfaces could cook several foods and show the antiquity of a regional cooking technology.",
              "The reported surface has no demonstrated maize residue or preserved round cake. Its age is contextual, and the synthesis does not prove an arepa.",
              ["malambo"]),
        entry("c. 800–500 BCE<br><small>associated charcoal · lower Orinoco</small>",
              "Maize starch on ceramic budare fragments",
              "At El Saladero, crop and cooking surface meet",
              "Oliver recovered maize starch in eight samples from six pottery sherds, including Saladero-style <em>budare</em> fragments. Three associated wood-charcoal dates place the Saladero component roughly in 800–500 BCE. This is the strongest cited precontact regional contact between maize and a cooking surface.",
              "The starch was not directly dated. Food-crust dates were rejected as contaminated. Residue on a surface cannot tell us whether someone formed a flat cake, roasted loose kernels, or made another food.",
              ["saladero", "saladero_dates"]),
        entry("First millennium CE<br><small>context dates uncalibrated</small>",
              "Maize starch on grater flakes · Middle Orinoco",
              "Processing and griddles occur together",
              "At Pozo Azul Norte-1, maize starch appeared on all five sampled quartz grater flakes, alongside yam and arrowroot starch. Clay griddle sherds were found in the broader context. The published radiocarbon measurements center on 430, 720, and 740 CE before calibration.",
              "The maize was identified on the grater flakes, not on those griddles. Their association does not demonstrate that a maize cake was cooked there.",
              ["perry"]),
        entry("13th–15th centuries CE<br><small>Hispaniola comparison</small>",
              "Maize starch on clay griddles",
              "A neighboring Caribbean food practice",
              "At El Flaco in today’s Dominican Republic, maize starch was recovered from clay griddles; some granules were heat altered. Nearby sites show other plants on similar equipment, a reminder that Caribbean cooks used diverse ingredients.",
              "This is outside present-day Colombia and Venezuela. Heat alteration and residue do not reveal the food’s shape or prove a transmission route to either country.",
              ["ciofalo"]),
        entry("1535; travels 1539–1553<br><small>colonial written accounts</small>",
              "Observed preparation · Tierra Firme",
              "Bollos and thick griddled rounds",
              "Oviedo’s 1535 account describes Indigenous women wet-grinding maize and forming leaf-wrapped <em>bollos</em>, boiled in water or roasted by embers. Galeotto Cey, during travels from 1539 to 1553, described thick round maize cakes turned on a greased griddle. These accounts show related but distinct preparations.",
              "The writers recorded contact-era practices through colonial eyes. The leaf-wrapped bollo is not a flat arepa; Cey’s travel span is not an exact observation date or a recovered precontact recipe.",
              ["oviedo", "cey"]),
        entry("1548<br><small>judicial record · Riohacha</small>",
              "Earliest surviving dictionary attestation",
              "The word <em>arepa</em> appears in writing",
              "A Riohacha judicial file names the scant arepas rationed to Indigenous pearl divers amid coercive labor. The historical dictionary derives <em>arepa</em> from Cumanagoto <em>erepa</em>, meaning maize. The word’s origin and this documentary occurrence cross today’s national borders.",
              "The record shows the term was in use by 1548. It neither locates the first cook nor proves a one-way route from a named modern nation.",
              ["rae"]),
        entry("1590–1653<br><small>colonial accounts</small>",
              "Named cakes and unequal labor",
              "The form was never a single recipe",
              "Acosta described ground-maize cakes cooked on fire and called <em>arepas</em> in some places (1590). Cobo contrasted thinner New Spain tortillas with finger-thick Tierra Firme arepas (1653). In New Granada, Indigenous women’s maize-bread labor was often compelled; Black women also made and sold maize foods, while Spanish households adopted and altered them.",
              "Colonial labels and authors flatten local variation. These records document exchange and coercion, without assigning every technique or ingredient to one people.",
              ["rae", "saldarriaga"]),
        entry("1757–1789<br><small>travel and commercial records</small>",
              "Distinct methods and Black vendors",
              "More than one colonial arepa",
              "Serra’s observations from 1757–1767 contrast a leaf-wrapped steamed <em>bollo</em> with maize dough flattened and roasted on a <em>callana</em>, called an arepa. In 1789, Alcedo describes Black women in Cartagena selling pork-filled maize <em>empanaditas</em> called arepas. Ingredients, shapes, and commerce were changing.",
              "Serra wrote his account later; Alcedo’s filled cake is not proof of the origin of today’s Luruaco egg arepa or its frying technique.",
              ["santa", "rae", "saldarriaga"]),
        entry("1955–1960 and after<br><small>documented modern change</small>",
              "Caracas shop, regional exchange, commercial flour",
              "New fillings and faster preparation",
              "The Álvarez family’s Reina Pepiada combined chicken and avocado with the maize cake in Caracas in 1955. A regional study describes Colombian egg arepas moving into Venezuela’s Zulia. Cartay’s historical account places the commercial launch of precooked maize flour in December 1960, shortening household preparation and changing everyday access to arepas.",
              "These are specific twentieth-century developments. They do not make a modern filling, fried pocket, or industrial flour a precontact recipe; accounts of time saved depend on what preparation steps are counted.",
              ["alvarez", "cartay", "polar", "ministry"]),
    ]

    body = f'''<section class="history-intro"><div class="wrap detail-intro">
      <a class="breadcrumb" href="index.html">← Overview</a>
      <span class="eyebrow">History / two investigations</span>
      <h1>One grain. Two histories.</h1>
      <p class="dek">When and how did maize move through the region? When can we identify a cooked corn cake? The evidence answers those questions at different times. Follow each trail independently, then see where they meet.</p>
      <div class="history-summary">An early maize date is not an early arepa date. The earliest traces here come from plants, tools, people, and layers; the named cake enters surviving written records much later.</div>
    </div></section>
    <nav class="wrap track-grid" aria-label="Explore the two history trails">
      <a class="track-card" href="#crop-timeline"><span class="eyebrow">01 / Crop</span><h2>Maize across the region</h2><p>Domestication in Mexico, early movements, Colombian and Venezuelan evidence, and the dating disputes.</p><strong>Follow the crop ↓</strong></a>
      <a class="track-card" href="#cake-timeline"><span class="eyebrow">02 / Food</span><h2>Corn cake and arepa</h2><p>Cooking surfaces, residues, colonial descriptions, labor, and regional reinvention.</p><strong>Follow the cake ↓</strong></a>
    </nav>
    <section class="wrap reading-key" aria-label="How to read the dates">
      <strong>Reading the evidence</strong><p><b>cal BP</b> means calibrated years before 1950: 7,500 cal BP is about 5550 BCE. A <b>direct date</b> is measured on the object named. A <b>context date</b> belongs to associated charcoal or a layer. A <b>model</b> estimates a historical process. Written accounts date a surviving description, not an invention.</p>
    </section>
    <section class="wrap history-evidence" id="crop-timeline" aria-labelledby="crop-title">
      <div class="period-heading"><span class="eyebrow">Trail one / the plant</span><h2 id="crop-title">Maize: origin, movement, adaptation</h2>
      <p>The Balsas origin precedes the crop’s regional appearances. The sequence below separates direct maize remains from starch in dated contexts, a dated person, dietary chemistry, and genomic models. Overlapping dates do not establish a single migration route.</p></div>
      <div class="timeline" aria-label="Maize crop evidence timeline">{''.join(crop)}</div>
    </section>
    <aside class="wrap meeting-point" aria-label="Where the evidence trails meet"><div>
      <span class="eyebrow">Where the trails meet</span><h2>El Saladero, roughly 800–500 BCE</h2>
      <p>Maize starch occurs on Saladero-style ceramic <em>budare</em> fragments in the lower Orinoco. Associated charcoal dates the component. It connects the crop to a cooking surface in this region; it does not preserve a formed cake or its name. {cite("saladero", "Oliver’s analysis")} · {cite("saladero_dates", "Chronology")}</p>
    </div></aside>
    <section class="wrap history-evidence" id="cake-timeline" aria-labelledby="cake-title">
      <div class="period-heading"><span class="eyebrow">Trail two / the food</span><h2 id="cake-title">Corn cakes: surfaces, records, reinvention</h2>
      <p>Evidence for cooking equipment appears before a named arepa. Residues narrow the possibilities; colonial descriptions finally give methods and words. A gap in surviving evidence is not proof that people did not cook maize cakes during that interval.</p></div>
      <div class="timeline" aria-label="Corn cake and arepa evidence timeline">{''.join(cakes)}</div>
      <div class="history-summary history-caution"><strong>What we can conclude</strong> Indigenous people developed maize and many ways of preparing it before modern borders. Regional archaeological evidence connects maize with processing and, at El Saladero, a ceramic cooking surface. Contact-era texts describe several breads and the word <em>arepa</em>. Colonial coercion, African and Indigenous labor, local ingredients, and later mobility shaped documented forms. No cited excavation yields a complete pre-1500 recipe or a uniquely Colombian or Venezuelan first arepa.</div>
    </section>
    <section class="wrap cultural-bridge" aria-labelledby="bridge-title">
      <span class="eyebrow">Bring the trails together</span><h2 id="bridge-title">How practices crossed and changed</h2>
      <p class="bridge-intro">The crop's movement and a cake's history are related, but they are not the same route. These are the handoffs the cited record can actually support.</p>
      <div class="bridge-grid">
        <article><span>01 / Indigenous exchange</span><h3>Seed, skill, and local plants</h3><p>Maize appeared in several early regional contexts alongside roots and other foods. Archaeologists propose exchanges of planting material and coastal movement, while the finds themselves establish local use, not an unbroken itinerary. {cite("panama", "Panama")} · {cite("trinidad", "Trinidad")}</p></article>
        <article><span>02 / Colonial households and markets</span><h3>Work under unequal power</h3><p>Indigenous and Black women made maize bread for colonial households, sometimes under compulsion. By 1789 a written account names Black Cartagena vendors selling filled maize arepas. Their documented work is part of the food's history, without an invented single moment of “fusion.” {cite("saldarriaga", "Archival study")} · {cite("rae", "1789 record")}</p></article>
        <article><span>03 / Regional and industrial change</span><h3>Recipes move again</h3><p>Luruaco's egg-filled arepa, Caracas's 1955 Reina Pepiada, movement of egg arepas into Zulia, and precooked flour from 1960 show distinct later changes. Each has its own people, technique, and provenance. {cite("ministry", "Luruaco")} · {cite("alvarez", "Caracas")} · {cite("cartay", "Zulia")} · {cite("polar", "Flour")}</p></article>
      </div>
    </section>'''
    bibliography = [(name, url, note) for _, name, url, note in REFERENCES]
    body += sources(bibliography, "Every entry links to the study, archaeological report, or historical text beside its claim. Notes distinguish directly dated remains, contextual dates, models, and retrospective accounts.")
    body += '<nav class="wrap next-links" aria-label="More Maíz pages"><a href="index.html">← Back to overview</a><a href="ancestral.html">Cook the reconstructed cake →</a></nav>'
    return document("Two histories behind the arepa",
                    "Independent evidence trails for maize as a crop and corn cakes as food, from Balsas domestication through Colombia, Venezuela, colonial records, and modern forms.",
                    body, "history")
