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

# Theme Colors - Logistics
NAVY = RGBColor(15, 23, 42)
SLATE = RGBColor(30, 41, 59)
BLUE = RGBColor(2, 132, 199)
CYAN = RGBColor(14, 165, 233)
LIGHT_BLUE = RGBColor(56, 189, 248)
WHITE = RGBColor(255, 255, 255)
DARK_TEXT = RGBColor(30, 41, 59)
MUTED = RGBColor(100, 116, 139)
BG_SOFT = RGBColor(248, 250, 252)

base_dir = r"c:\Users\User\Desktop\Spillburg Admin\projects\company_profile\spillburg logistics"
assets_dir = os.path.join(base_dir, "assets")

def add_header(slide, subtitle="Global Freight & Maritime Hub"):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(8.27), Inches(0.95))
    shape.fill.solid()
    shape.fill.fore_color.rgb = NAVY
    shape.line.fill.background()
    
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0.95), Inches(8.27), Inches(0.04))
    accent.fill.solid()
    accent.fill.fore_color.rgb = CYAN
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
    p2.text = "LOGISTICS 1 (PVT) LTD"
    p2.font.name = "Arial"
    p2.font.size = Pt(7.5)
    p2.font.bold = True
    p2.font.color.rgb = LIGHT_BLUE
    
    txBox2 = slide.shapes.add_textbox(Inches(4.8), Inches(0.25), Inches(3.0), Inches(0.4))
    tf2 = txBox2.text_frame
    p3 = tf2.paragraphs[0]
    p3.text = subtitle.upper()
    p3.alignment = PP_ALIGN.RIGHT
    p3.font.name = "Arial"
    p3.font.size = Pt(8.5)
    p3.font.color.rgb = LIGHT_BLUE

def add_footer(slide, page_num):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(11.15), Inches(8.27), Inches(0.54))
    shape.fill.solid()
    shape.fill.fore_color.rgb = NAVY
    shape.line.fill.background()
    
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(11.12), Inches(8.27), Inches(0.03))
    accent.fill.solid()
    accent.fill.fore_color.rgb = CYAN
    accent.line.fill.background()
    
    txBox = slide.shapes.add_textbox(Inches(0.45), Inches(11.20), Inches(5.0), Inches(0.35))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = "Spillburg Logistics 1 (Pvt) Ltd • www.spillburglogistics1.com"
    p.font.name = "Arial"
    p.font.size = Pt(8.5)
    p.font.color.rgb = LIGHT_BLUE
    
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

tx = slide1.shapes.add_textbox(Inches(0.6), Inches(0.8), Inches(7.0), Inches(1.0))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "SPILLBURG"
p.font.name = "Georgia"
p.font.size = Pt(28)
p.font.bold = True
p.font.color.rgb = WHITE
p2 = tf.add_paragraph()
p2.text = "LOGISTICS 1 PRIVATE LIMITED"
p2.font.name = "Arial"
p2.font.size = Pt(9.5)
p2.font.bold = True
p2.font.color.rgb = LIGHT_BLUE

tx2 = slide1.shapes.add_textbox(Inches(0.6), Inches(5.0), Inches(7.0), Inches(4.5))
tf2 = tx2.text_frame
p = tf2.paragraphs[0]
p.text = "GLOBAL FREIGHT, CUSTOMS & SUPPLY CHAIN SOLUTIONS"
p.font.name = "Arial"
p.font.size = Pt(9.5)
p.font.bold = True
p.font.color.rgb = LIGHT_BLUE

p = tf2.add_paragraph()
p.text = "COMPANY PROFILE 2026"
p.font.name = "Georgia"
p.font.size = Pt(36)
p.font.bold = True
p.font.color.rgb = WHITE

p = tf2.add_paragraph()
p.text = "\nConnecting international trade lanes with ocean freight, expedited air cargo, licensed customs brokerage, bonded warehousing, and multi-modal inland container haulage."
p.font.name = "Arial"
p.font.size = Pt(13)
p.font.color.rgb = RGBColor(226, 232, 240)

# ----------------- SLIDE 2: ABOUT -----------------
slide2 = prs.slides.add_slide(blank_slide_layout)
add_header(slide2, "Strategic Supply Chain Partner")
add_footer(slide2, 2)

