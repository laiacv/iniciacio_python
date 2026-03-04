import http.server
import socketserver
import webbrowser
import os

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def main():
    # El fitxer que volem servir és 'index.html'
    # Però per defecte el servidor busca 'index.html', així que fem un truc:
    # Si no existeix index.html, el creem temporalment o simplement avisem.
    
    html_file = "index.html"
    
    if not os.path.exists(html_file):
        print(f"Error: No s'ha trobat el fitxer '{html_file}'.")
        return

    print("--- AGENT G: MISSIÓ VIL·LA ENIGMÀTICA ---")
    print(f"Servidor iniciat a: http://localhost:{PORT}")
    print("Si estàs a VS Code/Codespaces, apareixerà una notificació per obrir el navegador.")
    print("Prem CTRL+C per tancar el servidor quan acabis de jugar.")
    
    # Intentem obrir el navegador automàticament (per si estàs en local)
    webbrowser.open(f"http://localhost:{PORT}/{html_file}")

    # Iniciem el servidor
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor tancat. Missió pausada.")
            httpd.shutdown()

if __name__ == "__main__":
    main()
