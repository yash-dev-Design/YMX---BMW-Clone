import os

# Define the pages to create
pages = {
    "sedans.html": "Sedans",
    "suvs.html": "SUVs / SAVs",
    "m_models.html": "M Models",
    "i_models.html": "i Models (Electric)",
    "leasing_offers.html": "Leasing Offers",
    "special_programs.html": "Special Programs",
    "insurance.html": "Insurance",
    "innovation.html": "Innovation",
    "design.html": "Design",
    "sustainability.html": "Sustainability",
    "bmw_magazine.html": "BMW Magazine",
    "service_and_repair.html": "Service & Repair",
    "owner_manuals.html": "Owner's Manuals",
    "bmw_app.html": "BMW App",
    "imprint.html": "Imprint",
    "legal_disclaimer.html": "Legal Disclaimer",
    "privacy_policy.html": "Privacy Policy",
    "cookie_settings.html": "Cookie Settings"
}

# Define the directory
output_dir = r"c:\Users\royst\OneDrive\Desktop\bmw\service"

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# HTML Template
template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BMW | {title}</title>
    <link rel="shortcut icon" href="/images/favicon.png" type="image/x-icon">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">

    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: 'Poppins', sans-serif;
            color: #fff;
            background: #000;
        }}

        body::-webkit-scrollbar {{
            display: none;
        }}

        /* HEADER */
        header {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 14px 48px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
            background-color: #000; /* Solid black for subpages */
            border-bottom: 1px solid #333;
        }}

        .logo h1 {{
            font-size: 25px;
            letter-spacing: 3px;
            font-weight: 600;
        }}

        nav ul {{
            list-style: none;
            display: flex;
            gap: 28px;
        }}

        nav ul li {{
            font-size: 15px;
            letter-spacing: 1px;
            cursor: pointer;
            position: relative;
        }}

        li a {{
            text-decoration: none;
            color: white;
            transition: all ease-in-out 0.4s;
        }}

        li a:hover {{
            text-shadow: 0 0 30px rgba(255, 255, 255, 0.578);
        }}

        .icons {{
            display: flex;
            gap: 20px;
            font-size: 20px;
        }}

        .icons i {{
            cursor: pointer;
            transition: color 0.3s;
        }}

        .icons i:hover {{
            color: #1c69d4;
        }}

        /* MAIN CONTENT */
        main {{
            padding-top: 100px; /* Space for fixed header */
            min-height: 80vh;
        }}

        .page-hero {{
            padding: 80px 6%;
            text-align: center;
            background: #111;
            margin-bottom: 40px;
        }}

        .page-hero h1 {{
            font-size: 48px;
            margin-bottom: 10px;
            color: #1c69d4;
        }}

        .content-section {{
            padding: 40px 6%;
            max-width: 1200px;
            margin: 0 auto;
            line-height: 1.8;
            color: #ccc;
        }}

        .content-section p {{
            margin-bottom: 20px;
        }}

        /* FOOTER */
        .bmw-footer {{
            background: #0b0b0b;
            color: #fff;
            padding: 80px 6% 40px;
            font-family: Arial, Helvetica, sans-serif;
            margin-top: 60px;
        }}

        .footer-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 30px;
        }}

        .footer-col h4 {{
            font-size: 14px;
            letter-spacing: 2px;
            margin-bottom: 20px;
        }}

        .footer-col a {{
            display: block;
            color: #b5b5b5;
            font-size: 15px;
            margin-bottom: 14px;
            text-decoration: none;
            transition: 0.3s;
        }}

        .footer-col a:hover {{
            color: #1c69d4;
        }}

        .social-icons {{
            display: flex;
            gap: 20px;
            margin-top: 10px;
        }}

        .social-icons a {{
            font-size: 18px;
            color: #b5b5b5;
            transition: 0.3s;
        }}

        .social-icons a:hover {{
            color: #1c69d4;
        }}

        .footer-bottom {{
            margin-top: 60px;
            padding-top: 30px;
            border-top: 1px solid #222;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
            color: #888;
            font-size: 14px;
        }}

        .footer-links a {{
            margin-left: 25px;
            color: #888;
            text-decoration: none;
            transition: 0.3s;
        }}

        .footer-links a:hover {{
            color: #1c69d4;
        }}
    </style>
</head>

<body>

    <header id="main-header">
        <div class="logo">
            <h1>BMW</h1>
        </div>

        <nav id="main-nav">
            <ul>
                <li><a href="/index.html#models">MODELS</a></li>
                <li><a href="/index.html#electric">ELECTRIC</a></li>
                <li><a href="/index.html#config">CONFIGURE</a></li>
                <li><a href="/index.html#cta-config">EXPERIENCE</a></li>
            </ul>
        </nav>

        <div class="icons">
            <i class="fa fa-search"></i>
            <i class="fa fa-map-marker"></i>
            <i class="fa fa-user"></i>
        </div>
    </header>

    <main>
        <section class="page-hero">
            <h1>{title}</h1>
            <p>Explore our {title} section</p>
        </section>

        <section class="content-section">
            <p>Welcome to the {title} page. Here you will find detailed information about our {title}.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
            <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </section>
    </main>

    <footer class="bmw-footer" id="footer">
        <div class="footer-grid">

            <div class="footer-col">
                <h4>MODELS</h4>
                <a href="sedans.html">Sedans</a>
                <a href="suvs.html">SUVs / SAVs</a>
                <a href="m_models.html">M Models</a>
                <a href="i_models.html">i Models (Electric)</a>
            </div>

            <div class="footer-col">
                <h4>FINANCE</h4>
                <a href="leasing_offers.html">Leasing Offers</a>
                <a href="special_programs.html">Special Programs</a>
                <a href="insurance.html">Insurance</a>
            </div>

            <div class="footer-col">
                <h4>DISCOVER</h4>
                <a href="innovation.html">Innovation</a>
                <a href="design.html">Design</a>
                <a href="sustainability.html">Sustainability</a>
                <a href="bmw_magazine.html">BMW Magazine</a>
            </div>

            <div class="footer-col">
                <h4>OWNERSHIP</h4>
                <a href="service_and_repair.html">Service & Repair</a>
                <a href="owner_manuals.html">Owner's Manuals</a>
                <a href="bmw_app.html">BMW App</a>
            </div>

            <div class="footer-col social">
                <h4>CONNECT</h4>
                <div class="social-icons">
                    <a href="instagram.com/yashroy9938"><i class="fa fa-instagram" aria-hidden="true"></i></a>
                    <a href="Wa.me/+917989552340"><i class="fa fa-whatsapp" aria-hidden="true"></i></a>
                    <a href="https://www.facebook.com/share/15ZUGuWBXY/"><i class="fa fa-facebook-official" aria-hidden="true"></i></a>
                </div>
            </div>

        </div>

        <div class="footer-bottom">
            <span>© 2025 BMW AG. All rights reserved • <a href="https://royz-portfolio.netlify.app/" target="_blank" style="text-decoration: none; color: #ffffff;">Developer</a></span>
            <div class="footer-links">
                <a href="imprint.html">Imprint</a>
                <a href="legal_disclaimer.html">Legal Disclaimer</a>
                <a href="privacy_policy.html">Privacy Policy</a>
                <a href="cookie_settings.html">Cookie Settings</a>
            </div>
        </div>
    </footer>

</body>

</html>
"""

# Generate files
for filename, title in pages.items():
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template.format(title=title))
    print(f"Created {filepath}")

print("All pages created successfully.")