tx = slide2.shapes.add_textbox(Inches(0.6), Inches(1.2), Inches(4.2), Inches(8.5))
tf = tx.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "ABOUT SPILLBURG LOGISTICS 1"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

p = tf.add_paragraph()
p.text = "\nSpillburg Logistics 1 (Pvt) Ltd is a premier total logistics provider headquartered in Colombo, Sri Lanka, perfectly situated along the busiest maritime artery in the Indian Ocean connecting Europe, the Middle East, Africa, and the Asia-Pacific region.\n\nAs part of the prestigious Spillburg Group, we deliver agile, technology-driven freight forwarding and supply chain solutions. Our comprehensive service portfolio encompasses international ocean freight (FCL/LCL), expedited IATA air cargo, licensed Sri Lanka Customs House Brokerage, customs-bonded warehousing, and heavy project haulage.\n\nWe leverage long-term carrier contracts, automated port customs electronic clearance, and dedicated prime mover fleets to ensure our clients experience unparalleled transit velocity and cost efficiency."
p.font.name = "Arial"
p.font.size = Pt(11)
p.font.color.rgb = DARK_TEXT

card1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(7.5), Inches(1.9), Inches(1.2))
card1.fill.solid()
card1.fill.fore_color.rgb = NAVY
card1.line.color.rgb = CYAN
tf = card1.text_frame
p = tf.paragraphs[0]
p.text = "15+\nTrade Lanes"
p.font.name = "Georgia"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = LIGHT_BLUE

card2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.7), Inches(7.5), Inches(1.9), Inches(1.2))
card2.fill.solid()
card2.fill.fore_color.rgb = NAVY
card2.line.color.rgb = CYAN
tf = card2.text_frame
p = tf.paragraphs[0]
p.text = "12K+\nAnnual TEUs"
p.font.name = "Georgia"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = LIGHT_BLUE

box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.0), Inches(1.5), Inches(2.7), Inches(7.2))
box.fill.solid()
box.fill.fore_color.rgb = BG_SOFT
box.line.color.rgb = RGBColor(226, 232, 240)
tf = box.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Core Operational Capabilities"
p.font.name = "Georgia"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = NAVY

capabilities = [
    "International Ocean Freight (FCL & LCL)",
    "Priority Air Cargo & Time-Critical Charters",
    "Licensed Sri Lanka Customs Brokerage",
    "Bonded Warehousing, 3PL & Cross-Docking",
    "Islandwide Container Fleet Haulage",
    "Colombo Port Transshipment Consolidation",
    "Cold Chain & Reefer Container Logistics",
    "Project Cargo & Heavy Lift Handling"
]
for c in capabilities:
    p = tf.add_paragraph()
    p.text = f"⚓ {c}"
    p.font.name = "Arial"
    p.font.size = Pt(9.5)
    p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 3: BOARD OF DIRECTORS -----------------
slide3 = prs.slides.add_slide(blank_slide_layout)
add_header(slide3, "Board & Executive Leadership")
add_footer(slide3, 3)

tx = slide3.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "BOARD OF DIRECTORS"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

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
p.font.color.rgb = BLUE
p = tf.add_paragraph()
p.text = "Former Director in the Board of Investment of Sri Lanka's Investment Promotions division with over 15 years hands-on experience in project setup, infrastructure planning, and trade facilitation. President of Sri Lanka Malaysia Business Council."
p.font.size = Pt(8.5)
p.font.color.rgb = DARK_TEXT

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
p.font.color.rgb = BLUE
p = tf.add_paragraph()
p.text = "Former banker at HSBC & Standard Chartered with over 15 years' expertise in maritime trade finance, supply chain structuring, and capital investment. President of Sri Lanka Nordic and Sri Lanka France Business Councils."
p.font.size = Pt(8.5)
p.font.color.rgb = DARK_TEXT

mgt = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(7.3), Inches(7.0), Inches(3.5))
mgt.fill.solid()
mgt.fill.fore_color.rgb = BG_SOFT
mgt.line.color.rgb = RGBColor(226, 232, 240)
tf = mgt.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Senior Logistics Operations & Customs Management"
p.font.name = "Georgia"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = NAVY

