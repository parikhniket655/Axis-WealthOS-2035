const pptxgen = require('pptxgenjs');

const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.3" x 7.5"

// ── PALETTE ──────────────────────────────────────────────────────────────────
const MAROON   = '6B1D2E';  // Axis Bank deep burgundy
const MAROON2  = '8B2035';  // slightly lighter
const GOLD     = 'C9A84C';  // accent gold
const OFFWHITE = 'FAF6F1';  // warm background
const WHITE    = 'FFFFFF';
const DARK     = '1A1A2E';
const LIGHTGRAY= 'E8E0D5';
const TEXTGRAY = '5A4A42';
const MINT     = '2E7D5E';  // green for positive metrics
const STEEL    = '34495E';

// ─────────────────────────────────────────────────────────────────────────────
// SLIDE 0 — TITLE
// ─────────────────────────────────────────────────────────────────────────────
const s0 = pres.addSlide();

// Full dark background
s0.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 13.3, h: 7.5, fill: { color: MAROON } });

// Decorative gold diagonal band
s0.addShape(pres.ShapeType.rect, { x: 8.8, y: 0, w: 0.06, h: 7.5, fill: { color: GOLD }, line: { type: 'none' } });
s0.addShape(pres.ShapeType.rect, { x: 9.1, y: 0, w: 0.02, h: 7.5, fill: { color: GOLD }, transparency: 50, line: { type: 'none' } });

// Right panel lighter bg
s0.addShape(pres.ShapeType.rect, { x: 8.86, y: 0, w: 4.44, h: 7.5, fill: { color: '500F1E' }, line: { type: 'none' } });

// AXIS BANK label top left
s0.addText('AXIS BANK', {
  x: 0.5, y: 0.35, w: 4, h: 0.35,
  fontSize: 11, bold: true, color: GOLD, fontFace: 'Calibri', charSpacing: 4
});

// Main title
s0.addText('AXIS WEALTHOS 2035', {
  x: 0.5, y: 1.4, w: 7.9, h: 1.1,
  fontSize: 46, bold: true, color: WHITE, fontFace: 'Cambria'
});

// Subtitle
s0.addText('From Relationship-Led Wealth Servicing\nto an AI-Native Household Wealth Operating System', {
  x: 0.5, y: 2.65, w: 7.9, h: 1.0,
  fontSize: 17, bold: false, color: LIGHTGRAY, fontFace: 'Calibri'
});

// Gold divider
s0.addShape(pres.ShapeType.rect, { x: 0.5, y: 3.75, w: 2.5, h: 0.05, fill: { color: GOLD }, line: { type: 'none' } });

// Competition / date
s0.addText('MOVES 2026  ·  Organization of the Future: Design for 2035', {
  x: 0.5, y: 3.9, w: 7.9, h: 0.3,
  fontSize: 12, color: LIGHTGRAY, fontFace: 'Calibri', italic: true
});

// Team label right panel
s0.addText('SUBMITTED BY', {
  x: 9.2, y: 1.6, w: 3.7, h: 0.3,
  fontSize: 10, bold: true, color: GOLD, fontFace: 'Calibri', charSpacing: 3, align: 'center'
});
s0.addText('Team CashCows', {
  x: 9.2, y: 2.0, w: 3.7, h: 0.5,
  fontSize: 22, bold: true, color: WHITE, fontFace: 'Cambria', align: 'center'
});

// Three KPIs on right panel
const kpis = [
  { val: '₹7.54T', lbl: 'Burgundy AUM\nBaseline' },
  { val: '17,400+', lbl: 'Burgundy Private\nFamilies' },
  { val: '1,700', lbl: 'Virtual RMs\nDeployed' },
];
kpis.forEach((k, i) => {
  const y = 3.1 + i * 1.3;
  s0.addShape(pres.ShapeType.rect, { x: 9.3, y, w: 3.5, h: 1.1, fill: { color: MAROON }, line: { color: GOLD, pt: 1 } });
  s0.addText(k.val, { x: 9.3, y: y + 0.08, w: 3.5, h: 0.5, fontSize: 22, bold: true, color: GOLD, fontFace: 'Cambria', align: 'center' });
  s0.addText(k.lbl, { x: 9.3, y: y + 0.58, w: 3.5, h: 0.45, fontSize: 10, color: LIGHTGRAY, fontFace: 'Calibri', align: 'center' });
});

