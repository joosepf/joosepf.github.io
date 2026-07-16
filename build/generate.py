# -*- coding: utf-8 -*-
"""Generate the bilingual portfolio: index.html + projects/<slug>.html."""
import os, html

ROOT = r"c:\Users\Lapakas\OneDrive\CV\joosepf.github.io"

def esc(s): return html.escape(s or "", quote=True)

# ---- bilingual project data (document order) --------------------------------
P = [
 dict(slug="boe-bot", draft=True,
   title_et="Boe-Bot voolumõõtja", title_en="Boe-Bot current meter",
   goal_et="Luua lihtsalt kasutatav laiendusplaat, mille saab asetada Boe-Boti peale, et mõõta erinevate komponentide voolu.",
   goal_en="Build an easy-to-use expansion board that mounts on top of the Boe-Bot to measure the current draw of its components.",
   desc_et="", desc_en="",
   tools_et=["KiCad","LTSpice"], tools_en=["KiCad","LTSpice"],
   github=None, video=None, images=[]),

 dict(slug="radiobuttons", draft=False,
   title_et="Raadionupud (RadioButtons)", title_en="Radio Buttons (RadioButtons)",
   goal_et="Luua lihtne ja mugav programm internetiraadio jaamade kuulamiseks ning nende vahel kiireks vahetamiseks.",
   goal_en="A simple, convenient app for listening to internet radio stations and switching between them quickly.",
   desc_et="Projekt sai alguse isiklikust vajadusest — soovist lihtsustada raadiojaamade kuulamist arvutis. Inspiratsiooniks olid auto raadiosüsteemid, kus jaama vahetamine käib ühe nupuvajutusega. Tulemuseks on graafilise kasutajaliidesega rakendus, kus kasutaja saab valida jaamu logode abil.",
   desc_en="The project grew out of a personal need to make listening to radio on a computer easier. The inspiration came from car radio systems, where switching stations takes a single button press. The result is a GUI application where you pick stations using their logos.",
   tools_et=["Python","PySimpleGUI","VLC"], tools_en=["Python","PySimpleGUI","VLC"],
   github="https://github.com/joosepf/RadioButtons", video=None,
   images=[("radiobuttons-1.png","RadioButtonsi peaaken raadiojaamade logodega","RadioButtons main window with station logos"),
           ("radiobuttons-2.png","RadioButtonsi liidese detail","RadioButtons interface detail")]),

 dict(slug="robot-platform", draft=True,
   title_et="Robotiplatvorm", title_en="Robot platform",
   goal_et="Luua modulaarne robotiplatvorm, millele saab lihtsalt lisada erinevaid sensoreid ja laiendusi.",
   goal_en="Create a modular robot platform to which different sensors and extensions can easily be added.",
   desc_et="Projekt sai alguse soovist arendada paindlikku ja laiendatavat roboti aluspõhja, mis oleks sobilik erinevate katsete ja projektide jaoks. Kasutatud on 3D-prinditud osi ning juhtimiseks Arduino platvormi.",
   desc_en="The project began with the wish to develop a flexible, extensible robot base suitable for a range of experiments and projects. It uses 3D-printed parts and an Arduino platform for control.",
   tools_et=["Fusion 360","3D-printimine","Arduino"], tools_en=["Fusion 360","3D printing","Arduino"],
   github=None, video=None,
   images=[("robot-platform-1.jpg","3D-prinditud modulaarne robotiplatvorm","3D-printed modular robot platform")]),

 dict(slug="phone-remote-robot", draft=True, part_of="robot-platform",
   title_et="Robot telefoni puldiga", title_en="Robot with a phone remote",
   goal_et="Kasutada telefoni güroskoopi ja muuta telefon roboti puldiks.",
   goal_en="Use a phone's gyroscope and turn the phone into the robot's remote control.",
   desc_et="Robotiplatvormi edasiarendus, mille peamine eesmärk on kasutada HC-04 Bluetooth-moodulit ning näidata selle võimekust. Antud näites kasutatakse telefoni ja selle güroskoopi, et vastavalt telefoni olekule robotit liigutada (kõrvale kallutamine = keeramine, ette/taha kallutamine = edasi/tagasi liikumine).",
   desc_en="An extension of the robot platform whose main goal is to use the HC-04 Bluetooth module and show off its capabilities. Here the phone and its gyroscope drive the robot according to the phone's orientation (tilt sideways = turn, tilt forward/back = drive forward/back).",
   tools_et=["Arduino","Bluetooth (HC-04)"], tools_en=["Arduino","Bluetooth (HC-04)"],
   github=None, video=None, images=[]),

 dict(slug="line-follower", draft=True, part_of="robot-platform",
   title_et="Joonejälgija robot", title_en="Line-following robot",
   goal_et="Luua lihtne joonejälgija roboti katsetamiseks.",
   goal_en="Build a simple line follower to experiment with the robot.",
   desc_et="Robotiplatvormi edasiarendus, mille peamine eesmärk on kasutada robotil olevaid andureid ning mootorite vahelist koostööd. Selle jaoks on koostatud lihtne joonejälgimisprogramm.",
   desc_en="An extension of the robot platform whose main goal is to use the robot's onboard sensors and the coordination between its motors. A simple line-following program was written for this.",
   tools_et=["Arduino"], tools_en=["Arduino"],
   github=None, video=None, images=[]),

 dict(slug="bt-adapter", draft=False,
   title_et="BT-adapter", title_en="BT adapter",
   goal_et="Anda vanale autole, millel on vaid kassetimängija, Bluetooth-toega muusikamängija (kasseti kujul).",
   goal_en="Give an old car that only has a cassette player a Bluetooth music player — in the shape of a cassette.",
   desc_et="Seade ühendab mitu komponenti, et pakkuda juhtmevaba muusika kuulamise kogemust. Süsteemile lisati suurem aku ja akuhaldussüsteem (BMS), mis võimaldab pikemat tööaega ja kiiremat laadimist. Korpus on disainitud ja 3D-prinditud auto sisustuse järgi.",
   desc_en="The device combines several components to deliver a wireless listening experience. A larger battery and a battery management system (BMS) were added for longer runtime and faster charging. The enclosure was designed and 3D-printed to match the car's interior.",
   tools_et=["3D-printimine","Fusion 360","elektroonika"], tools_en=["3D printing","Fusion 360","electronics"],
   github=None, video=None,
   images=[("bt-adapter-1.png","BT-adapteri disain","BT adapter design"),
           ("bt-adapter-2.jpg","Bluetooth-kassett autos","Bluetooth cassette in the car"),
           ("bt-adapter-3.png","BT-adapteri sisemus","BT adapter internals"),
           ("bt-adapter-4.jpg","Valmis 3D-prinditud kassett","Finished 3D-printed cassette")]),

 dict(slug="signal-generator", draft=True,
   title_et="Arduino signaaligeneraator", title_en="Arduino signal generator",
   goal_et="Luua signaaligeneraator, kasutades Arduinot ja takistite redelit.",
   goal_en="Build a signal generator using an Arduino and a resistor ladder.",
   desc_et="", desc_en="",
   tools_et=["Arduino"], tools_en=["Arduino"],
   github=None, video=None, images=[]),

 dict(slug="prt", draft=False,
   title_et="Gümnaasiumi praktiline töö (PRT)", title_en="High-school practical project (PRT)",
   goal_et="Tutvuda erinevate auto generaatoritega ning luua õppevahend energia muundamise demonstreerimiseks.",
   goal_en="Get to know different automotive generators and build a teaching aid that demonstrates energy conversion.",
   desc_et="Töö eesmärk oli näidata mehaanilise energia muundamist elektrienergiaks. Loodi süsteem, kus jalgratta väntamine käitab generaatorit ning toidab elektritarbijat.",
   desc_en="The aim was to show the conversion of mechanical energy into electrical energy. A system was built where pedalling a bicycle drives a generator that powers an electrical load.",
   tools_et=["elektroonika","3D-printimine ja disain","puutöö"], tools_en=["electronics","3D printing & design","woodworking"],
   github=None, video=None,
   images=[("prt-1.png","Energia muundamise õppevahendi skeem","Energy-conversion teaching-aid diagram"),
           ("prt-2.jpg","Jalgrattaga käitatav generaator","Bicycle-driven generator")]),

 dict(slug="nameexporter", draft=True,
   title_et="KJU (NameExporter)", title_en="KJU (NameExporter)",
   goal_et="Luua õppejõule tarkvaraline lahendus, mis töötleb Moodle'ist saadud tudengite nimekirju ning esitab need soovitud vormingus.",
   goal_en="Create a software tool for a lecturer that processes student lists exported from Moodle and outputs them in the desired format.",
   desc_et="„Tarkvaraprojekti“ kursuse raames loodud tööriist, mis loeb Moodle'i HTML-ist välja vajalikud andmed ning genereerib Exceli- või tekstivormingus nimekirjad. Graafiline liides on loodud GTK4 raamistikus. Minu vastutusalaks oli graafiline liides ja vigade parandamine.",
   desc_en="A tool built for the “Software Project” course that parses the needed data out of Moodle HTML and generates lists in Excel or text format. The GUI is built with the GTK4 framework. My responsibility was the GUI and bug fixing.",
   tools_et=["C","GTK4"], tools_en=["C","GTK4"],
   github="https://github.com/joosepf/NameExporter", video="https://youtu.be/we7dx5EpgHk",
   images=[("nameexporter-1.png","NameExporteri GTK4 liides","NameExporter GTK4 interface")]),

 dict(slug="trafficbot", draft=False,
   title_et="Liiklusrobot (TrafficBot)", title_en="Traffic robot (TrafficBot)",
   goal_et="Luua liiklusrobot, mis reageerib valgusfoori signaalidele, mis omakorda reageerivad liikluse hulgale.",
   goal_en="Build a traffic robot that reacts to traffic-light signals, which in turn react to the amount of traffic.",
   desc_et="Aine „Erialatutvustus“ raames loodud projekt, kus robot (Boe-Bot) jälgib fooritulesid ja käitub vastavalt (nt sõidab või peatub). Foor reageerib samuti keskkonnale, hoides peateel rohelist tuld, kuni kõrvalteele läheneb sõiduk. Minu vastutusalaks oli robot ja prinditud detailid.",
   desc_en="A project built for the “Introduction to the Field” course where a robot (Boe-Bot) watches the traffic lights and behaves accordingly (e.g. drives or stops). The light also responds to its environment, keeping the main road green until a vehicle approaches on the side road. My responsibility was the robot and the printed parts.",
   tools_et=["Arduino","3D-printimine ja disain"], tools_en=["Arduino","3D printing & design"],
   github="https://github.com/joosepf/TrafficBot", video="https://youtu.be/CH5EGiugwXg",
   images=[("trafficbot-1.jpg","Boe-Bot ja valgusfoor","Boe-Bot and the traffic light"),
           ("trafficbot-2.jpg","Liiklusroboti seadistus","Traffic-robot setup")]),

 dict(slug="movement-controller", draft=True,
   title_et="Liikumist toetav mängupult", title_en="Movement-based game controller",
   goal_et="Luua mängupult, mis sunnib mängijat liikuma.",
   goal_en="Create a game controller that forces the player to move.",
   desc_et="Projekt ühendab Wii-puldi ja kõndimismasina, et mängija peaks mängusisese liikumise ja tegevuse jaoks füüsiliselt liikuma. Arduino jälgib liikumist ja edastab info arvutisse, kus Python saadab liigutused mängu.",
   desc_en="The project combines a Wii remote and a treadmill so the player has to physically move for in-game movement and actions. An Arduino tracks the motion and sends the data to a computer, where Python passes the movements on to the game.",
   tools_et=["Python","Arduino"], tools_en=["Python","Arduino"],
   github=None, video=None, images=[]),

 dict(slug="flight-sim-controller", draft=True,
   title_et="Lennusimulaatori kontroller", title_en="Flight-simulator controller",
   goal_et="Luua soodne ja funktsionaalne lennusimulaatori juhtpult.",
   goal_en="Build an affordable, functional flight-simulator control panel.",
   desc_et="Juhtpult koosneb lihtsatest materjalidest (papp, puit) ning erinevatest sensoritest ja komponentidest. Kõik andurid on ühendatud Arduino külge ning info saadetakse Python-programmi kaudu simulaatorile. Minu vastutusalaks oli elektroonika ühendamine ja selle programmeerimine.",
   desc_en="The panel is made from simple materials (cardboard, wood) and a variety of sensors and components. All the sensors connect to an Arduino and are forwarded to the simulator through a Python program. My responsibility was wiring up and programming the electronics.",
   tools_et=["puutöö","Python","Arduino"], tools_en=["woodworking","Python","Arduino"],
   github=None, video=None, images=[]),

 dict(slug="watch-winder", draft=True,
   title_et="Kellalaadija", title_en="Watch winder",
   goal_et="Luua mehaanilisele kellale laadimisseade, et vältida selle pidevat kandmist.",
   goal_en="Create a winding device for a mechanical watch so it doesn't have to be worn constantly.",
   desc_et="Disainitud ja 3D-prinditud laadija, mis kasutab kella liikumise simuleerimiseks samm-mootorit. Sobib automaat- ja mehaanilistele käekelladele.",
   desc_en="A designed and 3D-printed winder that uses a stepper motor to simulate the watch's motion. Suitable for automatic and mechanical wristwatches.",
   tools_et=["Arduino","3D-printimine ja disain","elektroonika"], tools_en=["Arduino","3D printing & design","electronics"],
   github=None, video=None,
   images=[("watch-winder-1.jpg","3D-prinditud kellalaadija","3D-printed watch winder")]),

 dict(slug="film-warehouse", draft=True,
   title_et="Filmiladu", title_en="Film warehouse",
   goal_et="Luua lihtne andmebaasisüsteem filmide ja arvustuste haldamiseks.",
   goal_en="Build a simple database system for managing films and reviews.",
   desc_et="„Programmeerimine II“ kursuse raames loodud projekt, mis võimaldab kasutajal tekstipõhises keskkonnas filme lisada, hallata ja hinnata.",
   desc_en="A project built for the “Programming II” course that lets the user add, manage and rate films in a text-based environment.",
   tools_et=["C"], tools_en=["C"],
   github=None, video=None, images=[]),

 dict(slug="sales-calculator", draft=True,
   title_et="Müügitulemuste kalkulaator", title_en="Sales-results calculator",
   goal_et="Analüüsida müügiandmeid ja väljastada tulemused tekstina.",
   goal_en="Analyse sales data and output the results as text.",
   desc_et="Programmi sisendiks on erinevate müüjate andmed, mille põhjal arvutatakse igaühe müügitulemused ja statistika. Loodud aine „Programmeerimine I“ raames.",
   desc_en="The program takes data from various salespeople as input and computes each one's sales results and statistics. Created for the “Programming I” course.",
   tools_et=["C"], tools_en=["C"],
   github=None, video=None,
   images=[("sales-calculator-1.png","Kalkulaatori väljund 1","Calculator output 1"),
           ("sales-calculator-2.png","Kalkulaatori väljund 2","Calculator output 2")]),

 dict(slug="psu-mod", draft=False,
   title_et="Toiteploki modifitseerimine", title_en="Power-supply modification",
   goal_et="Modifitseerida vana arvuti toiteplokki, et saada lihtsaks kasutuseks standardsed pinged.",
   goal_en="Modify an old computer power supply to provide standard voltages for easy use.",
   desc_et="Projekt sai alguse vajadusest odava ja funktsionaalse laboritoiteallika järele. Vana ATX-toiteplokk ehitati ümber nii, et sellelt saab mugavalt kätte standardsed pinged (3.3 V, 5 V, 12 V). Lisatud on banaanipesad, LED-indikaatorid ja lüliti, mis muudavad seadme kasutamise lihtsaks ja turvaliseks. Lisaks projekteeriti ja 3D-prinditi korpuse puurimisšabloon, et kõik avad ja asetused oleksid korrektsed.",
   desc_en="The project started from the need for a cheap, functional bench power supply. An old ATX supply was rebuilt so that standard voltages (3.3 V, 5 V, 12 V) are conveniently available. Banana jacks, LED indicators and a switch make the device simple and safe to use. A drilling template for the enclosure was also designed and 3D-printed so every hole and placement would be correct.",
   tools_et=["elektroonika","3D-printimine ja disain"], tools_en=["electronics","3D printing & design"],
   github=None, video=None,
   images=[("psu-mod-1.png","Ümberehitatud toiteploki korpus","Modified power-supply enclosure"),
           ("psu-mod-2.jpg","Valmis laboritoiteallikas","Finished bench power supply")]),

 dict(slug="speaker-eq", draft=False, ongoing=True,
   title_et="Kõlar ja EQ", title_en="Speaker & EQ",
   goal_et="Luua kaasaskantav kõlar võimendi, ekraani ja ekvalaiseriga.",
   goal_en="Build a portable speaker with an amplifier, a display and an equaliser.",
   desc_et="Enginaator 2025 projekti raames loodud helisüsteem, millele on plaanis lisada spetsiaalselt disainitud trükkplaat, Bluetooth-tugi ja aku.",
   desc_en="An audio system created as part of the Enginaator 2025 project, to which a custom-designed PCB, Bluetooth support and a battery are planned to be added.",
   tools_et=["elektroonika","Arduino","3D-printimine ja disain"], tools_en=["electronics","Arduino","3D printing & design"],
   github=None, video=None, images=[]),

 dict(slug="laugen-motorsport", draft=False,
   title_et="Laugen Motorsport fännitooted", title_en="Laugen Motorsport fan merchandise",
   goal_et="Luua fännitooteid Laugen Motorsporti fännidele.",
   goal_en="Create fan merchandise for Laugen Motorsport supporters.",
   desc_et="Hea sõber Aksel Laugen sõidab venna Feliksiga EHKK sarjas motokrossi ning soovisime neid toetada. Võtsin vastutuse enda peale: suhtlesin kunstnikuga ja lõime soovitud disainid, misjärel tuli suhelda erinevate tootjatega, et disainid päriselt ellu tuua. Tulemusena valmisid pusad, särgid, mütsid ja lipud.",
   desc_en="My good friend Aksel Laugen races motocross with his brother Feliks in the EHKK series, and we wanted to support them. I took charge: I worked with an artist to create the designs, then dealt with various manufacturers to bring them to life. The result — hoodies, shirts, caps and flags.",
   tools_et=["suhtlus","Excel","disain"], tools_en=["communication","Excel","design"],
   github=None, video=None,
   images=[("laugen-motorsport-1.jpg","Laugen Motorsporti fännitooted","Laugen Motorsport merchandise"),
           ("laugen-motorsport-2.jpg","Fännitoodete disain","Merchandise design")]),

 dict(slug="audi-80", draft=False,
   title_et="Audi 80 parandamine", title_en="Audi 80 restoration",
   goal_et="Hoida vana auto töökorras ja turvaline igapäevaseks kasutamiseks.",
   goal_en="Keep an old car running and safe for everyday use.",
   desc_et="Isiklik projekt, mille raames on Audi 80 hooldatud ja parandatud. Vahetatud on kütusepump, pidurisadul, salongiradiaator, mitmed sensorid ja flantsid ning tehtud ka regulaarseid hooldusi. Projekti käigus on omandatud väärtuslikke automehaanika oskusi.",
   desc_en="A personal project of maintaining and repairing an Audi 80. The fuel pump, a brake caliper, the heater core, several sensors and flanges have been replaced, and routine servicing carried out. Along the way it has taught valuable car-mechanics skills.",
   tools_et=["automehaanika"], tools_en=["car mechanics"],
   github=None, video=None, images=[]),
]

