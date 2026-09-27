"""Indigenous maize-cake recipes with their evidence boundaries."""


def build_native_page(document, sources):
    zenu = "https://www.swissaid.org.co/wp-content/uploads/2022/05/cartilla-zenu-semillas.pdf"
    zenu_context = "https://www.semillas.org.co/es/publicaciones/semillas-criollas-del-pueblo-zen-recuperacin-de-la-memoria-del-territorio-y-del-conocimiento-tradicional"
    wayuu = "https://repositorio.sena.edu.co/bitstream/handle/11404/7308/cocina_ancestral_tradicional_guajira.pdf?sequence=5"
    wayuu_catalog = "https://repositorio.sena.edu.co/handle/11404/7308?show=full"
    warao = "https://www.academia.edu/35822397/Gu%C3%ADa_Pedag%C3%B3gica_para_la_Educaci%C3%B3n_Intercultural_Biling%C3%BCe_WARAO_pdf"

    body = '''<section class="wrap native-intro">
      <a class="breadcrumb" href="index.html">← Overview</a>
      <div class="native-opening"><div><span class="eyebrow">Indigenous cooks and community records</span>
      <h1>Corn cakes in living Indigenous kitchens</h1>
      <p class="native-lead">Two published recipes name the people and communities behind the method. Their dates tell us when the preparations were <em>documented</em>; neither publication establishes an unchanged recipe from before 1500.</p>
      <div class="native-key"><strong>How to read these cards</strong><span>Ingredients and steps are limited to what the cited records actually provide. An unspecified quantity or cooking time stays unspecified.</span></div></div>
      <figure class="native-illustration"><img src="assets/arepa-maiz-pelado.jpg" alt="Hands shaping yellow maize dough into flat rounds on leaves" loading="eager"><figcaption>Maize cakes being shaped, illustrative only: neither recipe source identifies this batch. Photograph by <a href="#source-6">Intimankiller [6]</a>.</figcaption></figure></div>
    </section>

    <section class="wrap native-recipes" aria-label="Documented Indigenous corn cake recipes">
      <article class="native-card" aria-labelledby="zenu-title">
        <div class="native-card-head"><span class="native-index">01 / Zenú</span><span class="native-record">Community publication · 2008</span></div>
        <h2 id="zenu-title">Arepa de maíz blanco asada</h2>
        <p class="native-context">Caribbean Colombia. The Zenú organization RECAR recorded this recipe in a 2001 regional maize-use collection; <em>Semillas criollas del pueblo Zenú</em> republished the table in 2008. It is not attributed to an individual cook or claimed as exclusive to one community. <a href="#source-1">[1]</a> <a href="#source-2">[2]</a></p>
        <div class="native-recipe-columns"><div><h3>Ingredients recorded</h3><ul><li>White maize</li><li>Salt</li></ul><p class="native-unspecified">Amounts are not given.</p></div>
        <div><h3>Method recorded</h3><ol><li>Pound the maize.</li><li>Cook it, then grind it.</li><li>Knead the dough and add salt.</li><li>Roast the arepa.</li></ol></div></div>
        <div class="native-limit"><strong>Extent of the record</strong><p>The original gives this sequence without soak time, grain-to-water ratio, cake dimensions, heat level, or roasting duration. “Pound” translates <em>pilar</em>; the recipe does not specify an alkaline treatment.</p></div>
        <a class="native-primary" href="https://www.swissaid.org.co/wp-content/uploads/2022/05/cartilla-zenu-semillas.pdf" target="_blank" rel="noopener noreferrer">Open the Zenú booklet, p. 45 ↗</a>
      </article>

      <article class="native-card" aria-labelledby="wayuu-title">
        <div class="native-card-head"><span class="native-index">02 / Wayúu</span><span class="native-record">Named contributor · 2021</span></div>
        <h2 id="wayuu-title">Arepa de maíz morado o chichiware</h2>
        <p class="native-context">Alta Guajira, Colombia. SENA’s culinary field publication credits Carmen Dayana Deluques Iguarán, who identifies herself as Wayúu and names her Epieyú clan. <a href="#source-3">[3]</a> <a href="#source-4">[4]</a></p>
        <div class="native-recipe-columns"><div><h3>Ingredients recorded</h3><ul><li>125 g purple highland maize</li><li>60 g criollo or coastal cheese</li><li>Salt and sugar to taste</li><li>Hot water for the rest</li></ul><p class="native-unspecified">The water amount is not given.</p></div>
        <div><h3>Method recorded</h3><ol><li>Grind the maize.</li><li>Add hot water; rest 20 minutes and remove the bran.</li><li>Grind again to make the dough.</li><li>Add cheese, salt, and sugar.</li><li>Form arepas and roast.</li></ol></div></div>
        <div class="native-limit"><strong>Extent of the record</strong><p>The book provides ingredient weights and a resting time, but no roasting duration or temperature. Cheese and sugar belong to this documented contemporary version; the source does not date this exact formula to before contact.</p></div>
        <a class="native-primary" href="https://repositorio.sena.edu.co/bitstream/handle/11404/7308/cocina_ancestral_tradicional_guajira.pdf?sequence=5" target="_blank" rel="noopener noreferrer">Open the SENA recipe, pp. 66–67 ↗</a>
      </article>
    </section>

    <section class="wrap native-boundary" aria-labelledby="warao-title"><div>
      <span class="eyebrow">Venezuela · a partial account</span><h2 id="warao-title">What the Warao guide establishes</h2>
      <p>A 2004 Venezuelan educational guide developed with Warao educators and elders describes dry maize pounded to flour and mixed with water to make dough for a <em>bollo</em> or <em>arepa</em>. It places maize among foods of “nontraditional” Warao communities. The guide does not give shaping or cooking steps, so this is a documented preparation rather than a complete recipe. <a href="#source-5">[5]</a></p>
    </div></section>

    <section class="wrap native-reading"><h2>What these sources can establish</h2><p>They document Indigenous knowledge and cooking at the time each account was made. For evidence about earlier maize use and griddled cakes, follow the <a href="history.html">separate crop and corn-cake histories</a>. The <a href="ancestral.html">whole-maize cake</a> is an explicitly modern reconstruction, not a third attested Indigenous recipe.</p></section>'''

    references = [
        ("Zenú / RECAR · Semillas criollas del pueblo Zenú (2008), p. 45", zenu,
         "Community publication. The recipe table gives white maize, salt, and the recorded sequence; its note on p. 47 credits RECAR’s 2001 regional maize-use booklet."),
        ("Pueblo Zenú / Grupo Semillas / SWISSAID · publication context", zenu_context,
         "First-person community description of the booklet’s purpose and its food and seed knowledge."),
        ("SENA · Cocina ancestral y tradicional de La Guajira A’lakajawaa (2021), pp. 66–67", wayuu,
         "Carmen Dayana Deluques Iguarán’s chichiware ingredient amounts, five preparation steps, and contributor profile."),
        ("SENA repository · book catalog and contributor credits", wayuu_catalog,
         "Publisher, issue year, and named contributor metadata for the Guajira cookbook."),
        ("Venezuela Ministry of Education and Warao contributors · Guía Pedagógica Warao (2004), pp. 145–146", warao,
         "Records the maize dough method and explicitly locates it among nontraditional Warao communities; it is not a full cake recipe."),
        ("Intimankiller · Arepa de mi tierra photograph", "https://commons.wikimedia.org/wiki/File:Arepa_de_mi_tierra.jpg",
         'Illustrative maize-cake photograph, not either documented recipe. <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer">CC BY 4.0</a>. Displayed with a responsive crop.'),
    ]
    body += sources(references, "Original publications and institutional records behind each preparation; the links also show where the documented method stops.")
    body += '''<nav class="wrap next-links" aria-label="More Maíz pages"><a href="index.html">← Back to overview</a><a href="history.html">Explore the historical evidence →</a></nav>'''
    return document("Indigenous corn-cake recipes", "Two documented Indigenous maize-cake recipes from Zenú and Wayúu sources, plus the boundaries of a Warao preparation account.", body, "native")
