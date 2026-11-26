"""Gera o QR code do cartão.
Uso: python3 src/gerar_qrcode.py [URL]   (requer: pip install "qrcode[pil]")"""
import sys, pathlib, qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageDraw, ImageFont

URL = sys.argv[1] if len(sys.argv) > 1 else "https://paulorenato2002.github.io/natal-gestao-contabil/"
out = pathlib.Path(__file__).resolve().parent.parent

q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=18, border=2)
q.add_data(URL); q.make(fit=True)
qr = q.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
                  color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(6, 11, 18))).convert("RGB")

W, H = qr.width + 160, qr.height + 300
card = Image.new("RGB", (W, H), (6, 11, 18))
d = ImageDraw.Draw(card)
d.rounded_rectangle((60, 140, 60 + qr.width + 40, 140 + qr.height + 40), radius=36, fill=(255, 255, 255))
card.paste(qr, (80, 160))

def font(size, bold=False):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono" + ("-Bold" if bold else "") + ".ttf"
    try: return ImageFont.truetype(path, size)
    except OSError: return ImageFont.load_default()

def center(y, text, f, color):
    d.text(((W - d.textlength(text, font=f)) / 2, y), text, font=f, fill=color)

# hexágono da marca desenhado (a fonte não tem o caractere ⬡)
import math
cx, cy, r = W / 2 - d.textlength("GESTÃO CONTÁBIL", font=font(34, True)) / 2 - 30, 60, 17
d.polygon([(cx + r * math.cos(math.radians(60 * i + 30)), cy + r * math.sin(math.radians(60 * i + 30))) for i in range(6)],
          outline=(62, 198, 224), width=4)
center(40, "GESTÃO CONTÁBIL", font(34, True), (62, 198, 224))
center(90, "um recado de fim de ano pra você", font(24), (138, 138, 143))
center(140 + qr.height + 70, "aponte a câmera do celular", font(26, True), (234, 242, 245))
center(140 + qr.height + 110, "BOAS FESTAS · 2026", font(22), (242, 193, 78))

card.save(out / "qrcode-cartao.png")
qr.save(out / "qrcode-simples.png")
print("ok ->", out / "qrcode-cartao.png", "|", URL)
