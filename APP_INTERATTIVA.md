# 📚 App Interattiva per lo Studio della GAS Documentation

## Descrizione

Questa è un'applicazione web interattiva progettata per facilitare lo studio della documentazione del GameplayAbilitySystem (GAS) di Unreal Engine 5. L'app offre un'interfaccia professionale e intuitiva con funzionalità avanzate per tracciare i progressi di studio.

## 🚀 Come Utilizzare l'App

### Installazione

1. L'app è completamente self-contained (HTML, CSS e JavaScript in un unico file)
2. Apri il file `index.html` nel tuo browser web preferito
3. L'app caricherà automaticamente il contenuto dal file `README.md` nella stessa directory

### Metodi di Apertura

**Metodo 1: Apertura Diretta**
- Fai doppio clic sul file `index.html`
- Oppure trascinalo nel browser

**Metodo 2: Server Locale (Consigliato)**
```bash
# Con Python 3
python -m http.server 8000

# Con Node.js (se hai http-server installato)
npx http-server

# Con PHP
php -S localhost:8000
```
Poi apri il browser su `http://localhost:8000`

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

- Browser moderno (Chrome, Firefox, Safari, Edge)
- JavaScript abilitato
- Il file `README.md` deve essere nella stessa directory di `index.html`
- Per immagini e risorse, mantieni la struttura delle directory esistente

## 🔄 Aggiornamenti

Per aggiornare il contenuto:
1. Modifica il file `README.md` con nuova documentazione
2. Ricarica la pagina nel browser (F5 o Cmd/Ctrl + R)
3. L'app caricherà automaticamente il nuovo contenuto

## 🐛 Risoluzione Problemi

**Problema**: Il contenuto non viene caricato
- **Soluzione**: Assicurati che `README.md` sia nella stessa directory di `index.html`
- **Soluzione**: Usa un server locale invece di aprire il file direttamente

**Problema**: Le immagini non vengono visualizzate
- **Soluzione**: Verifica che la cartella `Images/` sia presente
- **Soluzione**: Usa un server locale per servire correttamente le risorse

**Problema**: I progressi non vengono salvati
- **Soluzione**: Controlla che i cookie/localStorage siano abilitati nel browser
- **Soluzione**: Non usare modalità in incognito se vuoi salvare i progressi

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
