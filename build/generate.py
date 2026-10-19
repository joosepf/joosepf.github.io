# -*- coding: utf-8 -*-
"""Generate the bilingual portfolio: index.html + projects/<slug>.html."""
import os, html, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def esc(s): return html.escape(s or "", quote=True)

# ---- homepage sections (in display order) -----------------------------------
# Each project's `group` picks its section; projects without one go to "other".
SECTIONS = [
    ("fs",     "fsprojects",    "Tudengivormel (FS Team Tallinn)", "Formula Student (FS Team Tallinn)"),
    ("other",  "projects",      "Muud projektid",                  "Other projects"),
    ("robots", "robotprojects", "Robotid",                         "Robots"),
]

# ---- bilingual project data (document order) --------------------------------
P = [
 dict(slug="fs-emc", draft=False, group="fs",
   title_et="Võistlusauto EMC-katseprogramm", title_en="Race-car EMC test programme",
   goal_et="Leida ja lahendada FS Team Tallinna elektrilise võistlusauto elektromagnetilised häired (EMI).",
   goal_en="Find and fix the electromagnetic interference (EMI) problems on FS Team Tallinn's electric race car.",
   desc_et="Septembrist 2025 kuni augustini 2026 olin FS Team Tallinna elektroonikainsener (EMC) ja vastutasin auto EMI-probleemide lahendamise eest. Muutsin EMC-töö süstemaatiliseks katseprogrammiks: iga probleem sai oma seerianumbriga katsedokumendi, prioriteedi ja katsemetoodika. Mõõtsin TDR-meetodil (R&S RTP ostsilloskoop) CAN-kaablite, jätkukohtade ja trükkplaatide diferentsiaalimpedantsi. Uue kaabli ja paremate jätkumeetodite tõttu on FEST26 CAN-juhtmestik eelmise aasta autost märksa parem. Lisaks kaardistasin auto müra, et kinnitada DCU uue asukoha sobivust, võrdlesin 3D-prinditud korpuste varjestusmeetodeid ning mõõtsin DRS-i ja jahutusmootorite juhtivuslikke emissioone.",
   desc_en="From September 2025 to August 2026 I was FS Team Tallinn's electronics engineer (EMC), responsible for solving the car's EMI problems. I turned the EMC work into a structured test programme: every problem got its own serial-numbered test document, a priority and a defined test method. I measured the differential impedance of CAN cables, splices and PCBs with TDR on an R&S RTP oscilloscope. With the new cable and better splicing, the FEST26 CAN wiring is much better than on the previous car. I also mapped the noise in the car to confirm the DCU's new location, compared shielding methods for 3D-printed enclosures, and measured conducted emissions from the DRS and the cooling motors.",
   tools_et=["EMC","TDR","CAN","Spektrianalüsaator"], tools_en=["EMC","TDR","CAN","Spectrum analyser"],
   github=None, video=None, images=[]),

 dict(slug="near-field-probes", draft=False, group="fs",
   title_et="Lähivälja sondid", title_en="Near-field probes",
   goal_et="Valmistada meeskonnale odavad lähivälja sondid, et leida auto trükkplaatidel ja juhtmestikus häirete allikad.",
   goal_en="Build low-cost in-house near-field probes so the team can locate interference sources on the car's PCBs and wiring.",
   desc_et="Müügilolevad EMC-mõõtevahendid on kallid, seega valmistasime omad (ajapuuduse tõttu olemasolevate, end tõestanud disainide põhjal). Peamine nõue oli 50 Ω impedants: rajalaiused arvutati selle järgi ja tulemust kontrolliti vektorvõrguanalüsaatoriga. Valmis kolm H-välja (H01–H03) ja kolm E-välja sondi (E01–E03), mida võrdlesin 0–1 GHz vahemikus Rohde & Schwarzi HZ-11 komplektiga, kasutades signaaliallikana meie oma kammgeneraatorit. Parimad, H01 ja E02, annavad müügilolevate sondidega väga sarnase signaalikuju, kuigi veidi madalama tundlikkusega.",
   desc_en="Commercial EMC test equipment is expensive, so we built our own (based on existing, proven designs because of time constraints). The key requirement was a 50 Ω impedance: trace widths were calculated to match and verified with a vector network analyser. Three H-field (H01–H03) and three E-field probes (E01–E03) were made, and I compared them against the Rohde & Schwarz HZ-11 set over 0–1 GHz, using our own comb generator as the signal source. The best ones, H01 and E02, give a signal shape very close to the commercial probes, at slightly lower sensitivity.",
   tools_et=["Altium Designer","EMC","VNA"], tools_en=["Altium Designer","EMC","VNA"],
   github=None, video=None, images=[]),

 dict(slug="comb-generator", draft=False, group="fs",
   title_et="Kammgeneraator", title_en="Comb generator",
   goal_et="Valmistada kammgeneraator, mis annab teadaoleva ja korratava võrdlussignaali 0–1 GHz vahemikus sondide kalibreerimiseks ja võrdlemiseks.",
   goal_en="Build a comb generator that gives a known, repeatable 0–1 GHz reference signal for calibrating and comparing the probes.",
   desc_et="Kammgeneraator tekitab ühtlaste vahedega harmoonikutest koosneva spektri. Meil on see sondide kalibreerimis- ja võrdlusseade, õige antenniga saab seda kasutada ka mürageneraatorina. Hindasin nelja lahendust: ruutsignaalil põhinevat (kristall või mikrokontroller), sammtaastumisdioodiga (SRD), laviintransistoriga ja sagedussüntesaatoriga. LTspice'i simulatsioonide ja prototüüpide põhjal jõudsid trükkplaadini ruutsignaali- ja SRD-lahendus; laviinilahendus jäi kõrvale ~100 V toitepinge ja süntesaator keerukuse tõttu. Seadmele disainisin ka SLS-prinditud korpuse.",
   desc_en="A comb generator outputs a spectrum of evenly spaced harmonics. For us it is the calibration and reference device for the probes, and with the right antenna it can also serve as a noise source. I evaluated four approaches: square-wave based (crystal or microcontroller), step-recovery diode (SRD), avalanche transistor and frequency synthesizer. Based on LTspice simulations and prototypes, the square-wave and SRD designs went on to PCB; the avalanche design was dropped because of its ~100 V supply and the synthesizer because of its complexity. I also designed its SLS-printed enclosure.",
   tools_et=["LTspice","EMC","CAD"], tools_en=["LTspice","EMC","CAD"],
   github=None, video=None, images=[]),

 dict(slug="canqueen", draft=False, group="fs",
   title_et="CANQueen", title_en="CANQueen",
   goal_et="Luua CAN-siini monitor ja saatja, mis töötab eri tootjate ja avatud lähtekoodiga CAN-adapteritega.",
   goal_en="Build a CAN bus monitor and transmitter that works with adapters from many manufacturers as well as open-source ones.",
   desc_et="Kvaser CANKingist ja CANTrace'ist inspireeritud töölauarakendus FS Team Tallinnale (Windows ja Linux). Jälgib korraga mitut CAN-kanalit, dekodeerib liiklust DBC-failide põhjal, saadab ühekordseid ja tsüklilisi sõnumeid ning toetab CAN FD-d ja riistvaralisi ajatempleid. Sisaldab ka auto ülevaatepaneeli (plaadid, aku). Töötab Kvaseri, PEAK-i, Vectori ja IXXAT-i adapterite ning avatud lähtekoodiga gs_usb- ja slcan-adapteritega, sh meie oma USB–CAN-adapteriga. Meeskonnaliikmed uuendavad seda git'i kaudu; koodi katab üle 1000 testi.",
   desc_en="A desktop app for FS Team Tallinn (Windows and Linux), inspired by Kvaser CANKing and CANTrace. It monitors several CAN channels at once, decodes traffic against DBC files, sends single-shot and cyclic messages, and supports CAN FD and hardware timestamps. It also has a car overview dashboard (boards, accumulator). It works with Kvaser, PEAK, Vector and IXXAT adapters as well as open-source gs_usb and slcan adapters, including our own USB-to-CAN adapter. Teammates update it through git, and the code is covered by over 1000 tests.",
   tools_et=["Python","PySide6","python-can","CAN FD"], tools_en=["Python","PySide6","python-can","CAN FD"],
   github=None, video=None,
   images=[("canqueen-1.png","CANQueen jälgib CAN-siini: DBC-ga dekodeeritud sõnumid ja saatmispaneel (näidis-DBC)","CANQueen monitoring a CAN bus: DBC-decoded messages and the transmit panel (demo DBC)")]),

 dict(slug="newlogconverter", draft=False, group="fs",
   title_et="NewLogConverter", title_en="NewLogConverter",
   goal_et="Teisendada Kvaseri andmelogeri mälukaardi logid (.kmf) MoTeC i2 analüüsitarkvara jaoks (.ld).",
   goal_en="Convert Kvaser data-logger memory-card logs (.kmf) into MoTeC .ld files for analysis in MoTeC i2.",
   desc_et="Meeskonna andmeanalüüsi tööriist: loeb Kvaseri .kmf-logid, dekodeerib signaalid DBC-faili abil ja kirjutab MoTeC .ld-failid, mis avanevad nii i2 Standardis kui ka i2 Pros. Valmisrakendus on olemas Windowsile ja Linuxile, nii et meeskonnaliikmed ei pea Pythonit paigaldama.",
   desc_en="A data-analysis tool for the team: it reads Kvaser .kmf logs, decodes the signals with a DBC file and writes MoTeC .ld files that open in both i2 Standard and i2 Pro. Prebuilt executables for Windows and Linux mean teammates don't need to install Python.",
   tools_et=["Python","cantools","Kvaser CANlib"], tools_en=["Python","cantools","Kvaser CANlib"],
   github=None, video=None,
   images=[("newlogconverter-1.png","NewLogConverteri põhiaken: kaustad, DBC-failid ja sessiooni nimetamine","NewLogConverter main window: folders, DBC files and session naming")]),

 dict(slug="usb-can-adapter", draft=False, group="fs",
   title_et="USB–CAN FD adapter (DIY_KVASER)", title_en="USB-to-CAN FD adapter (DIY_KVASER)",
   goal_et="Anda meeskonnale odav USB–CAN-adapter, mis töötab ilma eraldi draiverita nii Windowsis kui ka Linuxis.",
   goal_en="Give the team a low-cost USB-to-CAN adapter that works without extra drivers on both Windows and Linux.",
   desc_et="Püsivara meeskonna STM32G431-põhisele plaadile. See rakendab gs_usb/candleLighti protokolli, nii et Linuxis töötab adapter tuuma draiveriga (SocketCAN) ja Windowsis paigaldub WinUSB kaudu automaatselt. Toetab CAN 2.0 ja CAN FD-d bitikiiruse vahetusega; kontrollisin pingil Kvaser Memorator Pro vastu kõiki klassikalisi kiirusi 10 kbit/s – 1 Mbit/s ja CAN FD andmefaasi kuni 8 Mbit/s. Porditud projektist budgetcan-fw (FreeRTOS).",
   desc_en="Firmware for the team's STM32G431-based board. It implements the gs_usb/candleLight protocol, so the adapter works with the Linux kernel driver (SocketCAN) and installs itself on Windows through WinUSB. It supports CAN 2.0 and CAN FD with bit-rate switching; I verified it on the bench against a Kvaser Memorator Pro at every classic rate from 10 kbit/s to 1 Mbit/s and with CAN FD data phases up to 8 Mbit/s. Ported from budgetcan-fw (FreeRTOS).",
   tools_et=["STM32","C","FreeRTOS","CAN FD"], tools_en=["STM32","C","FreeRTOS","CAN FD"],
   github=None, video=None, images=[]),

 dict(slug="fest26-dash", draft=False, group="fs",
   title_et="FEST26 juhiekraani tarkvara", title_en="FEST26 driver-display firmware",
   goal_et="Arendada FEST26 juhiekraani tarkvara, mis näitab sõitjale auto olekut ja hoiatusi.",
   goal_en="Develop the FEST26 driver-display firmware that shows the driver the car's state and warnings.",
   desc_et="Meeskonna ühisprojekt (Zephyr RTOS, C). Minu panus: inverteri ja kontrolleri olekud ning hoiatused, kahe invertertüübi tugi, isejuhtiva (DV) režiimi info, ekraani hämardamine, roolinuppude ja pöördlülitite loogika, ringiaja taimeri parandused, ekraani ühendamine uue DBC-ga ning mälukasutuse vähendamine (8-bitised värvid), et ekraan enam kokku ei jookseks.",
   desc_en="A team project (Zephyr RTOS, C). My contributions: inverter and controller states and warnings, support for both inverter types, driverless (DV) mode info, screen dimming, steering-wheel button and rotary-switch logic, lap-timer fixes, wiring the display to the new DBC, and cutting memory use (8-bit colour) so the display no longer crashed.",
   tools_et=["C","Zephyr RTOS","CAN"], tools_en=["C","Zephyr RTOS","CAN"],
   github=None, video=None, images=[]),

 dict(slug="fs-noise-standard", draft=False, ongoing=True, group="fs",
   title_et="Lõputöö: tudengivormeli müra standard", title_en="Thesis: a noise-immunity standard for Formula Student",
   goal_et="Välja selgitada, millise müra juures FEST26 elektroonikaplaadid hakkavad valesti töötama, ning koostada meeskonnale mürataluvuse standard.",
   goal_en="Find out at what noise levels the FEST26 electronics boards start to misbehave, and turn the results into a noise-immunity standard for the team.",
   desc_et="TalTechi bakalaureusetöö „Tudengivormeli müra standardi väljatöötamine“ (juhendaja Kaiser Pärnamets). Meeskonnal puudub seni ühtne nõue, kui suurt elektrilist müra peavad plaadid taluma. Töös uurin sõidukielektroonika EMÜ-standardeid (ISO 11452, CISPR 25), koostan kajavabas kambris katseseadistuse, kus plaatidesse suunatakse kontrollitult müra, ning määran alasüsteemide kaupa piirid, mille juures väljundid lähevad valeks või talitlus katkeb.",
   desc_en="TalTech bachelor's thesis, supervised by Kaiser Pärnamets. The team has had no common requirement for how much electrical noise its boards must withstand. The thesis reviews automotive EMC standards (ISO 11452, CISPR 25), builds a test setup in an anechoic chamber that injects controlled noise into the boards, and determines for each subsystem the levels at which outputs go wrong or the board stops working.",
   tools_et=["EMC","ISO 11452","CISPR 25"], tools_en=["EMC","ISO 11452","CISPR 25"],
   github=None, video=None, images=[]),

 dict(slug="sms-station", draft=False, ongoing=True,
   title_et="SMS-jaam väravale", title_en="SMS gate station",
   goal_et="Ehitada GSM-jaam, millega saab värava avada telefonikõne või SMS-iga.",
   goal_en="Build a GSM station that opens a gate with a phone call or a text message.",
   desc_et="ESP32 ja SIM800L-mooduli põhine seade. Kasutajatel on rollid (juhuslik, liige, helistaja, omanik): liige avab värava SMS-iga, helistaja ka kõnega ning omanik haldab numbreid SMS-käskudega. Kõik kõned ja sõnumid logitakse ning kõike saab hallata ka veebiliidese kaudu; esimesel käivitamisel avab seade oma WiFi-pääsupunkti, mille kaudu saab selle koduvõrku ühendada.",
   desc_en="Built on an ESP32 and a SIM800L module. Users have roles (random, member, caller, owner): members open the gate by SMS, callers by calling as well, and owners manage the number list with SMS commands. Every call and message is logged, and everything can also be managed through a web interface; on first boot the device opens its own Wi-Fi access point for connecting it to the home network.",
   tools_et=["ESP32","C++","PlatformIO","GSM"], tools_en=["ESP32","C++","PlatformIO","GSM"],
   github=None, video=None,
   images=[("sms-station-1.png","SMS-jaama veebiliides: avamiste statistika (näidisandmed)","SMS station web interface: opening statistics (sample data)"),
           ("sms-station-2.png","SMS-jaama sündmuste logi (näidisandmed)","SMS station event log (sample data)")]),

 dict(slug="milrem-drone", draft=False, ongoing=True,
   title_et="Autonoomne droon (Milremi projekt)", title_en="Autonomous drone (Milrem project)",
   goal_et="Programmeerida Webotsi simulaatoris droon, mis täidab missiooni iseseisvalt ja maandub sihtsõidukile.",
   goal_en="Program a drone in the Webots simulator that carries out its mission autonomously and lands on a target vehicle.",
   desc_et="TalTechi 5. semestri meeskonnaprojekt. Iga liige vastutab ühe osa eest, minu ülesanne on maandumine. Valmis on kaamerapõhine sihtmärgi tuvastus: droon leiab sõidukil oleva ArUco-markeri OpenCV abil.",
   desc_en="A 5th-semester TalTech team project. Each member owns one part, and mine is the landing. The camera-based target recognition is done: the drone finds the ArUco marker on the vehicle using OpenCV.",
   tools_et=["Python","Webots","OpenCV"], tools_en=["Python","Webots","OpenCV"],
   github=None, video=None,
   images=[("milrem-drone-1.jpg","Drooni kaamera tuvastab sõiduki katusel oleva ArUco-markeri ja sõiduki suuna","The drone camera detects the ArUco marker on the vehicle roof and the vehicle's heading"),
           ("milrem-drone-2.jpg","Droon stardiplatsil metsamaastikul Webotsi simulaatoris","The drone on its start pad in the forest terrain in the Webots simulator")]),

 dict(slug="boe-bot", draft=True,
   title_et="Boe-Bot voolumõõtja", title_en="Boe-Bot current meter",
   goal_et="Luua lihtsalt kasutatav laiendusplaat, mille saab asetada Boe-Boti peale, et mõõta erinevate komponentide voolu.",
   goal_en="Build an easy-to-use expansion board that mounts on top of the Boe-Bot to measure the current draw of its components.",
   desc_et="", desc_en="",
   tools_et=["KiCad","LTspice"], tools_en=["KiCad","LTspice"],
   github=None, video=None, images=[]),

 dict(slug="radiobuttons", draft=False,
   title_et="Raadionupud (RadioButtons)", title_en="Radio Buttons (RadioButtons)",
   goal_et="Luua lihtne ja mugav programm internetiraadio jaamade kuulamiseks ning nende vahel kiireks vahetamiseks.",
   goal_en="A simple, convenient app for listening to internet radio stations and switching between them quickly.",
   desc_et="Projekt sai alguse isiklikust vajadusest, soovist lihtsustada raadiojaamade kuulamist arvutis. Inspiratsiooniks olid auto raadiosüsteemid, kus jaama vahetamine käib ühe nupuvajutusega. Tulemuseks on graafilise kasutajaliidesega rakendus, kus kasutaja saab valida jaamu logode abil.",
   desc_en="The project grew out of a personal need to make listening to radio on a computer easier. The inspiration came from car radio systems, where switching stations takes a single button press. The result is a GUI application where you pick stations using their logos.",
   tools_et=["Python","PySimpleGUI","VLC"], tools_en=["Python","PySimpleGUI","VLC"],
   github="https://github.com/joosepf/RadioButtons", video=None,
   images=[("radiobuttons-1.png","RadioButtonsi peaaken raadiojaamade logodega","RadioButtons main window with station logos"),
           ("radiobuttons-2.png","RadioButtonsi liidese detail","RadioButtons interface detail")]),

 dict(slug="robot-platform", draft=True, group="robots",
   title_et="Robotiplatvorm", title_en="Robot platform",
   goal_et="Luua modulaarne robotiplatvorm, millele saab lihtsalt lisada erinevaid sensoreid ja laiendusi.",
   goal_en="Create a modular robot platform to which different sensors and extensions can easily be added.",
   desc_et="Projekt sai alguse soovist arendada paindlikku ja laiendatavat roboti aluspõhja, mis oleks sobilik erinevate katsete ja projektide jaoks. Kasutatud on 3D-prinditud osi ning juhtimiseks Arduino platvormi.",
   desc_en="The project began with the wish to develop a flexible, extensible robot base suitable for a range of experiments and projects. It uses 3D-printed parts and an Arduino platform for control.",
   tools_et=["Fusion 360","3D-printimine ja disain","Arduino"], tools_en=["Fusion 360","3D printing & design","Arduino"],
   github=None, video=None,
   images=[("robot-platform-1.jpg","3D-prinditud modulaarne robotiplatvorm","3D-printed modular robot platform")]),

 dict(slug="phone-remote-robot", draft=True, part_of="robot-platform", group="robots",
   title_et="Robot telefoni puldiga", title_en="Robot with a phone remote",
   goal_et="Kasutada telefoni güroskoopi ja muuta telefon roboti puldiks.",
   goal_en="Use a phone's gyroscope and turn the phone into the robot's remote control.",
   desc_et="Robotiplatvormi edasiarendus, mille peamine eesmärk on kasutada HC-04 Bluetooth-moodulit ning näidata selle võimekust. Antud näites kasutatakse telefoni ja selle güroskoopi, et vastavalt telefoni olekule robotit liigutada (kõrvale kallutamine = keeramine, ette/taha kallutamine = edasi/tagasi liikumine).",
   desc_en="An extension of the robot platform whose main goal is to use the HC-04 Bluetooth module and show off its capabilities. Here the phone and its gyroscope drive the robot according to the phone's orientation (tilt sideways = turn, tilt forward/back = drive forward/back).",
   tools_et=["Arduino","Bluetooth (HC-04)"], tools_en=["Arduino","Bluetooth (HC-04)"],
   github=None, video=None, images=[]),

 dict(slug="line-follower", draft=True, part_of="robot-platform", group="robots",
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
   goal_en="Give an old car that only has a cassette player a Bluetooth music player shaped like a cassette.",
   desc_et="Seade ühendab mitu komponenti, et pakkuda juhtmevaba muusika kuulamise kogemust. Süsteemile lisati suurem aku ja akuhaldussüsteem (BMS), mis võimaldab pikemat tööaega ja kiiremat laadimist. Korpus on disainitud ja 3D-prinditud auto sisustuse järgi.",
   desc_en="The device combines several components to deliver a wireless listening experience. A larger battery and a battery management system (BMS) were added for longer runtime and faster charging. The enclosure was designed and 3D-printed to match the car's interior.",
   tools_et=["3D-printimine ja disain","Fusion 360","Elektroonika"], tools_en=["3D printing & design","Fusion 360","Electronics"],
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
   tools_et=["Elektroonika","3D-printimine ja disain","Puutöö"], tools_en=["Electronics","3D printing & design","Woodworking"],
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
   tools_et=["Puutöö","Python","Arduino"], tools_en=["Woodworking","Python","Arduino"],
   github=None, video=None, images=[]),

 dict(slug="watch-winder", draft=True,
   title_et="Kellalaadija", title_en="Watch winder",
   goal_et="Luua mehaanilisele kellale laadimisseade, et vältida selle pidevat kandmist.",
   goal_en="Create a winding device for a mechanical watch so it doesn't have to be worn constantly.",
   desc_et="Disainitud ja 3D-prinditud laadija, mis kasutab kella liikumise simuleerimiseks samm-mootorit. Sobib automaat- ja mehaanilistele käekelladele.",
   desc_en="A designed and 3D-printed winder that uses a stepper motor to simulate the watch's motion. Suitable for automatic and mechanical wristwatches.",
   tools_et=["Arduino","3D-printimine ja disain","Elektroonika"], tools_en=["Arduino","3D printing & design","Electronics"],
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
   tools_et=["Elektroonika","3D-printimine ja disain"], tools_en=["Electronics","3D printing & design"],
   github=None, video=None,
   images=[("psu-mod-1.png","Ümberehitatud toiteploki korpus","Modified power-supply enclosure"),
           ("psu-mod-2.jpg","Valmis laboritoiteallikas","Finished bench power supply")]),

 dict(slug="speaker-eq", draft=False, ongoing=True,
   title_et="Kõlar ja EQ", title_en="Speaker & EQ",
   goal_et="Luua kaasaskantav kõlar võimendi, ekraani ja ekvalaiseriga.",
   goal_en="Build a portable speaker with an amplifier, a display and an equaliser.",
   desc_et="Enginaator 2025 projekti raames loodud helisüsteem, millele on plaanis lisada spetsiaalselt disainitud trükkplaat, Bluetooth-tugi ja aku.",
   desc_en="An audio system created as part of the Enginaator 2025 project, to which a custom-designed PCB, Bluetooth support and a battery are planned to be added.",
   tools_et=["Elektroonika","Arduino","3D-printimine ja disain"], tools_en=["Electronics","Arduino","3D printing & design"],
   github=None, video=None, images=[]),

 dict(slug="laugen-motorsport", draft=False,
   title_et="Laugen Motorsport fännitooted", title_en="Laugen Motorsport fan merchandise",
   goal_et="Luua fännitooteid Laugen Motorsporti fännidele.",
   goal_en="Create fan merchandise for Laugen Motorsport supporters.",
   desc_et="Hea sõber Aksel Laugen sõidab venna Feliksiga EHKK sarjas motokrossi ning soovisime neid toetada. Võtsin vastutuse enda peale: suhtlesin kunstnikuga ja lõime soovitud disainid, misjärel tuli suhelda erinevate tootjatega, et disainid päriselt ellu tuua. Tulemusena valmisid pusad, särgid, mütsid ja lipud.",
   desc_en="My good friend Aksel Laugen races motocross with his brother Feliks in the EHKK series, and we wanted to support them. I took charge: I worked with an artist to create the designs, then dealt with various manufacturers to bring them to life. The result was hoodies, shirts, caps and flags.",
   tools_et=["Suhtlus","Excel","Disain"], tools_en=["Communication","Excel","Design"],
   github=None, video=None,
   images=[("laugen-motorsport-1.jpg","Laugen Motorsporti fännitooted","Laugen Motorsport merchandise"),
           ("laugen-motorsport-2.jpg","Fännitoodete disain","Merchandise design")]),

 dict(slug="audi-80", draft=False,
   title_et="Audi 80 parandamine", title_en="Audi 80 repairs",
   goal_et="Hoida vana auto töökorras ja turvaline igapäevaseks kasutamiseks.",
   goal_en="Keep an old car running and safe for everyday use.",
   desc_et="Isiklik projekt, mille raames on Audi 80 hooldatud ja parandatud. Vahetatud on kütusepump, pidurisadul, salongiradiaator, mitmed sensorid ja flantsid ning tehtud ka regulaarseid hooldusi. Projekti käigus on omandatud väärtuslikke automehaanika oskusi.",
   desc_en="A personal project of maintaining and repairing an Audi 80. The fuel pump, a brake caliper, the heater core, several sensors and flanges have been replaced, and routine servicing carried out. Along the way it has taught valuable car-mechanics skills.",
   tools_et=["Automehaanika"], tools_en=["Car mechanics"],
   github=None, video=None, images=[]),
]

