// ────────────────────────────────────────────────────────
// AXIS BURGUNDY PRIVATE — WEALTHOS STATE LOGIC
// ────────────────────────────────────────────────────────

// State Management
let appState = {
    currentView: 'client', // 'client' or 'rm'
    accountAggregatorActive: false,
    selectedClient: 'Vikram Adani',
    activePodTab: 'rm',
    actions: [
        {
            id: 1,
            title: "Automated Tax-Loss Harvesting",
            category: "Tax Optimization",
            body: "Rebalance equity holdings across Axis Securities and external accounts to harvest accrued tax losses, reducing net tax liabilities.",
            impact: "Tax Saving: ~₹4.8 Lakhs",
            status: "pending",
            type: "tax"
        },
        {
            id: 2,
            title: "Concentration Risk Diversification",
            category: "Portfolio Risk",
            body: "Detected that 45% of external holdings are concentrated in a single sector. Propose diversifying ₹3.5 Cr into Axis ESG Integration Mutual Fund.",
            impact: "Risk Index: High → Balanced",
            status: "pending",
            type: "risk"
        },
        {
            id: 3,
            title: "Family Estate Plan & Trust Setup",
            category: "Succession",
            body: "Son Kabir is turning 21 in 60 days. Setup the Family Legacy Trust structure using Axis Trustee Services to ensure smooth succession.",
            impact: "Tax/Probate Mitigation",
            status: "pending",
            type: "estate"
        },
        {
            id: 4,
            title: "Liquidity Runway Advisory",
            category: "Credit / Leverage",
            body: "Upcoming working capital requirement identified for Q3. Secure ₹1.5 Cr Loan Against Mutual Funds (LAMF) at 7.2% via Axis Finance.",
            impact: "Avoid liquidating compounding equity",
            status: "pending",
            type: "credit"
        }
    ],
    podComments: {
        rm: [
            { author: "Arnika Dixit (Lead RM)", time: "10:15 AM", text: "Spoke to Vikram regarding the upcoming promoter liquidity event. He is keen on establishing the trust before the quarter end." },
            { author: "Arnika Dixit (Lead RM)", time: "Yesterday", text: "Client confirmed they will consent to the Account Aggregator link to bring in their external HDFC portfolio." }
        ],
        portfolio: [
            { author: "Devang Mehta (Portfolio)", time: "11:30 AM", text: "Ran simulated rebalancing. Diversifying the external equity concentration will lower portfolio volatility by 14% while retaining dividend yield." },
            { author: "Devang Mehta (Portfolio)", time: "Yesterday", text: "Axis ESG fund is the best fit for his sustainability preference." }
        ],
        credit: [
            { author: "Siddharth Rao (Credit)", time: "09:45 AM", text: "Approved the ₹1.5 Cr collateralized line of credit limit against their Axis AMC holdings. LTV sits at 40%." }
        ]
    },
    clients: {
        'Vikram Adani': {
            name: "Vikram Adani",
            role: "Promoter & Business Owner",
            netWorthAxis: 18.20,
            netWorthTotal: 42.50,
            assetsAxis: 14.50,
            assetsTotal: 38.80,
            liabilities: 3.70,
            dossier: {
                summary: "Vikram Adani is a first-generation promoter of a logistics conglomerate. He maintains a core deposit and trading account at Axis Bank, but holds substantial equity portfolios and real estate externally. He is focused on business expansion and family succession planning.",
                anomalies: "Anomalous business cash flow spike detected in July due to promoter dividend payouts. Long-term equity portfolio has drifted 8% away from the target asset allocation.",
                suitability: "Risk Profile: Balanced Growth. Maximum recommended equity allocation is 65%. High-leverage structures are currently restricted."
            }
        },
        'Rajesh Sharma': {
            name: "Rajesh Sharma",
            role: "Agri-Exporter (Mandi Operator)",
            netWorthAxis: 5.40,
            netWorthTotal: 8.40,
            assetsAxis: 4.20,
            assetsTotal: 7.20,
            liabilities: 1.20,
            dossier: {
                summary: "Rajesh Sharma operates a major agricultural trading and export firm in Indore. Managed via our virtual Hub-and-Spoke model: day-to-day relationship handled by the local Indore branch spoke, with complex structuring (leverage and commodity hedges) coordinated virtually by the Mumbai Advisory Hub. His wealth is highly cyclical, aligned with crop harvest payouts.",
                anomalies: "Seasonal cash inflow spike expected in late September. Concentration of wealth in commodity and mandis deposits, leaving him exposed to agricultural sector volatility.",
                suitability: "Risk Profile: Muted / Conservative. High-volatility alternative funds or international equities are marked unsuitable. Direct short-term debt instruments are preferred."
            }
        },
        'Dr. Priya Patel': {
            name: "Dr. Priya Patel",
            role: "Chief Cardiologist",
            netWorthAxis: 9.30,
            netWorthTotal: 12.10,
            assetsAxis: 8.10,
            assetsTotal: 10.90,
            liabilities: 1.20,
            dossier: {
                summary: "Dr. Priya Patel is a leading cardiologist based in Ahmedabad. She has steady, high-salary income and is looking for long-term wealth compounding, retirement planning, and tax-efficient investing.",
                anomalies: "Consistent monthly SIP flows. Cash drag observed in primary savings account (approx ₹85 Lakhs earning low interest).",
                suitability: "Risk Profile: Long-Term Growth. Propose shifting cash drag into dynamic asset allocation funds. Unregulated assets or volatile derivatives are flagged unsuitable."
            }
        }
    }
};

