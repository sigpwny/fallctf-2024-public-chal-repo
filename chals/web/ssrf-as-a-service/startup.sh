# Internal service - not exposed outside of the local network!
# [!] This is important [!]
cd /app/internal-service && python3 -m http.server 9999 &

# Main service
cd /app/ && python3 main.py