# 📚 App Interattiva per lo Studio della GAS Documentation

## Descrizione

Questa è un'applicazione web interattiva progettata per facilitare lo studio della documentazione del GameplayAbilitySystem (GAS) di Unreal Engine 5. L'app offre un'interfaccia professionale e intuitiva con funzionalità avanzate per tracciare i progressi di studio.

## 🚀 Come Utilizzare l'App

### ⚠️ Importante: Problema CORS

Quando si apre `index.html` direttamente dal file system (usando `file://`), i browser moderni bloccano il caricamento del file `README.md` per motivi di sicurezza (CORS - Cross-Origin Resource Sharing). 

**Esistono DUE soluzioni:**

### Soluzione 1: Versione Standalone (Raccomandato) ✨

Usa lo script di build per creare una versione standalone con il README.md incorporato:

```bash
# Esegui lo script di build
python3 build-app.py
```

Questo creerà `index-standalone.html` che può essere aperto direttamente nel browser senza bisogno di un server locale! Il file contiene tutto il contenuto del README.md incorporato.

**Vantaggi:**
- ✅ Funziona aprendo direttamente il file
- ✅ Non richiede server locale
- ✅ Perfetto per uso offline
- ✅ Condivisibile come singolo file

### Soluzione 2: Server Locale

Se preferisci usare il file `index.html` originale, avvialo tramite un server locale:

```bash
# Con Python 3 (il più semplice)
python -m http.server 8000

# Con Node.js (se hai http-server installato)
npx http-server

# Con PHP
php -S localhost:8000
```

Poi apri il browser su `http://localhost:8000`

**Vantaggi:**
- ✅ File più piccolo
- ✅ Aggiornamenti automatici quando modifichi README.md
- ✅ Utile per sviluppo

### ❌ NON Funziona

- ❌ Aprire `index.html` direttamente dal file system (doppio click)
- ❌ Usare protocollo `file://` senza build

## ✨ Funzionalità Principali

### 📖 Navigazione
- **Indice laterale**: Naviga facilmente tra tutti gli argomenti
- **Struttura gerarchica**: Gli argomenti sono organizzati in livelli per una migliore comprensione
- **Pulsanti di navigazione**: Vai al capitolo precedente o successivo

### 🔍 Ricerca
- Cerca qualsiasi argomento nella barra di ricerca
- I risultati vengono filtrati in tempo reale
- Trova rapidamente quello che ti serve

### ✅ Tracciamento Progressi
- Segna gli argomenti come completati cliccando "✓ Completato"
- Visualizza il tuo progresso con la barra di avanzamento
- I progressi vengono salvati automaticamente nel browser
- Contatore degli argomenti completati

### 🌙 Modalità Scura
- Passa tra modalità chiara e scura
- Ideale per studiare di notte
- Le preferenze vengono salvate

### 📱 Responsive Design
- Funziona perfettamente su desktop, tablet e smartphone
- Menu hamburger su dispositivi mobili
- Layout ottimizzato per ogni schermo

### 💾 Persistenza dei Dati
- I progressi di studio vengono salvati nel localStorage del browser
- Le preferenze del tema vengono mantenute tra le sessioni
- Possibilità di resettare i progressi quando necessario

## 🎯 Come Studiare Efficacemente

1. **Inizia dall'inizio**: Clicca su "🚀 Inizia a Studiare" nella schermata di benvenuto
2. **Leggi attentamente**: Prenditi il tempo necessario per ogni sezione
3. **Segna i completati**: Quando finisci un argomento, clicca "✓ Completato"
4. **Usa la ricerca**: Se cerchi qualcosa di specifico, usa la barra di ricerca
5. **Monitora i progressi**: Tieni d'occhio la barra di progresso per vedere quanto hai studiato

## 🛠️ Caratteristiche Tecniche

- **Single Page Application (SPA)**: Tutto in un unico file HTML
- **Nessuna dipendenza esterna**: Non richiede librerie aggiuntive
- **Parsing Markdown**: Converte automaticamente il README.md in HTML formattato
- **LocalStorage**: Salva i progressi localmente nel browser
- **CSS Moderno**: Design professionale con animazioni fluide
- **JavaScript Vanilla**: Codice pulito e performante

## 🎨 Personalizzazione

L'app utilizza variabili CSS che possono essere facilmente personalizzate:
- `--primary-color`: Colore primario (default: blu)
- `--success-color`: Colore di successo (default: verde)
- Modifica queste variabili nel tag `<style>` per cambiare l'aspetto

## 📋 Requisiti

### Per versione standalone (`index-standalone.html`)
- Browser moderno (Chrome, Firefox, Safari, Edge)
- JavaScript abilitato
- Nessun altro requisito! Tutto è incorporato

### Per versione originale (`index.html`)
- Browser moderno (Chrome, Firefox, Safari, Edge)
- JavaScript abilitato
- Server locale (Python, Node.js, o PHP)
- Il file `README.md` deve essere nella stessa directory di `index.html`
- Per immagini e risorse, mantieni la struttura delle directory esistente

## 🔄 Aggiornamenti

### Per versione standalone
1. Modifica il file `README.md` con nuova documentazione
2. Rigenera il file standalone: `python3 build-app.py`
3. Apri il nuovo `index-standalone.html`

### Per versione originale
1. Modifica il file `README.md` con nuova documentazione
2. Ricarica la pagina nel browser (F5 o Cmd/Ctrl + R)
3. L'app caricherà automaticamente il nuovo contenuto

## 🐛 Risoluzione Problemi

**Problema**: "Il contenuto non viene caricato" / "0 argomenti"
- **Causa**: Problema CORS quando si apre index.html direttamente
- **Soluzione 1**: Usa `python3 build-app.py` per creare la versione standalone
- **Soluzione 2**: Avvia un server locale con `python -m http.server 8000`

**Problema**: Le immagini non vengono visualizzate
- **Soluzione**: Verifica che la cartella `Images/` sia presente nella stessa directory
- **Soluzione**: Se usi versione standalone e le immagini sono importanti, usa un server locale

**Problema**: I progressi non vengono salvati
- **Soluzione**: Controlla che i cookie/localStorage siano abilitati nel browser
- **Soluzione**: Non usare modalità in incognito se vuoi salvare i progressi

**Problema**: Build script non funziona
- **Soluzione**: Assicurati di avere Python 3 installato: `python3 --version`
- **Soluzione**: Esegui dalla directory contenente index.html e README.md
- **Soluzione**: Verifica che entrambi i file esistano nella directory corrente

## 📱 Supporto Browser

✅ Chrome/Edge (versione 90+)
✅ Firefox (versione 88+)
✅ Safari (versione 14+)
✅ Opera (versione 76+)

## 📄 Licenza

Questo strumento di studio segue la stessa licenza del progetto GASDocumentation principale.

## 🤝 Contributi

Per miglioramenti o segnalazioni di bug, apri una issue sul repository GitHub.

## 📞 Supporto

Per domande o supporto, consulta il repository originale del progetto GASDocumentation.

---

**Buono Studio! 🎓**