# normalise optional keys
for p in P:
    p.setdefault("ongoing", False)
    p.setdefault("part_of", None)

BYSLUG = {p["slug"]: p for p in P}
CHILDREN = {}
for p in P:
    if p["part_of"]:
        CHILDREN.setdefault(p["part_of"], []).append(p)

# ---- helpers ----------------------------------------------------------------
def t(et, en):
    """inline bilingual span pair"""
    return f'<span class="lang-et">{esc(et)}</span><span class="lang-en">{esc(en)}</span>'

def tags(tools_et, tools_en):
    if not tools_et: return ""
    et = "".join(f'<span class="tag lang-et">{esc(x)}</span>' for x in tools_et)
    en = "".join(f'<span class="tag lang-en">{esc(x)}</span>' for x in tools_en)
    return f'<div class="tags">{et}{en}</div>'

def head(title, prefix, extra_desc=""):
    return f"""<!DOCTYPE html>
<html lang="et" data-lang="et">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#2b6cb0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(extra_desc)}">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<script>try{{document.documentElement.dataset.lang=localStorage.getItem('site-lang')||'et';document.documentElement.setAttribute('lang',document.documentElement.dataset.lang)}}catch(e){{}}</script>
<link rel="stylesheet" href="{prefix}assets/portfolio.css">
</head>
<body>"""

