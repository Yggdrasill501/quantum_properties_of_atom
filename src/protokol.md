# Měření kvantových vlastností atomu



## 1. Pracovní úkoly

### 1. Sestavte aparaturu pro stanovení Planckovy délky dle návodu[1].

### 2. Vykreslete závislost energií elektronů a frekvence záření do grafu. Z naměřených hodnot určete prahovou
frekvenci fotokatody.

### 3. Z naměřených dat určete Planckovu konstantu a výsledek porovnejte s tabulkovou hodnotou.

### 4. Sestavte aparaturu pro provedení Franckova-Hertzova experimentu a nechte rtuťovou trubici zahřát na zvole-
nou teplotu.

### 5. Pozorujte závislost procházejícího proudu IA na urychlujícím napětí U2 (Franckovu-Hertzovu křivku) na
digitálním osciloskopu. Nalezněte optimální hodnoty parametrů U1 a U3 a diskutujte jejich vliv na podobu
Franckovy-Hertzovy křivky.

### 6. Za pomoci dodatečných voltmetrů proměřte Franckovu-Hertzovu křivku pro napětí U2 v rozmezí 0 až 30 V a
sestavte její graf. Naměřte alespoň 80 hodnot.

### 7. V okolí maxim a minim Franckovy-Hertzovy křivky proložte naměřená data polynomy druhého stupně a
určete souřadnice extrémů. Postupnou metodou určete excitační energii atomu rtuti. Výsledek porovnejte
s tabulkovou hodnotou.

### 8. Využijte výslednou excitační energii a hodnotu Planckovy konstanty h získanou v úkolu 3. a s jejich pomocí
spočtěte, jakou vlnovou délku by měl foton vyzářený při deexcitaci atomů rtuti. Výsledek porovnejte s původním
výsledkem Francka a Hertze.


## 2. Pomůcky

Fotoelektrická buňka, vysokotlaká rtuťová lampa se zdrojem napájení, irisová clona, čočka (f = 100 mm),
interferenční filtry (578 nm, 546 nm, 436 nm, 405 nm, 365 nm), STE klíčový spínač, zesilovač elektrometru, STE
kondenzátor (100 pF, 630 V), voltmetr, optická lavice, dva optické jezdce (90 mm), tři optické jezdce (120 mm),
BNC adaptér, rtuťová Franck-Hertzova trubice, patice pro Franck-Hertzovu trubici s DIN konektorem, elektrická
pícka, napájecí jednotka, teplotní senzor NiCr-Ni, dvoukanálový digitální osciloskop GW Instek GDS-1072B, dva
stíněné kabely BNC/4 mm, dva voltmetry, vodiče.


## 3. Teoretický úvod

### 3.1. Fotoefekt na fotokatodě
Fotoefektem nazýváme jev, kdy fotoemisivní materiál emituje elektrony po zásahu elektromagnetickým zářením.
Při zapojení fotokatody v soustavě využité v této úloze pak pro napětí na kterém se ustálí elektrometrický zesilovač
U0 a frekvenci záření dopadajícího na fotokatodu f platí vztah

***Missing expresion***

kde h značí Planckovu konstantu, f0 prahovou frekvenci emisního materiálu a e náboj elektronu.

### 3.2. Franckův-Herztův pokus

Pro excitační energii materiálu Eex měřenou ve Franckově-Hertzově pokusu platí vztah

***Missing expresion***

kde e značí náboj elektronu a U0 velikost rozdílu napětí mezi maximy, respektive minimy proudového vývoje
v závislosti na napětí a pro frekvenci fotonů emitovaných tímto excitovaným materiálem f platí

***Missing expresion***

kde h značí Planckovu konstantu.


## 4. Postup měření

### 4.1 Příprava aparatury pro měření Planckovy konstanty
Na kraj optické lavice připevníme rtuťovou lampu a zapneme ji. Na zbytek optické lavice umístíme (ve směru
od lampy k druhému okraji lavice) irisovou clonu, čočku a fotoelektrickou buňku bez krytů a před upevněním
nastavíme tak, aby paprsek dopadající na fotokatodu dopadal pouze na černou fotocitlivou část a ne na žádný
z drátků vedoucí fotokatodou. Poté na fotoelektrickou buňku nasadíme stínící kryty a držák na interferenční filtry.
Lavici uzemníme, elektrometrický zesilovač zapojíme do zdroje a zapojíme na něm dle schéma na Obr. 1 (g) datový
kabel z fotoelektrické buňky, (f) kondenzátor s klíčovým spínačem, (h) uzemnění fotoelektrické buňky a voltmetr.


### 4.2 Měření Planckovy konstanty
Do držáku umístíme žlutý interferenční filtr, podržíme klíčový spínač dokud napětí na voltmetru neklesne na
0 V a uvolníme. Čekáme, dokud se napětí neustálí na Vstop. Opakujeme pro zelený, modrý, fialový a UV filtr.

### 4.3 Příprava aparatury a optimalizace na oscilátoru pro Franckův-Hertzův pokus
Rtuťovou trubici umístíme do pícky, zasuneme teploměr do pícky a zapneme zdroj pícky. Ujistíme se, že zdroj je
zdroj je nastavený, aby finální teplota θS byla mezi 170°C a 180°C a počkáme, než se teplota trubice ustálí na θS.
Poté ke zdroji připojíme oscilátor, na kterém pozorujeme křivku závislosti proudu IA na napětí U2 a upravujeme
parametry U1 a U3 dokud se dostatečně nepřiblížíme křivce v návodu[1].