// Confidential footer
s0.addText('CONFIDENTIAL  ·  BOARD-LEVEL STRATEGY BRIEF  ·  JULY 2026', {
  x: 0.5, y: 7.1, w: 8.2, h: 0.25,
  fontSize: 9, color: '9E8C84', fontFace: 'Calibri', charSpacing: 1
});


// ─────────────────────────────────────────────────────────────────────────────
// SLIDE 1 — THE BIG BET
// ─────────────────────────────────────────────────────────────────────────────
const s1 = pres.addSlide();
s1.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 13.3, h: 7.5, fill: { color: OFFWHITE }, line: { type: 'none' } });

// Top bar
s1.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 13.3, h: 0.7, fill: { color: MAROON }, line: { type: 'none' } });
s1.addText('SLIDE 1  ·  THE BIG BET', { x: 0.4, y: 0.1, w: 6, h: 0.45, fontSize: 10, bold: true, color: GOLD, fontFace: 'Calibri', charSpacing: 2 });
s1.addText('AXIS WEALTHOS 2035', { x: 0.4, y: 0.1, w: 12.5, h: 0.45, fontSize: 10, color: LIGHTGRAY, fontFace: 'Calibri', align: 'right' });

// Main headline
s1.addText('Reinventing Wealth Management into an AI-Native Household Wealth Operating System', {
  x: 0.4, y: 0.82, w: 12.5, h: 0.75,
  fontSize: 21, bold: true, color: MAROON, fontFace: 'Cambria'
});

// Gold underline
s1.addShape(pres.ShapeType.rect, { x: 0.4, y: 1.58, w: 12.5, h: 0.04, fill: { color: GOLD }, line: { type: 'none' } });

// ── THREE COLUMNS ─────────────────────────────────────────────────────────────
const colW = 3.9;
const colY = 1.72;
const colH = 5.35;
const cols = [
  { x: 0.35, color: MAROON,  label: '01', head: 'THE STRUCTURAL\nCHALLENGE', sub: 'Why Now?' },
  { x: 4.55, color: STEEL,   label: '02', head: 'THE CORE BET',             sub: 'The Transformation' },
  { x: 8.75, color: MINT,    label: '03', head: 'WHY AXIS WINS',            sub: 'Strategic Anchors' },
];
cols.forEach(c => {
  // Column card background
  s1.addShape(pres.ShapeType.rect, { x: c.x, y: colY, w: colW, h: colH, fill: { color: WHITE }, line: { color: LIGHTGRAY, pt: 1 } });
  // Colored header band
  s1.addShape(pres.ShapeType.rect, { x: c.x, y: colY, w: colW, h: 1.05, fill: { color: c.color }, line: { type: 'none' } });
  // Number
  s1.addText(c.label, { x: c.x + 0.15, y: colY + 0.08, w: 0.6, h: 0.4, fontSize: 22, bold: true, color: WHITE, fontFace: 'Cambria', transparency: 30 });
  // Heading
  s1.addText(c.head, { x: c.x + 0.15, y: colY + 0.08, w: colW - 0.25, h: 0.55, fontSize: 13, bold: true, color: WHITE, fontFace: 'Calibri', align: 'right' });
  // Sub
  s1.addText(c.sub, { x: c.x + 0.15, y: colY + 0.65, w: colW - 0.25, h: 0.3, fontSize: 10, color: WHITE, fontFace: 'Calibri', italic: true, align: 'right' });
});

// ── COL 1 CONTENT — Structural Challenge ────────────────────────────────────
const c1x = 0.5;
const c1y = colY + 1.18;

const challenges = [
  {
    icon: '⚡',
    head: 'Scale Impossibility',
    body: 'India\'s affluent class will hit 100M by 2027 (Goldman Sachs). 50%+ of new wealth creators are in Tier 2/3/4 cities. Human-only RM model cannot scale profitably outside metros.',
  },
  {
    icon: '📉',
    head: 'RM Productivity Ceiling',
    body: 'Each RM handles 80-120 clients with manual portfolio reviews. 70% of RM time spent on prep, compliance & paperwork — not client relationships.',
  },
  {
    icon: '🔗',
    head: 'Fragmented Client View',
    body: 'Axis sees only its own AUM. Client\'s full balance sheet — external MFs, insurance, property — is invisible. Product-pushing replaces holistic advisory.',
  },
  {
    icon: '💸',
    head: 'Cost-to-Serve Crisis',
    body: 'High-touch RM model is economically unsustainable at scale. Relentlessly expanding headcount creates service fragmentation, not depth.',
  },
];

