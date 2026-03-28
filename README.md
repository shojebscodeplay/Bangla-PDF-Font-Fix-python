# 🇧🇩 Bangla PDF Font Fix in Python

Fixing Bangla/Bengali text rendering (যুক্তাক্ষর) in Python PDF generation.

## 😤 Problem
When generating PDFs with Bangla text in Python, Bengali conjunct characters (যুক্তাক্ষর) break apart and render incorrectly.

**Libraries that FAILED:**
| Library | Problem |
|---------|---------|
| ReportLab | যুক্তাক্ষর breaks apart |
| WeasyPrint | GTK dependency error on Windows |
| xhtml2pdf | Font path error in temp folder |
| fpdf2 (without uharfbuzz) | HarfBuzz not found error |

## ✅ Solution
Use **fpdf2 + uharfbuzz**

## 📦 Installation
```bash
pip install fpdf2
pip install uharfbuzz==0.39.0
```

## 🔤 Font
Use **Kalpurush** font for best Bangla rendering.
- Download: https://omicronlab.com/bangla-fonts.html

## 💻 Code Example
```python
from fpdf import FPDF

FONT_PATH = "path/to/kalpurush.ttf"

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("Kalpurush", fname=FONT_PATH)
        self.set_font("Kalpurush", size=10)

pdf = PDF()
pdf.add_page(format=(80, 250))
pdf.set_text_shaping(True)  # ✨ This single line fixes everything!

pdf.set_font_size(12)
pdf.multi_cell(0, 10, "বাংলাদেশের ছোট দোকানদারদের জন্য AI-powered POS system")
pdf.output("output.pdf")
```

## 🔑 Key: `set_text_shaping(True)`
This enables HarfBuzz text shaping engine which correctly handles:
- Bengali conjunct characters (যুক্তাক্ষর)
- Right-to-left scripts
- Complex Unicode rendering

## 🌍 Works On
- ✅ Windows
- ✅ Linux
- ✅ Mac

## 👨‍💻 Author
**MD. Shojeb Hossain Shojol**  
📧 shojeb.ruetete18@gmail.com  
🔗 [GitHub](https://github.com/shojebscodeplay)

## ⭐ If this helped you, please star this repo!