// ────────────────────────────────────────────────────────
// INITIALIZATION
// ────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
    renderCharts();
    renderAIQueue();
    renderPodComments();
    generateDossier();
    resetSuitabilityState();
    initializeMetalCardEffects();
});

// ────────────────────────────────────────────────────────
// VIEW SWITCHER
// ────────────────────────────────────────────────────────

function switchView(view) {
    appState.currentView = view;
    
    // Toggle active classes on nav buttons
    document.getElementById('btn-client-view').classList.toggle('active', view === 'client');
    document.getElementById('btn-rm-view').classList.toggle('active', view === 'rm');
    
    // Toggle visible views
    document.getElementById('client-view').classList.toggle('active', view === 'client');
    document.getElementById('rm-view').classList.toggle('active', view === 'rm');

    // Sync client info to header
    const client = appState.clients[appState.selectedClient];
    if (view === 'rm') {
        document.getElementById('user-display-name').innerText = "Arnika Dixit";
        document.getElementById('user-display-role').innerText = "Lead Wealth Partner";
    } else {
        document.getElementById('user-display-name').innerText = client.name;
        document.getElementById('user-display-role').innerText = client.role;
    }
}

// ────────────────────────────────────────────────────────
// ACCOUNT AGGREGATOR TOGGLE
// ────────────────────────────────────────────────────────

