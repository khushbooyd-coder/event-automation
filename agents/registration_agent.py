def create_registration_page(
    event_name,
    location,
    event_date
):

    registration_link = (
        f"https://crescoevents.com/register?"
        f"event={event_name.replace(' ', '%20')}"
    )

    landing_page = {
        "event_name": event_name,
        "location": location,
        "event_date": event_date,
        "registration_link": registration_link
    }

    return landing_page

