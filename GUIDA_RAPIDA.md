# 🚀 Guida Rapida - App Interattiva GAS Documentation

## ⚡ Inizio Veloce

### Opzione 1: Usa la versione standalone (RACCOMANDATO)

```bash
# Genera la versione standalone
python3 build-app.py

# Apri index-standalone.html nel browser
# (doppio click o trascina nel browser)
```

✅ **Funziona subito senza configurazione!**

### Opzione 2: Usa un server locale

```bash
# Avvia server con Python 3
python -m http.server 8000

# Apri nel browser
# http://localhost:8000
```

## ❓ Quando usare quale versione?

### Usa `index-standalone.html` se:
- ✅ Vuoi semplicemente studiare subito
- ✅ Non hai familiarità con i server locali
- ✅ Vuoi condividere l'app con altri
- ✅ Vuoi usarla offline senza configurazione

### Usa `index.html` (con server) se:
- ✅ Stai modificando/sviluppando l'app
- ✅ Stai aggiornando frequentemente il README.md
- ✅ Preferisci file più piccoli
- ✅ Hai già un server locale in esecuzione

## 🐛 Problemi Comuni

### "0 argomenti" o contenuto vuoto?

**Causa**: Stai aprendo `index.html` direttamente (problema CORS)

**Soluzione**: Usa una delle due opzioni sopra!

### Script di build non funziona?

**Verifica**:
```bash
# Controlla Python
python3 --version

# Controlla di essere nella directory giusta
ls -la | grep -E "index.html|README.md"

# Riesegui lo script
python3 build-app.py
```

## 📖 Per Maggiori Informazioni

Consulta `APP_INTERATTIVA.md` per la documentazione completa!

---

**Buono Studio! 🎓**