function toggleAccountAggregator() {
    appState.accountAggregatorActive = !appState.accountAggregatorActive;
    
    const client = appState.clients[appState.selectedClient];
    const statusText = document.getElementById('aa-status-text');
    const statusDot = document.getElementById('aa-status-dot');
    const actionHint = document.getElementById('aa-action-hint');
    const banner = document.getElementById('aa-alert-banner');
    const trusteeItem = document.getElementById('eco-trustee');

    if (appState.accountAggregatorActive) {
        // Toggle on AA
        statusText.innerText = "ACTIVE";
        statusText.className = "bs-card-val text-mint"; // change color class
        statusDot.classList.add('online');
        actionHint.innerText = "Axis + External Linked";
        if (banner) banner.style.display = "none";
        
        // Animated numbers count-up
        animateValue("net-worth-val", client.netWorthAxis, client.netWorthTotal, "₹", " Cr");
        animateValue("assets-val", client.assetsAxis, client.assetsTotal, "₹", " Cr");
        document.getElementById('assets-status').innerHTML = '<i class="fa-solid fa-square-check text-mint"></i> Axis + External Assets';
        
        if (appState.selectedClient === 'Vikram Adani') {
            trusteeItem.classList.add('active');
            const routingStatus = trusteeItem.querySelector('.routing-status');
            if (routingStatus) {
                routingStatus.innerText = "Linked";
                routingStatus.style.color = "var(--mint)";
            }
        }
        
        showNotification("Account Aggregator Connected", "Consented external bank portfolios, stock holdings, and asset registries have been synced successfully via AA APIs.");
    } else {
        // Toggle off AA
        statusText.innerText = "OFFLINE";
        statusText.className = "bs-card-val text-burgundy";
        statusDot.classList.remove('online');
        actionHint.innerText = "Click to authorize sync";
        if (banner) banner.style.display = "flex";
        
        // Animated numbers count-down
        animateValue("net-worth-val", client.netWorthTotal, client.netWorthAxis, "₹", " Cr");
        animateValue("assets-val", client.assetsTotal, client.assetsAxis, "₹", " Cr");
        document.getElementById('assets-status').innerText = 'Axis Assets Only';
        
        trusteeItem.classList.remove('active');
        const routingStatus = trusteeItem.querySelector('.routing-status');
        if (routingStatus) {
            routingStatus.innerText = "Inactive";
            routingStatus.style.color = "var(--text-light)";
        }
    }

    renderCharts();
}

function animateValue(id, start, end, prefix = "", suffix = "") {
    const obj = document.getElementById(id);
    let current = start;
    const duration = 500; // ms
    const stepTime = 25; // ms
    const steps = duration / stepTime;
    const stepValue = (end - start) / steps;
    let stepCount = 0;

    const timer = setInterval(() => {
        current += stepValue;
        stepCount++;
        if (stepCount >= steps) {
            clearInterval(timer);
            current = end;
        }
        obj.innerText = prefix + current.toFixed(2) + suffix;
    }, stepTime);
}

// ────────────────────────────────────────────────────────
// DYNAMIC CHARTS (HTML5 Canvas Drawing - Sharp Light Theme)
// ────────────────────────────────────────────────────────

