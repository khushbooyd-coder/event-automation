def generate_followup_sequence(
    contacts,
    event_name,
    event_date
):

    followups = []

    for contact in contacts:

        reminder_1 = {
            "type": "T-7 Reminder",
            "message": (
                f"Reminder: {event_name} "
                f"is happening on {event_date}."
            )
        }

        reminder_2 = {
            "type": "T-1 Reminder",
            "message": (
                f"Looking forward to seeing you tomorrow "
                f"at {event_name}."
            )
        }

        post_event = {
            "type": "Post Event Follow-up",
            "message": (
                f"Thank you for attending {event_name}. "
                f"We would love to continue the conversation."
            )
        }

        followups.append({
            "contact": contact,
            "sequence": [
                reminder_1,
                reminder_2,
                post_event
            ]
        })

    return followups

