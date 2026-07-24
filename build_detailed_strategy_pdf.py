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
        self.drawString(54, 755, "AXIS BANK TRANSFORMATION COUNCIL | WEALTHOS 2035")
        
        # Header thin rule
        self.setLineWidth(0.5)
        self.setStrokeColor(colors.HexColor("#D3D3D3"))
        self.line(54, 750, 558, 750)
        
        # Footer thin rule
        self.line(54, 50, 558, 50)
        
        # Footer text
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#727272"))
        self.drawString(54, 38, "CONFIDENTIAL | PITCH & FEASIBILITY DETAIL GUIDE")
        
        # Page numbers
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 38, page_text)
        self.restoreState()

def create_strategy_guide_pdf(filename):
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
    secondary_color = colors.HexColor("#C9A84C") # Gold Accent
    text_color = colors.HexColor("#2C2C2C")      # Charcoal Body Text
    bg_tint = colors.HexColor("#F9F5F6")         # Soft Pink Background Tint
    border_color = colors.HexColor("#E5D2D6")    # Light Pink Border Tint

    # Custom Typography Styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=28,
        leading=34,
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
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#727272"),
        spaceAfter=6
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=primary_color,
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=primary_color,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=text_color,
        spaceAfter=8
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
        fontSize=9,
        leading=11,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=text_color
    )
    
    table_cell_bold_style = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=text_color
    )

    story = []

    # ------------------ COVER PAGE ------------------
    story.append(Spacer(1, 100))
    story.append(Paragraph("AXIS WEALTHOS 2035", title_style))
    story.append(Paragraph("PITCH SCRIPT & DEEP-DIVE FEASIBILITY GUIDE", subtitle_style))
    
    # Decorative line
    d_table = Table([[""]], colWidths=[504])
    d_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 3, primary_color),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(d_table)
    story.append(Spacer(1, 180))
    
    # Metadata Block
    story.append(Paragraph("<b>SUBMISSION BY:</b> Axis Bank Transformation Council", metadata_style))
    story.append(Paragraph("<b>PROJECT PATHWAY:</b> Wealth Management & Affluent Banking", metadata_style))
    story.append(Paragraph("<b>TARGET ENVIRONMENT:</b> MOVES 2026 Boardroom Pitch", metadata_style))
    story.append(Paragraph("<b>CONFIDENTIALITY:</b> Internal Council Use Only", metadata_style))
    story.append(PageBreak())

    # ------------------ SECTION 1: EXECUTIVE BRIEF ------------------
    story.append(Paragraph("1. Executive Brief: The Opportunity & Challenge", h1_style))
    story.append(Paragraph(
        "The Indian wealth management industry is experiencing a historic expansion. Powered by economic growth and "
        "digital public infrastructure, financial wealth in India is projected to grow from <b>$1.1 Trillion today to $2.3 Trillion by 2030</b>. "
        "McKinsey's Asia Wealth Report indicates that <b>80% of affluent investors</b> prefer a hybrid advisory model—combining advanced "
        "digital analytics with deep human relationship management—rather than a pure-play digital platform or a legacy physical RM.",
        body_style
    ))
    story.append(Paragraph(
        "At the same time, relationship managers (RMs) spend <b>67% of their time on administrative tasks</b> (statement collection, "
        "manual risk suitability checks, and portfolio reporting) rather than direct client interaction. Axis Bank Burgundy, which holds "
        "a leading market position with <b>₹6.78 Trillion in total Burgundy AUM and ₹2.40 Trillion in Burgundy Private AUM</b> (serving "
        "<b>16,453 families</b>), must transform its operating model. To capture the next wave of wealth, particularly in Tier-2 and Tier-3 "
        "regional hubs, Axis cannot simply hire more RMs. We must build a system that multiplies advisor capability rather than advisor headcount.",
        body_style
    ))
    story.append(Spacer(1, 10))
    story.append(PageBreak())

    # ------------------ SECTION 2: DEEP-DIVE FEASIBILITY ------------------
    story.append(Paragraph("2. Deep-Dive Feasibility Analysis & Financial Models", h1_style))
    story.append(Paragraph(
        "To satisfy the board's scrutiny, we must defend the feasibility of Axis WealthOS 2035 with granular, "
        "hard-quantified operational and economic models.",
        body_style
    ))
    
    story.append(Paragraph("A. Financial & Cost-to-Serve Feasibility", h2_style))
    story.append(Paragraph(
        "The financial viability of the WealthOS model relies on shifting the cost curve of wealth advisory. "
        "A traditional high-touch RM is limited by the cognitive bandwidth to manage client relationships, "
        "rebalance portfolios, and perform manual paperwork.",
        body_style
    ))
    
    # Financial Table comparison
    cost_data = [
        [Paragraph("<b>Cost Element (Annual per Client)</b>", table_header_style), 
         Paragraph("<b>Legacy RM Model (2026)</b>", table_header_style), 
         Paragraph("<b>WealthOS Pod Model (2035)</b>", table_header_style), 
         Paragraph("<b>Operational Change Mechanism</b>", table_header_style)],
        
        [Paragraph("RM Headcount Cost Share", table_cell_bold_style), 
         Paragraph("₹9,500", table_cell_style), 
         Paragraph("₹1,200", table_cell_style), 
         Paragraph("AI prepares client briefs, raising RM capacity from 80 to 180 accounts.", table_cell_style)],
        
        [Paragraph("Travel & Client Engagement", table_cell_bold_style), 
         Paragraph("₹3,000", table_cell_style), 
         Paragraph("₹450", table_cell_style), 
         Paragraph("Centralized virtual expert pods and localized Tier-2 branch RM support.", table_cell_style)],
         
        [Paragraph("Compliance, Audit & Operations", table_cell_bold_style), 
         Paragraph("₹1,800", table_cell_style), 
         Paragraph("₹150", table_cell_style), 
         Paragraph("Automated SEBI checks & automated audit trail generation.", table_cell_style)],
         
        [Paragraph("IT & Analytics Licensing", table_cell_bold_style), 
         Paragraph("₹700", table_cell_style), 
         Paragraph("₹450", table_cell_style), 
         Paragraph("Investment in core AI stack (capex) amortized over a larger base.", table_cell_style)],
         
        [Paragraph("<b>Total Cost-to-Serve / Client / Yr</b>", table_cell_bold_style), 
         Paragraph("<b>₹15,000</b>", table_cell_bold_style), 
         Paragraph("<b>₹2,250</b>", table_cell_bold_style), 
         Paragraph("<b>85% Net Cost Reduction</b>", table_cell_bold_style)]
    ]
    
    c_table = Table(cost_data, colWidths=[140, 94, 94, 176])
    c_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_tint]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
    ]))
    story.append(c_table)
    story.append(Spacer(1, 10))

    # Capital Investment & ROI formulas
    story.append(Paragraph("<b>Capital Expenditure (CapEx) & ROI Projections:</b>", body_style))
    story.append(Paragraph(
        "• <b>Development Phase Investment:</b> The total capital outlay to construct the Wealth Twin API gateway, "
        "integrate the Account Aggregator pipeline, and train the specialized AI Advice models is projected at "
        "<b>₹120 Crores</b> over a 5-year phased rollout. Opex is estimated at <b>₹15 Crores</b> annually.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Financial NPV & IRR:</b> Based on our industry-grounded base case (150 clients/pod, 75 bps fee, 12% WACC), the project yields "
        "a <b>Net Present Value (NPV) of ₹132.7 Crores</b> and an <b>Internal Rate of Return (IRR) of 21.4%</b> (payback: 3.6 years), "
        "clearing the bank's 20% strategic hurdle. Under our upside case (220 clients/pod), the project yields an "
        "<b>NPV of ₹224.5 Crores</b> and an <b>IRR of 26.7%</b> (payback: 3.3 years).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>One Axis Group Cross-Sell Lift:</b> WealthOS will automate client routing to Axis Securities, AMC, and Trustee. "
        "We project that the cross-sell attachment ratio (the average number of group products held by a Burgundy Private client) "
        "will rise from <b>1.8 today to 4.2 by 2035</b>, generating high-margin fee income across all subsidiaries.",
        bullet_style
    ))
    
    story.append(Spacer(1, 5))
    story.append(Paragraph("B. Operational & Structural Feasibility", h2_style))
    story.append(Paragraph(
        "The operational feasibility is ensured by restructuring the bank's front-office relationship teams and "
        "revising the advisor performance scorecard. We do not require RMs to become technical experts; we change their structural roles.",
        body_style
    ))
    story.append(Paragraph(
        "• <b>The 3-Person Advisory Pod Model:</b> We transition branches away from the single-RM structure. "
        "A Pod consists of: (1) <i>Lead Relationship Partner</i> (owns client trust, goal discovery, and family dynamics); "
        "(2) <i>Portfolio Architect</i> (conducts asset modeling and risk rebalancing); (3) <i>Credit Specialist</i> "
        "(manages asset leverage, mortgages, and business-owner capital loans). A single Pod supports a realistic base of "
        "<b>150 clients</b>, with an upside stretch target of <b>220 clients</b> as AI-assist tools mature, preventing the "
        "sum-of-caps error of 600/pod.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Performance Scorecard Transformation:</b> We will completely eliminate product-specific sales commission targets, "
        "which often lead to mis-selling. The new scorecard consists of: <b>60% Consolidated Wallet Share & Retention</b> "
        "(rewarding overall assets and liabilities held at Axis), and <b>40% SPARSH Compliance & Suitability</b> "
        "(rewarding low risk-profile drift and high client feedback scores).",
        bullet_style
    ))
    story.append(PageBreak())

    # ------------------ SECTION 2 CONTINUED: TECH & REGULATORY ------------------
    story.append(Paragraph("C. Technology & Data Feasibility", h2_style))
    story.append(Paragraph(
        "The data and technology architecture leverages India's advanced Digital Public Infrastructure (DPI) and secure API pipes.",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Account Aggregator (AA) Integration:</b> The data retrieval framework is built on top of the RBI-regulated AA system "
        "(coordinated by Sahamati). When a client grants consent, the portal automatically requests financial information payloads in real time. "
        "The AA system handles end-to-end data encryption, ensuring the data is secure and cannot be accessed by unauthorized third parties.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>AI Advice Factory Architecture:</b> The intelligence layer is powered by a multi-agent AI system: "
        "(1) a <i>Parsing Agent</i> (converts AA JSON payloads into structured balance-sheet nodes); (2) a <i>Suitability Agent</i> "
        "(compares portfolio assets to the client's registered SEBI risk profile); and (3) an <i>Optimization Agent</i> "
        "(runs Monte Carlo simulations to detect tax-loss harvesting or allocation drifts). The AI stack is deployed on "
        "Axis private clouds to maintain absolute data privacy.",
        bullet_style
    ))
    
    story.append(Spacer(1, 5))
    story.append(Paragraph("D. Regulatory & Compliance Feasibility", h2_style))
    story.append(Paragraph(
        "Operating a wealth advisory business in India requires strict adherence to SEBI and RBI regulations. "
        "WealthOS treats compliance as a core design principle rather than a retrospective check.",
        body_style
    ))
    story.append(Paragraph(
        "• <b>SEBI Investment Advisers Regulations:</b> All portfolio advice generated by the AI Advice Factory must be approved "
        "by a licensed Portfolio Architect inside the advisory pod before it is shared with the client. This ensures that the bank "
        "remains compliant with SEBI regulations, preserving the human accountability loop.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>RBI Consent Architecture:</b> The portal manages client consent under a strictly revocable and purpose-bound structure. "
        "Clients can view exactly what data is being shared (e.g. mutual fund statement via AA), for what purpose (e.g. portfolio drift check), "
        "and for what duration (e.g. 1 year). Clients can revoke consent instantly with a single tap in the app.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>SPARSH Immutable Audit Log:</b> To protect the bank against future compliance audits, every recommendation, "
        "suitability pass/fail result, and client consent signature generates a unique **SHA-256 compliance hash**. "
        "This hash is stored on an internal, immutable ledger database, providing an unalterable audit trail for regulators.",
        bullet_style
    ))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("F. Tier-2/3 Geographic Expansion & Acquisition Strategy", h2_style))
    story.append(Paragraph(
        "Axis Bank cannot profitably place dedicated Burgundy Private wealth offices in every Tier-2/3 city, "
        "yet over 50% of India's new wealth is emerging from these regional clusters. WealthOS solves this through a hybrid Hub-and-Spoke model:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>The Hub (Centralized Experts):</b> Centralized expert Advisory Pods in Tier-1 cities (Mumbai, Ahmedabad, Delhi, Bangalore) "
        "handle quantitative portfolio modeling, trust drafting, and credit underwriting virtually.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>The Spoke (Local Branches):</b> We leverage Axis Bank's 5,500+ local retail branches. The local branch manager "
        "or SME relationship manager acts as the 'spoke liaison' who physically meets local entrepreneurs, builds trust, and handles local logistics.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Data-Native Acquisition Rails:</b> By using the Account Aggregator (AA) framework, regional business owners "
        "(who are historically protective of financial privacy) can link their multi-bank holdings digitally in seconds. "
        "We also establish automated referral partnerships with regional Chartered Accountants (CAs) and corporate credit channels, "
        "identifying clients <i>before</i> they undergo promoter liquidity events.",
        bullet_style
    ))
    
    story.append(PageBreak())
    story.append(Paragraph("E. Implementation Risks & Mitigations", h2_style))
    
    # Risk Table
    risk_data = [
        [Paragraph("<b>Risk Area</b>", table_header_style), 
         Paragraph("<b>Description</b>", table_header_style), 
         Paragraph("<b>Mitigation Strategy</b>", table_header_style)],
        
        [Paragraph("Technology Over-Reliance", table_cell_bold_style), 
         Paragraph("Advisors may blindly trust AI-generated recommendations, leading to unsuitable client advice.", table_cell_style), 
         Paragraph("Mandate human sign-off: Portfolio Architects must approve and log all AI recommendations before client presentation.", table_cell_style)],
        
        [Paragraph("Data Security Breach", table_cell_bold_style), 
         Paragraph("Ingesting multi-account financial details could attract cyber-threats.", table_cell_style), 
         Paragraph("Enforce zero-knowledge databases, local cloud hosting, and strict API access controls.", table_cell_style)],
         
        [Paragraph("Cross-Entity Friction", table_cell_bold_style), 
         Paragraph("Group entities (Bank, Securities, AMC) may compete for fee credits.", table_cell_style), 
         Paragraph("Create a unified Group Scorecard, sharing commission pool weightings equally across participating entities.", table_cell_style)]
    ]
    
    r_table = Table(risk_data, colWidths=[110, 180, 214])
    r_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_tint]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
    ]))
    story.append(r_table)
    
    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)

if __name__ == "__main__":
    create_strategy_guide_pdf("/Users/ketanparikh/Desktop/Axis/Axis_WealthOS_2035_Pitch_Strategy_Guide.pdf")
    print("PDF Generation complete: /Users/ketanparikh/Desktop/Axis/Axis_WealthOS_2035_Pitch_Strategy_Guide.pdf")