# normalise optional keys
for p in P:
    p.setdefault("ongoing", False)
    p.setdefault("part_of", None)
    p.setdefault("group", "other")

BYSLUG = {p["slug"]: p for p in P}
CHILDREN = {}
for p in P:
    if p["part_of"]:
        CHILDREN.setdefault(p["part_of"], []).append(p)

# ---- helpers ----------------------------------------------------------------
def t(et, en):
    """inline bilingual span pair"""
    return f'<span class="lang-et">{esc(et)}</span><span class="lang-en">{esc(en)}</span>'

# tag colour by kind, keyed by the English tool name (unknown -> "other")
TAG_KIND = {
    # software
    "Python": "sw", "C": "sw", "C++": "sw", "PySide6": "sw", "python-can": "sw", "cantools": "sw",
    "Kvaser CANlib": "sw", "OpenCV": "sw", "Webots": "sw", "PySimpleGUI": "sw", "VLC": "sw", "GTK4": "sw",
    # embedded and buses
    "STM32": "emb", "ESP32": "emb", "Arduino": "emb", "FreeRTOS": "emb", "Zephyr RTOS": "emb",
    "PlatformIO": "emb", "GSM": "emb", "Bluetooth (HC-04)": "emb", "CAN": "emb", "CAN FD": "emb",
    # electronics, EMC and test equipment
    "EMC": "ee", "TDR": "ee", "VNA": "ee", "Spectrum analyser": "ee", "ISO 11452": "ee", "CISPR 25": "ee",
    "LTspice": "ee", "Altium Designer": "ee", "KiCad": "ee", "Electronics": "ee",
    # CAD and mechanical
    "Fusion 360": "mech", "CAD": "mech", "3D printing & design": "mech",
    "Woodworking": "mech", "Car mechanics": "mech",
}

