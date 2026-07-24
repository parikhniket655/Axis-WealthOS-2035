import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# Custom Canvas for Header/Footer & Dynamic Page Numbering
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Skip decorations on the cover page
        
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#861F41"))  # Axis Burgundy
        
        # Header text
        self.drawString(54, 755, "AXIS BANK TRANSFORMATION COUNCIL | MASTER REFERENCES")
        
        # Header thin rule
        self.setLineWidth(0.5)
        self.setStrokeColor(colors.HexColor("#D3D3D3"))
        self.line(54, 750, 558, 750)
        
        # Footer thin rule
        self.line(54, 50, 558, 50)
        
        # Footer text
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#727272"))
        self.drawString(54, 38, "CONFIDENTIAL | SLIDE EVIDENCE HIERARCHY MAP")
        
        # Page numbers
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 38, page_text)
        self.restoreState()

def build_links_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=72,
        bottomMargin=72
    )

    styles = getSampleStyleSheet()
    
    # Custom Palette
    primary_color = colors.HexColor("#861F41")   # Axis Burgundy
    secondary_color = colors.HexColor("#7F1D1D") # Deep Red Accent
    text_color = colors.HexColor("#2C2C2C")      # Charcoal Body Text
    bg_tint = colors.HexColor("#F9F5F6")         # Soft Pink Background Tint
    border_color = colors.HexColor("#E5D2D6")    # Light Pink Border Tint

    # Custom Typography Styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=primary_color,
        spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#555555"),
        spaceAfter=30
    )
    
    metadata_style = ParagraphStyle(
        'CoverMetadata',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#727272"),
        spaceAfter=6
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=primary_color,
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=secondary_color,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=text_color,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=text_color,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=text_color
    )
    
    table_cell_bold_style = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=text_color
    )

    story = []

    # ------------------ COVER PAGE ------------------
    story.append(Spacer(1, 100))
    story.append(Paragraph("AXIS WEALTHOS 2035", title_style))
    story.append(Paragraph("Master References & Slide-by-Slide Evidence Mapping Guide", subtitle_style))
    
    # Decorative line
    d_table = Table([[""]], colWidths=[504])
    d_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 4, primary_color),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(d_table)
    story.append(Spacer(1, 180))
    
    # Metadata Block
    story.append(Paragraph("<b>SUBMISSION BY:</b> Team CashCows", metadata_style))
    story.append(Paragraph("<b>COMPETITION:</b> MOVES 2026 — Organization of the Future: Design for 2035", metadata_style))
    story.append(Paragraph("<b>DATE:</b> July 24, 2026", metadata_style))
    story.append(Paragraph("<b>STATUS:</b> CONFIDENTIAL / BOARD-LEVEL BRIEF", metadata_style))
    story.append(PageBreak())

    # ------------------ SLIDE 1 SOURCES ------------------
    story.append(Paragraph("Slide 1 — The Big Bet: Section-Wise Source Map", h1_style))
    story.append(Paragraph(
        "Slide 1 establishes the macroeconomic case, current product-centric structural bottlenecks, "
        "and outlines the WealthOS operating model concept.",
        body_style
    ))
    story.append(Spacer(1, 5))

    # Slide 1 Mapping Table
    s1_data = [
        [Paragraph("<b>Section & Element</b>", table_header_style), 
         Paragraph("<b>Source / Verification Basis</b>", table_header_style), 
         Paragraph("<b>Reference URL Link</b>", table_header_style)],
        
        [Paragraph("<b>1. Future of Wealth</b><br/>• Wealth Market Opportunity", table_cell_bold_style), 
         Paragraph("Deloitte India – Financial Wealth Management Services in India", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.deloitte.com/in</u></font>", table_cell_style)],
        
        [Paragraph("<b>1. Future of Wealth</b><br/>• Advisory Shift (~80% Hybrid)", table_cell_bold_style), 
         Paragraph("McKinsey – Asia Wealth Report", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.mckinsey.com/industries/financial-services/our-insights/asia-wealth-management</u></font>", table_cell_style)],
         
        [Paragraph("<b>1. Future of Wealth</b><br/>• RM Productivity Gap (67% non-client)", table_cell_bold_style), 
         Paragraph("Capgemini – Wealth Management Top Trends 2024", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.capgemini.com/insights/research-library/top-trends-in-wealth-management/</u></font>", table_cell_style)],
         
        [Paragraph("<b>1. Future of Wealth</b><br/>• Household switching risk (79%+)", table_cell_bold_style), 
         Paragraph("Capgemini Top Trends 2024 & World Wealth Report 2023", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://worldwealthreport.com/</u></font>", table_cell_style)],
         
        [Paragraph("<b>2. Product-Centric Silos</b><br/>• Current model friction", table_cell_bold_style), 
         Paragraph("Original team synthesis based on Axis Burgundy Private positioning & Annual Report FY25", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.axisbank.com/burgundy-private</u></font>", table_cell_style)],
         
        [Paragraph("<b>3. Customer Journey</b><br/>• Wealth Twin architecture", table_cell_bold_style), 
         Paragraph("Original Framework supported by Sahamati Account Aggregator & Deloitte Agentic AI", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://sahamati.org.in/</u></font>", table_cell_style)],
         
        [Paragraph("<b>4. Enterprise Capability</b><br/>• Why wealth anchors Axis", table_cell_bold_style), 
         Paragraph("Original team framework based on Axis FY25 Integrated Annual Report", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.axisbank.com/shareholders-corner/shareholders-information/financial-results</u></font>", table_cell_style)],
         
        [Paragraph("<b>5. Building Blocks</b><br/>• Burgundy scale & virtual RMs", table_cell_bold_style), 
         Paragraph("Axis Bank Q4 FY26 Investor Presentation & Annual Report FY25 (₹6.78T Burgundy AUM base)", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.axisbank.com/shareholders-corner/shareholders-information/financial-results</u></font>", table_cell_style)],
         
        [Paragraph("<b>6. Redefining Banking</b><br/>• 2035 Outcomes", table_cell_bold_style), 
         Paragraph("Original team framework supported by McKinsey Wealth 2035 trends", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.mckinsey.com/industries/financial-services</u></font>", table_cell_style)]
    ]
    
    t1 = Table(s1_data, colWidths=[160, 160, 184])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_tint]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
    ]))
    story.append(t1)
    story.append(PageBreak())

    # ------------------ SLIDE 2 SOURCES ------------------
    story.append(Paragraph("Slide 2 — How It Works & Impact: Section-Wise Source Map", h1_style))
    story.append(Paragraph(
        "Slide 2 details the operational mechanics (Wealth Twin, Advisory Pod, AI Advice Factory) and "
        "reconciles the business case using the Feasibility v2 model.",
        body_style
    ))
    story.append(Spacer(1, 5))

    # Slide 2 Mapping Table
    s2_data = [
        [Paragraph("<b>Section & Element</b>", table_header_style), 
         Paragraph("<b>Source / Verification Basis</b>", table_header_style), 
         Paragraph("<b>Reference URL Link</b>", table_header_style)],
        
        [Paragraph("<b>1. Household Wealth Twin</b><br/>• Consented data retrieval", table_cell_bold_style), 
         Paragraph("Sahamati Account Aggregator APIs & Strategy Master Document", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://sahamati.org.in/</u></font>", table_cell_style)],
        
        [Paragraph("<b>2. Advisory Pod</b><br/>• LRP + PA + CS tag-team", table_cell_bold_style), 
         Paragraph("McKinsey Wealth 2035 (multi-advisor structures) & McKinsey Advisor Shortage briefs", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.mckinsey.com/industries/financial-services</u></font>", table_cell_style)],
         
        [Paragraph("<b>3. AI Advisory Factory</b><br/>• Agentic triggers", table_cell_bold_style), 
         Paragraph("Deloitte Agentic AI Whitepapers & Strategy Master Document", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.deloitte.com/</u></font>", table_cell_style)],
         
        [Paragraph("<b>4. Governance & Trust</b><br/>• Suitability, AA consent, SPARSH", table_cell_bold_style), 
         Paragraph("Deloitte Agentic AI, Sahamati consent guidelines & Capgemini World Wealth Report", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://worldwealthreport.com/</u></font>", table_cell_style)],
         
        [Paragraph("<b>5. Phased Rollout</b><br/>• Waves 1, 2, and 3", table_cell_bold_style), 
         Paragraph("Original team roadmap supported by Axis Annual Report branch footprints", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.axisbank.com/shareholders-corner/shareholders-information/financial-results</u></font>", table_cell_style)],
         
        [Paragraph("<b>6. Business Impact</b><br/>• Pod capacity (150-220)", table_cell_bold_style), 
         Paragraph("Capgemini WM Top Trends 2024 & McKinsey Advisor Capacity benchmarks", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://www.capgemini.com/insights/research-library/top-trends-in-wealth-management/</u></font>", table_cell_style)],
         
        [Paragraph("<b>6. Business Impact</b><br/>• Cost-to-serve drop (-85%)", table_cell_bold_style), 
         Paragraph("Internal calculations (automated RM prep) & Capgemini World Wealth Report cost splits", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://worldwealthreport.com/</u></font>", table_cell_style)],
         
        [Paragraph("<b>6. Business Impact</b><br/>• Churn guardrails & cross-sell", table_cell_bold_style), 
         Paragraph("Original IP (Team CashCows) supported by Capgemini World Wealth Report & McKinsey Wealth", table_cell_style), 
         Paragraph("<font color='#861F41'><u>https://worldwealthreport.com/</u></font>", table_cell_style)]
    ]
    
    t2 = Table(s2_data, colWidths=[160, 160, 184])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_tint]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
    ]))
    story.append(t2)
    story.append(Spacer(1, 15))

    # ------------------ ORIGINAL IP CHECKLIST ------------------
    story.append(Paragraph("Team Original IP & Intellectual Contribution", h2_style))
    story.append(Paragraph(
        "These core strategic frameworks are original conceptual architectures created by our team "
        "and should be defended confidently as proprietary IP:",
        body_style
    ))
    
    ips = [
        "<b>The WealthOS Paradigm:</b> Shifting from transactional product sales to a household-centric operating system.",
        "<b>The Household Wealth Twin:</b> Digital mapping of multi-generational balance sheets and lifecycle milestones.",
        "<b>The 3-Person Advisory Pod Model:</b> Reorganizing branch coverage teams (Lead RM, Portfolio Architect, Credit Specialist).",
        "<b>The AI Advisory Factory:</b> Continuous background scanning agents compressing administrative prep time by 95%.",
        "<b>SPARSH Advisory Control:</b> Suitability-by-design compliance filters embedded directly in the advisor workflow.",
        "<b>Feasibility v2 Financial Modeling:</b> Re-engineered NPV (₹132.7 Cr) and IRR (21.4%) using the bottleneck capacity rule."
    ]
    for ip in ips:
        story.append(Paragraph(f"• {ip}", bullet_style))

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)

if __name__ == "__main__":
    build_links_pdf("/Users/ketanparikh/Desktop/Axis/Axis_WealthOS_2035_Master_Links_Registry.pdf")
    print("Links PDF generated successfully.")
