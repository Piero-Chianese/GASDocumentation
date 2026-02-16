#!/usr/bin/env python3
"""
Build script per incorporare il contenuto del README.md direttamente nell'index.html.
Questo risolve il problema CORS quando si apre il file direttamente dal browser.

Uso: python3 build-app.py
Output: index-standalone.html (versione standalone con README incorporato)
"""

import os
import re
import json

def read_file(filepath):
    """Legge un file e restituisce il contenuto"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Scrive contenuto in un file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def escape_for_js(text):
    """Escapa il testo per essere usato come stringa JavaScript"""
    # Usa JSON.dumps per un escape sicuro
    return json.dumps(text)

def build_standalone():
    """Crea versione standalone di index.html con README.md incorporato"""
    
    print("🔨 Building standalone version...")
    
    # Leggi i file
    index_html = read_file('index.html')
    readme_md = read_file('README.md')
    
    # Trova la riga dove viene dichiarato markdown: ''
    # Usa un pattern più robusto che accetta sia singole che doppie virgolette
    pattern = r"(markdown:\s*)(['\"])\2"
    
    # Verifica che il pattern esista
    match = re.search(pattern, index_html)
    if not match:
        print("❌ Errore: Pattern 'markdown:' non trovato in index.html")
        return False
    
    # Sostituisci la dichiarazione vuota con il contenuto del README
    # json.dumps gestisce l'escaping e aggiunge le virgolette
    readme_escaped = escape_for_js(readme_md)
    
    # Usa una funzione di sostituzione per evitare problemi con escape sequences
    def replacer(match):
        return match.group(1) + readme_escaped
    
    modified_html = re.sub(
        pattern,
        replacer,
        index_html,
        count=1
    )
    
    # Verifica che la sostituzione sia avvenuta
    if modified_html == index_html:
        print("⚠️  Attenzione: La sostituzione del markdown potrebbe non essere avvenuta")
    
    # Modifica anche la funzione loadMarkdown per non fare fetch
    # Usa un pattern più flessibile che tollera variazioni di whitespace
    old_fetch_code = r"const\s+response\s*=\s*await\s+fetch\s*\(\s*['\"]README\.md['\"]\s*\)\s*;\s*if\s*\(\s*!\s*response\.ok\s*\)\s*throw\s+new\s+Error\s*\([^)]+\)\s*;\s*this\.markdown\s*=\s*await\s+response\.text\s*\(\s*\)\s*;"
    new_fetch_code = "// Contenuto già incorporato, non serve fetch"
    
    result = re.sub(old_fetch_code, new_fetch_code, modified_html, flags=re.DOTALL)
    
    # Verifica che anche questa sostituzione sia avvenuta
    if result == modified_html:
        print("⚠️  Attenzione: La sostituzione del codice fetch potrebbe non essere avvenuta")
        print("    Il file generato potrebbe comunque funzionare se il markdown è stato incorporato")
    
    modified_html = result
    
    # Aggiungi commento all'inizio per identificare la versione standalone
    standalone_comment = """<!-- 
    ═══════════════════════════════════════════════════════════════════════════
    VERSIONE STANDALONE - README.md INCORPORATO
    
    Questo file contiene il README.md incorporato direttamente e può essere
    aperto direttamente nel browser senza bisogno di un server locale.
    
    Generato automaticamente da build-app.py
    ═══════════════════════════════════════════════════════════════════════════
-->
"""
    
    modified_html = modified_html.replace('<!DOCTYPE html>', f'<!DOCTYPE html>\n{standalone_comment}', 1)
    
    # Scrivi il file standalone
    output_file = 'index-standalone.html'
    write_file(output_file, modified_html)
    
    # Calcola dimensioni
    original_size = len(index_html)
    standalone_size = len(modified_html)
    readme_size = len(readme_md)
    
    print(f"✅ Successo!")
    print(f"📄 File originale: {original_size:,} bytes")
    print(f"📄 README.md: {readme_size:,} bytes")
    print(f"📦 File standalone: {standalone_size:,} bytes")
    print(f"📁 Output: {output_file}")
    print(f"\n💡 Ora puoi aprire '{output_file}' direttamente nel browser!")
    
    return True

def main():
    """Funzione principale"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("=" * 70)
    print("🚀 Build Script - GAS Documentation Interactive App")
    print("=" * 70)
    print()
    
    # Verifica che i file esistano
    if not os.path.exists('index.html'):
        print("❌ Errore: index.html non trovato nella directory corrente")
        return 1
    
    if not os.path.exists('README.md'):
        print("❌ Errore: README.md non trovato nella directory corrente")
        return 1
    
    # Build standalone version
    if not build_standalone():
        return 1
    
    print()
    print("=" * 70)
    print("✨ Build completato con successo!")
    print("=" * 70)
    
    return 0

if __name__ == '__main__':
    exit(main())