def tag_key(en):
    """URL-safe key for a tag, from its English name ("C++" -> "cplusplus")"""
    return re.sub(r"[^a-z0-9]+", "-", en.lower().replace("+", "plus")).strip("-")

def tags(p, prefix=""):
    """tools as coloured boxes linking to the filtered project list, plus a status box"""
    out = [f'<a class="tag {TAG_KIND.get(en, "other")}" data-tag="{tag_key(en)}" '
           f'href="{prefix}index.html?tag={tag_key(en)}#filters">{t(et, en)}</a>'
           for et, en in zip(p["tools_et"], p["tools_en"])]
    if p["ongoing"]:
        out.append(f'<span class="tag ongoing">{t("pooleli", "in progress")}</span>')
    elif p["draft"]:
        out.append(f'<span class="tag draft">{t("mustand", "draft")}</span>')
    return f'<div class="tags">{"".join(out)}</div>' if out else ""

def meta_line(*bits):
    bits = [b for b in bits if b]
    return '<span class="sep"> · </span>'.join(bits)

CONTACT = ('<a href="mailto:joosepfi@gmail.com">joosepfi@gmail.com</a>'
           '<span class="sep"> · </span><a href="https://github.com/joosepf">GitHub</a>'
           '<span class="sep"> · </span><a href="https://www.linkedin.com/in/joosep-fingling-432716b1/">LinkedIn</a>')

