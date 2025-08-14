import requests
from bs4 import BeautifulSoup
import json

url = "https://udyamregistration.gov.in/UdyamRegistration.aspx"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

form_fields = []

# Only scrape fields from Step 1 section
step1_div = soup.find("div", {"id": "step1"})  # Adjust this if needed

if step1_div:
    for input_tag in step1_div.find_all('input'):
        if input_tag.get('type') == 'hidden':
            continue

        field = {
            "name": input_tag.get('name'),
            "type": input_tag.get('type'),
            "placeholder": input_tag.get('placeholder'),
            "required": input_tag.has_attr('required')
        }
        form_fields.append(field)

    for select_tag in step1_div.find_all('select'):
        field = {
            "name": select_tag.get('name'),
            "type": "select",
            "options": [opt.text.strip() for opt in select_tag.find_all('option') if opt.text.strip()]
        }
        form_fields.append(field)

# Save to JSON
with open("form_schema.json", "w", encoding="utf-8") as f:
    json.dump(form_fields, f, indent=2)

print("✅ Scraping complete. Saved to form_schema.json")