function renderCharts() {
    const canvas = document.getElementById('allocationChart');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    // Define segments based on AA connection status
    let segments = [];
    if (!appState.accountAggregatorActive) {
        segments = [
            { label: 'Axis Bank Deposits', value: 3.5, color: '#861F41' },
            { label: 'Axis Mutual Funds', value: 6.0, color: '#a32c53' },
            { label: 'Axis Equity PMS', value: 5.0, color: '#c24b6e' }
        ];
    } else {
        segments = [
            { label: 'Axis Bank Deposits', value: 3.5, color: '#861F41' },
            { label: 'Axis Mutual Funds', value: 6.0, color: '#a32c53' },
            { label: 'Axis Equity PMS', value: 5.0, color: '#c24b6e' },
            { label: 'Ext Cash & FDs', value: 4.3, color: '#E3C79D' },
            { label: 'Ext Mutual Funds', value: 12.0, color: '#ECD6B8' },
            { label: 'Ext Real Estate', value: 8.0, color: '#F5E5D0' }
        ];
    }

    // Animated Doughnut Draw
    let total = segments.reduce((sum, s) => sum + s.value, 0);
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = Math.min(centerX, centerY) - 15;
    const thickness = 24;
    
    let currentProgress = 0;
    
    function drawFrame() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        currentProgress += 0.05; // speed factor (approx 20 frames)
        if (currentProgress > 1) currentProgress = 1;
        
        let startAngle = -Math.PI / 2;
        segments.forEach(seg => {
            let sliceAngle = (seg.value / total) * (2 * Math.PI);
            let currentSliceAngle = sliceAngle * currentProgress;
            
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, startAngle, startAngle + currentSliceAngle);
            ctx.strokeStyle = seg.color;
            ctx.lineWidth = thickness;
            ctx.lineCap = 'butt';
            ctx.stroke();
            
            startAngle += sliceAngle;
        });
        
        if (currentProgress < 1) {
            requestAnimationFrame(drawFrame);
        }
    }
    
    requestAnimationFrame(drawFrame);

    // Update center label text
    const client = appState.clients[appState.selectedClient];
    document.getElementById('center-label-val').innerText = '₹' + (appState.accountAggregatorActive ? client.netWorthTotal : client.netWorthAxis).toFixed(2) + ' Cr';
    document.getElementById('center-label-title').innerText = appState.accountAggregatorActive ? 'Consolidated' : 'Axis Assets';

    // Render legend
    const legendContainer = document.getElementById('allocationLegend');
    legendContainer.innerHTML = '';
    
    segments.forEach(seg => {
        const item = document.createElement('div');
        item.className = 'legend-item';
        item.innerHTML = `
            <div class="legend-key">
                <span class="color-dot" style="background-color: ${seg.color}"></span>
                <span>${seg.label}</span>
            </div>
            <span class="legend-val">₹${seg.value.toFixed(1)} Cr</span>
        `;
        legendContainer.appendChild(item);
    });

    document.getElementById('asset-count-badge').innerText = `${segments.length} Asset Classes`;
}

// ────────────────────────────────────────────────────────
// AI ADVICE FACTORY QUEUE
// ────────────────────────────────────────────────────────

function renderAIQueue() {
    const container = document.getElementById('advice-action-list');
    if (!container) return;
    
    container.innerHTML = '';
    let pendingActions = appState.actions.filter(a => a.status === 'pending');
    
    document.getElementById('action-count-badge').innerText = `${pendingActions.length} Actions`;

    if (pendingActions.length === 0) {
        container.innerHTML = `
            <div class="result-placeholder" style="padding: 2rem 0; width: 100%;">
                <i class="fa-solid fa-circle-check text-mint" style="font-size: 2.5rem; margin-bottom: 10px; color: var(--mint);"></i>
                <p>All structural advisory actions completed and routed. Continuous scanning active.</p>
            </div>
        `;
        return;
    }

    pendingActions.forEach(act => {
        const item = document.createElement('div');
        item.className = 'advice-item';
        item.id = `advice-item-${act.id}`;
        
        let iconHtml = '<i class="fa-solid fa-circle-nodes"></i>';
        if (act.type === 'tax') iconHtml = '<i class="fa-solid fa-percent"></i>';
        if (act.type === 'risk') iconHtml = '<i class="fa-solid fa-shield-halved"></i>';
        if (act.type === 'estate') iconHtml = '<i class="fa-solid fa-crown"></i>';
        if (act.type === 'credit') iconHtml = '<i class="fa-solid fa-vault"></i>';

        item.innerHTML = `
            <span class="advice-tag">${act.category}</span>
            <div class="advice-item-icon">${iconHtml}</div>
            <div class="advice-details">
                <h4>${act.title}</h4>
                <p>${act.body}</p>
                <span class="advice-impact"><i class="fa-solid fa-circle-check"></i> ${act.impact}</span>
                <div class="advice-actions">
                    <button class="btn btn-burgundy btn-sm" onclick="approveAction(${act.id})"><i class="fa-solid fa-signature"></i> Grant Consent</button>
                    <button class="btn btn-secondary btn-sm" onclick="postponeAction(${act.id})">Hold Recommendation</button>
                </div>
            </div>
        `;
        container.appendChild(item);
    });
}

