def send_bulk_emails(subject, body, to_emails):
    for email in to_emails:
        send_email(subject, body, email)