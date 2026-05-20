from services.email_service import send_email


def send_campaign_email(
    contacts,
    invite_content
):

    email_results = []

    for index, contact in enumerate(contacts):

        personalized_data = invite_content[index]

        content = personalized_data["invite_content"]

        email_result = send_email(
            recipient_email=contact["email"],
            subject=content["subject"],
            body=content["email_body"]
        )

        print(
            f"Sending email to {contact['email']}"
        )

        email_results.append(email_result)

    return email_results