function approveAction(id) {
    const item = document.getElementById(`advice-item-${id}`);
    if (item) {
        item.style.transform = 'translateX(-30px)';
        item.style.opacity = '0';
        
        setTimeout(() => {
            const index = appState.actions.findIndex(a => a.id === id);
            if (index !== -1) {
                appState.actions[index].status = 'executed';
                
                // Specific action rewards
                if (id === 3) {
                    // Estate Trust linked
                    const linkStatus = document.getElementById('kabir-link-status');
                    if (linkStatus) {
                        linkStatus.className = "badge-status success";
                        linkStatus.innerText = "Trust Established";
                    }
                    // Update Timeline Milestone Step 2
                    const timelineItem = document.getElementById('eco-trustee-timeline');
                    if (timelineItem) {
                        timelineItem.className = "timeline-item completed";
                        timelineItem.querySelector('.timeline-dot').innerHTML = '<i class="fa-solid fa-check"></i>';
                        timelineItem.querySelector('.timeline-content span').innerText = "Step 2 · Completed";
                    }
                }
                
                renderAIQueue();
                
                let titleText = "Consent Logged & Executed";
                let bodyText = "Your digital approval has been logged in compliance with SEBI guidelines. This transaction has been securely routed across group entities and recorded in the audit trail.";
                
                showNotification(titleText, bodyText);
            }
        }, 200);
    }
}

function postponeAction(id) {
    const item = document.getElementById(`advice-item-${id}`);
    if (item) {
        item.style.transform = 'translateY(10px)';
        item.style.opacity = '0.4';
        setTimeout(() => {
            const index = appState.actions.findIndex(a => a.id === id);
            if (index !== -1) {
                appState.actions.push(appState.actions.splice(index, 1)[0]); // Move to end of queue
                renderAIQueue();
            }
        }, 200);
    }
}

// ────────────────────────────────────────────────────────
// CLIENT SELECTION & DOSSIER (RM VIEW)
// ────────────────────────────────────────────────────────

function selectClient(name) {
    appState.selectedClient = name;
    
    // Toggle active list item
    const items = document.querySelectorAll('.roster-item');
    items.forEach(el => {
        const clientName = el.querySelector('strong').innerText;
        el.classList.toggle('active', clientName === name);
    });

    // Update RM title
    document.getElementById('briefing-client-name').innerText = name;
    
    generateDossier();
    resetSuitabilityState();
}

function generateDossier() {
    const container = document.getElementById('dossier-content');
    if (!container) return;
    
    const client = appState.clients[appState.selectedClient];
    
    container.innerHTML = `
        <div class="brief-section">
            <h5>Executive Account Summary</h5>
            <p>${client.dossier.summary}</p>
        </div>
        <div class="brief-section">
            <h5>SPARSH Event Sensing & Anomalies</h5>
            <div class="brief-insights">
                <div class="insight-tag warning">
                    <i class="fa-solid fa-triangle-exclamation text-gold"></i>
                    <span>${client.dossier.anomalies}</span>
                </div>
            </div>
        </div>
        <div class="brief-section">
            <h5>Advisory Parameters</h5>
            <div class="brief-insights">
                <div class="insight-tag">
                    <i class="fa-solid fa-gavel text-burgundy"></i>
                    <span>${client.dossier.suitability}</span>
                </div>
            </div>
        </div>
    `;
}

// ────────────────────────────────────────────────────────
// POD WORKSPACE COMMENTS
// ────────────────────────────────────────────────────────

function renderPodComments() {
    const container = document.getElementById('pod-workspace-container');
    if (!container) return;
    
    container.innerHTML = '';
    const comments = appState.podComments[appState.activePodTab];
    
    comments.forEach(c => {
        const el = document.createElement('div');
        el.className = 'comment-bubble';
        el.innerHTML = `
            <div class="comment-bubble-header">
                <span>${c.author}</span>
                <span>${c.time}</span>
            </div>
            <div class="comment-bubble-body">
                ${c.text}
            </div>
        `;
        container.appendChild(el);
    });
}