def topbar(prefix, on_project=False):
    back = ""
    if on_project:
        back = f'<a class="back" href="{prefix}index.html">← <span class="lang-et">Kõik projektid</span><span class="lang-en">All projects</span></a>'
    nav_links = f"""
      {back}
      <a href="{prefix}index.html#projects"><span class="lang-et">Projektid</span><span class="lang-en">Projects</span></a>
      <a href="{prefix}gallery.html"><span class="lang-et">Galerii</span><span class="lang-en">Gallery</span></a>
      <a href="{prefix}docs/cv.pdf">CV</a>"""
    return f"""
<header class="topbar">
  <a class="brand" href="{prefix}index.html">Joosep Fingling</a>
  <nav>{nav_links}
    <span class="langtoggle" role="group" aria-label="Language">
      <button type="button" data-set="et" aria-label="Eesti keeles">ET</button>
      <button type="button" data-set="en" aria-label="In English">EN</button>
    </span>
  </nav>
</header>"""

def footer(prefix):
    return f"""
<footer class="wrap" style="padding-top:0;">
  <p>
    <span class="lang-et">Võta ühendust:</span><span class="lang-en">Get in touch:</span>
    <a href="mailto:joosepfi@gmail.com">joosepfi@gmail.com</a> ·
    <a href="https://github.com/joosepf">GitHub</a> ·
    <a href="https://www.linkedin.com/in/joosep-fingling-432716b1/?skipRedirect=true">LinkedIn</a>
  </p>
</footer>
<div class="lb" id="lightbox"><img src="" alt=""></div>
<script src="{prefix}assets/portfolio.js"></script>
</body>
</html>"""

