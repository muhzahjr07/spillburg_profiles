from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
import os

prs = Presentation()
prs.slide_width = Inches(8.27)
prs.slide_height = Inches(11.69)
blank_slide_layout = prs.slide_layouts[6]

# Theme Colors
NAVY = RGBColor(11, 25, 44)
NAVY_LIGHT = RGBColor(30, 62, 98)
BLUE = RGBColor(30, 64, 175)
GOLD = RGBColor(197, 160, 89)
GOLD_LIGHT = RGBColor(229, 195, 132)
WHITE = RGBColor(255, 255, 255)
DARK_TEXT = RGBColor(30, 41, 59)
MUTED = RGBColor(100, 116, 139)
BG_SOFT = RGBColor(248, 250, 252)

base_dir = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile\spillburg corporate services"
assets_dir = os.path.join(base_dir, "assets")

def add_header(slide, subtitle="Financial & Corporate Advisory"):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(8.27), Inches(0.95))
    shape.fill.solid()
    shape.fill.fore_color.rgb = NAVY
    shape.line.fill.background()
    
    # Gold accent line
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0.95), Inches(8.27), Inches(0.04))
    accent.fill.solid()
    accent.fill.fore_color.rgb = GOLD
    accent.line.fill.background()
    
    txBox = slide.shapes.add_textbox(Inches(0.45), Inches(0.12), Inches(4.5), Inches(0.75))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "SPILLBURG"
    p.font.name = "Georgia"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    p2 = tf.add_paragraph()
    p2.text = "CORPORATE SERVICES (PVT) LTD"
    p2.font.name = "Arial"
    p2.font.size = Pt(7.5)
    p2.font.bold = True
    p2.font.color.rgb = GOLD_LIGHT
    
    txBox2 = slide.shapes.add_textbox(Inches(4.8), Inches(0.25), Inches(3.0), Inches(0.4))
    tf2 = txBox2.text_frame
    p3 = tf2.paragraphs[0]
    p3.text = subtitle.upper()
    p3.alignment = PP_ALIGN.RIGHT
    p3.font.name = "Arial"
    p3.font.size = Pt(8.5)
    p3.font.color.rgb = GOLD_LIGHT

def add_footer(slide, page_num):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(11.15), Inches(8.27), Inches(0.54))
    shape.fill.solid()
    shape.fill.fore_color.rgb = NAVY
    shape.line.fill.background()
    
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(11.12), Inches(8.27), Inches(0.03))
    accent.fill.solid()
    accent.fill.fore_color.rgb = GOLD
    accent.line.fill.background()
    
    txBox = slide.shapes.add_textbox(Inches(0.45), Inches(11.20), Inches(5.0), Inches(0.35))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = "Spillburg Corporate Services (Pvt) Ltd • www.spillburgcorporate.com"
    p.font.name = "Arial"
    p.font.size = Pt(8.5)
    p.font.color.rgb = GOLD_LIGHT
    
    txBox2 = slide.shapes.add_textbox(Inches(6.5), Inches(11.20), Inches(1.3), Inches(0.35))
    tf2 = txBox2.text_frame
    p2 = tf2.paragraphs[0]
    p2.text = f"{page_num:02d}"
    p2.alignment = PP_ALIGN.RIGHT
    p2.font.name = "Arial"
    p2.font.size = Pt(10)
    p2.font.bold = True
    p2.font.color.rgb = WHITE

# ----------------- SLIDE 1: COVER -----------------
slide1 = prs.slides.add_slide(blank_slide_layout)
cover_img = os.path.join(assets_dir, "cover_hero.jpg")
if os.path.exists(cover_img):
    slide1.shapes.add_picture(cover_img, Inches(0), Inches(0), Inches(8.27), Inches(11.69))

ov = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(8.27), Inches(11.69))
ov.fill.solid()
ov.fill.fore_color.rgb = NAVY
# Semi-transparent overlay workaround: pptx fill color
# Let's add cover texts
tx = slide1.shapes.add_textbox(Inches(0.6), Inches(0.8), Inches(7.0), Inches(1.0))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "SPILLBURG"
p.font.name = "Georgia"
p.font.size = Pt(28)
p.font.bold = True
p.font.color.rgb = WHITE
p2 = tf.add_paragraph()
p2.text = "CORPORATE SERVICES PRIVATE LIMITED"
p2.font.name = "Arial"
p2.font.size = Pt(9.5)
p2.font.bold = True
p2.font.color.rgb = GOLD_LIGHT

