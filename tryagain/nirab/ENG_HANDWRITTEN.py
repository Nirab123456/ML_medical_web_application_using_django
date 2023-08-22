from PIL import Image
from fpdf import FPDF
from PIL import Image
class HandwrittenImageGenerator:
    def __init__(self, background_image_path, character_images_directory):
        self.BG = Image.open(background_image_path)
        self.sizeOfSheet = self.BG.width
        self.gap, self._ = 0, 0
        self.allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'
        self.character_images_directory = character_images_directory

    def write_character(self, char):
        if char != '\n':
            cases = Image.open(f"{self.character_images_directory}/{char.lower()}.png")
            self.BG.paste(cases, (self.gap, self._))
            size = cases.width
            self.gap += size

    def write_word(self, word):
        if self.gap > self.sizeOfSheet - 95 * len(word):
            self.gap = 0
            self._ += 200
        special_chars = {
            '.': 'fullstop',
            '!': 'exclamation',
            '?': 'question',
            ',': 'comma',
            '(': 'braketop',
            ')': 'braketcl',
            '-': 'hiphen'
        }
        for letter in word:
            if letter in self.allowedChars:
                if letter.islower():
                    pass
                elif letter.isupper():
                    letter = letter.lower() + 'upper'
                elif letter in special_chars:
                    letter = special_chars[letter]
                self.write_character(letter)

    def generate_handwritten_image(self, input_text, output_image_path):
        word_list = input_text.split(' ')
        for word in word_list:
            self.write_word(word)
            self.write_character('space')

        self.BG.save(output_image_path)

    def convert_photos_to_pdf(self, file_names, output_file):
        pdf = FPDF()

        # Add each photo as a page to the PDF
        for file_name in file_names:
            pdf.add_page()
            pdf.image(file_name, x=10, y=10, w=190)

        # Save the PDF
        pdf.output(output_file)