challenges.forEach((ch, i) => {
  const y = c1y + i * 1.03;
  s1.addShape(pres.ShapeType.rect, { x: c1x, y, w: colW - 0.3, h: 0.95, fill: { color: 'FDF0F0' }, line: { color: 'E8D0D0', pt: 1 } });
  s1.addText(ch.head, { x: c1x + 0.1, y: y + 0.05, w: colW - 0.45, h: 0.25, fontSize: 10, bold: true, color: MAROON, fontFace: 'Calibri' });
  s1.addText(ch.body, { x: c1x + 0.1, y: y + 0.28, w: colW - 0.45, h: 0.62, fontSize: 8.5, color: TEXTGRAY, fontFace: 'Calibri' });
});

// ── COL 2 CONTENT — The Core Bet ────────────────────────────────────────────
const c2x = 4.7;
const c2y = colY + 1.15;

// WealthOS tagline
s1.addShape(pres.ShapeType.rect, { x: c2x, y: c2y, w: colW - 0.3, h: 0.45, fill: { color: STEEL }, line: { type: 'none' } });
s1.addText('AXIS WEALTHOS: Stop managing accounts. Start orchestrating financial lives.', {
  x: c2x + 0.1, y: c2y + 0.05, w: colW - 0.45, h: 0.36,
  fontSize: 8.5, bold: true, color: WHITE, fontFace: 'Calibri', italic: true
});

const layers = [
  { lbl: 'DATA LAYER', head: 'Wealth Twin', body: 'Encrypted real-time financial graph — internal bank data + external consented holdings via Account Aggregator (AA) APIs. Maps full household balance sheet across generations.' },
  { lbl: 'INTELLIGENCE', head: 'AI Advice Factory', body: 'Autonomous multi-agent backend continuously scanning the Wealth Twin. Flags portfolio drift, tax-harvesting windows, ALM mismatches, concentrated stock risk, and succession triggers — in real time.' },
  { lbl: 'DELIVERY', head: 'Pod-Based Advisory', body: 'Replaces isolated RM model. Each client served by a Lead Relationship Partner + Portfolio Architect + Credit Specialist. Pods operate on AI-generated briefing dossiers — prep in minutes, not hours.' },
  { lbl: 'ECOSYSTEM', head: 'One Axis Orchestration', body: 'WealthOS routes seamlessly to Axis Securities, AMC, Capital, Finance & Trustee. A client liquidity event triggers coordinated action across all entities — not siloed product conversations.' },
];

layers.forEach((l, i) => {
  const y = c2y + 0.55 + i * 1.18;
  s1.addShape(pres.ShapeType.rect, { x: c2x, y, w: colW - 0.3, h: 1.1, fill: { color: 'F0F4F8' }, line: { color: 'C8D8E8', pt: 1 } });
  s1.addShape(pres.ShapeType.rect, { x: c2x, y, w: 0.06, h: 1.1, fill: { color: STEEL }, line: { type: 'none' } });
  s1.addText(l.lbl, { x: c2x + 0.15, y: y + 0.05, w: colW - 0.45, h: 0.2, fontSize: 7.5, bold: true, color: STEEL, fontFace: 'Calibri', charSpacing: 1 });
  s1.addText(l.head, { x: c2x + 0.15, y: y + 0.23, w: colW - 0.45, h: 0.22, fontSize: 11, bold: true, color: DARK, fontFace: 'Cambria' });
  s1.addText(l.body, { x: c2x + 0.15, y: y + 0.44, w: colW - 0.45, h: 0.6, fontSize: 8, color: TEXTGRAY, fontFace: 'Calibri' });
});

// ── COL 3 CONTENT — Why Axis Wins ───────────────────────────────────────────
const c3x = 8.9;
const c3y = colY + 1.15;

