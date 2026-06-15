import pandas as pd


def import_sales_navigator_csv(uploaded_file):

    df = pd.read_csv(uploaded_file)

    leads = []

    for _, row in df.iterrows():

        leads.append({

            "firstname": row.get("First Name", ""),

            "lastname": row.get("Last Name", ""),

            "full_name": (
                f"{row.get('First Name', '')} "
                f"{row.get('Last Name', '')}"
            ).strip(),

            "title": row.get("Title", ""),

            "company": row.get("Company", ""),

            "location": row.get("Location", ""),

            "linkedin_url": row.get("LinkedIn URL", ""),

            "email": row.get("Email", "")
        })

    return leads