function switchPodTab(tab) {
    appState.activePodTab = tab;
    
    const tabBtns = document.querySelectorAll('.pod-tab-links .pod-tab-link');
    tabBtns.forEach(btn => {
        const btnText = btn.innerText.toLowerCase();
        btn.classList.toggle('active', 
            (tab === 'rm' && btnText.includes('rm')) || 
            (tab === 'portfolio' && btnText.includes('portfolio')) || 
            (tab === 'credit' && btnText.includes('credit'))
        );
    });
    
    renderPodComments();
}

function addPodComment() {
    const input = document.getElementById('pod-comment-input');
    if (!input || !input.value.trim()) return;
    
    let author = "Arnika Dixit (Lead RM)";
    if (appState.activePodTab === 'portfolio') author = "Devang Mehta (Portfolio)";
    if (appState.activePodTab === 'credit') author = "Siddharth Rao (Credit)";
    
    appState.podComments[appState.activePodTab].push({
        author: author,
        time: "Just now",
        text: input.value
    });
    
    input.value = '';
    renderPodComments();
    
    // Scroll container to bottom
    const container = document.getElementById('pod-workspace-container');
    container.scrollTop = container.scrollHeight;
}

// ────────────────────────────────────────────────────────
// REGULATORY SUITABILITY CHECKER
// ────────────────────────────────────────────────────────

function resetSuitabilityState() {
    const box = document.getElementById('suitability-result-box');
    if (!box) return;
    
    box.innerHTML = `
        <div class="result-placeholder">
            <i class="fa-solid fa-shield-heart"></i>
            <p>Select a product and verify compliance to display audited results.</p>
        </div>
    `;
}