# ---- home page --------------------------------------------------------------
def card(p):
    thumb_img = p["images"][0][0] if p["images"] else None
    if thumb_img:
        alt = p["images"][0][2]
        thumb = f'<div class="thumb"><img src="images/projects/{thumb_img}" alt="{esc(alt)}" loading="lazy"></div>'
    else:
        letter = esc(p["title_en"].lstrip("x ").strip()[:1].upper())
        thumb = f'<div class="thumb noimg"><span>{letter}</span></div>'
    badge = ""
    if p["ongoing"]:
        badge = '<span class="badge ongoing"><span class="lang-et">Käimasolev</span><span class="lang-en">In&nbsp;progress</span></span>'
    elif p["draft"]:
        badge = '<span class="badge draft"><span class="lang-et">Mustand</span><span class="lang-en">Draft</span></span>'
    return f"""    <a class="card" href="projects/{p['slug']}.html">
      {badge}{thumb}
      <div class="body">
        <h3>{t(p['title_et'], p['title_en'])}</h3>
        <p class="goal">{t(p['goal_et'], p['goal_en'])}</p>
        {tags(p['tools_et'], p['tools_en'])}
      </div>
    </a>"""

def build_index():
    # order: finished first, then ongoing, then drafts — keep doc order within each
    order = sorted(range(len(P)), key=lambda i: (2 if P[i]["draft"] else (1 if P[i]["ongoing"] else 0), i))
    cards = "\n".join(card(P[i]) for i in order)
    n = len(P)
    html_out = head("Joosep Fingling — Portfoolio / Portfolio", "",
                    "Joosep Fingling — electronics, robotics, 3D printing and software projects.")
    html_out += topbar("", on_project=False)
    html_out += f"""
<main class="wrap">
  <section class="masthead">
    <p class="eyebrow"><span class="lang-et">Portfoolio</span><span class="lang-en">Portfolio</span></p>
    <h1>Joosep Fingling</h1>
    <p class="tagline">
      <span class="lang-et">Valik minu projekte — elektroonika, robootika, 3D-printimine, tarkvara ja rohkelt praktilist meisterdamist.</span>
      <span class="lang-en">A selection of my projects — electronics, robotics, 3D printing, software, and plenty of hands-on building.</span>
    </p>
  </section>

  <section id="projects">
    <h2 class="seclabel">
      <span class="lang-et">Projektid</span><span class="lang-en">Projects</span>
      <span class="count">{n}</span>
    </h2>
    <div class="grid">
{cards}
    </div>
  </section>
</main>
"""
    html_out += footer("")
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_out)

