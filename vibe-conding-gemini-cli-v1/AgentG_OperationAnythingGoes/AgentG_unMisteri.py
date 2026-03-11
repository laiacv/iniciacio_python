import http.server
import socketserver
import webbrowser
import os

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def main():
    # Establir el directori de treball on es troba el fitxer
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)
    
    if not os.path.exists("index.html"):
        print(f"Error: No s'ha trobat el fitxer 'index.html' a {base_dir}.")
        return

    print("--- AGENT G: OPERATION ANYTHING GOES ---")
    print("Una missió d'espionatge de 15-20 minuts.")
    print(f"Servidor iniciat a: http://localhost:{PORT}")
    print("\n>>> ATENCIÓ CODESPACES / VS CODE WEB <<<")
    print("Vés a la pestanya 'PORTS' (a costat de Terminal) i fes clic a la icona del globus terraqüi del port 8000.")
    print("O prem el botó 'Open in Browser' que apareixerà a la part inferior dreta.")
    print("------------------------------------------")
    print("Prem CTRL+C per tancar el servidor quan acabis de jugar.")
    
    # Intentem obrir el navegador automàticament
    webbrowser.open(f"http://localhost:{PORT}/index.html")

    # Iniciem el servidor
    # Allow address reuse to avoid "Address already in use" errors
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor tancat. Missió pausada.")
            httpd.shutdown()

if __name__ == "__main__":
    main()
