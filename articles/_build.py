"""Generator stron artykułów. Uruchamiaj z katalogu articles/.

Edytuj zawartość listy ARTICLES, potem:
    cd articles && python3 _build.py
"""
from pathlib import Path
import html as _html

OUT_DIR = Path(__file__).parent

NAV = """    <nav class="navbar">
        <div class="nav-container">
            <a href="../index.html" class="logo">
                <img src="../images/logo.svg" alt="The Community Events" class="logo-img">
            </a>
            <button class="nav-toggle" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu">
                <li><a href="../index.html#about">About us</a></li>
                <li><a href="../index.html#business">Dla firm</a></li>
                <li><a href="../index.html#private">Prywatnie</a></li>
                <li><a href="../index.html#events">Wydarzenia</a></li>
                <li><a href="../index.html#blog">Blog</a></li>
                <li><a href="../index.html#contact" class="nav-cta">Kontakt</a></li>
            </ul>
        </div>
    </nav>
"""

FOOTER = """    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <img src="../images/logo.svg" alt="The Community Events" class="footer-logo-img">
                    <p>Offline is the new online</p>
                </div>
                <div class="footer-links">
                    <a href="../index.html#about">About us</a>
                    <a href="../index.html#business">Dla firm</a>
                    <a href="../index.html#private">Prywatnie</a>
                    <a href="../index.html#events">Wydarzenia</a>
                    <a href="../index.html#contact">Kontakt</a>
                </div>
                <div class="footer-social">
                    <a href="https://instagram.com/the.community.events" target="_blank">Instagram</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 The Community Events. Wszystkie prawa zastrzeżone.</p>
            </div>
        </div>
    </footer>
"""


def render_blocks(blocks):
    """blocks: list of dicts with 'kind' = h2|p|ul|ol|quote and content."""
    parts = []
    for b in blocks:
        kind = b["kind"]
        if kind == "h2":
            parts.append(f"                <h2>{_html.escape(b['text'])}</h2>")
        elif kind == "p":
            parts.append(f"                <p>{b['text']}</p>")
        elif kind in ("ul", "ol"):
            items = "\n".join(f"                    <li>{li}</li>" for li in b["items"])
            parts.append(f"                <{kind}>\n{items}\n                </{kind}>")
        elif kind == "quote":
            parts.append(f"                <blockquote>{b['text']}</blockquote>")
        else:
            raise ValueError(f"Unknown block kind: {kind}")
    return "\n".join(parts)


def render_related(related):
    """related: list of dicts {slug, tag, title, image}."""
    cards = []
    for r in related:
        cards.append(f"""                <article class="blog-card">
                    <a href="{r['slug']}.html">
                        <div class="blog-image" style="background-image: url('{r['image']}');"></div>
                        <div class="blog-content">
                            <span class="blog-tag">{_html.escape(r['tag'])}</span>
                            <h3>{_html.escape(r['title'])}</h3>
                            <span class="blog-link">Czytaj więcej →</span>
                        </div>
                    </a>
                </article>""")
    return "\n".join(cards)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | The Community Events</title>
    <meta name="description" content="{description}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Old+Standard+TT:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
{nav}
    <section class="article-hero">
        <div class="container">
            <p class="article-breadcrumb"><a href="../index.html">Strona główna</a> / <a href="../index.html#blog">Blog</a> / {short_title}</p>
            <span class="article-tag">{tag}</span>
            <h1 class="article-title">{title}</h1>
        </div>
    </section>

    <div class="article-cover-wrap">
        <div class="article-cover" style="background-image: url('{cover_image}');"></div>
    </div>

    <section class="article-body">
        <div class="container">
{body}
                <div class="article-cta">
                    <p>{cta_text}</p>
                    <a href="../index.html#contact" class="btn btn-primary">Let's work together</a>
                </div>
        </div>
    </section>

    <section class="article-related">
        <div class="container">
            <h2 class="section-title centered">Czytaj dalej</h2>
            <div class="blog-grid">
{related}
            </div>
        </div>
    </section>