def head(title, prefix, extra_desc=""):
    return f"""<!DOCTYPE html>
<html lang="et" data-lang="et">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#8ccbf7">
<title>{esc(title)}</title>
<meta name="description" content="{esc(extra_desc)}">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<script>try{{var l=localStorage.getItem('site-lang')==='en'?'en':'et';document.documentElement.dataset.lang=l;document.documentElement.setAttribute('lang',l)}}catch(e){{}}</script>
<link rel="stylesheet" href="{prefix}assets/portfolio.css">
</head>
<body>"""

def cv_links(prefix):
    return (f'<a class="lang-et" href="{prefix}docs/cv-et.pdf">CV</a>'
            f'<a class="lang-en" href="{prefix}docs/cv-en.pdf">CV</a>')

def topbar(prefix):
    return f"""
<header class="topbar">
  <div class="topbar-in">
    <a class="brand" href="{prefix}index.html">Joosep Fingling</a>
    <nav>
      <a href="{prefix}index.html#{SECTIONS[0][1]}">{t("Projektid", "Projects")}</a>
      <a href="{prefix}gallery.html">{t("Galerii", "Gallery")}</a>
      {cv_links(prefix)}
      <span class="langtoggle" role="group" aria-label="Language">
        <button type="button" data-set="et" aria-label="Eesti keeles">ET</button><span aria-hidden="true">/</span><button type="button" data-set="en" aria-label="In English">EN</button>
      </span>
    </nav>
  </div>
</header>"""