tx2 = slide1.shapes.add_textbox(Inches(0.6), Inches(5.0), Inches(7.0), Inches(4.5))
tf2 = tx2.text_frame
p = tf2.paragraphs[0]
p.text = "FINANCIAL, TAX & CORPORATE GOVERNANCE SOLUTIONS"
p.font.name = "Arial"
p.font.size = Pt(9.5)
p.font.bold = True
p.font.color.rgb = GOLD_LIGHT

p = tf2.add_paragraph()
p.text = "COMPANY PROFILE 2026"
p.font.name = "Georgia"
p.font.size = Pt(36)
p.font.bold = True
p.font.color.rgb = WHITE

p = tf2.add_paragraph()
p.text = "\nEmpowering multinationals, BOI enterprises, and high-growth corporations with strategic financial leadership, RAMIS tax advisory, statutory compliance, and capital markets facilitation."
p.font.name = "Arial"
p.font.size = Pt(13)
p.font.color.rgb = RGBColor(226, 232, 240)

# ----------------- SLIDE 2: ABOUT -----------------
slide2 = prs.slides.add_slide(blank_slide_layout)
add_header(slide2, "Corporate Legacy & Expertise")
add_footer(slide2, 2)

tx = slide2.shapes.add_textbox(Inches(0.6), Inches(1.2), Inches(4.2), Inches(8.5))
tf = tx.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "ABOUT SPILLBURG CORPORATE"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

p = tf.add_paragraph()
p.text = "\nSpillburg Corporate Services (Pvt) Ltd is a premier corporate advisory and financial consulting firm dedicated to strengthening the operational and statutory foundation of businesses operating across Sri Lanka and international jurisdictions.\n\nWith over 18 years of specialized advisory practice, we partner with multinational corporations, Board of Investment (BOI) enterprises, Colombo Port City SEZ entities, and burgeoning SMEs to deliver tailored solutions spanning financial accounting, Inland Revenue Department (IRD) tax structuring, statutory secretarial compliance, and risk assurance.\n\nOur core mission is to protect enterprise value, ensure zero-deficiency statutory compliance, and unlock institutional capital for our clientele."
p.font.name = "Arial"
p.font.size = Pt(11)
p.font.color.rgb = DARK_TEXT

# Stat cards
card1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(7.5), Inches(1.9), Inches(1.2))
card1.fill.solid()
card1.fill.fore_color.rgb = NAVY
card1.line.color.rgb = GOLD
tf = card1.text_frame
p = tf.paragraphs[0]
p.text = "18+\nYears Experience"
p.font.name = "Georgia"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = GOLD_LIGHT

card2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.7), Inches(7.5), Inches(1.9), Inches(1.2))
card2.fill.solid()
card2.fill.fore_color.rgb = NAVY
card2.line.color.rgb = GOLD
tf = card2.text_frame
p = tf.paragraphs[0]
p.text = "350+\nCorporates Advised"
p.font.name = "Georgia"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = GOLD_LIGHT

# Right Box
box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.0), Inches(1.5), Inches(2.7), Inches(7.2))
box.fill.solid()
box.fill.fore_color.rgb = BG_SOFT
box.line.color.rgb = RGBColor(226, 232, 240)
tf = box.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Core Practice Disciplines"
p.font.name = "Georgia"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = NAVY

disciplines = [
    "Comprehensive Cloud Accounting (IFRS / LKAS)",
    "RAMIS Tax Compliance, VAT, SSCL & CIT",
    "Statutory Secretarial & Registrar Filings",
    "Financial & Operational Due Diligence",
    "Mergers & Acquisitions (M&A) Structuring",
    "CSE Empower Board Stock Listing Advisory",
    "Payroll Outsourcing & EPF/ETF Management",
    "Commercial Dispute Mitigation & Mediation"
]
for d in disciplines:
    p = tf.add_paragraph()
    p.text = f"• {d}"
    p.font.name = "Arial"
    p.font.size = Pt(9.5)
    p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 3: BOARD OF DIRECTORS -----------------
