from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
import os

base = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile"

def add_rect(slide, x, y, w, h, fill_rgb, line_rgb=None, line_pt=1):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid()
    s.fill.fore_color.rgb = fill_rgb
    if line_rgb:
        s.line.color.rgb = line_rgb
        s.line.width = Pt(line_pt)
    else:
        s.line.fill.background()
    return s

def add_round_rect(slide, x, y, w, h, fill_rgb, line_rgb=None, line_pt=1):
    s = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid()
    s.fill.fore_color.rgb = fill_rgb
    if line_rgb:
        s.line.color.rgb = line_rgb
        s.line.width = Pt(line_pt)
    else:
        s.line.fill.background()
    return s

def add_text(slide, x, y, w, h, text, size=10, color=RGBColor(15, 23, 42), bold=False, italic=False, font="Segoe UI", align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.04)
    tf.margin_right = Inches(0.04)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.italic = italic
    p.font.name = font
    p.alignment = align
    return tb

# ==============================================================================
# 1. DESTINATION CONSULTANCY PPTX
# ==============================================================================
def build_destination_pptx():
    prs = Presentation()
    prs.slide_width = Inches(8.27)
    prs.slide_height = Inches(11.69)
    blank = prs.slide_layouts[6]
    assets = os.path.join(base, "destination consultancy", "assets")

    NAVY = RGBColor(7, 30, 43)
    NAVY_MID = RGBColor(11, 45, 63)
    TEAL = RGBColor(25, 116, 152)
    GOLD = RGBColor(197, 155, 39)
    GOLD_LT = RGBColor(226, 190, 90)
    GOLD_PALE = RGBColor(251, 246, 232)
    BG_SOFT = RGBColor(244, 248, 250)
    WHITE = RGBColor(255, 255, 255)
    MUTED = RGBColor(74, 96, 112)

    def header_footer(slide, page_no, section_label="SUCCESS BEYOND BOUNDARIES"):
        add_rect(slide, 0, 0, 8.27, 0.92, NAVY)
        add_rect(slide, 0, 0.92, 8.27, 0.05, GOLD)
        slide.shapes.add_picture(os.path.join(assets, "icon_compass.png"), Inches(0.45), Inches(0.14), height=Inches(0.64))
        slide.shapes.add_picture(os.path.join(assets, "logo_white.png"), Inches(1.2), Inches(0.18), height=Inches(0.55))
        add_text(slide, 4.2, 0.22, 3.6, 0.28, "DESTINATION CONSULTANCY (PVT) LTD", 8.5, WHITE, True, font="Montserrat", align=PP_ALIGN.RIGHT)
        add_text(slide, 4.2, 0.48, 3.6, 0.24, section_label, 7, GOLD_LT, True, font="Montserrat", align=PP_ALIGN.RIGHT)

        add_rect(slide, 0, 11.12, 8.27, 0.04, GOLD)
        add_rect(slide, 0, 11.16, 8.27, 0.53, NAVY)
        add_text(slide, 0.45, 11.26, 5.5, 0.3, "DESTINATION CONSULTANCY (PVT) LTD  |  WWW.DESTINATIONCONSULTANCY.COM", 7.5, WHITE, False, font="Montserrat")
        add_round_rect(slide, 7.25, 11.24, 0.55, 0.3, GOLD)
        add_text(slide, 7.25, 11.25, 0.55, 0.28, f"{page_no:02d}", 8.5, NAVY, True, font="Montserrat", align=PP_ALIGN.CENTER)

    # Slide 1: Cover
    s1 = prs.slides.add_slide(blank)
    s1.shapes.add_picture(os.path.join(assets, "cover_hero.jpg"), Inches(0), Inches(0), width=Inches(8.27), height=Inches(11.69))
    ov = add_rect(s1, 0, 0, 8.27, 11.69, NAVY)
    ov.fill.transparency = 0.14
    add_rect(s1, 0, 0, 8.27, 1.35, NAVY)
    add_rect(s1, 0, 1.35, 8.27, 0.06, GOLD)
    s1.shapes.add_picture(os.path.join(assets, "icon_compass.png"), Inches(0.55), Inches(0.25), height=Inches(0.85))
    s1.shapes.add_picture(os.path.join(assets, "logo_white.png"), Inches(1.55), Inches(0.32), height=Inches(0.72))
    add_round_rect(s1, 5.7, 0.45, 2.05, 0.42, NAVY_MID, GOLD, 1)
    add_text(s1, 5.7, 0.52, 2.05, 0.3, "COMPANY PROFILE • 2026", 7.5, GOLD_LT, True, font="Montserrat", align=PP_ALIGN.CENTER)

    add_round_rect(s1, 0.6, 3.6, 4.8, 0.4, NAVY_MID, GOLD, 1)
    add_text(s1, 0.7, 3.66, 4.6, 0.3, "STRATEGIC ADVISORY & INVESTMENT FACILITATION", 8, GOLD_LT, True, font="Montserrat")
    add_text(s1, 0.6, 4.2, 7.1, 0.7, "DESTINATION", 32, WHITE, True, font="Montserrat")
    add_text(s1, 0.6, 4.85, 7.1, 0.7, "CONSULTANCY (PVT) LTD", 30, GOLD_LT, True, font="Montserrat")
    add_rect(s1, 0.6, 5.75, 0.06, 1.15, GOLD)
    add_text(s1, 0.8, 5.72, 6.8, 1.2, "A premier Sri Lanka-based multidisciplinary management and investment consultancy firm serving as your strategic bridge and execution partner for market entry, project development, sustainability, certification readiness, BPO setup, and digital growth.", 10.5, WHITE, False, font="Montserrat")

    pillars = [
        ("01 • INVESTMENT & M&A", "Market Entry, BOI & Port City Advisory, Project Structuring"),
        ("02 • ESG & STANDARDS", "Sustainability Frameworks, Carbon Accounting & ISO Readiness"),
        ("03 • BPO & DIGITAL", "Shared Services Setup, AI/CRM Automation & Digital Growth"),
    ]
    for idx, (t, d) in enumerate(pillars):
        px = 0.6 + idx * 2.4
        add_round_rect(s1, px, 7.3, 2.25, 1.1, NAVY_MID, GOLD, 0.75)
        add_text(s1, px + 0.12, 7.4, 2.0, 0.25, t, 7.5, GOLD_LT, True, font="Montserrat")
        add_text(s1, px + 0.12, 7.68, 2.0, 0.6, d, 8, WHITE, True, font="Montserrat")

    add_rect(s1, 4.5, 9.5, 3.77, 0.6, GOLD)
    add_text(s1, 4.6, 9.58, 3.5, 0.45, "“Success Beyond Boundaries”", 15, NAVY, True, True, font="Georgia", align=PP_ALIGN.CENTER)
    add_rect(s1, 0, 10.85, 8.27, 0.84, NAVY)
    add_rect(s1, 0, 10.82, 8.27, 0.04, GOLD)
    add_text(s1, 0.6, 11.08, 7.1, 0.35, "HQ: #14, Basement Level, Cinnamon Lakeside Hotel, Colombo 02  |  www.destinationconsultancy.com  |  +94 11 233 6116", 8, WHITE, False, font="Montserrat")

    # Slide 2: About Us & 4-Step Methodology
    s2 = prs.slides.add_slide(blank)
    header_footer(s2, 2, "CORPORATE OVERVIEW • WHO WE ARE")
    add_text(s2, 0.5, 1.15, 5.0, 0.25, "CORPORATE OVERVIEW • WHO WE ARE", 7.5, GOLD, True, font="Montserrat")
    add_text(s2, 0.5, 1.38, 7.2, 0.45, "A MULTIDISCIPLINARY ADVISORY PARTNER", 18, NAVY, True, font="Montserrat")
    add_round_rect(s2, 0.5, 1.95, 7.27, 1.85, NAVY, GOLD, 1)
    add_text(s2, 0.68, 2.08, 6.9, 1.6, "Destination Consultancy (Private) Limited is a premier, Sri Lanka-based multidisciplinary management and investment consultancy firm headquartered in Colombo. Positioned at the crossroads of South Asian commerce, we serve as a strategic bridge and execution partner for international investors, global corporations, development agencies, and domestic enterprises.\n\nWhether evaluating market entry under BOI or Colombo Port City frameworks, aligning with international ISO and ESG standards, or building a BPO centre or digital growth engine, we provide integrated end-to-end solutions.", 8.8, WHITE, False, font="Montserrat")

    add_round_rect(s2, 0.5, 4.0, 3.52, 1.55, BG_SOFT, TEAL, 1)
    add_text(s2, 0.65, 4.12, 3.2, 0.3, "OUR VISION", 10, NAVY, True, font="Montserrat")
    add_text(s2, 0.65, 4.42, 3.2, 1.0, "To be the most trusted strategic advisory and execution partner for sustainable investment, enterprise transformation, and cross-border business growth in Sri Lanka and the region.", 8.5, NAVY, False, font="Montserrat")

    add_round_rect(s2, 4.25, 4.0, 3.52, 1.55, GOLD_PALE, GOLD, 1)
    add_text(s2, 4.4, 4.12, 3.2, 0.3, "OUR MISSION", 10, NAVY, True, font="Montserrat")
    add_text(s2, 4.4, 4.42, 3.2, 1.0, "To empower investors and enterprises with actionable intelligence, seamless regulatory navigation, sustainable frameworks, and end-to-end operational support.", 8.5, NAVY, False, font="Montserrat")

    add_text(s2, 0.5, 5.75, 6.0, 0.25, "OUR CORE PILLARS", 7.5, GOLD, True, font="Montserrat")
    pillars4 = [
        ("STRATEGIC INSIGHT", "Data-driven feasibility studies, market intelligence & commercial structuring."),
        ("REGULATORY NAVIGATION", "Direct coordination across BOI, Port City Colombo & line ministries."),
        ("HANDS-ON EXECUTION", "Supporting incorporation, recruitment, facility setup & launch."),
        ("GLOBAL STANDARDS", "Aligning enterprises with international ISO, ESG & digital best practices."),
    ]
    for i, (pt, pd) in enumerate(pillars4):
        x = 0.5 + i * 1.84
        add_round_rect(s2, x, 6.05, 1.74, 1.5, WHITE, TEAL, 0.75)
        add_text(s2, x + 0.1, 6.15, 1.54, 0.35, pt, 7.5, NAVY, True, font="Montserrat")
        add_text(s2, x + 0.1, 6.52, 1.54, 0.95, pd, 7.2, MUTED, False, font="Montserrat")

    add_text(s2, 0.5, 7.75, 6.5, 0.25, "HOW WE WORK • A CLEAR 4-STEP PATH", 7.5, GOLD, True, font="Montserrat")
    steps = [
        ("01", "DISCOVER", "Understand commercial objectives, market context, regulatory needs & operational priorities."),
        ("02", "STRUCTURE", "Design the right market-entry, project finance, compliance, operating or growth model."),
        ("03", "EXECUTE", "Coordinate statutory approvals, documentation, partners, facility setup & delivery milestones."),
        ("04", "SCALE", "Support ongoing operational optimisation, ISO/ESG governance, digital adoption & expansion."),
    ]
    for i, (sn, st, sd) in enumerate(steps):
        x = 0.5 + i * 1.84
        add_round_rect(s2, x, 8.05, 1.74, 2.6, NAVY, GOLD, 1)
        add_text(s2, x + 0.12, 8.15, 1.5, 0.4, sn, 16, GOLD_LT, True, font="Montserrat")
        add_text(s2, x + 0.12, 8.58, 1.5, 0.3, st, 9, WHITE, True, font="Montserrat")
        add_text(s2, x + 0.12, 8.92, 1.5, 1.5, sd, 7.5, WHITE, False, font="Montserrat")

    # Slide 3: Board of Directors (4 Authentic Directors)
    s3 = prs.slides.add_slide(blank)
    header_footer(s3, 3, "LEADERSHIP & GOVERNANCE")
    add_text(s3, 0.5, 1.15, 5.0, 0.25, "LEADERSHIP & GOVERNANCE • SENIOR INVOLVEMENT", 7.5, GOLD, True, font="Montserrat")
    add_text(s3, 0.5, 1.38, 7.2, 0.45, "BOARD OF DIRECTORS", 18, NAVY, True, font="Montserrat")

    dirs = [
        ("Shaameel Mohideen", "Executive Director & CEO – Investment Facilitation & Market Entry", "MBA (Aus), CMA (Aus), MABE (UK), FCPM, AM (SLIM), FSLID, JP", "dir_shaameel.jpg", "Specialises in BOI and Port City Colombo advisory, government approvals, market entry, corporate services, project structuring, and cross-border partnerships. Provides institutional navigation and investor facilitation."),
        ("Azad Hamdoon", "Director – Sustainable Infrastructure & Project Development", "15+ Years in Renewable Energy, Waste Management & Agribusiness", "dir_azad.jpg", "Brings over 15 years of leadership in renewable energy, waste management, agribusiness infrastructure, and project development. Leads sustainability-linked projects, clean-energy transitions, and on-ground execution."),
        ("Faazil Ibrahim", "Director – Strategy, Digital Transformation & Business Growth", "20+ Years Across GCC & South Asia Operations & Digital Strategy", "dir_faazil.jpg", "Over 20 years of senior experience across customer success, business operations, digital strategy, and revenue growth in the GCC and South Asia. Connects strategy to execution through BPO capability and digital transformation."),
        ("Eardley Kern", "Director – Capital Markets & Investment Advisory", "32+ Years in Capital Markets, Financial Services & Corporate Performance", "dir_eardley.jpg", "Over 32 years of executive leadership in capital markets and financial services, combining an investment and corporate-performance perspective with marketing leadership. Strengthens funding strategy and investment readiness."),
    ]
    for idx, (name, role, creds, img_file, bio) in enumerate(dirs):
        col = idx % 2
        row = idx // 2
        x = 0.5 + col * 3.72
        y = 1.98 + row * 3.85
        add_round_rect(s3, x, y, 3.55, 3.65, WHITE, TEAL, 0.75)
        add_rect(s3, x, y, 3.55, 1.15, NAVY)
        s3.shapes.add_picture(os.path.join(assets, img_file), Inches(x + 0.15), Inches(y + 0.15), width=Inches(0.85), height=Inches(0.85))
        add_text(s3, x + 1.1, y + 0.12, 2.35, 0.28, name, 10, WHITE, True, font="Montserrat")
        add_text(s3, x + 1.1, y + 0.38, 2.35, 0.38, role, 6.8, GOLD_LT, True, font="Montserrat")
        add_text(s3, x + 1.1, y + 0.78, 2.35, 0.32, creds, 6.2, WHITE, False, font="Montserrat")
        add_text(s3, x + 0.15, y + 1.25, 3.25, 2.2, bio, 8, NAVY, False, font="Montserrat")

    add_round_rect(s3, 0.5, 9.75, 7.27, 1.05, NAVY, GOLD, 1)
    add_text(s3, 0.7, 9.85, 6.9, 0.25, "INTEGRATED BOARD-LEVEL STEWARDSHIP", 7.5, GOLD_LT, True, font="Montserrat")
    add_text(s3, 0.7, 10.1, 6.9, 0.6, "Together, our four directors cover the full commercial lifecycle—Market Entry, Capital Structuring, Sustainable Infrastructure, and Digital & Operational Growth.", 8, WHITE, False, font="Montserrat")

    # Slide 4: Connected Services Part I (01 - 03)
    s4 = prs.slides.add_slide(blank)
    header_footer(s4, 4, "CONNECTED SERVICES • PART I")
    add_text(s4, 0.5, 1.15, 5.5, 0.25, "SIX CONNECTED PRACTICE AREAS • PART I", 7.5, GOLD, True, font="Montserrat")
    add_text(s4, 0.5, 1.38, 7.2, 0.45, "INVESTMENT, M&A & SUSTAINABILITY", 18, NAVY, True, font="Montserrat")

    s_part1 = [
        ("01", "INVESTMENT, FEASIBILITY STUDY & MARKET ENTRY", "We guide foreign and domestic investors from initial exploration to legal establishment and commercial launch in Sri Lanka.", "• Market-entry strategy & commercial viability assessments\n• BOI & Port City Colombo advisory & applications\n• Government, ministry & line-agency approvals & licensing\n• Company incorporation, secretarial & legal set-up", "• Investment opportunity assessment & site selection\n• Foreign investor support, visas & banking coordination\n• Local representation & stakeholder engagement\n• Tax holiday & duty-free concession structuring"),
        ("02", "PROJECT DEVELOPMENT, MERGERS & ACQUISITIONS", "We transform high-potential concepts into bankable, investment-ready projects and guide corporate transactions with financial discipline.", "• Bankable feasibility studies & financial models\n• Investor-grade business plans, pitch decks & IMs\n• End-to-end project structuring (PPP, BOT, BOO)\n• Project financing facilitation & capital-market advisory", "• JV & strategic local/foreign partner matchmaking\n• Mergers & acquisitions (M&A) buy/sell-side advisory\n• Project management office (PMO) setup & oversight\n• Valuation reviews & pre-transaction readiness"),
        ("03", "SUSTAINABILITY & ESG ADVISORY", "We help organisations embed Environmental, Social, and Governance (ESG) principles into their core strategy and daily operations.", "• Corporate sustainability strategy & ESG frameworks\n• Organizational & product carbon-footprint (GHG)\n• Sustainability reporting (GRI & ISSB / IFRS S1 & S2)", "• Renewable-energy transition & green project advisory\n• Circular-economy solutions & resource efficiency\n• Sustainable supply chains & UN SDG alignment"),
    ]
    for i, (num, title, intro, col1, col2) in enumerate(s_part1):
        y = 1.98 + i * 2.95
        add_round_rect(s4, 0.5, y, 7.27, 2.75, WHITE, TEAL, 0.75)
        add_rect(s4, 0.5, y, 7.27, 0.52, NAVY)
        add_round_rect(s4, 0.65, y + 0.08, 0.45, 0.36, GOLD)
        add_text(s4, 0.65, y + 0.12, 0.45, 0.3, num, 9, NAVY, True, font="Montserrat", align=PP_ALIGN.CENTER)
        add_text(s4, 1.2, y + 0.12, 6.3, 0.3, title, 10, WHITE, True, font="Montserrat")
        add_text(s4, 0.65, y + 0.6, 6.95, 0.55, intro, 8, NAVY, False, font="Montserrat")
        add_text(s4, 0.65, y + 1.18, 3.4, 1.45, col1, 7.6, MUTED, False, font="Montserrat")
        add_text(s4, 4.15, y + 1.18, 3.4, 1.45, col2, 7.6, MUTED, False, font="Montserrat")

    # Slide 5: Connected Services Part II (04 - 06)
    s5 = prs.slides.add_slide(blank)
    header_footer(s5, 5, "CONNECTED SERVICES • PART II")
    add_text(s5, 0.5, 1.15, 5.5, 0.25, "SIX CONNECTED PRACTICE AREAS • PART II", 7.5, GOLD, True, font="Montserrat")
    add_text(s5, 0.5, 1.38, 7.2, 0.45, "ISO SYSTEMS, BPO & DIGITAL GROWTH", 18, NAVY, True, font="Montserrat")

    s_part2 = [
        ("04", "CERTIFICATION & MANAGEMENT SYSTEMS", "End-to-end advisory and implementation support to prepare your organisation for third-party ISO certification audits.", "• ISO 9001: Quality Management Systems\n• ISO 14001: Environmental Management Systems\n• ISO 45001: Occupational Health & Safety\n• ISO 27001: Information Security Management", "• ISO 22301: Business Continuity Management\n• ISO 22000 / HACCP: Food Safety Management\n• Gap assessments, policy/SOP drafting & training\n• Pre-audit readiness reviews (accredited body certifies)"),
        ("05", "BPO SETUP & SHARED SERVICES SUPPORT", "Turnkey BPO setup and operational scaling for international companies building captive shared-service centres or outsourcing hubs.", "• BPO feasibility studies & operating-model design\n• Incorporation, BOI IT/BPO concessions & facility setup\n• Talent acquisition strategy, recruitment & onboarding", "• End-to-end process mapping, SLA definition & SOPs\n• Quality assurance (QA) & KPI performance systems\n• Technology stack setup, IT & data security"),
        ("06", "DIGITAL GROWTH & TECHNOLOGY", "Combining strategic marketing, modern search visibility (SEO/AEO/GEO), software engineering, and enterprise IT support.", "• Digital strategy, B2B/B2C demand & lead generation\n• Brand identity, positioning & content strategy\n• Search visibility across SEO, AEO & GEO", "• Custom website, portal & enterprise app development\n• CRM implementation & marketing automation\n• Data analytics, BI dashboards, AI & managed IT"),
    ]
    for i, (num, title, intro, col1, col2) in enumerate(s_part2):
        y = 1.98 + i * 2.95
        add_round_rect(s5, 0.5, y, 7.27, 2.75, WHITE, TEAL, 0.75)
        add_rect(s5, 0.5, y, 7.27, 0.52, NAVY)
        add_round_rect(s5, 0.65, y + 0.08, 0.45, 0.36, GOLD)
        add_text(s5, 0.65, y + 0.12, 0.45, 0.3, num, 9, NAVY, True, font="Montserrat", align=PP_ALIGN.CENTER)
        add_text(s5, 1.2, y + 0.12, 6.3, 0.3, title, 10, WHITE, True, font="Montserrat")
        add_text(s5, 0.65, y + 0.6, 6.95, 0.55, intro, 8, NAVY, False, font="Montserrat")
        add_text(s5, 0.65, y + 1.18, 3.4, 1.45, col1, 7.6, MUTED, False, font="Montserrat")
        add_text(s5, 4.15, y + 1.18, 3.4, 1.45, col2, 7.6, MUTED, False, font="Montserrat")

    # Slide 6: Why Sri Lanka & The Five-Hub Vision
    s6 = prs.slides.add_slide(blank)
    header_footer(s6, 6, "WHY SRI LANKA & 5-HUB VISION")
    add_text(s6, 0.5, 1.15, 5.5, 0.25, "DESTINATION SRI LANKA • STRATEGIC INVESTMENT GATEWAY", 7.5, GOLD, True, font="Montserrat")
    add_text(s6, 0.5, 1.38, 7.2, 0.45, "WHY SRI LANKA & THE FIVE-HUB VISION", 18, NAVY, True, font="Montserrat")
    add_round_rect(s6, 0.5, 1.95, 7.27, 1.2, NAVY, GOLD, 1)
    add_text(s6, 0.65, 2.05, 6.95, 1.0, "Positioned at the centre of the Indian Ocean along the world’s busiest East–West maritime trade route, Sri Lanka offers unmatched connectivity to South Asia, the Middle East, Africa, East Asia, and Europe—combining deep-water ports, Colombo Port City, and an educated workforce.", 8.5, WHITE, False, font="Montserrat")

    stats = [("65,610 km²", "TOTAL LAND AREA"), ("445 × 225 km", "LENGTH × WIDTH"), ("27.5 °C", "MEAN TEMPERATURE"), ("Since 1948", "SOVEREIGN REPUBLIC")]
    for i, (sv, sl) in enumerate(stats):
        x = 0.5 + i * 1.84
        add_round_rect(s6, x, 3.3, 1.74, 0.95, NAVY, GOLD, 0.75)
        add_text(s6, x, 3.4, 1.74, 0.4, sv, 13, GOLD_LT, True, font="Montserrat", align=PP_ALIGN.CENTER)
        add_text(s6, x, 3.82, 1.74, 0.3, sl, 7, WHITE, True, font="Montserrat", align=PP_ALIGN.CENTER)

    add_text(s6, 0.5, 4.42, 6.0, 0.25, "THE FIVE-HUB STRATEGIC FRAMEWORK", 7.5, GOLD, True, font="Montserrat")
    hubs = [
        ("HUB 01", "MARITIME HUB", "Deep-water ports in Colombo, Hambantota & Trincomalee serving East–West shipping lanes."),
        ("HUB 02", "AVIATION HUB", "Expanding international air cargo & passenger connectivity across South Asia, GCC & APAC."),
        ("HUB 03", "COMMERCIAL HUB", "Colombo Port City & modernised BOI regimes creating an offshore financial centre."),
        ("HUB 04", "ENERGY HUB", "Abundant solar, wind, hydro & green-hydrogen potential driving clean-energy investment."),
        ("HUB 05", "KNOWLEDGE HUB", "High literacy, English proficiency & globally recognised accounting, IT & engineering talent."),
    ]
    for i, (hn, ht, hd) in enumerate(hubs):
        x = 0.5 + i * 1.47
        add_round_rect(s6, x, 4.72, 1.39, 2.2, BG_SOFT, TEAL, 0.75)
        add_text(s6, x + 0.08, 4.8, 1.2, 0.25, hn, 7, GOLD, True, font="Montserrat")
        add_text(s6, x + 0.08, 5.05, 1.2, 0.35, ht, 8, NAVY, True, font="Montserrat")
        add_text(s6, x + 0.08, 5.45, 1.2, 1.4, hd, 6.8, MUTED, False, font="Montserrat")

    add_text(s6, 0.5, 7.1, 6.0, 0.25, "HIGH-POTENTIAL INVESTMENT SECTORS", 7.5, GOLD, True, font="Montserrat")
    sectors = [
        ("RENEWABLE ENERGY", "Utility-scale solar, wind, biomass, mini-hydro, battery storage & waste-to-energy."),
        ("BPO, IT & SHARED SERVICES", "Finance & accounting, software engineering, AI data ops & customer experience."),
        ("TOURISM & HOSPITALITY", "Luxury eco-resorts, wellness tourism, integrated marinas & boutique hotels."),
        ("SUSTAINABLE AGRIBUSINESS", "Value-added Ceylon tea, spices, coconut derivatives, aquaculture & cold-chain."),
        ("EXPORT MANUFACTURING", "High-value apparel, rubber products, electronics assembly & pharmaceuticals."),
        ("URBAN INFRASTRUCTURE", "Commercial towers, mixed-use Port City developments, industrial zones & healthcare."),
    ]
    for i, (st, sd) in enumerate(sectors):
        col = i % 3
        row = i // 3
        x = 0.5 + col * 2.46
        y = 7.4 + row * 1.65
        add_round_rect(s6, x, y, 2.35, 1.5, WHITE, TEAL, 0.75)
        add_text(s6, x + 0.12, y + 0.12, 2.1, 0.3, st, 8, NAVY, True, font="Montserrat")
        add_text(s6, x + 0.12, y + 0.45, 2.1, 0.95, sd, 7.2, MUTED, False, font="Montserrat")

    # Slide 7: Regulatory & Institutional Gateway (Replaces Council Memberships!)
    s7 = prs.slides.add_slide(blank)
    header_footer(s7, 7, "INVESTOR FACILITATION & REGULATORY GATEWAY")
    add_text(s7, 0.5, 1.15, 6.0, 0.25, "INSTITUTIONAL NAVIGATION • REGULATORY CLEARANCES", 7.5, GOLD, True, font="Montserrat")
    add_text(s7, 0.5, 1.38, 7.2, 0.45, "INVESTOR FACILITATION & GATEWAY", 18, NAVY, True, font="Montserrat")

    gateways = [
        ("BOI", "Board of Investment Approvals", "Full lifecycle representation under Section 17 (special incentive regime) and Section 16 (normal law foreign investment entry) of the BOI Act.\n• Investment application preparation & financial projections\n• Negotiation & execution of BOI Investment Agreements\n• Customs duty-free import clearance for project capital goods\n• Expatriate entry permits & residence visa recommendations"),
        ("CPCC", "Colombo Port City Advisory", "Advisory for international businesses establishing offshore entities inside the Colombo Port City Special Economic Zone.\n• Authorised Person (AP) licensing & offshore registration\n• Business of Strategic Importance (BSI) incentive structuring\n• Designated foreign-currency banking & capital mobility\n• Leasehold plot & commercial office space coordination"),
        ("CBSL", "Foreign Exchange & Banking", "Compliant capital inflow structuring under the Foreign Exchange Act and Central Bank of Sri Lanka (CBSL) directions.\n• Inward Investment Account (IIA) opening with licensed banks\n• Equity remittance, shareholder loan & repatriation structuring\n• ROC eBiz company incorporation & corporate secretarial setup\n• IRD tax registration (TIN, Corporate Income Tax, VAT, SVAT)"),
        ("LINE", "Line-Ministry & Sector Approvals", "Multi-agency environmental, municipal, and sector-specific approvals required for physical project execution.\n• Central Environmental Authority (CEA) IEE / EIA & EPL clearances\n• Urban Development Authority (UDA) & local authority permits\n• Sri Lanka Sustainable Energy Authority (SLSEA) & CEB approvals\n• Sri Lanka Tourism Development Authority (SLTDA) licensing"),
    ]
    for i, (code, title, body) in enumerate(gateways):
        col = i % 2
        row = i // 2
        x = 0.5 + col * 3.72
        y = 2.0 + row * 3.7
        add_round_rect(s7, x, y, 3.55, 3.5, WHITE, TEAL, 0.75)
        add_rect(s7, x, y, 3.55, 0.52, NAVY)
        add_round_rect(s7, x + 0.12, y + 0.08, 0.58, 0.36, GOLD)
        add_text(s7, x + 0.12, y + 0.12, 0.58, 0.28, code, 8, NAVY, True, font="Montserrat", align=PP_ALIGN.CENTER)
        add_text(s7, x + 0.8, y + 0.12, 2.65, 0.3, title, 9.5, WHITE, True, font="Montserrat")
        add_text(s7, x + 0.15, y + 0.62, 3.25, 2.7, body, 7.8, NAVY, False, font="Montserrat")

    add_round_rect(s7, 0.5, 9.55, 7.27, 1.2, NAVY, GOLD, 1)
    add_text(s7, 0.7, 9.68, 6.9, 0.95, "SINGLE-WINDOW EXECUTION ADVANTAGE: Rather than managing separate legal, engineering, environmental, and corporate consultants, investors rely on Destination Consultancy as a unified project management office (PMO) that coordinates every regulatory milestone from day one.", 8.3, WHITE, False, font="Montserrat")

    # Slide 8: Representative Advisory Mandates
    s8 = prs.slides.add_slide(blank)
    header_footer(s8, 8, "REPRESENTATIVE ADVISORY MANDATES")
    add_text(s8, 0.5, 1.15, 6.0, 0.25, "INDUSTRIES & PROJECTS • PRACTICAL EXECUTION", 7.5, GOLD, True, font="Montserrat")
    add_text(s8, 0.5, 1.38, 7.2, 0.45, "REPRESENTATIVE ADVISORY MANDATES", 18, NAVY, True, font="Montserrat")

    mandates = [
        ("01 • INFRASTRUCTURE & MIXED-USE", "Market Entry & Regulatory Structuring", "Structured local incorporation, BOI application strategy, line-ministry approvals, and land/lease due diligence for a regional development consortium entering Sri Lanka."),
        ("02 • RENEWABLE ENERGY & CLEAN TECH", "Feasibility & Sustainability Framework", "Delivered commercial feasibility modelling, environmental alignment, grid-connection coordination, and ESG reporting frameworks for a utility-scale solar and biomass initiative."),
        ("03 • BPO & KNOWLEDGE SERVICES", "Turnkey Shared-Services Center Setup", "Designed the operating model, secured BOI IT/BPO concessions, established facility infrastructure, mapped SOPs, and guided initial recruitment for a GCC-backed support hub in Colombo."),
        ("04 • EXPORT MANUFACTURING", "Integrated ISO Systems Readiness", "Conducted gap assessments, developed integrated manuals, trained internal auditor teams, and prepared an export manufacturer for successful ISO 9001, 14001 & 45001 audits."),
        ("05 • TECHNOLOGY & DIGITAL", "Digital Transformation & Demand Gen", "Rebuilt corporate digital presence, implemented CRM pipeline automation, and deployed SEO, AEO, and GEO content strategies to expand international B2B inbound inquiries."),
        ("06 • TOURISM & HOSPITALITY", "Eco-Resort Investment Advisory", "Advised foreign promoters on SLTDA approvals, environmental clearances, capital structuring, and sustainable operations for a boutique coastal hospitality asset."),
    ]
    for i, (sec, title, desc) in enumerate(mandates):
        col = i % 2
        row = i // 2
        x = 0.5 + col * 3.72
        y = 2.0 + row * 2.5
        add_round_rect(s8, x, y, 3.55, 2.3, WHITE, GOLD if i % 2 else TEAL, 1)
        add_text(s8, x + 0.15, y + 0.12, 3.25, 0.25, sec, 7, TEAL, True, font="Montserrat")
        add_text(s8, x + 0.15, y + 0.38, 3.25, 0.35, title, 9.5, NAVY, True, font="Montserrat")
        add_text(s8, x + 0.15, y + 0.78, 3.25, 1.35, desc, 7.8, MUTED, False, font="Montserrat")

    add_round_rect(s8, 0.5, 9.65, 7.27, 1.1, GOLD_PALE, GOLD, 1)
    add_text(s8, 0.7, 9.8, 6.9, 0.8, "LOOKING FOR INVESTMENT OPPORTUNITIES OR PROJECT MATCHMAKING?\nWe maintain an active pipeline of vetted Sri Lankan projects in renewable energy, hospitality, agribusiness, BPO, and manufacturing.", 8.2, NAVY, True, font="Montserrat")

    # Slide 9: Contact Us
    s9 = prs.slides.add_slide(blank)
    header_footer(s9, 9, "CONNECT WITH OUR ADVISORY TEAM")
    add_text(s9, 0.5, 1.15, 5.5, 0.25, "CONNECT WITH OUR ADVISORY TEAM", 7.5, GOLD, True, font="Montserrat")
    add_text(s9, 0.5, 1.38, 7.2, 0.45, "CONTACT US", 18, NAVY, True, font="Montserrat")

    add_round_rect(s9, 0.5, 2.0, 7.27, 4.5, NAVY, GOLD, 1.5)
    s9.shapes.add_picture(os.path.join(assets, "icon_compass.png"), Inches(0.75), Inches(2.2), height=Inches(0.65))
    add_text(s9, 1.5, 2.25, 4.0, 0.5, "Destination Consultancy (Pvt) Ltd", 14, WHITE, True, font="Montserrat")
    s9.shapes.add_picture(os.path.join(assets, "logo_white.png"), Inches(5.6), Inches(2.22), height=Inches(0.55))

    add_text(s9, 0.75, 3.1, 4.4, 3.1, "REGISTERED OFFICE ADDRESS:\n#14, Basement Level, Cinnamon Lakeside Hotel,\nNo. 115, Sir Chittampalam A. Gardiner Mawatha,\nColombo 02, Sri Lanka.\n\nTELEPHONE & DIRECT HOTLINES:\nGeneral Lines: +94 11 233 6116  |  +94 11 249 2821\nDirect Hotlines: +94 77 779 0919  |  +94 75 675 3877\n\nDIGITAL & OFFICIAL PORTAL:\nEmail: info@destinationconsultancy.com\nWebsite: www.destinationconsultancy.com", 8.8, WHITE, False, font="Montserrat")

    add_round_rect(s9, 5.35, 3.1, 2.15, 3.1, WHITE, GOLD, 1.5)
    s9.shapes.add_picture(os.path.join(assets, "qr_website.png"), Inches(5.58), Inches(3.25), width=Inches(1.7), height=Inches(1.7))
    add_text(s9, 5.4, 5.05, 2.05, 0.6, "SCAN TO VISIT WEBSITE\ndestinationconsultancy.com", 7.5, NAVY, True, font="Montserrat", align=PP_ALIGN.CENTER)

    add_round_rect(s9, 0.5, 6.85, 7.27, 3.8, NAVY_MID, GOLD, 1)
    add_text(s9, 0.75, 7.2, 6.7, 0.4, "SCHEDULE AN EXECUTIVE CONSULTATION", 9, GOLD_LT, True, font="Montserrat")
    add_text(s9, 0.75, 7.7, 6.7, 0.6, "“Success Beyond Boundaries”", 20, WHITE, True, True, font="Georgia")
    add_text(s9, 0.75, 8.4, 6.7, 1.5, "Strategic Insight  •  Regulatory Navigation  •  Hands-On Execution\n\nMarket Entry & BOI  |  Project Structuring & M&A  |  Sustainability & ESG  |  ISO Readiness  |  BPO Setup  |  Digital Growth", 9, WHITE, False, font="Montserrat")

    out = os.path.join(base, "destination consultancy", "Company Profile - 2026.pptx")
    prs.save(out)
    print("Saved:", out)