// Big stat callout
s1.addShape(pres.ShapeType.rect, { x: c3x, y: c3y, w: colW - 0.3, h: 1.1, fill: { color: MINT }, line: { type: 'none' } });
s1.addText('₹7.54T', { x: c3x, y: c3y + 0.05, w: colW - 0.3, h: 0.55, fontSize: 36, bold: true, color: WHITE, fontFace: 'Cambria', align: 'center' });
s1.addText('Burgundy AUM  ·  20% YoY Growth  ·  Q1 FY27', { x: c3x, y: c3y + 0.65, w: colW - 0.3, h: 0.35, fontSize: 9, color: WHITE, fontFace: 'Calibri', align: 'center' });

const anchors = [
  { head: 'Citibank Integration', body: '₹1.11T wealth AUM added. Premium talent pool + disciplined UHNI base instantly elevates Axis\'s premiumization strategy.' },
  { head: 'Virtual RM Infrastructure', body: '1,700 virtual RMs serving 4.2M clients/month. Proves Axis already has the digital service backbone to scale automated advisory.' },
  { head: 'One Axis Multi-Entity Edge', body: 'Securities + AMC + Capital + Finance + Trustee. No standalone wealth boutique or competitor can replicate this integrated group capability.' },
  { head: 'AA Regulatory Tailwind', body: 'RBI\'s Account Aggregator framework provides legal, real-time consent-based data rails. Axis can legally view a client\'s FULL balance sheet — including competitor holdings.' },
];

anchors.forEach((a, i) => {
  const y = c3y + 1.2 + i * 1.0;
  s1.addShape(pres.ShapeType.rect, { x: c3x, y, w: colW - 0.3, h: 0.93, fill: { color: 'EFF8F4' }, line: { color: 'B8DECE', pt: 1 } });
  s1.addShape(pres.ShapeType.rect, { x: c3x, y, w: 0.06, h: 0.93, fill: { color: MINT }, line: { type: 'none' } });
  s1.addText(a.head, { x: c3x + 0.15, y: y + 0.05, w: colW - 0.45, h: 0.22, fontSize: 10, bold: true, color: MINT, fontFace: 'Calibri' });
  s1.addText(a.body, { x: c3x + 0.15, y: y + 0.27, w: colW - 0.45, h: 0.6, fontSize: 8.5, color: TEXTGRAY, fontFace: 'Calibri' });
});

// Speaker note pull-quote at bottom
s1.addShape(pres.ShapeType.rect, { x: 0.35, y: 7.08, w: 12.6, h: 0.32, fill: { color: MAROON }, line: { type: 'none' } });
s1.addText('"Burgundy is already a market leader. But to capture the next wave of India\'s wealth, we must multiply advisor capability — not headcount. WealthOS is that future."', {
  x: 0.5, y: 7.09, w: 12.3, h: 0.28,
  fontSize: 9, color: GOLD, fontFace: 'Calibri', italic: true, align: 'center'
});


// ─────────────────────────────────────────────────────────────────────────────
// SLIDE 2 — HOW IT WORKS & IMPACT
// ─────────────────────────────────────────────────────────────────────────────
const s2 = pres.addSlide();
s2.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 13.3, h: 7.5, fill: { color: OFFWHITE }, line: { type: 'none' } });

// Top bar
s2.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 13.3, h: 0.7, fill: { color: MAROON }, line: { type: 'none' } });
s2.addText('SLIDE 2  ·  HOW IT WORKS & STRATEGIC IMPACT', { x: 0.4, y: 0.1, w: 8, h: 0.45, fontSize: 10, bold: true, color: GOLD, fontFace: 'Calibri', charSpacing: 2 });
s2.addText('AXIS WEALTHOS 2035', { x: 0.4, y: 0.1, w: 12.5, h: 0.45, fontSize: 10, color: LIGHTGRAY, fontFace: 'Calibri', align: 'right' });

// Main headline
s2.addText('Advisory Pods · Multi-Entity Integration · Business Case', {
  x: 0.4, y: 0.82, w: 12.5, h: 0.55,
  fontSize: 20, bold: true, color: MAROON, fontFace: 'Cambria'
});
s2.addShape(pres.ShapeType.rect, { x: 0.4, y: 1.38, w: 12.5, h: 0.04, fill: { color: GOLD }, line: { type: 'none' } });