slide3 = prs.slides.add_slide(blank_slide_layout)
add_header(slide3, "Leadership & Governance")
add_footer(slide3, 3)

tx = slide3.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "BOARD OF DIRECTORS"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

# Director 1
dh_img = os.path.join(assets_dir, "director_hameez.jpg")
if os.path.exists(dh_img):
    slide3.shapes.add_picture(dh_img, Inches(0.6), Inches(1.7), Inches(3.3), Inches(2.4))
tx = slide3.shapes.add_textbox(Inches(0.6), Inches(4.2), Inches(3.3), Inches(2.8))
tf = tx.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "M H K M Hameez"
p.font.name = "Georgia"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = NAVY
p = tf.add_paragraph()
p.text = "Managing Director | CPA (Australia), CPM (London)"
p.font.size = Pt(8.5)
p.font.bold = True
p.font.color.rgb = GOLD
p = tf.add_paragraph()
p.text = "Former Director in the Board of Investment of Sri Lanka's Investment Promotions division with over 15 years hands-on experience in project setup and enterprise structuring. President of Sri Lanka Malaysia Business Council."
p.font.size = Pt(8.5)
p.font.color.rgb = DARK_TEXT

# Director 2
ds_img = os.path.join(assets_dir, "director_shaameel.jpg")
if os.path.exists(ds_img):
    slide3.shapes.add_picture(ds_img, Inches(4.3), Inches(1.7), Inches(3.3), Inches(2.4))
tx = slide3.shapes.add_textbox(Inches(4.3), Inches(4.2), Inches(3.3), Inches(2.8))
tf = tx.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Mohideen Shaameel (JP)"
p.font.name = "Georgia"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = NAVY
p = tf.add_paragraph()
p.text = "Executive Director / CEO | MBA (Sydney), CMA (Aust)"
p.font.size = Pt(8.5)
p.font.bold = True
p.font.color.rgb = GOLD
p = tf.add_paragraph()
p.text = "Former banker at HSBC & Standard Chartered with over 15 years' expertise in project financing and balance sheet structuring. President of Sri Lanka Nordic and Sri Lanka France Business Councils."
p.font.size = Pt(8.5)
p.font.color.rgb = DARK_TEXT

# Senior Team Box
mgt = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(7.3), Inches(7.0), Inches(3.5))
mgt.fill.solid()
mgt.fill.fore_color.rgb = BG_SOFT
mgt.line.color.rgb = RGBColor(226, 232, 240)
tf = mgt.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Senior Corporate Advisory & Management Team"
p.font.name = "Georgia"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = NAVY

team = [
    ("Mrs. N. H. Hameez", "ACA (SL), CPA (Australia) - Senior Tax Consultant", "15+ years advising MNCs and conglomerates on corporate tax, transfer pricing & RAMIS."),
    ("Mrs. C. Gunasekera", "Attorney-at-Law, Notary Public", "20+ years in legal conveyance, corporate contracts, and statutory corporate registrations."),
    ("Mr. Christian Ignatius", "Former Director, BOI Sri Lanka", "35+ years in project appraisal, FTZ enterprise setups, and regulatory licensing."),
    ("Mr. M. I. Razik", "Attorney-at-Law, Senior Legal Counsel", "30+ years advising boards on M&A, balance sheet restructuring, and commercial arbitration.")
]
for name, role, desc in team:
    p = tf.add_paragraph()
    p.text = f"• {name} ({role}): {desc}"
    p.font.name = "Arial"
    p.font.size = Pt(8.5)
    p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 4: SERVICE SPECTRUM -----------------
slide4 = prs.slides.add_slide(blank_slide_layout)
add_header(slide4, "End-to-End Enterprise Solutions")
add_footer(slide4, 4)

tx = slide4.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "SERVICE SPECTRUM & FACILITATION"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