# ==============================================================================
# 2. SPILLBURG CORPORATE SERVICES PPTX
# ==============================================================================
def build_corporate_pptx():
    prs = Presentation()
    prs.slide_width = Inches(8.27)
    prs.slide_height = Inches(11.69)
    blank = prs.slide_layouts[6]
    assets = os.path.join(base, "spillburg corporate services", "assets")

    ROYAL = RGBColor(0, 0, 77)
    ROYAL_DARK = RGBColor(0, 0, 56)
    COBALT = RGBColor(23, 61, 237)
    GOLD = RGBColor(197, 160, 89)
    GOLD_LT = RGBColor(223, 192, 130)
    ICE_BG = RGBColor(244, 246, 251)
    WHITE = RGBColor(255, 255, 255)
    MUTED = RGBColor(74, 85, 120)

    def header_footer(slide, page_no, sec_sub="COMPLIANCE. ASSURANCE. ACCELERATE GROWTH."):
        add_rect(slide, 0, 0, 8.27, 0.88, ROYAL)
        add_rect(slide, 0, 0.88, 5.2, 0.05, COBALT)
        add_rect(slide, 5.2, 0.88, 3.07, 0.05, GOLD)
        add_rect(slide, 0, 0.93, 0.09, 10.22, COBALT)
        add_round_rect(slide, 0.45, 0.14, 2.25, 0.58, WHITE)
        slide.shapes.add_picture(os.path.join(assets, "logo_corporate.png"), Inches(0.55), Inches(0.21), height=Inches(0.44))
        add_text(slide, 3.2, 0.2, 4.6, 0.25, "COMPLIANCE. ASSURANCE. ACCELERATE GROWTH.", 8, WHITE, True, font="Segoe UI", align=PP_ALIGN.RIGHT)
        add_text(slide, 3.2, 0.45, 4.6, 0.25, sec_sub, 7, GOLD_LT, True, font="Segoe UI", align=PP_ALIGN.RIGHT)

        add_rect(slide, 0, 11.15, 8.27, 0.54, ROYAL_DARK)
        add_rect(slide, 0, 11.12, 8.27, 0.03, COBALT)
        add_text(slide, 0.45, 11.25, 5.5, 0.3, "SPILLBURG CORPORATE SERVICES (PVT) LTD  |  WWW.SPILLBURGCORPORATE.COM", 7.5, WHITE, False, font="Segoe UI")
        add_round_rect(slide, 7.05, 11.23, 0.75, 0.32, COBALT, GOLD, 0.75)
        add_text(slide, 7.05, 11.25, 0.75, 0.28, f"PAGE {page_no:02d}", 7.5, WHITE, True, font="Segoe UI", align=PP_ALIGN.CENTER)

    # Slide 1: Cover
    s1 = prs.slides.add_slide(blank)
    s1.shapes.add_picture(os.path.join(assets, "cover_hero.jpg"), Inches(0), Inches(0), width=Inches(8.27), height=Inches(11.69))
    ov = add_rect(s1, 0, 0, 8.27, 11.69, ROYAL_DARK)
    ov.fill.transparency = 0.12
    add_round_rect(s1, 0.55, 0.45, 7.17, 1.0, WHITE, GOLD, 1.5)
    s1.shapes.add_picture(os.path.join(assets, "logo_corporate.png"), Inches(0.8), Inches(0.62), height=Inches(0.65))
    add_text(s1, 4.5, 0.62, 3.0, 0.6, "CORPORATE PROFILE • 2026\nCOLOMBO • SRI LANKA", 8.5, ROYAL, True, font="Segoe UI", align=PP_ALIGN.RIGHT)

    add_rect(s1, 0.6, 3.1, 0.08, 3.8, GOLD)
    add_round_rect(s1, 0.85, 3.1, 4.2, 0.38, COBALT, GOLD_LT, 0.75)
    add_text(s1, 0.95, 3.15, 4.0, 0.28, "ONE-STOP CORPORATE & FINANCIAL ADVISORY", 8, GOLD_LT, True, font="Segoe UI")
    add_text(s1, 0.85, 3.65, 6.8, 0.65, "COMPLIANCE. ASSURANCE.", 28, WHITE, True, font="Segoe UI")
    add_text(s1, 0.85, 4.25, 6.8, 0.65, "Accelerate Growth.", 26, GOLD_LT, True, True, font="Georgia")
    add_text(s1, 0.85, 5.05, 6.6, 1.3, "Spillburg Corporate Services (Private) Limited is your trusted partner for sustainable growth. We assist global enterprises, multinational corporations, and investors with comprehensive internal audit, taxation, accounting, company secretarial, due diligence, M&A, stock market listing, and workforce solutions.", 10, WHITE, False, font="Segoe UI")

    add_round_rect(s1, 0.55, 9.35, 7.17, 1.1, WHITE, COBALT, 1.5)
    cstats = [("15+", "YEARS EXPERIENCE"), ("200+", "GLOBAL CLIENTS"), ("200+", "SUCCESSFUL PROJECTS"), ("100%", "SATISFACTION RATE")]
    for i, (v, l) in enumerate(cstats):
        x = 0.65 + i * 1.75
        add_text(s1, x, 9.48, 1.65, 0.45, v, 18, ROYAL, True, font="Segoe UI", align=PP_ALIGN.CENTER)
        add_text(s1, x, 9.95, 1.65, 0.35, l, 7, MUTED, True, font="Segoe UI", align=PP_ALIGN.CENTER)

    add_rect(s1, 0, 10.9, 8.27, 0.79, ROYAL_DARK)
    add_text(s1, 0.55, 11.12, 7.17, 0.35, "Office 14, Basement Level, Cinnamon Lakeside Hotel, Colombo 02  |  www.spillburgcorporate.com  |  info@spillburg.com", 8, WHITE, False, font="Segoe UI")

    # Slide 2: About Us & Who We Serve
    s2 = prs.slides.add_slide(blank)
    header_footer(s2, 2, "SECTION 01 • CORPORATE IDENTITY")
    add_text(s2, 0.5, 1.1, 6.0, 0.25, "THE SPILLBURG STORY • WHO WE ARE", 7.5, COBALT, True)
    add_text(s2, 0.5, 1.32, 7.2, 0.45, "One-Stop-Shop Corporate Solutions", 18, ROYAL, True)
    add_round_rect(s2, 0.5, 1.88, 7.27, 1.75, ROYAL, GOLD, 1)
    add_text(s2, 0.68, 2.0, 6.9, 1.5, "Founded over 15 years ago, Spillburg Corporate Services (Private) Limited was built on a singular premise: businesses expanding into or operating within Sri Lanka deserve a single, reliable partner capable of handling complex regulatory, financial, secretarial, and operational mandates under one roof.\n\nCombining deep local regulatory intelligence across the ROC, BOI, IRD, CBSL, and CSE with global best practices, we have set up over 150 business ventures during the last 10 years.", 8.6, WHITE, False)

    add_round_rect(s2, 0.5, 3.8, 3.52, 1.4, ICE_BG, COBALT, 1)
    add_text(s2, 0.65, 3.9, 3.2, 0.3, "OUR MISSION", 9.5, ROYAL, True)
    add_text(s2, 0.65, 4.2, 3.2, 0.9, "To empower global and local enterprises with seamless, accurate, and compliant corporate services—transforming complex regulatory challenges into strategic advantages.", 8.2, ROYAL, False)

    add_round_rect(s2, 4.25, 3.8, 3.52, 1.4, ICE_BG, GOLD, 1)
    add_text(s2, 4.4, 3.9, 3.2, 0.3, "OUR VISION", 9.5, ROYAL, True)
    add_text(s2, 4.4, 4.2, 3.2, 0.9, "To be the undisputed premier corporate services and transaction advisory partner in Sri Lanka, recognized globally for unwavering integrity and precision.", 8.2, ROYAL, False)

    add_text(s2, 0.5, 5.4, 7.0, 0.25, "WHO WE SERVE • 150+ BUSINESS VENTURES ESTABLISHED IN THE LAST 10 YEARS", 7.5, COBALT, True)
    segs = [
        ("01. International Investors", "Foreign promoters & funds entering Sri Lanka via BOI or normal law."),
        ("02. Multinational Companies", "Global subsidiaries needing local IFRS accounting, tax & compliance."),
        ("03. Growing SMEs", "Domestic enterprises looking for outsourced finance, tax & HR."),
        ("04. High-Growth Startups", "Founders incorporating and establishing compliant operations."),
        ("05. Project Developers", "Infrastructure & hospitality sponsors requiring structuring & DD."),
        ("06. Expatriate Executives", "Foreign professionals requiring visa, personal tax & corporate support."),
    ]
    for i, (st, sd) in enumerate(segs):
        col = i % 3
        row = i // 3
        x = 0.5 + col * 2.46
        y = 5.7 + row * 1.3
        add_round_rect(s2, x, y, 2.35, 1.18, WHITE, COBALT, 0.75)
        add_text(s2, x + 0.12, y + 0.1, 2.1, 0.3, st, 8, ROYAL, True)
        add_text(s2, x + 0.12, y + 0.42, 2.1, 0.68, sd, 7.2, MUTED, False)

    add_text(s2, 0.5, 8.45, 6.0, 0.25, "PRINCIPLES OF OUR WORK", 7.5, COBALT, True)
    prins = [("Accuracy", "Zero error tolerance across all records."), ("Compliance", "Strict adherence to local & IFRS rules."), ("Confidentiality", "Fiduciary-grade client data security."), ("Timeliness", "On-schedule statutory filings & reports."), ("Insight", "Actionable commercial intelligence.")]
    for i, (pt, pd) in enumerate(prins):
        x = 0.5 + i * 1.47
        add_round_rect(s2, x, 8.75, 1.39, 1.9, ROYAL, GOLD, 0.75)
        add_text(s2, x + 0.08, 8.88, 1.2, 0.3, pt, 8, GOLD_LT, True)
        add_text(s2, x + 0.08, 9.25, 1.2, 1.2, pd, 7.2, WHITE, False)

    # Slide 3: Leadership & Advisory Team
    s3 = prs.slides.add_slide(blank)
    header_footer(s3, 3, "SECTION 02 • EXECUTIVE LEADERSHIP")
    add_text(s3, 0.5, 1.1, 6.0, 0.25, "GOVERNANCE & SENIOR PARTNERS", 7.5, COBALT, True)
    add_text(s3, 0.5, 1.32, 7.2, 0.45, "Leadership & Advisory Team", 18, ROYAL, True)

    leaders = [
        ("M H K M Hameez", "MANAGING DIRECTOR", "BSc. (Hons) University of London • CPM (London) • CPA (Australia)", "dir_hameez.jpg", "Former Director attached to the Investment Promotions Division of the Board of Investment (BOI) of Sri Lanka, bringing over 15 years of hands-on experience setting up projects, corporate structuring, financial due diligence, and cross-border investment advisory across SAFTA, ISLFTA, and SLPFTA."),
        ("Mohideen Shaameel (JP)", "DIRECTOR / CEO", "MABE (UK) • MBA (Sydney) • CMA (Australia) • FCPM • AM SLIM • JP", "dir_shaameel.jpg", "Former trade and corporate banker attached to HSBC and Standard Chartered Bank with over 15 years of senior executive experience in project financing, M&A deal structuring, BOI & Port City regulatory approvals, capital market readiness, and international investor facilitation."),
        ("N H Hameez", "SENIOR TAX & AUDIT CONSULTANT", "Associate Chartered Accountant (ACA) • Certified Practising Accountant (CPA)", None, "Over 15 years of specialized public practice and corporate advisory experience guiding multinational corporations, mega infrastructure projects, and SMEs on IFRS financial reporting, statutory & internal auditing, RAMIS corporate tax compliance, VAT/APIT planning, and IRD tax appeal representation."),
        ("M. I. Razik", "DIRECTOR – LEGAL & SECRETARIAL", "Attorney-at-Law (Sri Lanka) • Commissioner for Oaths • Notary Public", "dir_razik.jpg", "Over 30 years of distinguished legal practice specialising in corporate and commercial law, Companies Act secretarial governance, M&A legal due diligence, shareholder & joint-venture agreements, property conveyancing, and commercial arbitration & dispute resolution."),
    ]
    for i, (name, role, creds, img_f, bio) in enumerate(leaders):
        y = 1.95 + i * 2.15
        add_round_rect(s3, 0.5, y, 7.27, 1.98, ICE_BG if i % 2 else WHITE, COBALT if i % 2 else ROYAL, 1)
        if img_f:
            s3.shapes.add_picture(os.path.join(assets, img_f), Inches(0.68), Inches(y + 0.24), width=Inches(1.4), height=Inches(1.4))
        else:
            add_round_rect(s3, 0.68, y + 0.24, 1.4, 1.4, ROYAL, GOLD, 1)
            add_text(s3, 0.68, y + 0.65, 1.4, 0.6, "NHH\nACA • CPA", 11, GOLD_LT, True, align=PP_ALIGN.CENTER)
        add_text(s3, 2.25, y + 0.15, 3.5, 0.3, name, 11, ROYAL, True)
        add_round_rect(s3, 5.5, y + 0.16, 2.1, 0.28, ROYAL)
        add_text(s3, 5.5, y + 0.18, 2.1, 0.24, role, 6.5, GOLD_LT, True, align=PP_ALIGN.CENTER)
        add_text(s3, 2.25, y + 0.45, 5.3, 0.25, creds, 7.5, COBALT, True)
        add_text(s3, 2.25, y + 0.72, 5.3, 1.15, bio, 7.8, ROYAL, False)

    # Slide 4: Core Services Part I (01 - 04)
    s4 = prs.slides.add_slide(blank)
    header_footer(s4, 4, "SECTION 03 • CORE PRACTICE AREAS (I)")
    add_text(s4, 0.5, 1.1, 6.0, 0.25, "CORE SERVICES PORTFOLIO • PART I (01 – 04)", 7.5, COBALT, True)
    add_text(s4, 0.5, 1.32, 7.2, 0.45, "Finance, Tax, Audit & Workforce", 18, ROYAL, True)

    srvs1 = [
        ("01", "Accounting & Finance", "Financial Intelligence & Control", "Rigorous bookkeeping and reconciliation discipline with executive-level reporting aligned with SLFRS / IFRS and GAAP standards.\n\n• Full-Spectrum Bookkeeping & Statutory Financial Statements\n• Monthly Management Accounts & Financial KPIs\n• Financial & Cashflow Analysis & Forecasting Models\n• Turnkey Outsourced Finance Department Operations"),
        ("02", "Taxation Advisory", "Strategic Planning & Fiscal Adherence", "Forward-thinking tax planning and IRD representation that protects your bottom line while maintaining 100% statutory compliance.\n\n• Corporate Income Tax (CIT) & Annual Returns\n• VAT, SVAT, PAYE / APIT & WHT Filings\n• TIN & IRD RAMIS e-Services Registration\n• Strategic Tax Planning & Tax Appeal Representation"),
        ("03", "Audit & Assurance", "Governance & Independent Assurance", "Independent assurance and 360° internal control evaluations to safeguard enterprise value and eliminate operational vulnerabilities.\n\n• External Statutory Audit Coordination\n• Internal Audit & Forensic Reviews\n• Financial Controls & Enterprise Risk Assessment\n• Statutory Compliance & Board Governance Advisory"),
        ("04", "Payroll & HR Services", "Turnkey Workforce Management", "Frictionless, 100% confidential payroll processing, meticulous documentation, and compliant Sri Lankan employment practices.\n\n• Monthly Payroll Processing, Bank Files & Payslips\n• EPF & ETF Statutory Contributions (C-Forms)\n• Standardized Employment Contracts & Onboarding\n• Shop & Office Act Compliance & Expatriate Visas"),
    ]
    for i, (idx_s, title, sub, body) in enumerate(srvs1):
        col = i % 2
        row = i // 2
        x = 0.5 + col * 3.72
        y = 1.95 + row * 4.4
        add_round_rect(s4, x, y, 3.55, 4.2, WHITE, COBALT if i % 2 else ROYAL, 1)
        add_text(s4, x + 0.15, y + 0.12, 2.8, 0.22, sub.upper(), 6.8, COBALT, True)
        add_text(s4, x + 0.15, y + 0.34, 2.8, 0.35, title, 11, ROYAL, True)
        add_text(s4, x + 2.9, y + 0.15, 0.5, 0.4, idx_s, 15, GOLD, True, font="Georgia", align=PP_ALIGN.RIGHT)
        add_text(s4, x + 0.15, y + 0.78, 3.25, 3.25, body, 8, ROYAL, False)

    # Slide 5: Core Services Part II (05 - 08)
    s5 = prs.slides.add_slide(blank)
    header_footer(s5, 5, "SECTION 04 • CORE PRACTICE AREAS (II)")
    add_text(s5, 0.5, 1.1, 6.0, 0.25, "CORE SERVICES PORTFOLIO • PART II (05 – 08)", 7.5, COBALT, True)
    add_text(s5, 0.5, 1.32, 7.2, 0.45, "Transactions, IPOs & Arbitration", 18, ROYAL, True)

    srvs2 = [
        ("05", "Due Diligence (DD)", "Risk Assessment & Investment Intelligence", "Independent, forensic-grade investigations giving investors, acquirers, and boards 360° visibility into counterparty risk.\n\n• Financial & Quality-of-Earnings (QoE) Due Diligence\n• Legal, Regulatory & Contractual Due Diligence\n• Operational, Commercial & Tax Exposure DD\n• Vendor DD, Red Flag Reviews & Risk Registers"),
        ("06", "M&A & Takeovers", "Strategic Transactions & Restructuring", "Strategic counsel across the full deal lifecycle—from target identification and valuation through negotiation and closing.\n\n• Buy-Side & Sell-Side M&A Transaction Advisory\n• Independent Business Valuations & Fairness Opinions\n• Deal Structuring, Term Sheets & Takeover Defense\n• CBSL, SEC & BOI Regulatory Approvals & Post-Merger"),
        ("07", "Stock Market Listing", "Capital Markets & IPO Advisory", "End-to-end coordination with stockbrokers, lawyers, auditors, SEC, and the Colombo Stock Exchange (CSE).\n\n• IPO Readiness Assessment & Gap Remediation\n• Pre-Listing Corporate & Financial Restructuring\n• Prospectus Preparation & SEC / CSE Submissions\n• Pre-IPO Investor Relations, Post-Listing & Rights Issues"),
        ("08", "Mitigation & Arbitration", "Dispute Resolution & Risk Mitigation", "Forensic financial analysis, contractual risk assessment, and representation across Sri Lanka’s arbitration framework.\n\n• Commercial Arbitration, Mediation & Conciliation\n• Independent Financial & Quantum Expert Witness\n• Pre-Dispute Contractual Risk Audits\n• Regulatory Dispute Navigation & Settlement Advisory"),
    ]
    for i, (idx_s, title, sub, body) in enumerate(srvs2):
        col = i % 2
        row = i // 2
        x = 0.5 + col * 3.72
        y = 1.95 + row * 4.4
        add_round_rect(s5, x, y, 3.55, 4.2, WHITE, COBALT if i % 2 else ROYAL, 1)
        add_text(s5, x + 0.15, y + 0.12, 2.8, 0.22, sub.upper(), 6.8, COBALT, True)
        add_text(s5, x + 0.15, y + 0.34, 2.8, 0.35, title, 11, ROYAL, True)
        add_text(s5, x + 2.9, y + 0.15, 0.5, 0.4, idx_s, 15, GOLD, True, font="Georgia", align=PP_ALIGN.RIGHT)
        add_text(s5, x + 0.15, y + 0.78, 3.25, 3.25, body, 8, ROYAL, False)

    # Slide 6: Entity Incorporation & Secretarial Lifecycle
    s6 = prs.slides.add_slide(blank)
    header_footer(s6, 6, "SECTION 05 • SECRETARIAL & MARKET ENTRY")
    add_text(s6, 0.5, 1.1, 6.0, 0.25, "UNCOMPROMISING CORPORATE EXCELLENCE", 7.5, COBALT, True)
    add_text(s6, 0.5, 1.32, 7.2, 0.45, "Entity Incorporation & Secretarial Lifecycle", 18, ROYAL, True)
    s6.shapes.add_picture(os.path.join(assets, "boardroom_hero.jpg"), Inches(0.5), Inches(1.9), width=Inches(7.27), height=Inches(1.85))
    add_round_rect(s6, 0.5, 3.95, 3.52, 3.2, ICE_BG, COBALT, 1)
    add_text(s6, 0.65, 4.1, 3.2, 0.3, "PHASE I: INCORPORATION & LICENSING", 9.5, ROYAL, True)
    add_text(s6, 0.65, 4.45, 3.2, 2.5, "• Name reservation via Department of Registrar of Companies (ROC eBiz)\n• Drafting bespoke Articles of Association & Shareholder Agreements\n• Private Limited, Public Limited, Overseas Branch & Offshore setups\n• BOI Section 17 / 16 approvals & CBSL Inward Investment Account (IIA) setup", 8.2, ROYAL, False)

    add_round_rect(s6, 4.25, 3.95, 3.52, 3.2, ICE_BG, GOLD, 1)
    add_text(s6, 4.4, 4.1, 3.2, 0.3, "PHASE II: ONGOING SECRETARIAL", 9.5, ROYAL, True)
    add_text(s6, 4.4, 4.45, 3.2, 2.5, "• Acting as Named Registered Company Secretary & Registered Office\n• Filing Annual Returns (Form 15) & maintaining Statutory Registers\n• Share allotments (Form 6), transfers, buybacks & capital reductions\n• Board & AGM minutes, resolutions & director changes (Form 20)", 8.2, ROYAL, False)

    add_round_rect(s6, 0.5, 7.4, 7.27, 3.2, ROYAL, GOLD, 1)
    add_text(s6, 0.7, 7.55, 6.8, 0.35, "WHY GLOBAL ENTERPRISES CHOOSE SPILLBURG CORPORATE SERVICES", 9.5, GOLD_LT, True)
    add_text(s6, 0.7, 8.0, 6.8, 2.4, "01. RELIABLE & PROVEN — A service-oriented firm ensuring absolute delivery and flawless execution on every corporate engagement.\n02. IMPECCABLE TRUST — Unwavering commitment to confidentiality and fiduciary integrity to safeguard our clients' interests.\n03. FRICTIONLESS EXPANSION — Seasoned experts rapidly navigate complex bureaucratic requirements so your operations are hassle-free.\n04. BESPOKE ATTENTION — We dedicate time to deeply understand your corporate architecture, deploying strategically tailored plans.", 8.3, WHITE, False)

    # Slide 7: Important Regulatory & Institutional Links (Replaces Council Memberships!)
    s7 = prs.slides.add_slide(blank)
    header_footer(s7, 7, "SECTION 06 • REGULATORY ECOSYSTEM")
    add_text(s7, 0.5, 1.1, 6.0, 0.25, "SRI LANKAN STATUTORY & INSTITUTIONAL DIRECTORY", 7.5, COBALT, True)
    add_text(s7, 0.5, 1.32, 7.2, 0.45, "Regulatory & Institutional Ecosystem", 18, ROYAL, True)

    reg_cats = [
        ("01 • GOVERNMENT & CORPORATE PORTALS", "• Dept. of Registrar of Companies (ROC eBiz) — drc.gov.lk\n• Board of Investment of Sri Lanka (BOI) — investsrilanka.com\n• Sri Lanka Export Development Board (EDB) — srilankabusiness.com\n• Department of Labour — labourdept.gov.lk"),
        ("02 • FINANCIAL & AUDIT REGULATORS", "• Central Bank of Sri Lanka (CBSL) — cbsl.gov.lk\n• Securities & Exchange Commission (SEC) — sec.gov.lk\n• SL Accounting & Auditing Standards Board — slaasmb.gov.lk\n• Employees' Provident Fund (EPF) — epf.lk"),
        ("03 • TAXATION & REVENUE AUTHORITIES", "• Inland Revenue Department (IRD) — ird.gov.lk\n• IRD RAMIS e-Services Portal — eservices.ird.gov.lk\n• Sri Lanka Customs — customs.gov.lk\n• Ministry of Finance / Treasury — treasury.gov.lk"),
        ("04 • CAPITAL MARKETS & ARBITRATION", "• Colombo Stock Exchange (CSE) & CDS — cse.lk / cds.lk\n• SL National Arbitration Centre (SLNAC) — slnac.org.lk\n• ICLP Arbitration Centre — iclp.lk\n• Bar Association of Sri Lanka (BASL) — basl.lk"),
    ]
    for i, (rt, rb) in enumerate(reg_cats):
        col = i % 2
        row = i // 2
        x = 0.5 + col * 3.72
        y = 1.98 + row * 3.7
        add_round_rect(s7, x, y, 3.55, 3.45, WHITE, COBALT, 0.75)
        add_rect(s7, x, y, 3.55, 0.5, ROYAL)
        add_text(s7, x + 0.15, y + 0.12, 3.25, 0.28, rt, 8, GOLD_LT, True)
        add_text(s7, x + 0.15, y + 0.65, 3.25, 2.65, rb, 8.2, ROYAL, False)

    add_round_rect(s7, 0.5, 9.5, 7.27, 1.2, ROYAL, GOLD, 1)
    add_text(s7, 0.7, 9.65, 6.8, 0.9, "CONTINUOUS REGULATORY INTELLIGENCE: Our technical desk actively tracks real-time gazettes, Inland Revenue circulars, Central Bank Monetary Policy Reviews, and Colombo Stock Exchange listing rule updates so our clients remain ahead of every statutory change.", 8.3, WHITE, False)

    # Slide 8: Client Testimonials & Success Stories
    s8 = prs.slides.add_slide(blank)
    header_footer(s8, 8, "SECTION 07 • CLIENT SUCCESS STORIES")
    add_text(s8, 0.5, 1.1, 6.0, 0.25, "ENDURING PARTNERSHIPS • VERIFIED TRACK RECORD", 7.5, COBALT, True)
    add_text(s8, 0.5, 1.32, 7.2, 0.45, "Client Testimonials & Success Stories", 18, ROYAL, True)

    testis = [
        ("Maneevannan Bhakthavathsalu", "Country Director, ECU World Wide Lanka (Pvt) Ltd", "“We have been using Spillburg services for more than 10 years and have always been completely satisfied with their commitment and overall performance. Knowledgeable, courteous and accessible at any time.”"),
        ("Ross Mayles", "Director, RDM Investments (Pvt) Ltd", "“I have been using Spillburg for a long time now and their service is punctual and efficient. They have a ‘can do’ and ‘work with’ attitude and approach. I would highly recommend them.”"),
        ("Sergey Mikheev", "Founder & CEO, Surf Discovery Lanka (Private) Limited", "“Spillburg Corporate Services is a reliable partner on the way to the success of the company. We are happy to walk together for eight years. Always finds ways and solutions to complex problems.”"),
        ("Qu Yucai", "General Manager, Yanjian Group Lanka (Pvt) Ltd", "“Spillburg Corporate Services has provided us professional services for more than 8 years in Sri Lanka. All the staff are accessible and well educated along with adequate knowledge.”"),
        ("Mr. Shabbir Abidali Jafferjee", "Chairman, Serendib Properties Group of Companies", "“Professional, efficient and get the job done. Have no hesitation in recommending them for corporate and advisory mandates.”"),
        ("Mark Butson", "Director, Sharafi Lanka (Pvt) Ltd", "“Thank you for the excellent corporate secretarial, accounting, and compliance service—greatly appreciated by our board.”"),
    ]
    for i, (au, rl, qt) in enumerate(testis):
        col = i % 2
        row = i // 2
        x = 0.5 + col * 3.72
        y = 1.95 + row * 2.5
        add_round_rect(s8, x, y, 3.55, 2.3, ICE_BG, GOLD if i % 2 else COBALT, 0.75)
        add_text(s8, x + 0.15, y + 0.12, 3.25, 1.45, qt, 7.6, ROYAL, False, True)
        add_text(s8, x + 0.15, y + 1.65, 3.25, 0.25, au, 8, ROYAL, True)
        add_text(s8, x + 0.15, y + 1.9, 3.25, 0.25, rl, 7, COBALT, True)

    add_round_rect(s8, 0.5, 9.6, 7.27, 1.15, WHITE, COBALT, 0.75)
    for idx, p in enumerate(["agoda", "balaji", "royalty", "amtrad", "umms"]):
        s8.shapes.add_picture(os.path.join(assets, f"partner_{p}.png"), Inches(0.8 + idx * 1.38), Inches(9.9), height=Inches(0.5))

    # Slide 9: Contact Us
    s9 = prs.slides.add_slide(blank)
    header_footer(s9, 9, "SECTION 08 • EXECUTIVE CONTACT")
    add_text(s9, 0.5, 1.1, 6.0, 0.25, "START A CONVERSATION • LET'S SHAPE YOUR FUTURE", 7.5, COBALT, True)
    add_text(s9, 0.5, 1.32, 7.2, 0.45, "Consult With Our Experts", 18, ROYAL, True)

    add_round_rect(s9, 0.5, 1.95, 7.27, 4.6, ROYAL, GOLD, 1.5)
    add_text(s9, 0.75, 2.2, 4.5, 0.5, "Spillburg Corporate Services (Private) Limited", 13.5, WHITE, True)
    add_round_rect(s9, 5.5, 2.15, 2.0, 0.58, WHITE)
    s9.shapes.add_picture(os.path.join(assets, "logo_corporate.png"), Inches(5.62), Inches(2.22), height=Inches(0.42))

    add_text(s9, 0.75, 3.05, 4.4, 3.2, "REGISTERED OFFICE LOCATION:\nOffice 14, Basement Level, Cinnamon Lakeside Hotel,\nNo. 115, Sir Chittampalam A. Gardiner Mawatha,\nColombo 02, Sri Lanka.\n\nDIRECT TELEPHONE & FACSIMILE:\nTelephone: +94 11 233 6116\nHotlines: +94 77 779 0919  |  +94 77 748 7720\nFacsimile: +94 11 252 9309\n\nOFFICIAL EMAIL & WEB PORTAL:\nEmail: info@spillburg.com\nWebsite: www.spillburgcorporate.com", 8.8, WHITE, False)

    add_round_rect(s9, 5.35, 3.05, 2.15, 3.15, WHITE, COBALT, 1.5)
    s9.shapes.add_picture(os.path.join(assets, "qr_website.png"), Inches(5.58), Inches(3.2), width=Inches(1.7), height=Inches(1.7))
    add_text(s9, 5.4, 5.0, 2.05, 0.6, "SCAN TO VISIT WEBSITE\nspillburgcorporate.com", 7.5, ROYAL, True, align=PP_ALIGN.CENTER)

    add_round_rect(s9, 0.5, 6.85, 7.27, 3.8, ROYAL_DARK, COBALT, 1)
    add_text(s9, 0.75, 7.25, 6.5, 0.35, "YOUR TRUSTED PARTNER FOR SUSTAINABLE GROWTH", 8.5, GOLD_LT, True)
    add_text(s9, 0.75, 7.7, 6.5, 0.6, "“Compliance. Assurance. Accelerate Growth.”", 19, WHITE, True, True, font="Georgia")
    add_text(s9, 0.75, 8.45, 6.5, 1.5, "15+ Years Experience  •  200+ Global Clients  •  200+ Successful Projects  •  100% Satisfaction Rate", 9, WHITE, False)

    out = os.path.join(base, "spillburg corporate services", "Company Profile - 2026.pptx")
    prs.save(out)
    print("Saved:", out)

