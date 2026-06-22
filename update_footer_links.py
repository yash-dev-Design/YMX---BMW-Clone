import os

filepath = r"c:\Users\royst\OneDrive\Desktop\bmw\index.html"

replacements = {
    '<a href="#">Sedans</a>': '<a href="service/sedans.html">Sedans</a>',
    '<a href="#">SUVs / SAVs</a>': '<a href="service/suvs.html">SUVs / SAVs</a>',
    '<a href="#">M Models</a>': '<a href="service/m_models.html">M Models</a>',
    '<a href="#">i Models (Electric)</a>': '<a href="service/i_models.html">i Models (Electric)</a>',
    '<a href="#">Leasing Offers</a>': '<a href="service/leasing_offers.html">Leasing Offers</a>',
    '<a href="#">Special Programs</a>': '<a href="service/special_programs.html">Special Programs</a>',
    '<a href="#">Insurance</a>': '<a href="service/insurance.html">Insurance</a>',
    '<a href="#">Innovation</a>': '<a href="service/innovation.html">Innovation</a>',
    '<a href="#">Design</a>': '<a href="service/design.html">Design</a>',
    '<a href="#">Sustainability</a>': '<a href="service/sustainability.html">Sustainability</a>',
    '<a href="#">BMW Magazine</a>': '<a href="service/bmw_magazine.html">BMW Magazine</a>',
    '<a href="#">Service & Repair</a>': '<a href="service/service_and_repair.html">Service & Repair</a>',
    '<a href="#">Owner\'s Manuals</a>': '<a href="service/owner_manuals.html">Owner\'s Manuals</a>',
    '<a href="#">BMW App</a>': '<a href="service/bmw_app.html">BMW App</a>',
    '<a href="#">Imprint</a>': '<a href="service/imprint.html">Imprint</a>',
    '<a href="#">Legal Disclaimer</a>': '<a href="service/legal_disclaimer.html">Legal Disclaimer</a>',
    '<a href="#">Privacy Policy</a>': '<a href="service/privacy_policy.html">Privacy Policy</a>',
    '<a href="#">Cookie Settings</a>': '<a href="service/cookie_settings.html">Cookie Settings</a>'
}

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated footer links in index.html")