services_corp = [
    ("Accounting & Financial Reporting", ["Full-cycle computerized accounting & ledgers", "IFRS / LKAS compliant financial statements", "Monthly management accounts & forecasting", "Cloud accounting ERP (QuickBooks, Xero, Zoho)"]),
    ("RAMIS Tax Advisory & Compliance", ["Inland Revenue Dept RAMIS registration & e-filing", "Corporate Income Tax (CIT) & APIT filings", "VAT & Social Security Contribution Levy (SSCL)", "Transfer pricing & tax audit defense representation"]),
    ("Statutory Secretarial & Governance", ["Incorporation under Companies Act No. 07 of 2007", "Statutory minute books, registers & share ledgers", "Annual returns filing with Registrar of Companies", "Capital restructuring, share allotments & transfers"]),
    ("Audit Readiness & Assurance", ["Pre-audit statutory documentation & assessments", "Liaison with external auditors and Big 4 firms", "Internal controls review & SOP design", "Corporate governance benchmarking & compliance"]),
    ("Due Diligence & M&A Advisory", ["Financial, tax & legal due diligence reviews", "Independent business valuation & DCF appraisals", "Merger, acquisition & takeover structuring", "Share purchase agreement (SPA) facilitation"]),
    ("CSE Capital Markets Listing", ["Colombo Stock Exchange Empower Board listing", "Pre-IPO financial governance cleanup", "Prospectus drafting support & sponsor coordination", "Post-listing disclosure compliance advisory"])
]

coords = [
    (0.6, 1.8), (4.2, 1.8),
    (0.6, 4.8), (4.2, 4.8),
    (0.6, 7.8), (4.2, 7.8)
]
for idx, (title, items) in enumerate(services_corp):
    x, y = coords[idx]
    card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(3.4), Inches(2.7))
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = BLUE
    tf = card.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"Pillar 0{idx+1}: {title}"
    p.font.name = "Georgia"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = NAVY
    for it in items:
        p = tf.add_paragraph()
        p.text = f"✓ {it}"
        p.font.name = "Arial"
        p.font.size = Pt(8.5)
        p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 5: PRACTICE AREAS -----------------
slide5 = prs.slides.add_slide(blank_slide_layout)
add_header(slide5, "Specialized Practice Areas")
add_footer(slide5, 5)

tx = slide5.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "PRACTICE AREAS & CORPORATE MOBILITY"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

practice_areas = [
    ("01", "Payroll Outsourcing & HR Compliance", [
        "Confidential monthly executive & staff payroll processing",
        "EPF and ETF monthly statutory electronic returns",
        "Gratuity liability actuarial calculations & provisioning",
        "Employment contracts, NDAs & labor compliance advisory"
    ]),
    ("02", "Dispute Mitigation & Mediation", [
        "Commercial dispute negotiation & out-of-court mediation",
        "Contractual breach risk management & settlements",
        "Creditor restructuring, debt recovery advisory",
        "Representation at commercial arbitration tribunals in Sri Lanka"
    ]),
    ("03", "BOI & Port City SEZ Fiscal Incentives", [
        "Structuring projects under Board of Investment (BOI) Sec 17",
        "Corporate income tax holidays & customs duty exemptions",
        "Colombo Port City SEZ Authorised Person (AP) setup",
        "Foreign exchange exemptions & offshore banking accounts"
    ]),
    ("04", "Expatriate Visas & Executive Mobility", [
        "BOI investor, director & executive residence visas",
        "Private sector work permits & employment clearances",
        "Resident Guest Scheme (RGS) for foreign investors",
        "Dual citizenship processing & expatriate relocation support"
    ])
]
pcoords = [(0.6, 1.8), (4.2, 1.8), (0.6, 6.2), (4.2, 6.2)]
for idx, (num, title, items) in enumerate(practice_areas):
    x, y = pcoords[idx]
    box = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(3.4), Inches(4.0))
    box.fill.solid()
    box.fill.fore_color.rgb = BG_SOFT
    box.line.color.rgb = RGBColor(226, 232, 240)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"{num} | {title}"
    p.font.name = "Georgia"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = NAVY
    for it in items:
        p = tf.add_paragraph()
        p.text = f"▪ {it}"
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 6: FLAGSHIP CASE -----------------
slide6 = prs.slides.add_slide(blank_slide_layout)
add_header(slide6, "Flagship Value Proposition")
add_footer(slide6, 6)

tx = slide6.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "RAMIS TAX & CSE LISTING ADVISORY"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

