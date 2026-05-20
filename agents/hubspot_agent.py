from services.hubspot_service import upsert_contact


def create_campaign_contacts(contacts):

    results = []

    for contact in contacts:

        result = upsert_contact(
            firstname=contact["firstname"],
            lastname=contact["lastname"],
            email=contact["email"],
            company=contact["company"],
            job_title=contact["job_title"]
        )

        results.append(result)

    return results

