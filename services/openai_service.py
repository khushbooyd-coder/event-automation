import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_ai_invite(
    contact_name,
    company,
    job_title,
    event_name,
    location,
    event_date
):

    prompt = f"""
Write a professional personalized event invitation.

Contact Name: {contact_name}
Company: {company}
Job Title: {job_title}

Event:
{event_name}

Location:
{location}

Date:
{event_date}

The tone should be executive-level,
professional, concise, and persuasive.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