hero = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.8), Inches(7.0), Inches(2.4))
hero.fill.solid()
hero.fill.fore_color.rgb = NAVY
hero.line.fill.background()
tf = hero.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "ENTERPRISE VALUE ACCELERATION"
p.font.name = "Arial"
p.font.size = Pt(9)
p.font.bold = True
p.font.color.rgb = GOLD_LIGHT
p = tf.add_paragraph()
p.text = "Architecting Institutional Grade Governance & Capital Growth"
p.font.name = "Georgia"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = WHITE
p = tf.add_paragraph()
p.text = "\nSpillburg Corporate Services bridges the gap between statutory precision and public capital readiness. We resolve legacy tax complexities and guide enterprises onto the national stock exchange."
p.font.name = "Arial"
p.font.size = Pt(10)
p.font.color.rgb = RGBColor(203, 213, 225)

# Case 1
c1 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(4.5), Inches(3.4), Inches(5.8))
c1.fill.solid()
c1.fill.fore_color.rgb = WHITE
c1.line.color.rgb = RGBColor(226, 232, 240)
tf = c1.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Case 01: RAMIS IRD Tax Navigation"
p.font.name = "Georgia"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = NAVY
steps1 = [
    "Automated linkage of corporate ledgers with IRD RAMIS digital system.",
    "Advanced liability modeling to optimize legitimate capital allowances.",
    "Full audit defense representation before IRD assessors, eliminating unwarranted penalties.",
    "Continuous monitoring of tax amendments, preventing fiscal exposure."
]
for s in steps1:
    p = tf.add_paragraph()
    p.text = f"• {s}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = DARK_TEXT

# Case 2
c2 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.2), Inches(4.5), Inches(3.4), Inches(5.8))
c2.fill.solid()
c2.fill.fore_color.rgb = WHITE
c2.line.color.rgb = RGBColor(226, 232, 240)
tf = c2.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Case 02: CSE Empower Board IPO"
p.font.name = "Georgia"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = NAVY
steps2 = [
    "Pre-listing diagnostic review to resolve governance and accounting gaps.",
    "Restructuring debt-equity ratios and converting to a public limited company (PLC).",
    "Collaborative drafting of introductory memorandum & listing prospectus.",
    "Facilitating successful investor roadshows and official listing on the CSE."
]
for s in steps2:
    p = tf.add_paragraph()
    p.text = f"• {s}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 7: AFFILIATIONS -----------------
slide7 = prs.slides.add_slide(blank_slide_layout)
add_header(slide7, "Institutional Endorsements")
add_footer(slide7, 7)

tx = slide7.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "GLOBAL NETWORK & CHAMBERS"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

aff_img = os.path.join(assets_dir, "affiliations_grid.png")
if os.path.exists(aff_img):
    slide7.shapes.add_picture(aff_img, Inches(0.6), Inches(1.8), Inches(7.0), Inches(3.5))

cbox = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(5.6), Inches(7.0), Inches(4.2))
cbox.fill.solid()
cbox.fill.fore_color.rgb = BG_SOFT
cbox.line.color.rgb = RGBColor(226, 232, 240)
tf = cbox.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "The Ceylon Chamber of Commerce - Bilateral Councils & Chamber Network"
p.font.name = "Georgia"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = NAVY

councils = [
    "Sri Lanka Malaysia Business Council (President)",
    "Sri Lanka France Business Council (President)",
    "Sri Lanka Nordic Business Council (President)",
    "European Chamber of Commerce Sri Lanka (ECCSL)",
    "Sri Lanka Australia - New Zealand Business Council",
    "Sri Lanka Germany Business Council",
    "Indo-Lanka Chamber of Commerce & Industry",
    "Sri Lanka China Business Council",
    "The National Chamber of Exporters of Sri Lanka (NCE)",
    "Representative Clients: Agoda Global, Balaji Group, Royalty Holdings, Amtrad International"
]
for c in councils:
    p = tf.add_paragraph()
    p.text = f"• {c}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 8: SECTORS -----------------
slide8 = prs.slides.add_slide(blank_slide_layout)
add_header(slide8, "Sectoral Expertise")
add_footer(slide8, 8)

tx = slide8.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "STRATEGIC SECTOR PORTFOLIO"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

