# Cartão de Natal 2026 · Gestão Contábil

Cartão de fim de ano animado em ASCII para os colaboradores da Gestão Contábil.

**Link:** https://paulorenato2002.github.io/natal-gestao-contabil/

## Estrutura

```
index.html            # o cartão (arquivo final, publicado pelo GitHub Pages)
qrcode-cartao.png     # QR code pronto para enviar no Teams
qrcode-simples.png    # só o QR, sem moldura
src/template.html     # fonte do cartão (edite aqui)
src/build.py          # gera index.html a partir do template (letreiros em ASCII)
src/gerar_qrcode.py   # gera os QR codes
```

## Como editar

1. Textos, nomes, bordões e velocidade ficam no bloco `CONFIG` no topo do script em `src/template.html`.
2. Gere o arquivo final:
   ```bash
   pip install pyfiglet "qrcode[pil]"
   python3 src/build.py
   ```
3. Faça commit e push — o GitHub Pages atualiza em ~1 minuto.

## Controles

- Toque na direita da tela: avança · na esquerda: volta
- Nos créditos: toque para acelerar
- Teclado: ← →
