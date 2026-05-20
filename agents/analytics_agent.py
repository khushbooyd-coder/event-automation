def generate_campaign_report(
    contacts,
    email_results,
    followup_sequences
):

    total_contacts = len(contacts)

    emails_sent = len([
        email for email in email_results
        if email["status"] == "sent"
    ])

    followups_created = len(
        followup_sequences
    )

    report = {
        "total_contacts": total_contacts,
        "emails_sent": emails_sent,
        "followups_created": followups_created,
        "delivery_rate": (
            f"{(emails_sent / total_contacts) * 100:.0f}%"
        )
    }

    return report