sectors = [
    ("Tech, BPO & Shared Services", "Colombo Port City SEZ & Tech Hubs", [
        "BPO/KPO company incorporation & Authorised Person status",
        "Multi-currency offshore payroll & tax exemption filings",
        "Cross-border software export transfer pricing compliance",
        "IP assignment, software licensing & GDPR alignment"
    ]),
    ("Manufacturing & Export Ventures", "BOI Free Trade Zones & Estates", [
        "BOI Section 17 project appraisal & duty-free machinery",
        "TIEP and inward processing fiscal scheme administration",
        "Factory statutory compliance & CEA environmental clearance",
        "Customs duty drawback & raw material procurement advisory"
    ]),
    ("Hospitality & Real Estate", "Resorts & Prime Developments", [
        "Tourist Development Authority (SLTDA) licensing",
        "Title deeds verification & 99-year state land lease structuring",
        "Condominium Management Authority (CMA) legal compliance",
        "Hospitality VAT deferrals & tourism revival incentives"
    ])
]
for idx, (title, sub, items) in enumerate(sectors):
    x = 0.6 + idx * 2.4
    card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(1.8), Inches(2.2), Inches(8.5))
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = NAVY
    tf = card.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = "Georgia"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p = tf.add_paragraph()
    p.text = sub
    p.font.size = Pt(8.5)
    p.font.color.rgb = GOLD
    for it in items:
        p = tf.add_paragraph()
        p.text = f"• {it}"
        p.font.size = Pt(8.5)
        p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 9: CONTACT -----------------
slide9 = prs.slides.add_slide(blank_slide_layout)
add_header(slide9, "Direct Engagement")
add_footer(slide9, 9)

tx = slide9.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "CONTACT INFORMATION"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

hero9 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.8), Inches(7.0), Inches(2.0))
hero9.fill.solid()
hero9.fill.fore_color.rgb = NAVY
tf = hero9.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "PARTNER WITH SPILLBURG FOR CORPORATE EXCELLENCE"
p.font.name = "Georgia"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = WHITE
p = tf.add_paragraph()
p.text = "\nSchedule a confidential consultation with our directors and senior consultants to address your taxation, accounting, secretarial, or capital markets requirements."
p.font.size = Pt(10)
p.font.color.rgb = RGBColor(203, 213, 225)

# Offices
o1 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(4.1), Inches(3.4), Inches(2.2))
o1.fill.solid()
o1.fill.fore_color.rgb = BG_SOFT
o1.line.color.rgb = RGBColor(226, 232, 240)
tf = o1.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Corporate Headquarters"
p.font.name = "Georgia"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = NAVY
p = tf.add_paragraph()
p.text = "\nOffice 14, Basement Level, Cinnamon Lakeside Hotel,\nNo. 115, Sir Chittampalam A Gardiner Mawatha,\nColombo 02, Sri Lanka."
p.font.size = Pt(9.5)
p.font.color.rgb = DARK_TEXT

o2 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.2), Inches(4.1), Inches(3.4), Inches(2.2))
o2.fill.solid()
o2.fill.fore_color.rgb = BG_SOFT
o2.line.color.rgb = RGBColor(226, 232, 240)
tf = o2.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Registered Office"
p.font.name = "Georgia"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = NAVY
p = tf.add_paragraph()
p.text = "\nNo. 568/2, Aluthmawatha Road,\nColombo 15,\nSri Lanka."
p.font.size = Pt(9.5)
p.font.color.rgb = DARK_TEXT

# Table & QR
tx_ct = slide9.shapes.add_textbox(Inches(0.6), Inches(6.6), Inches(4.5), Inches(3.8))
tf = tx_ct.text_frame
contacts = [
    ("Telephone", "+94 11 233 6116"),
    ("Telefax", "+94 11 252 9309"),
    ("Hotlines", "+94 77 748 7720 | +94 77 779 0919"),
    ("E-Mail", "info@spillburgcorporate.com / info@spillburg.com"),
    ("Websites", "www.spillburgcorporate.com • www.spillburg.com")
]
for lbl, val in contacts:
    p = tf.add_paragraph()
    p.text = f"{lbl:12s}: {val}"
    p.font.name = "Arial"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = DARK_TEXT

qr_img = os.path.join(assets_dir, "qr_code.jpg")
if os.path.exists(qr_img):
    slide9.shapes.add_picture(qr_img, Inches(5.5), Inches(6.8), Inches(1.8), Inches(1.8))

pptx_out = os.path.join(base_dir, "Company Profile - 2026.pptx")
prs.save(pptx_out)
print(f"Saved editable PowerPoint: {pptx_out}")