def footer(prefix):
    return f"""
<footer>
  <div class="wrap">
    <p>{CONTACT}</p>
  </div>
</footer>
<div class="lb" id="lightbox"><img alt=""></div>
<script src="{prefix}assets/portfolio.js"></script>
</body>
</html>"""

# ---- home page --------------------------------------------------------------
def card(p):
    img = ""
    if p["images"]:
        fn, _alt_et, alt_en = p["images"][0]
        img = f'<img class="card-img" src="images/projects/{fn}" alt="{esc(alt_en)}" loading="lazy">'
    keys = " ".join(tag_key(en) for en in p["tools_en"])
    # the title link stretches over the whole card (CSS); the tag links sit above it
    return f"""    <article class="card" data-tags="{keys}">
      {img}
      <div class="card-body">
        <h3><a class="card-link" href="projects/{p['slug']}.html">{t(p['title_et'], p['title_en'])}</a></h3>
        <p>{t(p['goal_et'], p['goal_en'])}</p>
        {tags(p)}
      </div>
    </article>"""

def build_index():
    # order: finished first, then ongoing, then drafts; keep doc order within each
    order = sorted(range(len(P)), key=lambda i: (2 if P[i]["draft"] else (1 if P[i]["ongoing"] else 0), i))
    sections = []
    for group, sec_id, label_et, label_en in SECTIONS:
        members = [P[i] for i in order if P[i]["group"] == group]
        if not members: continue
        cards = "\n".join(card(p) for p in members)
        sections.append(f"""  <section class="projsec" id="{sec_id}">
    <h2>{t(label_et, label_en)}</h2>
    <div class="grid">
{cards}
    </div>
  </section>""")
    sections_html = "\n\n".join(sections)
    html_out = head("Joosep Fingling", "",
                    "Portfolio of Joosep Fingling: hardware student at TalTech and team captain of FS Team Tallinn.")
    html_out += topbar("")
    html_out += f"""
<section class="hero">
  <div class="hero-in">
    <img class="portrait" src="images/joosep.jpg" alt="Joosep Fingling" width="200" height="240">
    <div class="hero-text">
      <h1>Joosep Fingling</h1>
      <p class="role">{t("FS Team Tallinna meeskonnakapten (tegevjuht)", "Team Captain (CEO), FS Team Tallinn")}<br>
        {t("Riistvara arendus ja programmeerimine, TalTech", "Hardware Engineering and Programming, TalTech")}</p>
      <p class="intro">
        <span class="lang-et">Õpin TalTechis riistvara arendust ja programmeerimist ning juhin FS Team Tallinna. Enne seda tegelesin meeskonnas auto elektromagnetilise ühilduvuse ja mõõtmistega. Siin on minu projektid vormelist, koolist ja vabast ajast.</span>
        <span class="lang-en">I study hardware engineering and programming at TalTech and lead FS Team Tallinn. Before that I worked on the car's electromagnetic compatibility and measurements. Below are my projects from the team, from university and from my free time.</span>
      </p>
      <p class="contact">{CONTACT}<span class="sep"> · </span>{cv_links("")}</p>
    </div>
  </div>
</section>
<main class="wrap">
  <div class="filterbar" id="filters" hidden>
    {t("Sildiga", "Tagged")} <span class="tag filter-tag"></span>
    <span class="filter-count"></span>
    <button type="button" class="filter-clear">{t("Näita kõiki projekte", "Show all projects")}</button>
  </div>
{sections_html}
</main>
"""
    html_out += footer("")
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_out)