// ── LEFT: OPERATING MODEL FLOWCHART (6.1" wide) ──────────────────────────────
const LX = 0.35;
const LY = 1.5;
const LW = 6.7;

s2.addText('THE WEALTHOS OPERATING MODEL', {
  x: LX, y: LY, w: LW, h: 0.28,
  fontSize: 10, bold: true, color: MAROON, fontFace: 'Calibri', charSpacing: 1
});

// Flow steps
const flowSteps = [
  {
    label: 'INPUT',
    color: '34495E',
    head: 'Client Financial Data',
    items: ['Internal: Axis deposits, credit, card spends', 'External (AA APIs): MFs, equities, insurance,\nliabilities, property, business cash flows'],
  },
  {
    label: 'INTELLIGENCE',
    color: STEEL,
    head: 'AI Advice Factory',
    items: ['Continuous event detection: drift, tax-harvest,\nALM mismatch, succession triggers', 'Risk suitability audit + explainability log\nbefore any recommendation surfaces'],
  },
  {
    label: 'DELIVERY',
    color: MAROON,
    head: 'Advisory Pod',
    items: ['Lead RM (trust + goal discovery)', 'Portfolio Architect (asset allocation)', 'Credit Specialist (leverage + liquidity)'],
  },
  {
    label: 'EXECUTION',
    color: MINT,
    head: 'One Axis Ecosystem',
    items: ['Axis Securities  ·  Axis AMC  ·  Axis Capital', 'Axis Finance  ·  Axis Trustee Services', 'Seamless group routing — single client view'],
  },
];

const fBoxW = LW / 4 - 0.12;
flowSteps.forEach((f, i) => {
  const fx = LX + i * (fBoxW + 0.12);
  const fy = LY + 0.38;
  const fh = 2.55;

  // Box
  s2.addShape(pres.ShapeType.rect, { x: fx, y: fy, w: fBoxW, h: fh, fill: { color: WHITE }, line: { color: LIGHTGRAY, pt: 1 } });
  // Colored header
  s2.addShape(pres.ShapeType.rect, { x: fx, y: fy, w: fBoxW, h: 0.48, fill: { color: f.color }, line: { type: 'none' } });
  s2.addText(f.label, { x: fx + 0.08, y: fy + 0.04, w: fBoxW - 0.1, h: 0.18, fontSize: 7.5, bold: true, color: WHITE, fontFace: 'Calibri', charSpacing: 1 });
  s2.addText(f.head, { x: fx + 0.08, y: fy + 0.22, w: fBoxW - 0.1, h: 0.22, fontSize: 9.5, bold: true, color: WHITE, fontFace: 'Cambria' });

  f.items.forEach((item, j) => {
    s2.addText('▸  ' + item, {
      x: fx + 0.08, y: fy + 0.56 + j * 0.65, w: fBoxW - 0.12, h: 0.6,
      fontSize: 8, color: TEXTGRAY, fontFace: 'Calibri'
    });
  });

  // Arrow between boxes
  if (i < 3) {
    s2.addShape(pres.ShapeType.rect, {
      x: fx + fBoxW, y: fy + fh / 2 - 0.04, w: 0.12, h: 0.08,
      fill: { color: GOLD }, line: { type: 'none' }
    });
  }
});

// Phase rollout timeline
s2.addShape(pres.ShapeType.rect, { x: LX, y: LY + 3.07, w: LW, h: 0.26, fill: { color: MAROON }, line: { type: 'none' } });
s2.addText('IMPLEMENTATION ROADMAP', { x: LX + 0.15, y: LY + 3.1, w: LW - 0.2, h: 0.2, fontSize: 9, bold: true, color: GOLD, fontFace: 'Calibri', charSpacing: 1 });

const phases = [
  { ph: 'PHASE 1  ·  Yr 1–2', col: MAROON2, head: 'Foundation & HNI Pilot', items: ['Wealth Twin data layer build', 'AA API integration', '500 RM pilot deployment', 'Advisory productivity lift proof'] },
  { ph: 'PHASE 2  ·  Yr 3–5', col: STEEL, head: 'Affluent Scale-Up', items: ['Expand to full Burgundy segment', 'Family Banking 2.0 launch', 'Pod-based coverage rollout', 'GST + business cash flow data'] },
  { ph: 'PHASE 3  ·  Yr 6–10', col: MINT, head: 'One Axis Integration', items: ['Full entity routing activated', 'Open API ecosystem partners', 'Cross-border & AIF integration', '100% data-native household advisory'] },
];

