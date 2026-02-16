# 🔨 Build Script per GAS Documentation App

Questo script Python crea una versione standalone dell'app interattiva incorporando il contenuto del README.md direttamente nell'HTML.

## Uso

```bash
python3 build-app.py
```

## Cosa fa

1. Legge `index.html` e `README.md`
2. Incorpora il contenuto del README.md come stringa JavaScript nell'HTML
3. Modifica la funzione `loadMarkdown()` per non fare richieste fetch
4. Crea `index-standalone.html` con tutto incorporato

## Output

- **File generato**: `index-standalone.html` (~360 KB)
- Può essere aperto direttamente nel browser senza server locale
- Include tutto il contenuto della documentazione

## Vantaggi della versione standalone

✅ Nessun problema CORS
✅ Funziona con file:// protocol
✅ Può essere condivisa come singolo file
✅ Perfetta per uso offline

## Note

- Il file standalone è più grande (~360 KB vs ~30 KB)
- È automaticamente escluso dal git (vedi `.gitignore`)
- Rigenera il file ogni volta che aggiorni il README.md

## Requisiti

- Python 3.x (con moduli standard: os, re, json)
- File `index.html` e `README.md` nella stessa directory dello script