team = [
    ("Head of Customs House Brokerage", "Licensed Customs House Agent (CHA)", "25+ years directing fast-track customs clearance at Colombo Port (JCT, CICT, SAGT) & Katunayake Air Cargo."),
    ("Director - Ocean & Air Freight", "IATA Certified Operations Specialist", "18+ years managing global liner carrier contracts, LCL consolidation hubs & air cargo charters."),
    ("General Manager - 3PL & Warehousing", "Supply Chain & Bonded Logistics Manager", "15+ years overseeing customs-bonded facilities, high-bay inventory distribution & cross-dock operations."),
    ("Fleet & Overland Transport Controller", "Inland Haulage Specialist", "20+ years coordinating prime mover fleets, multi-axle trailers & heavy-lift industrial plant transport.")
]
for name, role, desc in team:
    p = tf.add_paragraph()
    p.text = f"• {name} ({role}): {desc}"
    p.font.name = "Arial"
    p.font.size = Pt(8.5)
    p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 4: FREIGHT MODES -----------------
slide4 = prs.slides.add_slide(blank_slide_layout)
add_header(slide4, "Multi-Modal Freight Spectrum")
add_footer(slide4, 4)

tx = slide4.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "SERVICE SPECTRUM & FREIGHT MODES"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

modes = [
    ("International Ocean Freight", ["Full Container Load (FCL) tier-1 liner contracts", "LCL weekly consolidation services", "Buyer's consolidation & multi-vendor cargo", "Reefer container bookings for seafood & fruit"]),
    ("Expedited Air Cargo Forwarding", ["IATA accredited scheduled departures to global hubs", "Full & part charter flight arrangements", "Garment-on-Hanger (GOH) air freight", "Cold-chain pharma air transport"]),
    ("Customs House Brokerage", ["Full licensed brokerage at sea & air ports", "Automated ASYCUDA World electronic filings", "HS Code tariff optimization & classification", "BOI inward processing & TIEP clearances"]),
    ("Bonded Warehousing & 3PL", ["Customs-bonded warehouse near Colombo port", "High-bay selective racking with WMS system", "Value-added services: barcoding, shrink-wrap", "Pick-and-pack fulfillment for retail distribution"]),
    ("Inland Transport & Fleet Haulage", ["Prime mover fleet with 20ft & 40ft trailers", "Real-time 24/7 satellite GPS tracking", "Multi-axle low-bed trailers for heavy machinery", "Dedicated port-to-factory shuttle runs"]),
    ("Project Cargo & Heavy Lift", ["Out-of-Gauge (OOG) flat-rack & open-top solutions", "Heavy industrial machinery & transformers", "Turnkey wind turbine & solar park logistics", "Route feasibility surveys & police escorts"])
]
coords = [
    (0.6, 1.8), (4.2, 1.8),
    (0.6, 4.8), (4.2, 4.8),
    (0.6, 7.8), (4.2, 7.8)
]
pcoords = [(0.6, 1.8), (4.2, 1.8), (0.6, 6.2), (4.2, 6.2)]

for idx, (title, items) in enumerate(modes):
    x, y = coords[idx]
    card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(3.4), Inches(2.7))
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = BLUE
    tf = card.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"Mode 0{idx+1}: {title}"
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
add_header(slide5, "Specialized Supply Chain Solutions")
add_footer(slide5, 5)

tx = slide5.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "PRACTICE AREAS & COLD CHAIN HUB"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

spec_log = [
    ("01", "Perishables & Cold Chain Logistics", [
        "Reefer container pre-cooling, monitoring & plug-in yard",
        "Air cargo cold room storage at BIA Katunayake airport",
        "Yellowfin tuna, seafood & fresh agricultural exports",
        "GDP-compliant cold storage for pharmaceuticals & vaccines"
    ]),
    ("02", "Transshipment & Entrepot Trade", [
        "Multi-Country Consolidation (MCC) at Colombo Port",
        "Duty-free entrepot processing, repacking & re-export",
        "Container de-stuffing & multi-carrier reloading",
        "Direct feeder connectivity to India & GCC markets"
    ]),
    ("03", "Dangerous Goods (DG) Handling", [
        "Certified IMO maritime and ICAO air DG specialists",
        "Material Safety Data Sheet (MSDS) validation",
        "UN-certified compliant packaging & hazardous labeling",
        "Port Authority hazardous storage permits & approvals"
    ]),
    ("04", "Supply Chain Technology & Tracking", [
        "Cloud-based track-and-trace with real-time updates",
        "Electronic Data Interchange (EDI) with shipping lines",
        "Automated departure, arrival & clearance milestone alerts",
        "Customized KPI dashboards for container turnaround"
    ])
]
for idx, (num, title, items) in enumerate(spec_log):
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
add_header(slide6, "Flagship Logistics Corridor")
add_footer(slide6, 6)

