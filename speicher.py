from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
import sys
import random
import pickle
import os

# Datei, in der der Zustand gespeichert wird
save_file = "language_state.pkl"


def save_state(remaining_languages, used_dict):
    with open(save_file, 'wb') as f:
        pickle.dump((remaining_languages, used_dict), f)


def load_state():
    if os.path.exists(save_file):
        with open(save_file, 'rb') as f:
            return pickle.load(f)
    else:
        return None, None


def good_morning_generator():
    original_dict = {
        "Deutsch": "Guten Morgen",
        "Englisch": "Good Morning",
        "Französisch": "Bonjour",
        "Spanisch": "Buenos días",
        "Italienisch": "Buongiorno",
        "Portugiesisch": "Bom dia",
        "Niederländisch": "Goedemorgen",
        "Schwedisch": "God morgon",
        "Norwegisch": "God morgen",
        "Dänisch": "Godmorgen",
        "Finnisch": "Hyvää huomenta",
        "Russisch": "Доброе утро",
        "Polnisch": "Dzień dobry",
        "Tschechisch": "Dobré ráno",
        "Slowakisch": "Dobré ráno",
        "Ungarisch": "Jó reggelt",
        "Rumänisch": "Bună dimineața",
        "Griechisch": "Καλημέρα",
        "Türkisch": "Günaydın",
        "Arabisch": "صباح الخير",
        "Hebräisch": "בוקר טוב",
        "Chinesisch (Mandarin)": "早上好",
        "Chinesisch (Kantonesisch)": "早晨",
        "Japanisch": "おはようございます",
        "Koreanisch": "좋은 아침입니다",
        "Hindi": "सुप्रभात",
        "Bengalisch": "সুপ্রভাত",
        "Tamil": "காலை வணக்கம்",
        "Telugu": "శుభోదయం",
        "Malayalam": "ഗുഡ്‌മോണിംഗ്",
        "Kannada": "ಶುಭೋದಯ",
        "Punjabi": "ਸ਼ੁਭ ਸਵੇਰ",
        "Gujarati": "સુપ્રભાત",
        "Marathi": "सुप्रभात",
        "Sinhalesisch": "සුභ උදෑසනක්",
        "Nepali": "शुभ प्रभात",
        "Thai": "สวัสดีตอนเช้า",
        "Vietnamesisch": "Chào buổi sáng",
        "Malaiisch": "Selamat pagi",
        "Indonesisch": "Selamat pagi",
        "Filipino (Tagalog)": "Magandang umaga",
        "Swahili": "Habari za asubuhi",
        "Zulu": "Sawubona ekuseni",
        "Xhosa": "Molo kusasa",
        "Isländisch": "Góðan daginn",
        "Estnisch": "Tere hommikust",
        "Lettisch": "Labrīt",
        "Litauisch": "Labas rytas",
        "Irisch": "Maidin mhaith",
        "Schottisch-Gälisch": "Madainn mhath",
        "Walisisch": "Bore da",
        "Bretonisch": "Demat",
        "Korsisch": "Bonghjornu",
        "Baskisch": "Egun on",
        "Katalanisch": "Bon dia",
        "Galicisch": "Bos días",
        "Maltesisch": "L-għodwa t-tajba",
        "Jiddisch": "גוט מארגן",
        "Kroatisch": "Dobro jutro",
        "Serbisch": "Добро јутро",
        "Bosnisch": "Dobro jutro",
        "Montenegrinisch": "Добро јутро",
        "Slowenisch": "Dobro jutro",
        "Mazedonisch": "Добро утро",
        "Bulgarisch": "Добро утро",
        "Albanisch": "Mirëmëngjes",
        "Armenisch": "Բարի լույս",
        "Georgisch": "დილა მშვიდობისა",
        "Aserbaidschanisch": "Sabahınız xeyir",
        "Kasachisch": "Қайырлы таң",
        "Usbekisch": "Xayrli tong",
        "Tadschikisch": "Субҳи хайр",
        "Kirgisisch": "Кутман таң",
        "Paschtu": "سهار مو پخير",
        "Farsi (Persisch)": "صبح بخیر",
        "Urdu": "صبح بخیر",
        "Sorani (Kurdisch)": "بەیانی باش",
        "Kurmanji (Kurdisch)": "Beyanî baş",
        "Mongolisch": "Өглөөний мэнд",
        "Tibetisch": "སྔ་དྲོ་བདེ་ལེགས།",
        "Lao": "ສະບາຍດີຕອນເຊົ້າ",
        "Khmer": "អរុណសួស្ដី",
        "Burmesisch": "မင်္ဂလာနံနက်ခင်းပါ",
        "Hausa": "Ina kwana",
        "Igbo": "Ụtụtụ ọma",
        "Yoruba": "E kaaro",
        "Amharisch": "እንደምን አመሸ",
        "Tigrinya": "ታሕዋት ዓድላ",
        "Somali": "Subax wanaagsan",
        "Madagassisch": "Manao ahoana ny maraina",
        "Tonga (Simbabwe)": "Mwaramutsa",
        "Tshivenda": "Matsheloni",
        "Shona": "Mangwanani",
        "Sesotho": "Khotsong",
        "Tswana": "Dumelang",
        "Oshiwambo": "Wa lalapo",
        "Afrikaans": "Goeie môre",
        "Maori": "Ata mārie",
        "Samoanisch": "Manuia le taeao",
        "Hawaiianisch": "Aloha kakahiaka"
    }

    # Lade den gespeicherten Zustand, falls vorhanden
    remaining_languages, used_dict = load_state()

    if remaining_languages is None:
        # Wenn kein gespeicherter Zustand vorhanden ist, initialisiere die Listen
        remaining_languages = list(original_dict.keys())
        used_dict = {}

    while True:
        if not remaining_languages:
            # Reset when all languages have been used
            remaining_languages = list(original_dict.keys())
            used_dict.clear()

        # Randomly select a language
        selected_language = random.choice(remaining_languages)
        greeting = original_dict[selected_language]

        # Remove from the remaining list and add to the used list
        remaining_languages.remove(selected_language)
        used_dict[selected_language] = greeting

        # Speichere den aktuellen Zustand
        save_state(remaining_languages, used_dict)

        yield selected_language, greeting, len(used_dict), len(original_dict)


class GoodMorningApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.generator = good_morning_generator()

    def initUI(self):
        self.setWindowTitle('Guten Morgen Generator')

        # Setze die Mindestgröße des Fensters
        self.resize(800, 500)

        # Erstelle eine Schriftart mit angepasster Größe
        font_language = QFont('Arial', 16)  # Schriftgröße für Sprache
        font_greeting = QFont('Arial', 20)  # Schriftgröße für Gruß
        font_counter = QFont('Arial', 14)  # Schriftgröße für den Counter

        self.label_language = QLabel('Sprache:', self)
        self.label_language.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_language.setFont(font_language)  # Setze die Schriftart für das Sprach-Label

        self.label_greeting = QLabel('Gruß:', self)
        self.label_greeting.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_greeting.setFont(font_greeting)  # Setze die Schriftart für das Gruß-Label
        self.label_greeting.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.label_counter = QLabel('Benutzte Sprachen: 0', self)
        self.label_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_counter.setFont(font_counter)  # Setze die Schriftart für den Counter

        self.button_generate = QPushButton('Zeige Gruß', self)
        self.button_generate.setFont(font_language)  # Setze die Schriftart für den Button
        self.button_generate.clicked.connect(self.display_greeting)

        layout = QVBoxLayout()
        layout.addWidget(self.label_language)
        layout.addWidget(self.label_greeting)
        layout.addWidget(self.label_counter)
        layout.addWidget(self.button_generate)

        self.setLayout(layout)

    def display_greeting(self):
        language, greeting, used_count, total_count = next(self.generator)
        self.label_language.setText(f'Sprache: {language}')
        self.label_greeting.setText(f'Gruß: {greeting}')
        self.label_counter.setText(f'Benutzte Sprachen: {used_count}/{total_count}')


def main():
    app = QApplication(sys.argv)
    ex = GoodMorningApp()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