function runSuitabilityCheck() {
    const productVal = document.getElementById('proposed-product').value;
    const weightVal = document.getElementById('proposed-weight').value;
    const box = document.getElementById('suitability-result-box');
    
    if (!productVal) {
        alert("Please select a proposed product to evaluate.");
        return;
    }

    let status = "passed";
    let titleText = "";
    let bodyText = "";
    let logLines = [];

    // Mock evaluation logic
    if (productVal === 'high-beta-aif') {
        if (appState.selectedClient === 'Rajesh Sharma') {
            status = "failed";
            titleText = "Audit Failed: Asset Volatility Breach";
            bodyText = "The proposed investment is unsuitable for Rajesh Sharma. His client risk profile is Conservative, which prohibits Alternative High-Beta AIFs.";
            logLines = [
                "2026-07-22 00:27:01 UTC - [SPARSH] Running risk profiling validation for Rajesh Sharma...",
                "2026-07-22 00:27:01 UTC - [RULE_CHECK] Profiling: Conservative vs Asset Class: High-Beta AIF (RESTRICTED)",
                "2026-07-22 00:27:02 UTC - [RESULT] FAILED. Suitability mismatch detected.",
                "2026-07-22 00:27:02 UTC - [ACTION] Proposal routing blocked. Auditor alert generated."
            ];
        } else {
            status = "passed";
            titleText = "Audit Passed: Risk Suitable";
            bodyText = "Product is suitable for Vikram Adani's risk profile (Growth). Allocation weight is within SEBI diversification bounds.";
            logLines = [
                "2026-07-22 00:27:01 UTC - [SPARSH] Running risk profiling validation for Vikram Adani...",
                "2026-07-22 00:27:01 UTC - [RULE_CHECK] Profiling: Growth. Allocation Weight: " + weightVal + "% (Allowed Max: 25%)",
                "2026-07-22 00:27:02 UTC - [RESULT] PASSED. Risk score matches profile parameters.",
                "2026-07-22 00:27:02 UTC - [ACTION] Compliance hash generated: 0xa87c4f1d89"
            ];
        }
    } else if (productVal === 'crypto-index') {
        status = "failed";
        titleText = "Audit Failed: Unregulated Asset Class";
        bodyText = "Cryptocurrency exposure index is blocked. Transaction violates current RBI FEMA & SEBI wealth guidelines.";
        logLines = [
            "2026-07-22 00:27:01 UTC - [SPARSH] Evaluated Asset: Cryptocurrency Token index",
            "2026-07-22 00:27:01 UTC - [RBI_RULE_9] Asset Category: Unregulated Digital Tokens (Crypto)",
            "2026-07-22 00:27:02 UTC - [CRITICAL] VIOLATION: Transaction violates bank license compliance parameters.",
            "2026-07-22 00:27:02 UTC - [LOG] Advisory block triggered. Incident reported to compliance monitoring."
        ];
    } else { // esg-mutual-fund or short-term-debt
        status = "passed";
        titleText = "Audit Passed: Asset Suitable";
        bodyText = "Complies fully with asset class limits, risk score match, and KYC compliance criteria.";
        logLines = [
            "2026-07-22 00:27:01 UTC - [SPARSH] Running risk suitability checks...",
            "2026-07-22 00:27:01 UTC - [KYC_CHECK] Active & validated. Product is classified suitable.",
            "2026-07-22 00:27:02 UTC - [RESULT] PASSED. Compliance ledger logged.",
            "2026-07-22 00:27:02 UTC - [ACTION] Compliance hash generated: 0x9f5a7e8b91a2d3c4"
        ];
    }

    // Render results
    box.innerHTML = `
        <div class="result-box">
            <div class="result-header ${status === 'passed' ? 'passed' : 'failed'}">
                <i class="fa-solid ${status === 'passed' ? 'fa-circle-check' : 'fa-circle-xmark'}"></i>
                <span>${titleText}</span>
            </div>
            <p class="result-detail">${bodyText}</p>
            <div class="audit-log-box">
                ${logLines.join('<br/>')}
            </div>
            ${status === 'passed' ? `<button class="btn btn-burgundy btn-sm" onclick="routeToClient()"><i class="fa-solid fa-paper-plane"></i> Route Proposal to Client</button>` : ''}
        </div>
    `;
}

function routeToClient() {
    showNotification("Proposal Transmitted", "The suitability-cleared proposal has been pushed to the client's Wealth Twin action queue.");
    resetSuitabilityState();
}

// ────────────────────────────────────────────────────────
// POPUP MODAL NOTIFICATIONS
// ────────────────────────────────────────────────────────

function showNotification(title, body) {
    document.getElementById('modal-title-text').innerText = title;
    document.getElementById('modal-body-text').innerText = body;
    document.getElementById('notification-modal').classList.add('active');
}

function closeModal() {
    document.getElementById('notification-modal').classList.remove('active');
}

// ────────────────────────────────────────────────────────
// INTERACTIVE 3D METAL CARD PARALLAX EFFECT
// ────────────────────────────────────────────────────────

function initializeMetalCardEffects() {
    const card = document.querySelector('.private-metal-card');
    if (!card) return;
    
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const xc = rect.width / 2;
        const yc = rect.height / 2;
        const angleX = (yc - y) / 12; // Max 10 deg rotation
        const angleY = (x - xc) / 12;
        
        card.style.transform = `rotateY(${angleY}deg) rotateX(${angleX}deg) scale(1.03)`;
        
        const glow = card.querySelector('.metal-card-glow');
        if (glow) {
            const pctX = (x / rect.width) * 100;
            const pctY = (y / rect.height) * 100;
            glow.style.background = `radial-gradient(circle at ${pctX}% ${pctY}%, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0) 65%)`;
        }
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'rotateY(0deg) rotateX(0deg) scale(1)';
        const glow = card.querySelector('.metal-card-glow');
        if (glow) {
            glow.style.background = 'radial-gradient(circle, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0) 70%)';
        }
    });
}