tx = slide6.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "COLOMBO PORT & SEA-AIR CORRIDOR"
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
p.text = "INDIAN OCEAN MARITIME SUPERHUB"
p.font.name = "Arial"
p.font.size = Pt(9)
p.font.bold = True
p.font.color.rgb = LIGHT_BLUE
p = tf.add_paragraph()
p.text = "Colombo Port Connectivity & Expedited Sea-Air Corridors"
p.font.name = "Georgia"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = WHITE
p = tf.add_paragraph()
p.text = "\nSpillburg Logistics 1 utilizes Colombo's geographic supremacy as South Asia's deepest container port to accelerate global trade. We bridge maritime ocean liners with global air cargo freighters in under four hours."
p.font.name = "Arial"
p.font.size = Pt(10)
p.font.color.rgb = RGBColor(226, 232, 240)

c1 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(4.5), Inches(3.4), Inches(5.8))
c1.fill.solid()
c1.fill.fore_color.rgb = WHITE
c1.line.color.rgb = RGBColor(226, 232, 240)
tf = c1.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Hub 01: Deep-Water Port Synergy"
p.font.name = "Georgia"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = NAVY
hsteps1 = [
    "Direct berthing access at CICT & CWIT for 24,000+ TEU mega vessels.",
    "Rapid inter-terminal transfer between JCT, SAGT, and CICT with zero gate delays.",
    "Dedicated priority customs inspection lanes enabling 4-hour express container clearance.",
    "Feeder connections reaching Chennai, Mumbai, Karachi & Male within 48-72 hours."
]
for s in hsteps1:
    p = tf.add_paragraph()
    p.text = f"• {s}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = DARK_TEXT

c2 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.2), Inches(4.5), Inches(3.4), Inches(5.8))
c2.fill.solid()
c2.fill.fore_color.rgb = WHITE
c2.line.color.rgb = RGBColor(226, 232, 240)
tf = c2.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Hub 02: Intermodal Sea-Air Freight Relay"
p.font.name = "Georgia"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = NAVY
hsteps2 = [
    "Fast container vessel arrival at Colombo Port from Southeast Asia / Bangladesh.",
    "Priority bonded de-consolidation directly in Colombo Port customs bonded zone.",
    "Expressway bonded road transit to BIA Katunayake airport cargo terminal.",
    "Immediate palletization onto wide-body freighters bound for Europe & North America."
]
for s in hsteps2:
    p = tf.add_paragraph()
    p.text = f"• {s}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 7: ALLIANCES -----------------
slide7 = prs.slides.add_slide(blank_slide_layout)
add_header(slide7, "Global Freight Alliance")
add_footer(slide7, 7)

tx = slide7.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "GLOBAL ALLIANCE & PORT NETWORK"
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
p.text = "Maritime, Port & Trade Chamber Affiliations"
p.font.name = "Georgia"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = NAVY

alliances = [
    "Sri Lanka Ports Authority (SLPA) Registered Forwarder",
    "Airport & Aviation Services Sri Lanka (AASL) Cargo Partner",
    "Sri Lanka Freight Forwarders Association (SLFFA)",
    "FIATA (International Federation of Freight Forwarders)",
    "The Ceylon Chamber of Commerce (Maritime Committee)",
    "The National Chamber of Exporters of Sri Lanka (NCE)",
    "European Chamber of Commerce Sri Lanka (ECCSL)",
    "Strategic Carrier Alliances: Maersk, MSC, CMA CGM, Hapag-Lloyd, ONE, Emirates SkyCargo"
]
for a in alliances:
    p = tf.add_paragraph()
    p.text = f"• {a}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 8: SECTORS -----------------
slide8 = prs.slides.add_slide(blank_slide_layout)
add_header(slide8, "Sector Logistics Solutions")
add_footer(slide8, 8)

tx = slide8.shapes.add_textbox(Inches(0.6), Inches(1.1), Inches(7.0), Inches(0.5))
tf = tx.text_frame
p = tf.paragraphs[0]
p.text = "STRATEGIC SECTOR PORTFOLIO"
p.font.name = "Georgia"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = NAVY

