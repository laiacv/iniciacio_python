import http.server
import socketserver
import webbrowser
import os

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def main():
    # Canviem el directori de treball al directori del fitxer per trobar index.html
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    html_file = "index.html"
    
    if not os.path.exists(html_file):
        print(f"Error: No s'ha trobat el fitxer '{html_file}'.")
        return

    print("--- AGENT G: OPERATION ANYTHING GOES ---")
    print("Una missió d'espionatge de 15-20 minuts.")
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