# ---- project pages ----------------------------------------------------------
def build_project(p):
    prefix = "../"
    title = f"{p['title_et']} — Joosep Fingling"
    out = head(title, prefix, p["goal_en"])
    out += topbar(prefix, on_project=True)

    # badges / pills
    pills = ""
    if p["ongoing"]:
        pills = '<span class="pill ongoing"><span class="lang-et">Käimasolev</span><span class="lang-en">In progress</span></span>'
    elif p["draft"]:
        pills = '<span class="pill draft"><span class="lang-et">Mustand</span><span class="lang-en">Draft</span></span>'

    # part-of link
    partof = ""
    if p["part_of"]:
        par = BYSLUG[p["part_of"]]
        partof = (f'<span><span class="lang-et">Osa projektist:</span><span class="lang-en">Part of:</span> '
                  f'<a href="{par["slug"]}.html" style="color:var(--accent)">{t(par["title_et"], par["title_en"])}</a></span>')

    kicker_bits = []
    if pills: kicker_bits.append(pills)
    if partof: kicker_bits.append(partof)
    kicker = f'<p class="kicker">{"".join(kicker_bits)}</p>' if kicker_bits else ""

    out += f"""
<main class="wrap narrow">
  <div class="proj-head">
    {kicker}
    <h1>{t(p['title_et'], p['title_en'])}</h1>
    {tags(p['tools_et'], p['tools_en'])}
  </div>

  <div class="field lead">
    <h2><span class="lang-et">Eesmärk</span><span class="lang-en">Goal</span></h2>
    <p class="lang-et">{esc(p['goal_et'])}</p>
    <p class="lang-en">{esc(p['goal_en'])}</p>
  </div>
"""
    # description (optional)
    if p["desc_et"] or p["desc_en"]:
        out += f"""
  <div class="field">
    <h2><span class="lang-et">Kirjeldus</span><span class="lang-en">Description</span></h2>
    <p class="lang-et">{esc(p['desc_et'])}</p>
    <p class="lang-en">{esc(p['desc_en'])}</p>
  </div>
"""
    # links
    link_items = []
    if p["github"]:
        link_items.append(f'<li><a href="{esc(p["github"])}" target="_blank" rel="noopener">GitHub <span class="mono">↗</span></a></li>')
    if p["video"]:
        link_items.append(f'<li><a href="{esc(p["video"])}" target="_blank" rel="noopener">Video <span class="mono">↗</span></a></li>')
    if link_items:
        out += f'\n  <ul class="links">\n    ' + "\n    ".join(link_items) + "\n  </ul>\n"

    # related children (for robot-platform)
    kids = CHILDREN.get(p["slug"], [])
    if kids:
        rel = "".join(
            f'<a href="{k["slug"]}.html">{t(k["title_et"], k["title_en"])} →</a>' for k in kids)
        out += f"""
  <div class="field" style="margin-top:2rem;">
    <h2><span class="lang-et">Edasiarendused</span><span class="lang-en">Extensions</span></h2>
    <div class="related">{rel}</div>
  </div>
"""

    # image gallery
    if p["images"]:
        figs = "\n".join(
            f'      <figure><img src="../images/projects/{fn}" alt="{esc(alt_en)}" loading="lazy"></figure>'
            for (fn, alt_et, alt_en) in p["images"])
        out += f"""
  <section style="margin-top:2.4rem;">
    <h2 class="seclabel"><span class="lang-et">Pildid</span><span class="lang-en">Images</span></h2>
    <div class="gallery">
{figs}
    </div>
  </section>
"""
    out += "</main>\n"
    out += footer(prefix)
    projdir = os.path.join(ROOT, "projects")
    os.makedirs(projdir, exist_ok=True)
    with open(os.path.join(projdir, p["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(out)

# ---- gallery ----------------------------------------------------------------
def build_gallery():
    order = sorted(range(len(P)), key=lambda i: (2 if P[i]["draft"] else (1 if P[i]["ongoing"] else 0), i))
    figs = []
    for i in order:
        p = P[i]
        for (fn, alt_et, alt_en) in p["images"]:
            cap = (f'<figcaption><a href="projects/{p["slug"]}.html">'
                   f'{t(p["title_et"], p["title_en"])}</a></figcaption>')
            figs.append(
                f'    <figure><img src="images/projects/{fn}" alt="{esc(alt_en)}" loading="lazy">{cap}</figure>')
    figs_html = "\n".join(figs)
    out = head("Galerii / Gallery — Joosep Fingling", "",
               "A visual gallery of Joosep Fingling's projects.")
    out += topbar("", on_project=False)
    out += f"""
<main class="wrap">
  <section class="masthead" style="margin-bottom:2rem;">
    <p class="eyebrow"><span class="lang-et">Galerii</span><span class="lang-en">Gallery</span></p>
    <h1><span class="lang-et">Galerii</span><span class="lang-en">Gallery</span></h1>
    <p class="tagline">
      <span class="lang-et">Pildid tehtud töödest — klõpsa pildil suurendamiseks.</span>
      <span class="lang-en">Photos of finished work — click any image to enlarge.</span>
    </p>
  </section>
  <div class="gallery gallery-page">
{figs_html}
  </div>
</main>
"""
    out += footer("")
    with open(os.path.join(ROOT, "gallery.html"), "w", encoding="utf-8") as f:
        f.write(out)

# ---- run --------------------------------------------------------------------
build_index()
for p in P:
    build_project(p)
build_gallery()
print("Generated index.html, gallery.html and", len(P), "project pages.")