# ==============================================================================
# 3. SPILLBURG LOGISTICS 1 PPTX
# ==============================================================================
def build_logistics_pptx():
    prs = Presentation()
    prs.slide_width = Inches(8.27)
    prs.slide_height = Inches(11.69)
    blank = prs.slide_layouts[6]
    assets = os.path.join(base, "spillburg logistics", "assets")

    SLATE = RGBColor(15, 23, 42)
    SLATE_DARK = RGBColor(11, 17, 32)
    OCEAN = RGBColor(2, 132, 199)
    SKY = RGBColor(56, 189, 248)
    AMBER = RGBColor(245, 158, 11)
    TECH_BG = RGBColor(241, 245, 249)
    WHITE = RGBColor(255, 255, 255)
    MUTED = RGBColor(71, 85, 105)

    def header_footer(slide, page_no, code_str="SEC // MULTIMODAL OPERATIONS"):
        add_rect(slide, 0, 0, 8.27, 0.88, SLATE)
        add_rect(slide, 0, 0.88, 5.5, 0.05, OCEAN)
        add_rect(slide, 5.5, 0.88, 2.77, 0.05, AMBER)
        add_rect(slide, 0, 0, 3.3, 0.88, WHITE)
        slide.shapes.add_picture(os.path.join(assets, "logo_logistics_live.png"), Inches(0.35), Inches(0.16), height=Inches(0.54))
        add_text(slide, 3.6, 0.18, 4.2, 0.25, code_str, 7.5, SKY, True, font="Consolas", align=PP_ALIGN.RIGHT)
        add_text(slide, 3.6, 0.44, 4.2, 0.28, "MOVING CARGO. CONNECTING BUSINESSES.", 8.5, WHITE, True, font="Segoe UI", align=PP_ALIGN.RIGHT)

        add_rect(slide, 0, 11.15, 8.27, 0.54, SLATE_DARK)
        add_rect(slide, 0, 11.12, 8.27, 0.03, OCEAN)
        add_text(slide, 0.45, 11.25, 5.5, 0.3, "SPILLBURG LOGISTICS 1 (PVT) LTD // WWW.SPILLBURGLOGISTICS1.COM", 7.5, WHITE, False, font="Consolas")
        add_rect(slide, 7.05, 11.23, 0.75, 0.32, OCEAN)
        add_text(slide, 7.05, 11.25, 0.75, 0.28, f"PAGE {page_no:02d}", 7.5, WHITE, True, font="Consolas", align=PP_ALIGN.CENTER)

    # Slide 1: Cover
    s1 = prs.slides.add_slide(blank)
    s1.shapes.add_picture(os.path.join(assets, "cover_hero.jpg"), Inches(0), Inches(0), width=Inches(8.27), height=Inches(11.69))
    ov = add_rect(s1, 0, 0, 8.27, 11.69, SLATE_DARK)
    ov.fill.transparency = 0.14
    add_rect(s1, 0, 0, 3.9, 1.15, WHITE)
    s1.shapes.add_picture(os.path.join(assets, "logo_logistics_live.png"), Inches(0.45), Inches(0.22), height=Inches(0.68))
    add_rect(s1, 5.1, 0.25, 2.65, 0.65, SLATE, SKY, 1)
    add_text(s1, 5.2, 0.32, 2.45, 0.5, "PORT OF COLOMBO // LKCMB\nCOMPANY PROFILE • 2026", 7.5, AMBER, True, font="Consolas", align=PP_ALIGN.RIGHT)

    add_text(s1, 0.6, 3.6, 7.1, 0.7, "SPILLBURG LOGISTICS 1", 32, WHITE, True)
    add_text(s1, 0.6, 4.25, 7.1, 0.55, "(PRIVATE) LIMITED", 22, SKY, True)
    add_rect(s1, 0.6, 4.95, 4.6, 0.45, AMBER)
    add_text(s1, 0.7, 5.02, 4.4, 0.35, "MOVING CARGO. CONNECTING BUSINESSES.", 12, SLATE_DARK, True)
    add_text(s1, 0.6, 5.65, 6.8, 1.1, "A licensed international Freight Forwarder, Customs House Agent, and Multimodal Logistics Service Provider headquartered in Colombo, Sri Lanka—delivering economical, secure, and time-critical export and import cargo solutions across the globe.", 10, WHITE, False)

    promises = [
        ("[01 // SUPPORT]", "CONTACT 24H", "Dedicated operations & customer support desk ready round-the-clock."),
        ("[02 // CUSTODY]", "PACKAGE SECURITY", "All export, import & bonded goods handled with extreme care and CCTV."),
        ("[03 // LICENSED]", "FULL PERMISSIONS", "Required statutory authority & ASYCUDA customs permissions in Sri Lanka."),
        ("[04 // SCHEDULE]", "DELIVERY ON TIME", "Precision vessel, flight & haulage scheduling for punctual door delivery."),
    ]
    for i, (pi, pt, pd) in enumerate(promises):
        x = 0.6 + i * 1.8
        add_rect(s1, x, 7.1, 1.7, 1.45, SLATE, SKY, 0.75)
        add_text(s1, x + 0.1, 7.18, 1.5, 0.25, pi, 6.8, AMBER, True, font="Consolas")
        add_text(s1, x + 0.1, 7.45, 1.5, 0.28, pt, 8.5, WHITE, True)
        add_text(s1, x + 0.1, 7.75, 1.5, 0.7, pd, 7.2, WHITE, False)

    add_rect(s1, 0, 10.9, 8.27, 0.79, SLATE_DARK)
    add_text(s1, 0.6, 11.12, 7.1, 0.35, "HQ: Office 14, Basement Level, Cinnamon Lakeside Hotel, Colombo 02  |  www.spillburglogistics1.com  |  +94 11 233 6116", 7.8, WHITE, False, font="Consolas")

    # Slide 2: About Us, Vision & Mission
    s2 = prs.slides.add_slide(blank)
    header_footer(s2, 2, "SEC-01 // CORPORATE OVERVIEW")
    add_text(s2, 0.5, 1.1, 6.0, 0.25, "WHO WE ARE • INTERNATIONAL TRANSPORT & CLEARING SPECIALISTS", 7.5, OCEAN, True, font="Consolas")
    add_text(s2, 0.5, 1.32, 7.2, 0.45, "ABOUT SPILLBURG LOGISTICS 1", 18, SLATE, True)
    add_rect(s2, 0.5, 1.9, 7.27, 1.75, SLATE, AMBER, 1)
    add_text(s2, 0.68, 2.02, 6.9, 1.5, "Spillburg Logistics 1 (Private) Limited is a premier Logistic Service Provider and licensed clearing agent with a team of seasoned experts providing international transport solutions for customers around the globe. Headquartered in Colombo, we deliver reliable cargo handling services for both export and import consignments at Sri Lanka Customs.\n\nEnsuring that cargo arrives at the right place and at the right time involves real skill—we ensure moving goods globally is executed economically and efficiently.", 8.5, WHITE, False)

    add_rect(s2, 0.5, 3.85, 3.52, 1.65, TECH_BG, OCEAN, 1)
    add_text(s2, 0.65, 3.95, 3.2, 0.3, "FAST & PROFESSIONAL EXECUTION", 9.5, SLATE, True)
    add_text(s2, 0.65, 4.28, 3.2, 1.1, "Moving finished products, raw materials, and industrial equipment worldwide requires specialized operational expertise across ocean, air, and road networks.", 8, SLATE, False)

    add_rect(s2, 4.25, 3.85, 3.52, 1.65, TECH_BG, AMBER, 1)
    add_text(s2, 4.4, 3.95, 3.2, 0.3, "CUSTOMIZED SUPPLY SOLUTIONS", 9.5, SLATE, True)
    add_text(s2, 4.4, 4.28, 3.2, 1.1, "Every mandate starts with a complete assessment of your business needs—engineering tailored routing, consolidation, and customs clearance workflows.", 8, SLATE, False)

    add_rect(s2, 0.5, 5.7, 3.52, 1.35, WHITE, SLATE, 1)
    add_text(s2, 0.65, 5.8, 3.2, 0.28, "OUR VISION", 9.5, SLATE, True)
    add_text(s2, 0.65, 6.1, 3.2, 0.8, "“To be the preferred transportation and total logistics solutions provider for our customers across domestic and international trade lanes.”", 8, SLATE, False, True)

    add_rect(s2, 4.25, 5.7, 3.52, 1.35, WHITE, OCEAN, 1)
    add_text(s2, 4.4, 5.8, 3.2, 0.28, "OUR MISSION", 9.5, SLATE, True)
    add_text(s2, 4.4, 6.1, 3.2, 0.8, "“To provide total logistics solutions that gain the confidence and trust of our valued clients by conducting business with complete integrity.”", 8, SLATE, False, True)

    add_text(s2, 0.5, 7.25, 6.5, 0.25, "WHY CHOOSE SPILLBURG LOGISTICS 1 • FIVE COMMITMENTS", 7.5, OCEAN, True, font="Consolas")
    whys = [("01 // SUPPORT", "100% Customer Support"), ("02 // FRICTIONLESS", "Ease & Convenience"), ("03 // BESPOKE", "Customer Oriented"), ("04 // NETWORK", "Wide Global Coverage"), ("05 // DISCIPLINE", "Professional & Efficient")]
    for i, (wn, wt) in enumerate(whys):
        x = 0.5 + i * 1.47
        add_rect(s2, x, 7.55, 1.39, 1.4, SLATE, SKY, 0.75)
        add_text(s2, x + 0.08, 7.68, 1.2, 0.25, wn, 6.5, AMBER, True, font="Consolas")
        add_text(s2, x + 0.08, 8.0, 1.2, 0.7, wt, 8, WHITE, True)

    # Slide 3: Management Team (From 4-BOD.jpg)
    s3 = prs.slides.add_slide(blank)
    header_footer(s3, 3, "SEC-02 // LEADERSHIP & GOVERNANCE")
    add_text(s3, 0.5, 1.1, 6.0, 0.25, "BOARD OF DIRECTORS & SENIOR OPERATIONS LEADERSHIP", 7.5, OCEAN, True, font="Consolas")
    add_text(s3, 0.5, 1.32, 7.2, 0.45, "MANAGEMENT TEAM", 18, SLATE, True)

    mgmt = [
        ("Mr. M H K M Hameez", "MANAGING DIRECTOR", "BSc. (Hons) University of London, CPM (London), CPA (Australia)", "dir_hameez.jpg", "Former Director attached to the Investment Promotions division of the Board of Investment (BOI) of Sri Lanka, with over 15 years of hands-on experience setting up projects and providing project management services. Seasoned adviser and expert in Trade Agreements such as SAFTA, ISLFTA, and SLPFTA."),
        ("Shaameel Mohideen", "DIRECTOR", "MABE (UK), MBA (Aus), CMA (Aus)", "dir_shaameel.jpg", "Former banker attached to the Trade and Finance divisions of HSBC and Standard Chartered Bank, bringing over 15 years of senior experience in international trade finance, Letters of Credit (LC), project financing, project management, and project structuring."),
        ("Mr. M. I. Razik", "DIRECTOR", "Attorney-at-Law (SL), Commissioner of Oaths & Notary Public", "dir_razik.jpg", "Attorney-at-Law, Notary Public, and Senior Consultant with over 30 years of experience across commercial and corporate law, M&A, business structuring, customs and maritime legal compliance, and legal advisory."),
        ("Mr. Mafaz Azeez", "SENIOR MANAGER", "21+ Years in Maritime Port, Cruise & Freight Operations", "dir_mafaz.jpg", "Over 21 years of hands-on operational experience in transport, tourism, and port logistics, including passenger (Pax) and baggage exchange operations for international passenger cruise lines calling at Sri Lankan ports alongside air, sea, and land freight coordination."),
    ]
    for i, (name, role, creds, img_f, bio) in enumerate(mgmt):
        col = i % 2
        row = i // 2
        x = 0.5 + col * 3.72
        y = 1.95 + row * 3.9
        add_rect(s3, x, y, 3.55, 3.7, WHITE, OCEAN, 0.75)
        add_rect(s3, x, y, 3.55, 1.15, TECH_BG)
        s3.shapes.add_picture(os.path.join(assets, img_f), Inches(x + 0.15), Inches(y + 0.15), width=Inches(0.85), height=Inches(0.85))
        add_text(s3, x + 1.1, y + 0.12, 2.35, 0.28, name, 10, SLATE, True)
        add_text(s3, x + 1.1, y + 0.4, 2.35, 0.25, role, 7, AMBER, True, font="Consolas")
        add_text(s3, x + 1.1, y + 0.66, 2.35, 0.4, creds, 6.5, OCEAN, True)
        add_text(s3, x + 0.15, y + 1.25, 3.25, 2.3, bio, 8, SLATE, False)

    # Slide 4: Core Services Part I (Sea, Air & Land Freight)
    s4 = prs.slides.add_slide(blank)
    header_footer(s4, 4, "SEC-03 // MULTIMODAL TRANSPORT (I)")
    add_text(s4, 0.5, 1.1, 6.0, 0.25, "FROM DOCUMENTS TO BULK GOODS • GLOBAL FORWARDING", 7.5, OCEAN, True, font="Consolas")
    add_text(s4, 0.5, 1.32, 7.2, 0.45, "SEA, AIR & LAND FREIGHT", 18, SLATE, True)

    mods1 = [
        ("MOD-01", "SEA FREIGHT FORWARDING (FCL & LCL)", "Flexible ocean freight solutions for shipping large volumes of containerized and bulk cargo across global trade lanes.", "• Full Container Load (FCL 20' / 40' / 40'HC) & LCL Consolidation\n• Export & Import Port-to-Port and Door-to-Door Execution\n• Project Shipping (Breakbulk, Ro-Ro, Flat Rack & Open Top)\n• Reefer Containers, MCC Transshipment & Marine Cargo Insurance"),
        ("MOD-02", "AIR FREIGHT & EXPRESS CARGO COORDINATION", "Robust global air freight network centered at Bandaranaike International Airport (CMB) for time-critical shipments.", "• Import & Export Air Consolidation (Belly-Hold & Freighter)\n• Door-to-Door Express & Urgent AOG/VOR Spares\n• Rapid CMB Airport Customs Clearance & AWB Documentation\n• Airport Warehousing, Cold-Room Transfers & IATA DG Handling"),
        ("MOD-03", "LAND FREIGHT & INLAND ROAD HAULAGE", "Fleet capacity to transport and forward all road freight shipments in and out of Sri Lanka with flexible, safe execution.", "• Full Truck Load (FTL) & Less-Than-Truck Load (LTL) Haulage\n• 20' & 40' Container Deliveries & BOI Zone Port Drayage\n• Door-to-Door Domestic & Residential Pick-Up / Delivery\n• High-Quality Protective Wrapping & GPS-Monitored Dispatch"),
    ]
    for i, (code, title, lead, bullets) in enumerate(mods1):
        y = 1.95 + i * 2.95
        add_rect(s4, 0.5, y, 7.27, 2.75, WHITE, OCEAN, 0.75)
        add_rect(s4, 0.5, y, 7.27, 0.5, SLATE)
        add_text(s4, 0.65, y + 0.12, 6.8, 0.3, f"[{code}]  {title}", 9.5, WHITE, True)
        add_text(s4, 0.65, y + 0.6, 6.95, 0.5, lead, 8.2, SLATE, True)
        add_text(s4, 0.65, y + 1.15, 6.95, 1.45, bullets, 8, MUTED, False)

    # Slide 5: Core Services Part II (Warehousing, Customs & Project Cargo)
    s5 = prs.slides.add_slide(blank)
    header_footer(s5, 5, "SEC-04 // MULTIMODAL TRANSPORT (II)")
    add_text(s5, 0.5, 1.1, 6.0, 0.25, "ANCILLARY SHIPPING, STORAGE & BORDER CLEARANCE", 7.5, OCEAN, True, font="Consolas")
    add_text(s5, 0.5, 1.32, 7.2, 0.45, "WAREHOUSING, CUSTOMS & SPECIAL CARGO", 18, SLATE, True)

    mods2 = [
        ("MOD-04", "WAREHOUSING, BONDED STORAGE & COLD ROOM", "Accommodating your goods safely until ready to be shipped or collected at destination with commodity-specific storage.", "• Picking, Packing, Export Crating, Palletizing & Shrink-Wrapping\n• 24-Hour Security & Continuous CCTV Surveillance\n• Customs Bonding Warehouse & Bulk/Racked Storage Spaces\n• Temperature-Controlled Cold Room Facilities for Perishables"),
        ("MOD-05", "CUSTOMS BROKERAGE & ASYCUDA CLEARANCE", "Authorized Customs Clearing Agent in Sri Lanka delivering frictionless export and import consignment clearance.", "• Direct Electronic ASYCUDA World CUSDEC Lodgment & Assessment\n• HS Code Tariff Classification & Valuation Advisory\n• SAFTA, ISLFTA & SLPFTA Preferential Certificate of Origin Clearance\n• BOI Section 17 / TIEP Duty-Free & SLSI/NMRA/Quarantine Permits"),
        ("MOD-06", "PROJECT CARGO, HEAVY LIFT & CRUISE LOGISTICS", "Engineered transport for Out-of-Gauge (OOG) industrial machinery and specialized passenger cruise vessel turnarounds.", "• Heavy Lift & OOG (Transformers, Turbines, Boilers & Plant)\n• Route Surveys, Low-Bed Modular Trailers & Escort Permits\n• Turnkey Passenger (Pax) & Baggage Exchange for Cruise Lines\n• Urgent Ship Spares in Transit Clearance & Launch Delivery"),
    ]
    for i, (code, title, lead, bullets) in enumerate(mods2):
        y = 1.95 + i * 2.95
        add_rect(s5, 0.5, y, 7.27, 2.75, WHITE, OCEAN, 0.75)
        add_rect(s5, 0.5, y, 7.27, 0.5, SLATE)
        add_text(s5, 0.65, y + 0.12, 6.8, 0.3, f"[{code}]  {title}", 9.5, WHITE, True)
        add_text(s5, 0.65, y + 0.6, 6.95, 0.5, lead, 8.2, SLATE, True)
        add_text(s5, 0.65, y + 1.15, 6.95, 1.45, bullets, 8, MUTED, False)

    # Slide 6: 5-Step Operating Procedure & Capabilities Matrix (Replaces Council Memberships!)
    s6 = prs.slides.add_slide(blank)
    header_footer(s6, 6, "SEC-05 // OPERATIONAL WORKFLOW & SPECS")
    add_text(s6, 0.5, 1.1, 6.0, 0.25, "STANDARDIZED CHAIN-OF-CUSTODY & TECHNICAL MATRIX", 7.5, OCEAN, True, font="Consolas")
    add_text(s6, 0.5, 1.32, 7.2, 0.45, "OPERATING PROCEDURE & CAPABILITIES", 18, SLATE, True)
    s6.shapes.add_picture(os.path.join(assets, "warehouse_hero.jpg"), Inches(0.5), Inches(1.9), width=Inches(7.27), height=Inches(1.65))

    steps5 = [
        ("STEP 01", "Booking & Space", "Carrier routing, rate lock & vessel/flight slot allocation."),
        ("STEP 02", "Documentation", "Invoice, Packing List, B/L or AWB & CoO verification."),
        ("STEP 03", "Customs Clear", "ASYCUDA World CUSDEC filing, tariff & wharf exam."),
        ("STEP 04", "Transit Track", "Proactive vessel/flight milestone & arrival alerts."),
        ("STEP 05", "Final Handover", "DO collection, gate-out, haulage & signed POD."),
    ]
    for i, (sn, st, sd) in enumerate(steps5):
        x = 0.5 + i * 1.47
        add_rect(s6, x, 3.75, 1.39, 1.65, SLATE, SKY, 0.75)
        add_text(s6, x + 0.08, 3.85, 1.2, 0.22, sn, 6.8, AMBER, True, font="Consolas")
        add_text(s6, x + 0.08, 4.1, 1.2, 0.28, st, 8, WHITE, True)
        add_text(s6, x + 0.08, 4.42, 1.2, 0.9, sd, 6.8, WHITE, False)

    add_rect(s6, 0.5, 5.65, 7.27, 5.0, TECH_BG, OCEAN, 1)
    add_text(s6, 0.68, 5.8, 6.9, 0.3, "TECHNICAL SERVICE CAPABILITIES & PARAMETER MATRIX", 9.5, SLATE, True)
    add_text(s6, 0.68, 6.2, 6.9, 4.2, "• SEA FREIGHT FORWARDING (OCEAN FCL/LCL): 20' / 40' / 40'HC Dry, Reefer, Open Top, Flat Rack | Global Port-to-Port & Door-to-Door | Ocean B/L, Sea Waybill, VGM, Manifest\n\n• AIR CARGO COORDINATION (AIR EXPRESS): ULD Pallets, Belly-Hold, Main-Deck Freighter | CMB Airport to Global Hubs | MAWB / HAWB, Dangerous Goods Declaration\n\n• LAND FREIGHT & DRAYAGE (ROAD FTL/LTL): 20'/40' Prime Movers, Covered Box Trucks, Tail-Lift | Island-wide Sri Lanka & BOI Zones | Waybill, Gate Pass, EIR, Signed POD\n\n• CUSTOMS BROKERAGE (BORDER CLEAR): ASYCUDA World, RAMIS, Single Window | Seaport (LKCMB) & Airport (CMB) | CUSDEC, HS Assessment, FTA CoO, BOI\n\n• WAREHOUSING & STORAGE (CFS / BONDED): Racked Dry, Customs Bonded, Cold Room | Colombo Port Access Corridors | Goods Received Note (GRN), Tally Sheet", 8, SLATE, False)

    # Slide 7: Sri Lanka Maritime Crossroads Spotlight
    s7 = prs.slides.add_slide(blank)
    header_footer(s7, 7, "SEC-06 // COLOMBO HUB ADVANTAGE")
    add_text(s7, 0.5, 1.1, 6.0, 0.25, "STRATEGIC INDIAN OCEAN TRANSSHIPMENT & FTA GATEWAY", 7.5, OCEAN, True, font="Consolas")
    add_text(s7, 0.5, 1.32, 7.2, 0.45, "SRI LANKA MARITIME CROSSROADS", 18, SLATE, True)

    hub_stats = [("#1 Hub", "SOUTH ASIA TRANSSHIPMENT"), ("18m+ Draft", "DEEP-WATER ULCV BERTHS"), ("7.2M+ TEUs", "TERMINAL CAPACITY"), ("24 / 7 / 365", "ASYCUDA CLEARANCE")]
    for i, (hv, hl) in enumerate(hub_stats):
        x = 0.5 + i * 1.84
        add_rect(s7, x, 1.95, 1.74, 1.15, SLATE, SKY, 0.75)
        add_text(s7, x, 2.1, 1.74, 0.45, hv, 14, AMBER if i % 2 else SKY, True, align=PP_ALIGN.CENTER)
        add_text(s7, x, 2.6, 1.74, 0.35, hl, 6.8, WHITE, True, font="Consolas", align=PP_ALIGN.CENTER)

    add_rect(s7, 0.5, 3.35, 7.27, 3.4, WHITE, OCEAN, 1)
    add_text(s7, 0.7, 3.55, 6.8, 3.0, "REGIONAL TRADE AGREEMENT ADVISORY (SAFTA / ISLFTA / SLPFTA):\nLed by our Managing Director’s extensive background with the Board of Investment (BOI) and regional trade treaties, we assist exporters and importers in structuring shipments under the Indo-Sri Lanka Free Trade Agreement (ISLFTA), Pakistan-Sri Lanka FTA (SLPFTA), and SAFTA—securing duty concessions and rules-of-origin compliance.\n\nMULTI-COUNTRY CONSOLIDATION (MCC) & ENTREPÔT TRADE:\nWe coordinate LCL cargo originating from multiple regional ports to be de-stuffed, sorted, relabeled, and consolidated into FCL containers under customs bond in Colombo for onward shipment to Europe, the UK, the Middle East, and North America.", 8.5, SLATE, False)

    add_rect(s7, 0.5, 7.0, 7.27, 3.6, SLATE, AMBER, 1)
    add_text(s7, 0.7, 7.2, 6.8, 3.1, "DIRECT TERMINAL & BORDER COVERAGE ACROSS SRI LANKA:\n\n• PORT OF COLOMBO TERMINALS: Direct wharf operations across JCT (Jaya Container Terminal), SAGT (South Asia Gateway Terminals), CICT (Colombo International Container Terminals), and ECT.\n• HAMBANTOTA & TRINCOMALEE: Ro-Ro vehicle transshipment, project breakbulk discharge, bulk industrial commodities, and heavy-lift port clearance.\n• BIA AIR CARGO & BOI ZONES: Express air cargo clearance at Katunayake (CMB) and direct bonded trucking to Katunayake, Biyagama, Seethawaka, Horana, and Koggala EPZs.", 8.5, WHITE, False)

    # Slide 8: Industries Served & Verified Client Testimonials
    s8 = prs.slides.add_slide(blank)
    header_footer(s8, 8, "SEC-07 // SECTORS & CLIENT ENDORSEMENTS")
    add_text(s8, 0.5, 1.1, 6.0, 0.25, "VERTICAL SUPPLY CHAIN EXPERTISE & PROVEN RELIABILITY", 7.5, OCEAN, True, font="Consolas")
    add_text(s8, 0.5, 1.32, 7.2, 0.45, "INDUSTRIES SERVED & TESTIMONIALS", 18, SLATE, True)

    inds = [
        ("01. APPAREL & TEXTILES", "Raw fabric rolls & trims under BOI/TIEP, and Garments-on-Hanger (GOH) & boxed exports to EU, UK & US buyers."),
        ("02. INDUSTRIAL MACHINERY", "Factory production lines, generators, construction plant & steel structures via Flat Rack, Open Top & low-bed."),
        ("03. RETAIL & FMCG", "High-frequency FCL & consolidated LCL consumer goods, SLSI/NMRA clearance, bonded storage & distribution."),
        ("04. AUTOMOTIVE & SPARES", "Urgent air freight spares for fleet maintenance alongside FCL tyres, batteries, lubricants & components."),
        ("05. PERISHABLES & TEA", "Pure Ceylon Tea, spices, coconut products, seafood & fresh produce in pre-cooled Reefers & cold rooms."),
        ("06. RENEWABLE ENERGY", "Solar PV modules, inverters, battery storage units & substation transformers delivered to project sites."),
    ]
    for i, (it, idesc) in enumerate(inds):
        col = i % 3
        row = i // 3
        x = 0.5 + col * 2.46
        y = 1.95 + row * 1.95
        add_rect(s8, x, y, 2.35, 1.8, WHITE, OCEAN, 0.75)
        add_text(s8, x + 0.12, y + 0.12, 2.1, 0.3, it, 8, SLATE, True)
        add_text(s8, x + 0.12, y + 0.45, 2.1, 1.25, idesc, 7.3, MUTED, False)

    add_text(s8, 0.5, 6.05, 6.5, 0.25, "VERIFIED CLIENT TESTIMONIALS • FROM SPILLBURGLOGISTICS1.COM", 7.5, OCEAN, True, font="Consolas")
    l_testis = [
        ("Marks Philip", "INTERNATIONAL SEA FREIGHT", "“Very good service and I was very impressed with the product delivery and the packaging methods for long-time sea voyage.”"),
        ("Kavainda Perera", "CARGO & TRANSPORT CLIENT", "“Most trustable transportation company. All my goods were properly cared for and properly delivered. I am very happy to have worked with this company.”"),
        ("Tony Johnson", "COMMERCIAL LOGISTICS CLIENT", "“One of the best services I had for the first time in my business—very flexible and reliable across every stage of delivery.”"),
    ]
    for i, (au, rl, qt) in enumerate(l_testis):
        x = 0.5 + i * 2.46
        add_rect(s8, x, 6.38, 2.35, 2.6, SLATE, AMBER if i % 2 == 0 else SKY, 1)
        add_text(s8, x + 0.12, y=6.5, w=2.1, h=1.6, text=qt, size=7.6, color=WHITE, italic=True)
        add_text(s8, x + 0.12, y=8.25, w=2.1, h=0.25, text=au, size=8.5, color=AMBER, bold=True)
        add_text(s8, x + 0.12, y=8.52, w=2.1, h=0.25, text=rl, size=6.2, color=SKY, bold=True, font="Consolas")

    # Slide 9: Contact Us
    s9 = prs.slides.add_slide(blank)
    header_footer(s9, 9, "SEC-08 // DISPATCH & FREIGHT DESK")
    add_text(s9, 0.5, 1.1, 6.0, 0.25, "24/7 OPERATIONS DESK • REQUEST A FREIGHT QUOTE", 7.5, OCEAN, True, font="Consolas")
    add_text(s9, 0.5, 1.32, 7.2, 0.45, "GET IN TOUCH", 18, SLATE, True)

    add_rect(s9, 0.5, 1.95, 7.27, 4.6, SLATE, OCEAN, 1.5)
    add_text(s9, 0.75, 2.2, 4.5, 0.5, "SPILLBURG LOGISTICS 1 (PRIVATE) LIMITED", 13.5, WHITE, True)
    add_rect(s9, 5.4, 2.15, 2.1, 0.58, WHITE)
    s9.shapes.add_picture(os.path.join(assets, "logo_logistics_live.png"), Inches(5.52), Inches(2.22), height=Inches(0.42))

    add_text(s9, 0.75, 3.05, 4.4, 3.2, "HEADQUARTERS ADDRESS:\nOffice 14, Basement Level, Cinnamon Lakeside Hotel,\nNo. 115, Sir Chittampalam A. Gardiner Mawatha,\nColombo 02, Sri Lanka.\n\n24H HOTLINES, LANDLINE & FAX:\n24h Hotlines: +94 777 487 720  |  +94 777 790 919\nGeneral Line: +94 11 233 6116  |  Fax: +94 11 252 9309\n\nFREIGHT DESK EMAIL & WEB PORTAL:\nEmail: info@spillburglogistics1.com\nWebsite: www.spillburglogistics1.com", 8.8, WHITE, False)

    add_rect(s9, 5.35, 3.05, 2.15, 3.15, WHITE, OCEAN, 1.5)
    s9.shapes.add_picture(os.path.join(assets, "qr_website.png"), Inches(5.58), Inches(3.2), width=Inches(1.7), height=Inches(1.7))
    add_text(s9, 5.4, 5.0, 2.05, 0.6, "SCAN FOR ONLINE PORTAL\nspillburglogistics1.com", 7.5, SLATE, True, align=PP_ALIGN.CENTER)

    add_rect(s9, 0.5, 6.85, 7.27, 3.8, SLATE_DARK, AMBER, 1)
    add_text(s9, 0.75, 7.25, 6.5, 0.35, "AIR FREIGHT  •  SEA FREIGHT  •  LAND FREIGHT  •  WAREHOUSING", 8.5, AMBER, True, font="Consolas")
    add_text(s9, 0.75, 7.7, 6.5, 0.6, "“MOVING CARGO. CONNECTING BUSINESSES.”", 18, WHITE, True)
    add_text(s9, 0.75, 8.45, 6.5, 1.5, "Economical, Secure & Time-Critical International Transport Solutions\n\nPort of Colombo (LKCMB)  |  Bandaranaike Int'l Airport (CMB)  |  Island-Wide BOI Zones", 9, WHITE, False)

    out = os.path.join(base, "spillburg logistics", "Company Profile - 2026.pptx")
    prs.save(out)
    print("Saved:", out)

if __name__ == "__main__":
    build_destination_pptx()
    build_corporate_pptx()
    build_logistics_pptx()