log_sectors = [
    ("Apparel, Garments & Textiles", "Fast-Fashion & High-Value Exports", [
        "Garment on Hanger (GOH) specialized 40ft container fleet",
        "Fast-track clearance at Katunayake BIA airport terminal",
        "Time-definite air freight for retail seasonal launches in EU/US",
        "Raw material fabric & accessories import consolidation"
    ]),
    ("Perishables, Seafood & Agro", "Ceylon Tea, Tuna & Perishables", [
        "Air-freight yellowfin tuna to Tokyo, EU & North America",
        "Controlled atmosphere reefer containers for Ceylon tea export",
        "Cold-chain tarmac transfer minimizing temperature excursions",
        "Phytosanitary & health inspection certificate facilitation"
    ]),
    ("Industrial, Energy & Pharma", "Solar Modules, API & Machinery", [
        "Solar PV panels & 50MW battery storage container transport",
        "Temperature-monitored pharmaceutical active ingredient imports",
        "Heavy-lift prime mover haulage for transformers & factory plant",
        "Route police escorts, bridge surveys and permit acquisitions"
    ])
]
for idx, (title, sub, items) in enumerate(log_sectors):
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
    p.font.color.rgb = BLUE
    for it in items:
        p = tf.add_paragraph()
        p.text = f"• {it}"
        p.font.size = Pt(8.5)
        p.font.color.rgb = DARK_TEXT

# ----------------- SLIDE 9: CONTACT -----------------
slide9 = prs.slides.add_slide(blank_slide_layout)
add_header(slide9, "24/7 Operations Desk")
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
p.text = "MOBILIZE YOUR GLOBAL SUPPLY CHAIN"
p.font.name = "Georgia"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = WHITE
p = tf.add_paragraph()
p.text = "\nConnect with our freight forwarding directors and customs brokerage team to request instant freight quotes, schedule sea-air consignments, or book bonded warehouse space."
p.font.size = Pt(10)
p.font.color.rgb = RGBColor(226, 232, 240)

o1 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(4.1), Inches(3.4), Inches(2.2))
o1.fill.solid()
o1.fill.fore_color.rgb = BG_SOFT
o1.line.color.rgb = RGBColor(226, 232, 240)
tf = o1.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Port Operations Hub"
p.font.name = "Georgia"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = NAVY
p = tf.add_paragraph()
p.text = "\nColombo Port Maritime Logistics Center,\nNo. 568/2, Aluthmawatha Road, Colombo 15,\nSri Lanka."
p.font.size = Pt(9.5)
p.font.color.rgb = DARK_TEXT

o2 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.2), Inches(4.1), Inches(3.4), Inches(2.2))
o2.fill.solid()
o2.fill.fore_color.rgb = BG_SOFT
o2.line.color.rgb = RGBColor(226, 232, 240)
tf = o2.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Corporate & Airport Desk"
p.font.name = "Georgia"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = NAVY
p = tf.add_paragraph()
p.text = "\nOffice 14, Cinnamon Lakeside Hotel, Colombo 02.\nAir Cargo Village Operations Desk,\nBIA Katunayake, Sri Lanka."
p.font.size = Pt(9.5)
p.font.color.rgb = DARK_TEXT

tx_ct = slide9.shapes.add_textbox(Inches(0.6), Inches(6.6), Inches(4.5), Inches(3.8))
tf = tx_ct.text_frame
contacts = [
    ("Telephone", "+94 11 233 6116"),
    ("Telefax", "+94 11 252 9309"),
    ("24/7 Hotlines", "+94 77 748 7720 | +94 77 779 0919"),
    ("E-Mail", "info@spillburglogistics1.com / info@spillburg.com"),
    ("Websites", "www.spillburglogistics1.com • www.spillburg.com")
]
for lbl, val in contacts:
    p = tf.add_paragraph()
    p.text = f"{lbl:14s}: {val}"
    p.font.name = "Arial"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = DARK_TEXT

qr_img = os.path.join(assets_dir, "qr_code.jpg")
if os.path.exists(qr_img):
    slide9.shapes.add_picture(qr_img, Inches(5.5), Inches(6.8), Inches(1.8), Inches(1.8))

pptx_out = os.path.join(base_dir, "Company Profile - 2026.pptx")
prs.save(pptx_out)
print(f"Saved editable PowerPoint for Logistics: {pptx_out}")