### 4.4 Franckův-Hertzův pokus
Následně odpojíme oscilátor a připojíme k výstupům U2 a UA voltmetry a pro různá napětí U2 měříme napětí
UA (z něhož známe proud IA díky poměru od výrobce IA[nA] = UA[V ]) pro více než 80 hodnot.
5 Naměřené hodnoty a vypracování
5.1 Měření Planckovy konstanty
Naměřená napětí Ustop v závislosti na frekvenci záření propouštěného interferenčními filtry (vlnové délky 578
nm, 546 nm, 436 nm, 405 nm a 365 nm) jsou zobrazené na Obr. 3 s lineárním fitem
f(x) = (0, 00168 ± 0, 00008)(x − (360 ± 20)) který odpovídá Ustop[mV ] vyjádřeným ze vztahu (1). Koeficient
(0, 00168 ± 0, 00008) značí
h
e
· 1012, tudíž dostáváme experimentální hodnotu Planckovy konstanty

hexp = (1, 68 ± 0, 08) · 10−15 eVs. Tabulková hodnota je[3] htab = 4, 135667696 · 10−15 eVs. Zároveň koeficient (360 ± 20)
značí f0
[T Hz], tedy prahovou frekvenci fotokatody.
5.2 Franckův-Hertzův pokus
Graf naměřených proudů I v závislosti na napětí U2

spolu s kvadratickými fity v okolí lokálních extrémů jsou
zobrazené na Obr. 4. Souřadnice fitem získaných extrémů maxim a minim jsou vypsány v Tab. 1. Průměrná
vzdálenost napětí maxim od sebe je U
max
0 = (4, 900 ± 0, 002) V a minim od sebe E
min
0 = (4, 90 ± 0, 02) V.

2

S využitím vztahu (2) získáváme E
max
ex = (4, 900 ± 0, 002) eV a E
min
ex = (4, 90 ± 0, 02) eV. Tabulková hodnota[2]
je

E
tab
ex = 4, 9 eV.
Z těchto hodnot pomocí vztahu (3) získáváme frekvenci záření emitovaného excitovanými atomy rtuti
f
max = (2900 ± 100) THz, f

min = (2900 ± 100) THz a tabulková hodnota[2]
je f
tab = 1181, 1THz (λ
tab = 254

nm).


## 6. Diskuse

### 6.1 Měření Planckovy konstanty
Námi naměřená hodnota Planckovy konstanty hexp = (1, 68±0, 08)·10−15 eVs se poměrně, ovšem nikoliv řádově
liší od tabulkové hodnoty htab = 4, 135667696 · 10−15 eVs. Nejpravděpodobnějším důvodem nepřesnosti bude fakt,
že během našeho měření se vykazované hodnoty napětí na multimetru nikdy neustálily a namísto toho neustále
fluktuovaly. Hodnoty naměřené jsou tedy pouze ty, na nichž se hodnota ustálila na nejdelší dobu (například 3 s).
Důvodem tohoto kolísání by mohlo být nesprávné zapojení obvodu, nebo nesprávné nastavení čočky a clony, které
by vedlo k ozařování přívodových drátků ve fotobuňce, nicméně tyto faktory jsme opakovaně kontrolovali a proto je
mnohem pravděpodobnější příčinou závada na kondenzátoru, který měl zajišťovat právě ono ustálení na přibližně
konstantním Ustop. Zároveň je samozřejmě možné, že chyba měření byla způsobena nedostatkem naměřených dat,
nicméně vzhledem k tomu, že očekávané naměřené hodnoty pro 3 nejvyšší frekvence záření měly dle návodu[1]
přesahovat hodnotu 1 V, čehož nedosáhlo ani jedno z našich měření, chyba bude opravdu nejpravděpodobněji v
kondenzátoru.

### 6.2 Franckův-Hertzův pokus
Obě experimentálně získané hodnoty excitační energie atomu rtuti E
max
ex = (4, 900 ± 0, 002) eV a

E
min
ex = (4, 90 ± 0, 02) eV vyšly velmi blízko tabulkové hodnoty E
tab
ex = 4, 9 eV. Obě metody jsou tedy validní,
hodnota získaná z měření maxim má ovšem větší informační hodnotu, jelikož její chyba je o řád menší, což je velmi

pravděpodobně způsobeno větším množství naměřených maxim než naměřených minim. Hodnoty frekvence emito-
vaného záření excitovanými hodnotami pro obě metody vychází různě od tabulkové hodnoty z důvodu nepřesnosti

námi naměřené Planckovy konstanty (viz výše).


## 7. Závěr
Seznámili jsme se s Planckovou konstantou, kvantovými vlastnostmi atomu a metodami jejich měření. Sestavili
jsme obě sestavy pro zmíněná měření a změřili Planckovu konstantu jako h = (1, 68 ± 0, 08) · 10−15 eVs, prahovou
frekvenci fotokatody jako f0 = (360 ± 20) THz, excitační energii atomu rtuti jako Eex = (4, 900 ± 0, 002) eV a
frekvenci záření emitovanou excitovanými atomy rtuti jako f

min = (2900 ± 100) THz.


## Literatura

1. Návod k úloze Měření Planckovy konstanty - Fyzikální Praktika 2 [15.3.2022]
https://moodle-vyuka.cvut.cz/pluginfile.php/435643/mod_resource/content/1/11a_Planck_210408.
pdf

2. Návod k úloze Franckův-Hertzův experiment - Fyzikální Praktika 2 [15.3.2022]
https://moodle-vyuka.cvut.cz/pluginfile.php/435642/mod_resource/content/1/11b_Franck-Hertz_
210408.pdf

3. Fyzikální tabulky - Laboratorní průvodce [15.3.2022]
https://www.labo.cz/mft/zkonst.htm


## Přílohy
