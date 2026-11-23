"""Gera index.html a partir de template.html, injetando os letreiros figlet.
Uso: python3 src/build.py  (requer: pip install pyfiglet)"""
import json, pathlib, pyfiglet
root = pathlib.Path(__file__).resolve().parent
def fig(text, font):
    lines = pyfiglet.figlet_format(text, font=font, width=200).rstrip('\n').split('\n')
    while lines and not lines[-1].strip(): lines.pop()
    w = max(len(l) for l in lines)
    return [l.ljust(w) for l in lines]
FIG = {
  'renato': fig('RENATO', 'small'),
  'valter': fig('VALTER', 'small'),
  'feliz':  fig('FELIZ', 'ansi_shadow'),
  'natal':  fig('NATAL', 'ansi_shadow'),
  'y2026':  fig('2026', 'ansi_shadow'),
  'y2027':  fig('2027', 'ansi_shadow'),
}
w = max(len(FIG['y2026'][0]), len(FIG['y2027'][0]))
for k in ('y2026','y2027'): FIG[k] = [l.ljust(w) for l in FIG[k]]
tpl = (root / 'template.html').read_text(encoding='utf-8')
out = tpl.replace('__FIG__', json.dumps(FIG, ensure_ascii=False))
(root.parent / 'index.html').write_text(out, encoding='utf-8')
print('ok ->', root.parent / 'index.html')
