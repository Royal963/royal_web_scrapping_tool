import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alerts():
    conn = sqlite3.connect('vulnerabilities.db')
    c = conn.cursor()
    c.execute("SELECT * FROM vulnerabilities WHERE severity IN ('Critical', 'High')")
    vulnerabilities = c.fetchall()
    conn.close()

    if not vulnerabilities:
        print("No critical or high-severity vulnerabilities found.")
        return

    # Email setup
    smtp_server = 'smtp.example.com'
    port = 587
    sender_email = 'your_email@example.com'
    password = 'your_password'
    recipient_email = 'recipient@example.com'

    subject = "Critical/High Severity Vulnerability Alert"
    body = "The following vulnerabilities have been found:\n\n"

    for vuln in vulnerabilities:
        body += f"Product Name: {vuln[1]}\nVulnerability: {vuln[2]}\nSeverity: {vuln[3]}\nMitigation: {vuln[4]}\nPublished Date: {vuln[5]}\n\n"

    # Send the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