{footer}
    <script src="../script.js"></script>
</body>
</html>
"""


ARTICLES = [
    {
        "slug": "regularne-eventy-wellbeing",
        "tag": "Wellbeing dla IT",
        "title": "Dlaczego regularne eventy wellbeing zwracają się w retencji i produktywności pracownika?",
        "short_title": "Regularne eventy wellbeing",
        "description": "W IT, gdzie deadline'y i ciągły stres to codzienność, regularne eventy wellbeing to realna inwestycja w retencję i produktywność zespołu.",
        "cover_image": "https://images.unsplash.com/photo-1632146639278-c2203c404d89?w=1600&h=900&fit=crop",
        "cta_text": "Chcesz przetestować, jak wellbeing wpłynie na Twój zespół IT? Zacznij od jednorazowego eventu.",
        "blocks": [
            {"kind": "p", "text": "W dzisiejszym świecie, gdzie deadline'y, zdalna praca i ciągły stres to codzienność, <strong>wellbeing dla IT</strong> staje się nie tylko modnym hasłem, ale realną inwestycją w zespół. Regularne eventy wellbeing pozwalają pracownikom na reset, budowanie relacji offline i regenerację."},
            {"kind": "h2", "text": "Jak regularne eventy wellbeing poprawiają retencję pracowników w IT?"},
            {"kind": "p", "text": "Retencja, czyli zatrzymywanie kluczowych talentów, to jedno z największych wyzwań w branży IT. Wysoka rotacja kosztuje firmy miliony: rekrutacja, szkolenie i utrata wiedzy to realne straty. Regularne eventy wellbeing bezpośrednio zmniejszają ryzyko odejść, ponieważ pracownicy czują, że firma o nich dba."},
            {"kind": "p", "text": "Badania wskazują, że firmy inwestujące w wellbeing notują o 10% lepsze wskaźniki retencji. Dlaczego? Ponieważ spotkania offline redukują wypalenie, budują lojalność i wzmacniają poczucie przynależności. Pracownicy IT, którzy regularnie uczestniczą w aktywnościach, rzadziej myślą o zmianie pracy, bo widzą, że ich samopoczucie jest priorytetem."},
            {"kind": "p", "text": "Ponadto, wellbeing zmniejsza absencję i rotację, co przekłada się na stabilność zespołu. Abonament na wellbeing to inwestycja, która się zwraca. Zespoły czują się docenione, co motywuje do długoterminowego zaangażowania."},
            {"kind": "h2", "text": "Wzrost produktywności dzięki wellbeing dla IT — fakty i liczby"},
            {"kind": "p", "text": "Produktywność w IT zależy nie tylko od narzędzi, ale przede wszystkim od kondycji zespołu. Szczęśliwi i zregenerowani pracownicy pracują lepiej. Badania pokazują, że mogą być nawet o 20% bardziej produktywni. Regularne eventy wellbeing, takie jak warsztaty relaksacyjne czy integracje offline, pozwalają na odzyskanie skupienia i energii. Firmy, które traktują takie działania jako stały element kultury, notują wyraźnie lepsze wyniki w retencji i efektywności pracy."},
            {"kind": "h2", "text": "Raport McLean & Company (2025)"},
            {"kind": "p", "text": "Organizacje z dobrze rozwiniętymi programami wellbeing osiągają 1,4 raza wyższą ogólną wydajność firmy i prawie dwukrotnie wyższą produktywność zespołów. Raport podkreśla, że brak systemowego podejścia (np. ignorowanie obciążeń pracą) powoduje, iż tylko 43% pracowników czuje wsparcie, co prowadzi do strat w wysokości 322 mld USD rocznie z powodu burnout (dane WHO). W kontekście IT regularne eventy mogą znacząco zmniejszyć te koszty poprzez lepszą lojalność i fokus."},
            {"kind": "h2", "text": "Badania Deloitte (2024)"},
            {"kind": "p", "text": "Według raportu Deloitte firmy priorytetyzujące wellbeing (w tym programy offline i narzędzia regeneracyjne) notują 24% wzrost zaangażowania pracowników i 19% wyższą retencję. Dodatkowo 85% organizacji zgłasza pozytywny wpływ na produktywność i wydajność ogólną."},
            {"kind": "p", "text": "Według ekspertów, wellbeing w pracy to strategia, która buduje zaangażowanie i kulturę troski w firmie. W IT, gdzie zespoły często pracują zdalnie, takie eventy offline przywracają prawdziwe relacje, co jest kluczowe dla długoterminowego sukcesu organizacji."},
            {"kind": "h2", "text": "Jak The Community Events realizuje wellbeing dla IT?"},
            {"kind": "p", "text": "The Community Events specjalizuje się w tworzeniu eventów offline, które łączą estetykę, ruch i uważność. Subskrypcja wellbeing to idealne rozwiązanie dla firm IT: roczny abonament z miesięcznymi eventami w biurze, dopasowanymi do zespołu. Efekty? Mniejsze wypalenie, lepsza koncentracja i pracownicy, którzy wracają z nową energią."},
            {"kind": "p", "text": "Jeśli chcesz przetestować, zacznij od jednorazowego eventu, na integrację lub jako reset po dużym projekcie. Wellbeing dla IT to nie luksus, to konieczność. Inwestycja, która zwraca się w retencji i produktywności."},
        ],
    },
    {
        "slug": "rytualy-regeneracji-w-pracy",
        "tag": "Wellbeing",
        "title": "Jak wprowadzić małe rytuały regeneracji do pracy — bez wychodzenia z biura",
        "short_title": "Rytuały regeneracji",
        "description": "Wiedza o oddechu i przerwach nie wystarcza. Liczy się doświadczenie. Pokazujemy, jak małe rytuały regeneracji wprowadzić na warsztacie i zostawić zespołowi proste kotwice.",
        "cover_image": "https://images.unsplash.com/photo-1749104953222-9d6ed76e4bf0?w=1600&h=900&fit=crop",
        "cta_text": "Zróbmy jeden warsztat testowy. Pokazujemy, uczymy, zostawiamy proste kotwice — Wy decydujecie, co zabieracie dalej.",
        "blocks": [
            {"kind": "p", "text": "Teoretycznie wszyscy wiemy, że trzeba robić przerwy, oddychać głębiej, czy rozluźnić kark. Ale w praktyce mało kto to robi regularnie. Dlaczego? Bo wiedza sama w sobie nie wystarcza, liczy się doświadczenie, przyjemna atmosfera i ktoś, kto pokaże, jak to zrobić naprawdę prosto i skutecznie."},
            {"kind": "p", "text": "Właśnie dlatego małe rytuały regeneracji najlepiej wprowadzać na warsztatach, w bezpiecznej przestrzeni, gdzie zespół może spróbować kilku technik przy biurku, poczuć różnicę i potem powtarzać je samodzielnie. My w The Community Events robimy to regularnie i widzimy, że efekt jest zupełnie inny niż czytanie poradników czy oglądanie filmików na YouTube."},
            {"kind": "h2", "text": "Dlaczego warsztaty dla firm działają?"},
            {"kind": "ul", "items": [
                "Pokazujemy konkretne techniki w 5 minut — nikt nie musi robić jogi przez godzinę, chociaż do tego zachęcamy ;)",
                "Robimy to razem — w grupie ludzie czują się swobodniej, śmieją się z początkowego skrępowania i łatwiej przełamują opór.",
                "Tworzymy atmosferę: bez presji, bez oceniania, z dużą dawką humoru. Technika zostaje w głowie jako coś miłego, a nie kolejnego obowiązku wellness.",
                "Dajemy proste kotwice, np. „zrób trzy oddechy za każdym razem, gdy kończysz taska”, dzięki czemu ludzie naprawdę zaczynają to powtarzać po warsztacie.",
            ]},
            {"kind": "p", "text": "Badania pokazują, że osoby, które raz doświadczyły techniki w grupie, wracają do niej 2–3 razy częściej niż te, które próbowały same. W firmach, gdzie wszyscy są przeładowani informacjami, właśnie taki żywy pokaz robi różnicę."},
            {"kind": "h2", "text": "Co robimy na warsztatach: przykłady rytuałów firmowych"},
            {"kind": "ol", "items": [
                "Trzy oddechy resetujące",
                "Box breathing w wersji biurkowej",
                "Szybki skan ciała siedząc",
                "Mikro-ruch + oddech",
                "Atmosfera, zapachy i relaks",
            ]},
            {"kind": "p", "text": "Każdy wie, że powinien robić przerwy w pracy. Ale kiedy ktoś pokaże Ci to w pracy, w grupie, z humorem — nagle staje się to realne i przyjemne. Właśnie dlatego warsztaty są tu kluczowe: dają doświadczenie, a nie tylko informację. Zwłaszcza, że zespół wychodzi z wiedzą, której może użyć w życiu prywatnym."},
        ],
    },
    {
        "slug": "team-building-bez-paintballa",
        "tag": "Team building",
        "title": "Team building bez paintballa — jak kameralne warsztaty offline poprawiają współpracę w zdalnych zespołach",
        "short_title": "Team building bez paintballa",
        "description": "Praca zdalna dała dużo wolności, ale zabrała poczucie bliskości. Klasyczny team building już nie wystarcza — pokazujemy, co działa zamiast.",
        "cover_image": "https://images.unsplash.com/photo-1739430170523-29f7a6c7093f?w=1600&h=900&fit=crop",
        "cta_text": "Nie potrzebujesz weekendowego wyjazdu. Wystarczy kilka godzin dobrze zaprojektowanej obecności.",
        "blocks": [
            {"kind": "p", "text": "Praca zdalna dała nam dużo wolności. Ale zabrała też coś ważnego — poczucie prawdziwej bliskości w zespole. Wielu liderów zauważa, że choć zadania są realizowane sprawnie, to poczucie wspólnoty i naturalnej współpracy słabnie."},
            {"kind": "p", "text": "Tradycyjne formy team buildingu, takie jak paintball czy spływy kajakowe, nie zawsze odpowiadają potrzebom zespołów pracujących zdalnie lub hybrydowo. Często są one zbyt głośne, oparte na rywalizacji i po jednym weekendzie efekt szybko się ulatnia. Dlatego coraz więcej firm wybiera spokojniejsze i bardziej przemyślane rozwiązanie — kameralne warsztaty offline."},
            {"kind": "h2", "text": "Dlaczego spotkania na żywo przynoszą lepsze rezultaty?"},
            {"kind": "p", "text": "Spotkanie twarzą w twarz tworzy przestrzeń, której nie da się w pełni zastąpić callami. Pojawia się naturalna bliskość, możliwość odczytywania mowy ciała i wspólne przeżywanie chwili. Dzięki temu członkowie zespołu łatwiej się otwierają, lepiej się słuchają i zaczynają postrzegać siebie nawzajem nie tylko przez pryzmat ról zawodowych. Efektem jest większe zaufanie, płynniejsza komunikacja i mniej nieporozumień w codziennej pracy."},
            {"kind": "h2", "text": "Co zamiast tradycyjnych integracji?"},
            {"kind": "p", "text": "W The Community Events projektujemy warsztaty, które odchodzą od klasycznego modelu team buildingu. Są kameralne, estetyczne i skupione na wspólnym doświadczeniu. Przykłady takich aktywności to:"},
            {"kind": "ul", "items": [
                "<strong>Warsztaty uważności i pracy z oddechem</strong>, wspierające lepsze radzenie sobie ze stresem oraz umiejętność słuchania.",
                "<strong>Zajęcia twórcze</strong>, takie jak malowanie, storytelling czy praca z roślinami. Gdy ręce są zajęte, rozmowy rozwijają się w naturalny sposób.",
                "<strong>Warsztaty sensoryczne</strong>: degustacje herbaty, wina, wina 0% lub tworzenie kompozycji zapachowych w niewielkich grupach.",
                "<strong>Ruch inaczej</strong> — joga, mindful spacer, tenis zespołowy.",
            ]},
            {"kind": "p", "text": "Dopasowujemy formę do konkretnych potrzeb zespołu."},
            {"kind": "h2", "text": "Kiedy warto rozważyć takie rozwiązanie?"},
            {"kind": "p", "text": "Jeśli Twój zespół pracuje głównie zdalnie lub hybrydowo i dostrzegasz, że brakuje mu prawdziwej spójności, nie musi to być kolejny intensywny wyjazd. Wystarczy kilka godzin w biurze lub innym dopasowanym otoczeniu. Integracja to jedno — ale może zespół po prostu potrzebuje resetu po dużym projekcie."},
            {"kind": "p", "text": "W The Community Events tworzymy właśnie takie doświadczenia — kameralne, dopasowane do potrzeb zespołu i skupione na tym, co naprawdę buduje relacje."},
        ],
    },
    {
        "slug": "retencja-pracownikow",
        "tag": "Burnout",
        "title": "Jak uniknąć odejścia kluczowych pracowników — rola regeneracji offline w walce z burnoutem",
        "short_title": "Retencja a regeneracja offline",
        "description": "Wypalenie zawodowe jest dziś jedną z głównych przyczyn rotacji najcenniejszych pracowników. Pokazujemy, dlaczego benefity online już nie wystarczają.",
        "cover_image": "https://images.unsplash.com/photo-1758237782492-be2393b4d945?w=1600&h=900&fit=crop",
        "cta_text": "Podaj wielkość zespołu i główne wyzwania (wypalenie, integracja) — przygotujemy dedykowaną koncepcję.",
        "blocks": [
            {"kind": "p", "text": "W dobie powszechnej cyfryzacji i życia w trybie zawsze online, granica między pracą a odpoczynkiem niemal całkowicie się zatarła. Dla kluczowych specjalistów — developerów, sprzedawców czy managerów — oznacza to życie w ciągłym przebodźcowaniu. Kiedy prawdziwe relacje i chwile spokoju stają się luksusem, pojawia się widmo wypalenia zawodowego, które jest jedną z głównych przyczyn rotacji najcenniejszych pracowników."},
            {"kind": "h2", "text": "Paradoks połączenia: dlaczego benefity online już nie wystarczają?"},
            {"kind": "p", "text": "Współczesne miejsce pracy mierzy się z wyzwaniem, które trafnie zdiagnozowała Natalia Hatalska w książce „Wiek paradoksów. Czy technologia nas ocali?”:"},
            {"kind": "quote", "text": "„W świecie online jesteśmy ze sobą połączeni, w świecie offline samotni. […] W świecie online urządzenia mobilne, komputery, aplikacje i programy mają zwiększyć naszą produktywność. W świecie offline, żeby naprawdę móc coś zrobić, musimy wyłączyć przynajmniej część funkcji tych urządzeń. Technologia […] miała nam oszczędzić czas, ale w świecie offline nam ten czas zabrała.”"},
            {"kind": "p", "text": "Ten paradoks bezpośrednio uderza w Twoich pracowników. Tradycyjne benefity często nie trafiają w sedno problemu, ponieważ kluczowi pracownicy potrzebują dziś przede wszystkim:"},
            {"kind": "ul", "items": [
                "Zwolnienia tempa i oddechu.",
                "Budowania relacji face-to-face, które rodzą się poza ekranem.",
                "Odzyskania skupienia i regeneracji w spokoju, a nie w pośpiechu.",
            ]},
            {"kind": "h2", "text": "Regeneracja offline jako strategia retencji"},
            {"kind": "p", "text": "Zatrzymanie talentów w firmie wymaga zmiany podejścia z reaktywnego na prewencyjne. Zamiast ratować pracownika, gdy jest już u progu burnoutu, warto postawić na regularny reset."},
            {"kind": "p", "text": "<strong>Jak działają eventy wellbeingowe w praktyce?</strong>"},
            {"kind": "ul", "items": [
                "<strong>Mniejsze wypalenie i lepsza koncentracja</strong>: regularne odłączanie się pozwala odzyskać jasność umysłu i wrócić do pracy z nową energią.",
                "<strong>Lepsza retencja</strong>: ludzie, którzy czują, że firma dba o ich dobrostan, rzadziej szukają zmian.",
                "<strong>Autentyczna integracja</strong>: wspólne doświadczenia przez ruch i uważność łączą zespół skuteczniej niż firmowe czaty.",
            ]},
            {"kind": "h2", "text": "Abonament na reset, czyli nowa kultura pracy"},
            {"kind": "p", "text": "W The Community Events proponujemy firmom Subskrypcję Wellbeing. To nie jest jednorazowy zryw, ale regularny, dopasowany do potrzeb zespołu reset w biurze lub innym wyjątkowym miejscu. Naszą misją jest pokazanie, że offline to nie trend — to powrót."},
            {"kind": "h2", "text": "Zacznij od jednego kroku"},
            {"kind": "p", "text": "Nie musisz od razu zmieniać całej strategii firmy. Możecie zacząć od pojedynczego wydarzenia, np. świątecznego resetu lub boostu po dużym projekcie."},
        ],
    },
    {
        "slug": "relacje-bez-telefonow",
        "tag": "Offline",
        "title": "Co naprawdę buduje relacje — nie slajdy, a chwile bez telefonu",
        "short_title": "Relacje bez telefonów",
        "description": "Relacje w zespole nie budują się przez prezentacje, agendy ani warsztat z flipchartem. Budują się w chwilach między — kiedy nikt nie nagrywa.",
        "cover_image": "https://images.unsplash.com/photo-1758525225745-c91556434170?w=1600&h=900&fit=crop",
        "cta_text": "Jeśli Twój zespół realizuje zadania, ale brakuje mu prawdziwej nici porozumienia — pogadajmy.",
        "blocks": [
            {"kind": "p", "text": "Znasz to spotkanie integracyjne, gdzie wszyscy siedzą przy stole, a połowa zespołu dyskretnie scrolluje telefon pod blatem? Albo ten firmowy wyjazd, po którym wracasz zmęczony bardziej niż przed nim?"},
            {"kind": "p", "text": "Relacje w zespole nie budują się przez prezentacje, agendy ani kolejny warsztat z flipchartem. Budują się w chwilach między. Kiedy razem coś przeżyjesz, poczujesz, dotkniesz. Kiedy nikt nie nagrywa i nikt nie ocenia."},
            {"kind": "h2", "text": "Telefon jako ściana, której nie widać"},
            {"kind": "p", "text": "Średni użytkownik sięga po telefon ponad 90 razy dziennie. W pracy, na przerwach, na spotkaniach. Efekt? Nawet gdy jesteśmy razem, jesteśmy osobno. Rozmowy urywają się w połowie. Kontakt wzrokowy trwa sekundy. Bliskość, która powinna powstawać naturalnie, nie ma szans się rozwinąć."},
            {"kind": "p", "text": "To nie jest kwestia złej woli. To kwestia nawyku i środowiska, które temu nawykowi sprzyja."},
            {"kind": "h2", "text": "Co się dzieje, gdy telefony znikają?"},
            {"kind": "p", "text": "Kiedy zespół przez kilka godzin działa bez ekranów, dzieje się coś prostego i zaskakującego jednocześnie: ludzie zaczynają ze sobą rozmawiać. Naprawdę. Nie przez czat, nie przez komentarz w dokumencie, ale twarzą w twarz, z pełną uwagą."},
            {"kind": "p", "text": "Pojawia się śmiech, który nie ma emotikonki. Rozmowa, która nie ma punktów na agendzie. I właśnie w tych momentach rodzi się zaufanie, które potem przekłada się na lepszą komunikację, mniej konfliktów i większą lojalność wobec zespołu."},
            {"kind": "h2", "text": "Chwile, które naprawdę łączą"},
            {"kind": "p", "text": "W The Community Events projektujemy doświadczenia, które celowo tworzą przestrzeń bez ekranów. Nie przez zakaz, ale przez wciągnięcie. Kiedy ręce są zajęte malowaniem, kompozycją zapachową albo wspólnym gotowaniem, telefon naturalnie ląduje w kieszeni."},
            {"kind": "p", "text": "Efekt? Zespół, który po warsztacie nie wraca do pracy zmęczony kolejnym „eventem”, ale z czymś, czego nie da się zorganizować przez Teams — z poczuciem, że naprawdę się zna."},
            {"kind": "h2", "text": "Kiedy warto to zrobić?"},
            {"kind": "p", "text": "Jeśli Twój zespół sprawnie realizuje zadania, ale czujesz, że brakuje mu prawdziwej nici porozumienia, to nie jest problem do rozwiązania nowym narzędziem. To jest problem do rozwiązania przy wspólnym stole, bez telefonów, z kilkoma godzinami prawdziwej obecności."},
            {"kind": "p", "text": "Nie potrzebujesz weekendowego wyjazdu. Potrzebujesz dobrze zaprojektowanej chwili."},
        ],
    },
    {
        "slug": "vision-board-w-pracy",
        "tag": "Lifestyle",
        "title": "Dlaczego vision board działa lepiej niż Ci się wydaje?",
        "short_title": "Vision board w pracy",
        "description": "Za prostą techniką vision boardu stoi konkretna neuropsychologia. Pokazujemy, dlaczego prywatny vision board w pracy zbliża zespół bardziej niż feedback.",
        "cover_image": "https://images.unsplash.com/photo-1690733546551-1007bc0a3414?w=1600&h=900&fit=crop",
        "cta_text": "Sprzedajemy dobrze zaprojektowane doświadczenie, które ma swoje podstawy w tym, jak naprawdę działa ludzki mózg.",
        "blocks": [
            {"kind": "p", "text": "Vision board kojarzy się z plakatami z Pinteresta, wycinankami z magazynów i motywacyjnymi cytatami na ścianie. I właśnie dlatego większość ludzi traktuje go z przymrużeniem oka. Tymczasem za tą prostą techniką stoi konkretna neuropsychologia. I coraz więcej badań, które trudno zbagatelizować."},
            {"kind": "h2", "text": "Co mówi nauka?"},
            {"kind": "p", "text": "Wizualizacja celów aktywuje te same obszary mózgu co ich realne przeżywanie. To nie metafizyka — to mechanizm potwierdzony przez neuronaukę, znany jako <em>„mental simulation”</em>. Kiedy wyobrażasz sobie cel jako już osiągnięty, Twój mózg zaczyna traktować go jako punkt odniesienia i nieświadomie kieruje uwagę na działania, które do niego prowadzą."},
            {"kind": "p", "text": "Tworzenie vision boardu angażuje też tzw. system retikularny (RAS), część mózgu odpowiedzialną za filtrowanie informacji. Po stworzeniu obrazu celu, mózg zaczyna „wyłapywać” z otoczenia sygnały i okazje, które wcześniej były niewidoczne. To dlatego po zakupie czerwonego samochodu nagle widzisz czerwone samochody wszędzie."},
            {"kind": "h2", "text": "Vision board zawodowy — czy to nie kolejny OKR w ładniejszej formie?"},
            {"kind": "p", "text": "Vision board w kontekście zawodowym ma sens — pomaga zespołowi zwizualizować kierunek, zsynchronizować priorytety i nadać sens codziennej pracy. Kiedy ludzie widzą wspólny obraz tego, do czego dążą, łatwiej im podejmować decyzje i współpracować bez ciągłego dopytywania."},
            {"kind": "p", "text": "Ale jest jeden haczyk. Zawodowy vision board wciąż trzyma ludzi w rolach. Widzisz managera, developera, sprzedawcę. Nie widzisz człowieka."},
            {"kind": "h2", "text": "Prywatny vision board w pracy? Właśnie to zbliża najbardziej"},
            {"kind": "p", "text": "I tu zaczyna się najciekawsza część. W The Community Events coraz częściej proponujemy warsztat, w którym vision board jest w pełni prywatny. Wakacje marzeń, rodzina, pasje, miejsca do odwiedzenia, styl życia, który chcesz prowadzić. Nic o celach kwartalnych."},
            {"kind": "p", "text": "Efekt jest za każdym razem podobny i za każdym razem zaskakuje liderów: ludzie się otwierają. Nagle okazuje się, że developer obok Ciebie marzy o przejściu Camino, że Twoja project managerka zbiera winyle, a ktoś z zespołu planuje przeprowadzkę do innego kraju."},
            {"kind": "p", "text": "Te informacje nie są „zawodowo istotne”. Ale właśnie dlatego są bezcenne dla relacji. Zaczynasz widzieć współpracownika jako człowieka z życiem poza Teamsem. I to zmienia jakość codziennej komunikacji bardziej niż jakikolwiek warsztat z feedbacku."},
            {"kind": "h2", "text": "Razem, ale każdy swój"},
            {"kind": "p", "text": "Warsztat vision board działa też dlatego, że łączy dwa pozornie sprzeczne elementy: jest wspólnym doświadczeniem, ale każdy tworzy coś głęboko osobistego. Nie ma rywalizacji, nie ma oceniania, nie ma jednej prawidłowej odpowiedzi. Jest skupienie, cisza, muzyka w tle i rozmowy, które zaczynają się naturalnie, gdy ktoś zauważa na Twoim vision boardzie zdjęcie miejsca, które sam odwiedził."},
            {"kind": "p", "text": "Takich rozmów nie zorganizujesz przez agendę."},
            {"kind": "h2", "text": "Kiedy to działa najlepiej?"},
            {"kind": "p", "text": "Warsztat vision board sprawdza się świetnie jako reset na początku roku, ale też po intensywnym projekcie, przed wakacjami albo jako element głębszej integracji — gdy zespół potrzebuje oddechu i czegoś, co zostanie po warsztacie dłużej niż tydzień."},
            {"kind": "p", "text": "Bo vision board nie znika po evencie. Wraca na biurko, do domu, na ścianę. I przypomina — i o celu, i o człowieku obok, który ma podobne marzenia."},
            {"kind": "p", "text": "Vision board nie zastąpi strategii, planu działania ani dobrego managementu. Działa jako narzędzie uzupełniające — nadaje kierunek i wzmacnia motywację. Ale żeby działał, musi być konkretny, regularnie przypominany i osadzony w realnym kontekście."},
            {"kind": "p", "text": "Dlatego nie sprzedajemy „magicznego myślenia”. Sprzedajemy dobrze zaprojektowane doświadczenie, które ma swoje podstawy w tym, jak naprawdę działa ludzki mózg."},
        ],
    },
]


def _escape_url(u):
    # & must be &amp; inside HTML attribute values
    return u.replace("&", "&amp;")


def main():
    by_slug = {a["slug"]: a for a in ARTICLES}
    for a in ARTICLES:
        # related = the 3 next articles (rotating)
        others = [x for x in ARTICLES if x["slug"] != a["slug"]]
        related_list = others[:3]
        related_html = render_related([
            {"slug": r["slug"], "tag": r["tag"], "title": r["title"], "image": _escape_url(r["cover_image"].replace("w=1600&h=900", "w=600&h=400"))}
            for r in related_list
        ])
        body_html = render_blocks(a["blocks"])
        page = PAGE_TEMPLATE.format(
            title=_html.escape(a["title"]),
            description=_html.escape(a["description"]),
            nav=NAV,
            footer=FOOTER,
            short_title=_html.escape(a["short_title"]),
            tag=_html.escape(a["tag"]),
            cover_image=_escape_url(a["cover_image"]),
            body=body_html,
            cta_text=_html.escape(a["cta_text"]),
            related=related_html,
        )
        out = OUT_DIR / f"{a['slug']}.html"
        out.write_text(page, encoding="utf-8")
        print(f"wrote {out.name}")


if __name__ == "__main__":
    main()
