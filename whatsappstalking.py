from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# Email function to send alert when the person is online
def send_email(to_email, subject, body):
    from_email = "ashikamwork@gmail.com"  # Your email
    from_password = "Nidha-hameed"  # Your email password (or app password if using Gmail)

    # Set up the email content
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Set up the SMTP server (for Gmail)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection
    server.login(from_email, from_password)

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Set up Edge driver (replace with your own path)
service = Service(r"C:\Users\ashik\Downloads\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for manual QR code scanning
input("Scan QR code and press Enter to continue...")

# Search for the contact you want to monitor
contact_name = "Nidha"  # Replace with the person's name on WhatsApp
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(contact_name)
search_box.send_keys(Keys.ENTER)

# Set the running time limit to 24 hours
start_time = datetime.now()
end_time = start_time + timedelta(hours=24)

# Flag to track if the email has been sent
email_sent = False

# Continuously check online status for 24 hours
try:
    while datetime.now() < end_time:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Checking status at {current_time}...")  # Print timestamp for each iteration
        
        try:
            # Check if the person is online
            online_status = driver.find_element(By.XPATH, "//span[@title='online']")
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{contact_name} is online at {current_time}!")

            # Send email if online status is detected (and email hasn't been sent already)
            if not email_sent:
                send_email(
                    to_email="ashikamwork@gmail.com",  # Replace with your email
                    subject=f"{contact_name} is online!",
                    body=f"{contact_name} just came online on WhatsApp at {current_time}."
                )
                print(f"Email sent at {current_time}.")
                email_sent = True  # Prevent sending multiple emails

            # Wait until the person goes offline before checking again
            while driver.find_element(By.XPATH, "//span[@title='online']"):
                time.sleep(5)  # Pause checking while person is still online

        except:
            print(f"{contact_name} is offline.")

        # Reset email_sent flag when the person goes offline
        email_sent = False

        # Wait for a few seconds before checking again
        time.sleep(10)

except KeyboardInterrupt:
    print("Stopping the script.")
finally:
    driver.quit()
