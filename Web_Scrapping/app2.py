import sqlite3

def store_vulnerabilities(vulnerabilities):
    conn = sqlite3.connect('vulnerabilities.db')
    c = conn.cursor()

    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS vulnerabilities
                 (id INTEGER PRIMARY KEY, product_name TEXT, vulnerability TEXT, severity TEXT, mitigation TEXT, published_date TEXT)''')

    for vuln in vulnerabilities:
        c.execute('''INSERT INTO vulnerabilities (product_name, vulnerability, severity, mitigation, published_date) 
                     VALUES (?, ?, ?, ?, ?)''', 
                     (vuln['product_name'], vuln['vulnerability'], vuln['severity'], vuln['mitigation'], vuln['published_date']))

    conn.commit()
    conn.close()