const phW = LW / 3 - 0.1;
phases.forEach((p, i) => {
  const px = LX + i * (phW + 0.1);
  const py = LY + 3.4;
  s2.addShape(pres.ShapeType.rect, { x: px, y: py, w: phW, h: 2.55, fill: { color: WHITE }, line: { color: LIGHTGRAY, pt: 1 } });
  s2.addShape(pres.ShapeType.rect, { x: px, y: py, w: phW, h: 0.38, fill: { color: p.col }, line: { type: 'none' } });
  s2.addText(p.ph, { x: px + 0.08, y: py + 0.04, w: phW - 0.12, h: 0.2, fontSize: 7.5, bold: true, color: WHITE, fontFace: 'Calibri', charSpacing: 1 });
  s2.addText(p.head, { x: px + 0.08, y: py + 0.4, w: phW - 0.12, h: 0.28, fontSize: 10, bold: true, color: DARK, fontFace: 'Cambria' });
  p.items.forEach((item, j) => {
    s2.addText('•  ' + item, { x: px + 0.1, y: py + 0.72 + j * 0.44, w: phW - 0.15, h: 0.4, fontSize: 8, color: TEXTGRAY, fontFace: 'Calibri' });
  });
});

// ── RIGHT: IMPACT + RISK (6.2" wide) ─────────────────────────────────────────
const RX = 7.2;
const RY = 1.5;
const RW = 5.75;

s2.addText('FINANCIAL & FEASIBILITY SCORECARD', {
  x: RX, y: RY, w: RW, h: 0.28,
  fontSize: 10, bold: true, color: MAROON, fontFace: 'Calibri', charSpacing: 1
});

// Metrics table header
const tY = RY + 0.32;
s2.addShape(pres.ShapeType.rect, { x: RX, y: tY, w: RW, h: 0.3, fill: { color: MAROON }, line: { type: 'none' } });
const hCols = ['INDICATOR', 'FY27 BASE', '2030', '2035'];
const hWids = [2.0, 1.15, 1.15, 1.15];
let hOff = RX + 0.08;
hCols.forEach((h, i) => {
  s2.addText(h, { x: hOff, y: tY + 0.05, w: hWids[i], h: 0.2, fontSize: 8, bold: true, color: GOLD, fontFace: 'Calibri' });
  hOff += hWids[i] + 0.05;
});

const rows = [
  ['Burgundy AUM',            '₹7.54T',    '₹11.50T',  '₹16.50T'],
  ['Burgundy Private AUM',    '₹2.68T',    '₹4.50T',   '₹7.00T'],
  ['UHNWI Families Served',   '17,400+',   '30,000+',  '55,000+'],
  ['RM Productivity',         '1.0x',      '1.3x',     '1.6x'],
  ['Wallet Share (Affluent)', '~18%',      '25%',      '35%'],
  ['Cost-to-Serve',           'Baseline',  '–35%',     '–85%'],
  ['Advisory Turnaround',     'T+2 days',  'T+4 hrs',  '<5 min'],
];

rows.forEach((r, i) => {
  const ry = tY + 0.3 + i * 0.37;
  const bg = i % 2 === 0 ? 'F5F0EB' : WHITE;
  s2.addShape(pres.ShapeType.rect, { x: RX, y: ry, w: RW, h: 0.37, fill: { color: bg }, line: { type: 'none' } });
  let xOff = RX + 0.08;
  r.forEach((cell, j) => {
    const isPositive = (j >= 2) && (cell.includes('T') || cell.includes('%') || cell.includes('min') || cell.includes('hrs') || cell.includes('+') || cell.includes('x'));
    const isNegative = cell.startsWith('–');
    s2.addText(cell, {
      x: xOff, y: ry + 0.07, w: hWids[j], h: 0.24,
      fontSize: j === 0 ? 8.5 : 9, bold: j > 0, color: isPositive ? MINT : isNegative ? MINT : j === 0 ? TEXTGRAY : DARK,
      fontFace: 'Calibri'
    });
    xOff += hWids[j] + 0.05;
  });
});

