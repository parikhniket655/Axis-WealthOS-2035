import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

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
        self.drawString(54, 755, "AXIS BANK TRANSFORMATION COUNCIL | MOVES 2026")
        
        # Header thin rule
        self.setLineWidth(0.5)
        self.setStrokeColor(colors.HexColor("#D3D3D3"))
        self.line(54, 750, 558, 750)
        
        # Footer thin rule
        self.line(54, 50, 558, 50)
        
        # Footer text
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#727272"))
        self.drawString(54, 38, "CONFIDENTIAL | BOARD-LEVEL STRATEGY BRIEF")
        
        # Page numbers
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 38, page_text)
        self.restoreState()

def create_strategy_pdf(filename):
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
        fontSize=32,
        leading=38,
        textColor=primary_color,
        spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=14,
        leading=18,
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
        fontSize=18,
        leading=22,
        textColor=primary_color,
        spaceBefore=18,
        spaceAfter=10,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=secondary_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=text_color,
        spaceAfter=8
    )

    bullet_style = ParagraphStyle(
        'BulletDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=text_color,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=5
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=text_color
    )
    
    table_cell_bold_style = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=text_color
    )

    story = []

    # ------------------ COVER PAGE ------------------
    story.append(Spacer(1, 100))
    story.append(Paragraph("AXIS WEALTHOS 2035", title_style))
    story.append(Paragraph("From Relationship-Led Wealth Servicing to an AI-Native Household Wealth Operating System", subtitle_style))
    
    # Decorative line
    d_table = Table([[""]], colWidths=[504])
    d_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 4, primary_color),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(d_table)
    story.append(Spacer(1, 150))
    
    # Metadata Block
    story.append(Paragraph("<b>SUBMISSION BY:</b> Axis Bank Transformation Council", metadata_style))
    story.append(Paragraph("<b>COMPETITION:</b> MOVES 2026 — Organization of the Future: Design for 2035", metadata_style))
    story.append(Paragraph("<b>DATE:</b> July 2026", metadata_style))
    story.append(Paragraph("<b>STATUS:</b> CONFIDENTIAL / BOARD-LEVEL BRIEF", metadata_style))
    story.append(PageBreak())

    # ------------------ SECTION 1: EXECUTIVE SUMMARY ------------------
    story.append(Paragraph("1. Executive Summary", h1_style))
    story.append(Paragraph(
        "Axis Bank has established itself as India's third-largest wealth management franchise, backed by rapid growth in the "
        "affluent segment and the integration of Citibank's premium consumer assets. However, as India's affluent class expands and "
        "wealth creation spreads outside metros, the traditional relationship manager (RM)-led model faces scalability, consistency, "
        "and personalization limits. Relentlessly expanding headcount is economically unsustainable and prone to service fragmentation.",
        body_style
    ))
    story.append(Paragraph(
        "This strategy document outlines <b>Axis WealthOS 2035</b>: a bold, enterprise-level transformational bet to shift wealth management "
        "from individual product distribution into a consent-driven, AI-native household wealth operating system. By combining continuous "
        "data orchestration (via India's Account Aggregator framework), automated multi-agent intelligence (the AI Advice Factory), and "
        "collaborative human advisory pods, Axis Bank can unlock immense cross-sell opportunities across its multi-entity group ecosystem "
        "('One Axis'). This model is designed to multiply advisor productivity by 60%, slash the cost-to-serve by 85%, and secure "
        "unmatched wallet-share stickiness by 2035.",
        body_style
    ))
    
    # Callout Box: The Core Thesis
    summary_box_data = [[
        Paragraph(
            "<b>THE CORE THESIS</b><br/>"
            "Axis Bank should stop managing isolated 'accounts' and begin orchestrating the entire financial life of affluent "
            "households. Axis WealthOS 2035 creates a live 'Wealth Twin' for every client, continuously analyzing asset-liability "
            "mismatches, tax efficiencies, succession events, and credit needs. The human RM remains the anchor of trust, while AI "
            "handles the analytic and compliance heavy lifting.",
            body_style
        )
    ]]
    summary_box_table = Table(summary_box_data, colWidths=[504])
    summary_box_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_tint),
        ('BOX', (0,0), (-1,-1), 1, border_color),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(Spacer(1, 10))
    story.append(summary_box_table)
    story.append(Spacer(1, 15))

    # ------------------ SECTION 2: CURRENT STATE ANALYSIS ------------------
    story.append(Paragraph("2. Current-State Baseline & Strategic Assets", h1_style))
    story.append(Paragraph(
        "To build a credible transformation case, the proposal must anchor on Axis Bank's actual financial and operational baseline as of Q1 FY27. "
        "Axis is uniquely positioned to execute this transformation due to several proprietary assets:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Scaled Wealth Franchise:</b> As of March 31, 2026 (Q4 FY26), Axis Bank's total Burgundy wealth AUM stood at <b>₹6.78 trillion</b>. "
        "The ultra-high-net-worth (UHNWI) segment, Burgundy Private, stood at <b>₹2.40 trillion AUM</b>, serving over "
        "<b>16,453 families</b>. This provides a massive, high-value deposit and fee-generating engine.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>The Citibank Integration:</b> The acquisition of Citibank's consumer business added approximately <b>₹1.11 trillion in wealth AUM</b>, "
        "significantly accelerating Axis's premiumization strategy and providing a highly disciplined affluent client base and premium talent pool.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Industrialized Virtual Servicing:</b> Through the Axis Virtual Centre, the bank deploys <b>1,700 virtual RMs</b>, connecting with "
        "<b>4.2 million customers monthly</b>. This proves Axis already possess the digital service infrastructure needed to scale automated "
        "advisory preparation.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>The 'One Axis' Ecosystem:</b> Unlike standalone wealth boutiques, Axis Bank can draw from its comprehensive family of legal entities "
        "including Axis Securities (broking), Axis AMC (mutual funds/PMS/AIF), Axis Capital (investment banking), Axis Finance (lending), and "
        "Axis Trustee Services (estate planning). Currently, these entities operate in parallel; WealthOS will integrate them around the client.",
        bullet_style
    ))
    story.append(Spacer(1, 15))

    # ------------------ SECTION 3: MARKET & TECHNOLOGY TAILWINDS ------------------
    story.append(Paragraph("3. Market Dynamics & Technological Tailwinds", h1_style))
    story.append(Paragraph(
        "Why must Axis Bank make this transition now? A convergence of macroeconomic, regulatory, and technological shifts makes "
        "the legacy model obsolete by 2035:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Demographic Wealth Expansion:</b> Goldman Sachs estimates that India's affluent class (income > $10,000) will grow to 100 million "
        "by 2027. Over 50% of incremental wealth creators will reside in Tier-2/3/4 cities. A human-only RM model cannot scale to these "
        "regions profitably due to high travel, talent acquisition, and physical branch costs.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>The Account Aggregator (AA) Revolution:</b> The RBI-governed Account Aggregator framework (coordinated by Sahamati) provides the "
        "regulatory and technical rails for real-time, consent-driven, secure financial data sharing. This enables Axis to view a client's "
        "entire balance sheet (including holdings at competing banks and brokerages) continuously and legally.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Hybrid Advisory Imperative:</b> McKinsey research indicates that in Asian wealth markets, the winning firms will not be "
        "pure-play robo-advisors or pure-play traditional RMs. Instead, hybrid models—where AI automates portfolio diagnostics and risk suitability "
        "while humans deliver empathy and relationship depth—will capture the majority of net new flows.",
        bullet_style
    ))
    story.append(PageBreak())

    # ------------------ SECTION 4: THE AXIS WEALTHOS 2035 ARCHITECTURE ------------------
    story.append(Paragraph("4. The WealthOS Target Operating Model", h1_style))
    story.append(Paragraph(
        "The proposed future-state operating model shifts the unit of value from <i>individual accounts</i> to <i>household wealth orchestration</i>.",
        body_style
    ))
    
    story.append(Paragraph("A. The Wealth Twin (Core Data Layer)", h2_style))
    story.append(Paragraph(
        "Instead of static PDF statements gathered during sporadic reviews, Axis builds a dynamic <b>Wealth Twin</b> for every household. "
        "This is an encrypted, real-time financial graph integrating internal bank deposits, credit lines, and card spends with external "
        "consented holdings (mutual funds, equities, insurance, liabilities, property registries, and business cash flows) accessed via AA rails. "
        "It maps the full balance sheet of the family, including cross-generational links.",
        body_style
    ))

    story.append(Paragraph("B. The AI Advice Factory (Intelligence Layer)", h2_style))
    story.append(Paragraph(
        "An autonomous backend engine running specialized analytical agents. Rather than relying on RM memory, the engine continuously checks "
        "the Wealth Twin against rule-based models and machine learning heuristics. It automatically flags portfolio drift, tax-harvesting opportunities, "
        "concentrated stock risk, asset liability mismatch (e.g., short-term business debt vs. long-term illiquid assets), and legacy planning triggers.",
        body_style
    ))

    story.append(Paragraph("C. The Pod-Based Coverage Model (Talent & Delivery Layer)", h2_style))
    story.append(Paragraph(
        "The bank restructures relationship management away from isolated RMs. Instead, clients are served by an <b>Advisory Pod</b> consisting of: "
        "a Lead Relationship Partner (owning relationship trust and goal discovery), a Portfolio Architect (structuring asset allocation), and "
        "a Credit/Liquidity Specialist (managing leverage, business lending, and working capital). The pod is equipped with the AI Advice Factory's "
        "briefing dossiers, allowing them to prepare for meetings in minutes rather than hours.",
        body_style
    ))

    story.append(Paragraph("D. One Axis Orchestration & Group Integration", h2_style))
    story.append(Paragraph(
        "WealthOS functions as a group-wide client router. When a business-owner client approaches a liquidity event (such as an IPO or promoter stake sale), "
        "the engine coordinates services across Axis Capital (for transaction handling), Axis Finance (for bridge credit), Axis Private (for post-sale wealth management), "
        "and Axis Trustee Services (for trust establishment) seamlessly. This ensures 'One Axis' is a reality, not just a group org chart.",
        body_style
    ))

    story.append(Paragraph("E. Trust & Suitability Guardrails (Governance Layer)", h2_style))
    story.append(Paragraph(
        "To ensure compliance with SEBI and RBI guidelines, every advisory action must pass through automated risk suitability, concentration, "
        "and conflict-of-interest checks. No trade suggestion reaches the RM's dashboard without a clear, auditable explanation log. This protects "
        "Axis from mis-selling risks and model biases.",
        body_style
    ))
    story.append(Paragraph("F. Tier-2/3 Acquisition & Distribution Engine (The Hub-and-Spoke Model)", h2_style))
    story.append(Paragraph(
        "Axis Bank cannot profitably place dedicated Burgundy Private wealth offices in every Tier-2/3 city (like Nashik, Indore, Nagpur, or Guntur), "
        "yet over 50% of India's new wealth is emerging from these regional clusters. WealthOS solves this through a hybrid Hub-and-Spoke model:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Centralized Hubs (The Experts):</b> Centralized expert Advisory Pods in Tier-1 cities (Mumbai, Ahmedabad, Delhi, Bangalore) "
        "handle quantitative portfolio modeling, trust drafting, and credit underwriting virtually.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Localized Spokes (The Human Connection):</b> We leverage Axis Bank's 5,500+ local retail branches. The local branch manager "
        "or SME relationship manager acts as the 'spoke liaison' who physically meets local entrepreneurs, builds trust, and handles local logistics.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Data-Native Acquisition Rails:</b> By using the Account Aggregator (AA) framework, regional business owners "
        "can link their multi-bank holdings digitally in seconds. We also establish automated referral partnerships with regional "
        "Chartered Accountants (CAs) and corporate credit channels, identifying clients <i>before</i> they undergo promoter liquidity events.",
        bullet_style
    ))
    story.append(Spacer(1, 15))

    # ------------------ SECTION 5: FEASIBILITY ANALYSIS ------------------
    story.append(Paragraph("5. Feasibility Analysis", h1_style))
    story.append(Paragraph(
        "A rigorous feasibility assessment ensures the board understands that Axis WealthOS is realistic, deployable, and highly defensible.",
        body_style
    ))
    
    # Feasibility Table
    feasibility_data = [
        [Paragraph("<b>Feasibility Pillar</b>", table_header_style), 
         Paragraph("<b>Score</b>", table_header_style), 
         Paragraph("<b>Strategic Rationale & Enablement</b>", table_header_style)],
        
        [Paragraph("Strategic Fit", table_cell_bold_style), 
         Paragraph("9 / 10", table_cell_bold_style), 
         Paragraph("Aligns perfectly with Axis's existing premiumization strategy, Citi consumer acquisition synergies, and 'One Axis' cross-entity focus.", table_cell_style)],
        
        [Paragraph("Market Demand", table_cell_bold_style), 
         Paragraph("9 / 10", table_cell_bold_style), 
         Paragraph("Supported by India's rapidly expanding mass-affluent segment in Tier-2/3 cities, requiring scalable wealth advisory solutions.", table_cell_style)],
        
        [Paragraph("Tech & Data", table_cell_bold_style), 
         Paragraph("8 / 10", table_cell_bold_style), 
         Paragraph("Leverages India's Account Aggregator (AA) APIs and Axis's virtual RM platform. Data unification across entities is the key engineering task.", table_cell_style)],
        
        [Paragraph("Operational", table_cell_bold_style), 
         Paragraph("7 / 10", table_cell_bold_style), 
         Paragraph("Requires transitioning RMs into collaborative 'Pods' and updating internal cross-sell credit systems to prevent channel friction.", table_cell_style)],
         
        [Paragraph("Regulatory", table_cell_bold_style), 
         Paragraph("8 / 10", table_cell_bold_style), 
         Paragraph("Complies with SEBI Investment Adviser rules and RBI AA regulations. Proactive compliance is treated as a core design principle.", table_cell_style)]
    ]
    
    f_table = Table(feasibility_data, colWidths=[110, 54, 340])
    f_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_tint]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
    ]))
    story.append(f_table)
    story.append(PageBreak())

    # ------------------ SECTION 6: FINANCIAL & BUSINESS IMPACT ------------------
    story.append(Paragraph("6. Financial & Business Impact Model", h1_style))
    story.append(Paragraph(
        "Below is an illustrative board-level business case projecting growth, productivity, and cost-efficiency gains "
        "enabled by the transition to Axis WealthOS 2035. (Note: Baseline figures are sourced from Q1 FY27 disclosures; targets are strategic team estimates).",
        body_style
    ))
    
    # Impact Table
    impact_data = [
        [Paragraph("<b>Performance Indicator</b>", table_header_style), 
         Paragraph("<b>Q1 FY27 Baseline</b>", table_header_style), 
         Paragraph("<b>2030 Target</b>", table_header_style), 
         Paragraph("<b>2035 Ambition</b>", table_header_style)],
        
        [Paragraph("Total Burgundy AUM", table_cell_bold_style), 
         Paragraph("₹6.78 Lakh Cr", table_cell_style), 
         Paragraph("₹11.50 Lakh Cr", table_cell_style), 
         Paragraph("₹16.50 Lakh Cr", table_cell_style)],
         
        [Paragraph("Burgundy Private AUM", table_cell_bold_style), 
         Paragraph("₹2.40 Lakh Cr", table_cell_style), 
         Paragraph("₹4.50 Lakh Cr", table_cell_style), 
         Paragraph("₹7.00 Lakh Cr", table_cell_style)],
         
        [Paragraph("Burgundy Private Families", table_cell_bold_style), 
         Paragraph("16,453", table_cell_style), 
         Paragraph("30,000+", table_cell_style), 
         Paragraph("55,000+", table_cell_style)],
         
        [Paragraph("RM Productivity multiplier", table_cell_bold_style), 
         Paragraph("1.0x (Baseline)", table_cell_style), 
         Paragraph("1.3x (+30% capacity)", table_cell_style), 
         Paragraph("1.6x (+60% capacity)", table_cell_style)],
         
        [Paragraph("Affluent Household Wallet Share", table_cell_bold_style), 
         Paragraph("Estimated 18%", table_cell_style), 
         Paragraph("25% (+700 bps)", table_cell_style), 
         Paragraph("35% (+1700 bps)", table_cell_style)],
         
        [Paragraph("Cost-to-Serve per Client", table_cell_bold_style), 
         Paragraph("High (Human-Led)", table_cell_style), 
         Paragraph("-35% (AI-Assisted)", table_cell_style), 
         Paragraph("-85% (AI-Automated prep)", table_cell_style)],
         
        [Paragraph("Advisory Action Turnaround", table_cell_bold_style), 
         Paragraph("T + 2 days", table_cell_style), 
         Paragraph("T + 4 hours", table_cell_style), 
         Paragraph("Real-Time (< 5 mins)", table_cell_style)]
    ]
    
    i_table = Table(impact_data, colWidths=[180, 108, 108, 108])
    i_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_tint]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
    ]))
    story.append(i_table)
    story.append(Spacer(1, 15))

    # ------------------ SECTION 7: IMPLEMENTATION ROADMAP ------------------
    story.append(Paragraph("7. Implementation Roadmap & Rollout Strategy", h1_style))
    story.append(Paragraph(
        "To mitigate execution risks and distribute capital investment, the transformation is structured into three logical horizons:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Phase 1: Foundation & HNI Pilot (Years 1–2):</b> Focus on Burgundy Private and UHNW families. Build the core 'Wealth Twin' data layer, "
        "integrate internal bank data with Account Aggregator APIs, and deploy the AI Advice Factory to a pilot group of 500 RMs. Target: prove "
        "advisory productivity lift and client satisfaction.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Phase 2: Affluent Scale-Up & Family Banking (Years 3–5):</b> Expand the platform to Burgundy affluent segments. Launch Family Banking 2.0, "
        "allowing families to consolidate balance sheets. Implement basic pod-based coverage models. Integrate GST and invoice-based business "
        "cash flows for entrepreneur wealth clients.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Phase 3: One Axis Integration & Ecosystem Scaling (Years 6–10):</b> Establish full, seamless routing to Axis Securities, Capital, "
        "AMC, Finance, and Trustee. Open API access to external ecosystem partners (e.g., cross-border tax firms, alternative investment managers). "
        "ACHIEVE: 100% data-native, continuous household advisory across India.",
        bullet_style
    ))
    story.append(Spacer(1, 15))

    # ------------------ SECTION 8: RISK MANAGEMENT & MITIGATION ------------------
    story.append(Paragraph("8. Risk Management Matrix", h1_style))
    
    risk_data = [
        [Paragraph("<b>Identified Risk Factor</b>", table_header_style), 
         Paragraph("<b>Mitigation Strategy</b>", table_header_style)],
        
        [Paragraph("<b>Advisor Resistance & Fear of Replacement:</b> RMs may resist AI-generated suggestions, fearing their role is minimized.", table_cell_bold_style), 
         Paragraph("Position AI as a co-pilot that automates manual research and compliance tasks, freeing RMs to spend 100% of their time on trust-building, client relationships, and estate negotiations.", table_cell_style)],
        
        [Paragraph("<b>Data Privacy & Security Concerns:</b> Ingesting multi-account financial details via AA may trigger client privacy anxiety.", table_cell_bold_style), 
         Paragraph("Strictly enforce granular, client-revocable consent. Implement zero-knowledge proof databases and clear client-facing dashboards displaying what data is accessed and for what purpose.", table_cell_style)],
        
        [Paragraph("<b>Model Bias & Regulatory Violations:</b> AI might output unsuitable investment advice or show biases.", table_cell_bold_style), 
         Paragraph("Implement rigid regulatory guardrails at the output layer. Mandate that every AI proposal is approved by a licensed Portfolio Architect before being shared with the client.", table_cell_style)],
         
        [Paragraph("<b>One Axis Coordination Friction:</b> Conflict over revenue sharing and client ownership across different Axis group entities.", table_cell_bold_style), 
         Paragraph("Redesign corporate incentive plans. Implement a unified 'Group Wallet Share' scorecard, sharing commissions and credit equally across bank, brokerage, and AMC entities.", table_cell_style)]
    ]
    
    r_table = Table(risk_data, colWidths=[200, 304])
    r_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_tint]),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
    ]))
    story.append(r_table)
    story.append(PageBreak())

    # ------------------ SECTION 9: PITCH DECK STORYBOARD ------------------
    story.append(Paragraph("9. The 2-Slide Pitch Deck Blueprint", h1_style))
    story.append(Paragraph(
        "A layout plan to structure the maximum 2-slide presentation (excluding title) required by the judges. The strategy prioritizes "
        "executive-level visual simplicity, clear quantitative anchors, and structural contrast.",
        body_style
    ))
    
    story.append(Paragraph("Slide 1: The Big Bet (Strategic Rationale & Vision)", h2_style))
    story.append(Paragraph(
        "<b>Slide Header:</b> <i>Axis WealthOS 2035: Reinventing Wealth Management into an AI-Native Household Wealth Operating System</i><br/>"
        "<b>Visual Layout:</b> Three vertical columns establishing contrast and logic:<br/>"
        "• <b>Column 1: The Structural Challenge (Why Now?):</b> Highlight that India's affluent class is expanding outside metros (Goldman Sachs: 100M by 2027), "
        "making traditional high-touch RM-only models too expensive to scale. Relentless RM headcount expansion is not viable.<br/>"
        "• <b>Column 2: The Core Bet (The Transformation):</b> Introduce WealthOS. Outline the shift from managing accounts and pushing products to "
        "real-time household wealth orchestration using 'Wealth Twins' and the AI Advice Factory.<br/>"
        "• <b>Column 3: Why Axis Wins (Strategic Anchors):</b> Quantify Axis's scale: ₹6.78 Lakh Cr Burgundy AUM, ₹2.40 Lakh Cr Burgundy Private AUM, "
        "16,453 Burgundy Private families, and Citibank integration synergies. Anchor this with a large graphic showing Axis's leadership position.<br/>"
        "<b>Speaker Script Highlight:</b> <i>'Burgundy is already a market leader. But to capture the next wave of wealth in India's Tier-2 and Tier-3 hubs, "
        "we must build a model that multiplies advisor capability rather than advisor headcount. Axis WealthOS is that future.'</i>",
        body_style
    ))
    
    story.append(Paragraph("Slide 2: How It Works & Strategic Impact", h2_style))
    story.append(Paragraph(
        "<b>Slide Header:</b> <i>Advisory Pods, Multi-Entity Integration, and the Business Case</i><br/>"
        "<b>Visual Layout:</b> Split layout — Left side is a flowchart; Right side is the quantitative business case table:<br/>"
        "• <b>Left: The Operating Model Flowchart:</b> Map the flow: client consented external data (via AA) + bank internal data $\rightarrow$ "
        "AI Advice Factory (continuous event detection, risk suitability auditing) $\rightarrow$ Advisory Pod (Lead RM, Portfolio Architect, Credit Specialist) $\rightarrow$ "
        "integrated execution across the 'One Axis' group (Securities, AMC, Finance, Trustee).<br/>"
        "• <b>Right: Financial & Feasibility Scorecard:</b> Detail target metrics: +60% RM productivity, -85% Cost-to-Serve, ₹16.5 Lakh Cr Burgundy AUM by 2035. "
        "Include a small, high-impact box detailing 4 key risk mitigations (consent management, explainable AI, human oversight, and incentive alignment).<br/>"
        "<b>Speaker Script Highlight:</b> <i>'WealthOS is not an app or a chatbot. It is a fundamental operational rewiring. By moving to collaborative "
        "advisory pods and automating proposal preparation via AI, we turn our group's multi-entity capabilities into a single, cohesive client experience.'</i>",
        body_style
    ))
    story.append(Spacer(1, 15))

    # ------------------ SECTION 10: Q&A DEFENSE GUIDE ------------------
    story.append(Paragraph("10. Q&A Defense Guide: Key Objections & Strategic Responses", h1_style))
    story.append(Paragraph(
        "Pre-empting the judges' critical questions during the defense phase:",
        body_style
    ))
    
    story.append(Paragraph("Q1: 'How is this an operational change rather than a new technology tool?'", h2_style))
    story.append(Paragraph(
        "<b>Strategic Response:</b> <i>'The operational change lies in three structural shifts: First, the client service unit changes from a single RM to a collaborative advisory pod (Lead Partner, Portfolio Architect, Credit Specialist). Second, the workflow shifts from reactive periodic reviews to continuous automated preparation. Third, the corporate incentive scorecard shifts from short-term product conversions to long-term household share of wallet and risk-adjusted suitability. The technology is simply the enabler; the organization is what we are redesigning.'</i>",
        body_style
    ))

    story.append(Paragraph("Q2: 'Why wouldn't competitors like HDFC or ICICI copy this immediately?'", h2_style))
    story.append(Paragraph(
        "<b>Strategic Response:</b> <i>'While competitors have access to the same digital public infrastructure, Axis possesses a unique structural advantage: our comprehensive, closely integrated multi-entity group (One Axis) coupled with the premium customer base and servicing standards acquired from Citibank. Standalone players lack our scale, and other large banks struggle with siloed entity coordination. WealthOS leverages this cross-entity strength from day one, creating a higher barrier to imitation.'</i>",
        body_style
    ))

    story.append(Paragraph("Q3: 'How do you address the risk of AI model hallucination or unsuitable advice?'", h2_style))
    story.append(Paragraph(
        "<b>Strategic Response:</b> <i>'We enforce a strict 'Human-in-the-Loop' architecture. The AI Advice Factory does not interface directly with the client. It acts as an advisor copilot, generating draft proposals and risk analyses. A licensed Portfolio Architect inside the advisory pod must review, validate, and sign off on every proposal before the Lead RM presents it. Additionally, a hard suitability filter blocks any recommendation that violates regulatory parameters.'</i>",
        body_style
    ))

    story.append(Paragraph("Q4: 'Is the Account Aggregator ecosystem mature enough to support real-time wealth twins?'", h2_style))
    story.append(Paragraph(
        "<b>Strategic Response:</b> <i>'The AA ecosystem is scaling rapidly, with all major public and private banks, mutual fund registries, and insurers already live as financial information providers (FIPs). However, our model does not depend on 100% external coverage from day one. Phase 1 operates primarily on internal Axis assets and liabilities (which account for Burgundy's large scale), alongside early AA adopters. As the ecosystem matures over the next decade, our data coverage will naturally expand.'</i>",
        body_style
    ))

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)

if __name__ == "__main__":
    create_strategy_pdf("/Users/ketanparikh/Desktop/Axis/Axis_WealthOS_2035_Strategy_Pack.pdf")
    print("PDF Generation complete: /Users/ketanparikh/Desktop/Axis/Axis_WealthOS_2035_Strategy_Pack.pdf")
