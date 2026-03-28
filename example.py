from fpdf import FPDF

FONT_PATH = "kalpurush.ttf"  # Download from omicronlab.com

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("Kalpurush", fname=FONT_PATH)
        self.set_font("Kalpurush", size=10)

def generate_bangla_pdf():
    pdf = PDF()
    pdf.add_page(format=(210, 297))  # A4
    pdf.set_text_shaping(True)  # Magic line!
    
    pdf.set_font_size(16)
    pdf.multi_cell(100, 10, "বাংলা PDF টেস্ট")
    
    pdf.set_font_size(12)
    pdf.multi_cell(100, 8, "যুক্তাক্ষর সঠিকভাবে আসছে: বাংলাদেশ, প্রযুক্তি, স্বাধীনতা")
    pdf.multi_cell(100, 8, "আরো কিছু টেক্সট: বিশ্ববিদ্যালয়, পরিবেশ, অর্থনীতি")
    
    pdf.output("bangla_output.pdf")
    print("✅ PDF generated successfully!")

if __name__ == "__main__":
    generate_bangla_pdf()