// Feasibility scores
const feasY = tY + 0.3 + rows.length * 0.37 + 0.15;
s2.addShape(pres.ShapeType.rect, { x: RX, y: feasY, w: RW, h: 0.28, fill: { color: STEEL }, line: { type: 'none' } });
s2.addText('FEASIBILITY ASSESSMENT', { x: RX + 0.1, y: feasY + 0.05, w: RW - 0.15, h: 0.18, fontSize: 9, bold: true, color: WHITE, fontFace: 'Calibri', charSpacing: 1 });

const feases = [
  { lbl: 'Strategic Fit', score: '9/10' },
  { lbl: 'Market Demand', score: '9/10' },
  { lbl: 'Tech & Data', score: '8/10' },
  { lbl: 'Operational', score: '7/10' },
  { lbl: 'Regulatory', score: '8/10' },
];
const fFW = RW / feases.length;
feases.forEach((f, i) => {
  const fx = RX + i * fFW;
  const fy = feasY + 0.3;
  s2.addShape(pres.ShapeType.rect, { x: fx + 0.04, y: fy, w: fFW - 0.08, h: 0.7, fill: { color: WHITE }, line: { color: LIGHTGRAY, pt: 1 } });
  s2.addText(f.score, { x: fx + 0.04, y: fy + 0.06, w: fFW - 0.08, h: 0.3, fontSize: 16, bold: true, color: MAROON, fontFace: 'Cambria', align: 'center' });
  s2.addText(f.lbl, { x: fx + 0.04, y: fy + 0.38, w: fFW - 0.08, h: 0.26, fontSize: 7.5, color: TEXTGRAY, fontFace: 'Calibri', align: 'center' });
});

// Risk mitigations
const riskY = feasY + 1.1;
s2.addShape(pres.ShapeType.rect, { x: RX, y: riskY, w: RW, h: 0.28, fill: { color: MAROON2 }, line: { type: 'none' } });
s2.addText('KEY RISK MITIGATIONS', { x: RX + 0.1, y: riskY + 0.05, w: RW - 0.15, h: 0.18, fontSize: 9, bold: true, color: WHITE, fontFace: 'Calibri', charSpacing: 1 });

const risks = [
  { risk: 'RM Resistance', mit: 'AI as co-pilot: automates prep & compliance; RMs own 100% relationship time' },
  { risk: 'Data Privacy', mit: 'Granular client-revocable consent; zero-knowledge proofs; live data dashboards' },
  { risk: 'Model Bias / Hallucination', mit: 'Human-in-the-loop: Portfolio Architect validates every AI proposal before client' },
  { risk: 'One Axis Friction', mit: 'Unified Group Wallet Share scorecard; shared commissions across all entities' },
];

risks.forEach((r, i) => {
  const ry = riskY + 0.32 + i * 0.52;
  const bg = i % 2 === 0 ? 'FDF0F0' : WHITE;
  s2.addShape(pres.ShapeType.rect, { x: RX, y: ry, w: RW, h: 0.5, fill: { color: bg }, line: { color: LIGHTGRAY, pt: 1 } });
  s2.addText('⚠ ' + r.risk + ':', { x: RX + 0.1, y: ry + 0.04, w: 1.5, h: 0.42, fontSize: 8, bold: true, color: MAROON, fontFace: 'Calibri' });
  s2.addText(r.mit, { x: RX + 1.6, y: ry + 0.1, w: RW - 1.65, h: 0.35, fontSize: 8, color: TEXTGRAY, fontFace: 'Calibri' });
});

// Footer quote
s2.addShape(pres.ShapeType.rect, { x: 0, y: 7.17, w: 13.3, h: 0.33, fill: { color: MAROON }, line: { type: 'none' } });
s2.addText('"WealthOS is not an app or a chatbot. It is a fundamental operational rewiring — turning Axis\'s multi-entity capabilities into one cohesive client experience."', {
  x: 0.4, y: 7.18, w: 12.5, h: 0.28,
  fontSize: 9, color: GOLD, fontFace: 'Calibri', italic: true, align: 'center'
});

// ── WRITE ─────────────────────────────────────────────────────────────────────
pres.writeFile({ fileName: '/home/claude/AxisWealthOS2035_TeamCashCows.pptx' })
  .then(() => console.log('DONE'))
  .catch(e => { console.error(e); process.exit(1); });