# ---- project pages ----------------------------------------------------------
def build_project(p):
    prefix = "../"
    title = f"{p['title_et']} | Joosep Fingling"
    out = head(title, prefix, p["goal_en"])
    out += topbar(prefix)

    partof = ""
    if p["part_of"]:
        par = BYSLUG[p["part_of"]]
        partof = (f'{t("Osa projektist", "Part of")} '
                  f'<a href="{par["slug"]}.html">{t(par["title_et"], par["title_en"])}</a>')

    out += f"""
<main class="wrap narrow">
  <p class="back"><a href="{prefix}index.html">← {t("Kõik projektid", "All projects")}</a></p>
  <h1>{t(p['title_et'], p['title_en'])}</h1>
  {tags(p, prefix)}
  {f'<p class="meta">{partof}</p>' if partof else ''}

  <h2>{t("Eesmärk", "Goal")}</h2>
  <p class="lang-et">{esc(p['goal_et'])}</p>
  <p class="lang-en">{esc(p['goal_en'])}</p>
"""
    if p["desc_et"] or p["desc_en"]:
        out += f"""
  <h2>{t("Kirjeldus", "Description")}</h2>
  <p class="lang-et">{esc(p['desc_et'])}</p>
  <p class="lang-en">{esc(p['desc_en'])}</p>
"""
    links = []
    if p["github"]:
        links.append(f'<a href="{esc(p["github"])}" target="_blank" rel="noopener">GitHub</a>')
    if p["video"]:
        links.append(f'<a href="{esc(p["video"])}" target="_blank" rel="noopener">Video</a>')
    if links:
        out += f'\n  <p class="links">{meta_line(*links)}</p>\n'

    # related children (for robot-platform)
    kids = CHILDREN.get(p["slug"], [])
    if kids:
        rel = "\n".join(f'    <li><a href="{k["slug"]}.html">{t(k["title_et"], k["title_en"])}</a></li>' for k in kids)
        out += f"""
  <h2>{t("Edasiarendused", "Extensions")}</h2>
  <ul>
{rel}
  </ul>
"""
    if p["images"]:
        figs = "\n".join(
            f'    <figure><img src="../images/projects/{fn}" alt="{esc(alt_en)}" loading="lazy">'
            f'<figcaption>{t(alt_et, alt_en)}</figcaption></figure>'
            for (fn, alt_et, alt_en) in p["images"])
        out += f"""
  <h2>{t("Pildid", "Images")}</h2>
  <div class="gallery">
{figs}
  </div>
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
    out = head("Galerii | Joosep Fingling", "",
               "Photos from Joosep Fingling's projects.")
    out += topbar("")
    out += f"""
<main class="wrap">
  <h1>{t("Galerii", "Gallery")}</h1>
  <p class="lede">{t("Pildid minu projektidest. Klõpsa pildil, et seda suuremalt näha.", "Photos from my projects. Click a photo to see it larger.")}</p>
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

# GitHub Pages only serves committed files: warn about new files git doesn't track yet
try:
    import subprocess
    new = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], cwd=ROOT,
                         capture_output=True, text=True, timeout=10).stdout.split()
    if new:
        print(f"\nNote: {len(new)} new file(s) are not in git yet, so GitHub Pages won't have them:")
        for f in new[:15]:
            print("   " + f)
        if len(new) > 15:
            print("   ...")
        print("Add them before committing:  git add -A")
except Exception:
    pass
