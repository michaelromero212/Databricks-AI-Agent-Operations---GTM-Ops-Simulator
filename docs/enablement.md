# AI Agent Enablement Guide

## Document Purpose

This guide helps GTM users understand how to effectively use AI agents, when to trust agent outputs, and when to escalate to humans.

---

## Quick Start

### Accessing the Agent

1. **Web App**: Navigate to [Agent Dashboard](http://localhost:8000)
2. **Login**: Use your company SSO credentials
3. **Select Task Type**: Choose from available options (Lead Summary, Follow-Up Suggestion, Risk Analysis, etc.)
4. **Submit Query**: Provide context (lead name, deal info, etc.)
5. **Review Output**: Agent response appears within seconds

---

## Task Types & Use Cases

### 1. Lead Summary
**When to use**: When you receive a new inbound lead or are researching a prospect

**What you provide**:
- Lead name and company
- Any known context (campaign source, industry, etc.)

**What you get**:
- Company overview
- Industry and use case fit
- Intent signals (if available)
- Suggested qualification questions
- Recommended next steps

**Example**:
```
Input: "Summarize lead: Jane Smith, Acme Financial Services"
Output: 
- Acme Financial Services is a mid-market banking institution ($500M revenue)
- Strong fit for Databricks: data analytics, regulatory reporting, fraud detection
- Intent signals: Recent visit to pricing page, downloaded lakehouse whitepaper
- Suggested questions: "What data challenges are you facing with your current platform?"
- Next step: Schedule discovery call within 24 hours
```

---

### 2. Follow-Up Suggestion
**When to use**: After a meeting or customer interaction when you need next steps

**What you provide**:
- Brief summary of last interaction
- Current deal stage

**What you get**:
- Personalized follow-up message suggestions
- Relevant resources to share (case studies, docs)
- Timeline recommendation

**Example**:
```
Input: "Follow-up suggestion for demo completed yesterday with Acme Corp CTO"
Output:
- Send thank-you email within 4 hours
- Include: Link to relevant lakehouse architecture docs
- Offer: Technical deep-dive session with Solutions Architect
- Timeline: Propose next meeting within 3-5 business days
```

---

### 3. Risk Analysis
**When to use**: When a deal seems stalled or you sense potential issues

**What you provide**:
- Deal name and stage
- Recent activity summary (or lack thereof)

**What you get**:
- Risk signals identified
- Suggested mitigation actions
- Escalation recommendations

**Example**:
```
Input: "Analyze risk for Acme Corp deal - Stage 3, no activity in 2 weeks"
Output:
- Risk signals: Extended silence, missed follow-up commitments
- Suggested actions: Re-engage with multi-threaded outreach, involve SE for value review
- Escalation: Consider manager involvement if no response in 3 days
```

---

## Understanding Agent Responses

### Confidence Indicators

Agent outputs include a confidence level:

- **High Confidence (✓)**: Agent has strong data support, low ambiguity
- **Medium Confidence (!)**: Agent has partial data, some assumptions made
- **Low Confidence / Escalate (⚠)**: Agent recommends human review

**Rule of Thumb**: 
- High confidence → Use as-is or with minor edits
- Medium confidence → Review carefully, validate key claims
- Low confidence → Treat as starting point, do your own research

---

### When Agent Will Abstain

The agent is designed to **not** provide answers in certain situations:

1. **Legal/Compliance Topics**
   - "What security certifications do we have?" → Escalate to legal
   - "Can we sign this BAA?" → Escalate to legal

2. **Pricing & Discounting**
   - "What discount should I offer?" → Escalate to manager
   - "Can we reduce price by 30%?" → Escalate to manager

3. **Executive Decisions**
   - "Should we pursue this deal?" → Escalate to AE/manager
   - "Is this customer strategic?" → Escalate to leadership

4. **Technical Depth Beyond Training**
   - "How do we configure Delta Live Tables for XYZ use case?" → Escalate to SE

**What happens**: Agent will respond with:
```
⚠ This query requires human expertise. 
Recommended action: Consult with [Legal/Manager/SE/etc.]
Reason: [Brief explanation]
```

**Your action**: Follow the escalation guidance. Do not push the agent to answer.

---

## Best Practices

### ✅ DO

- **Provide context**: More detail = better outputs
  - Good: "Summarize lead: Jane Smith, Acme Bank, came from AWS Marketplace"
  - Poor: "Lead summary"

- **Review outputs**: Always review before using in customer communications
- **Give feedback**: Rate agent outputs (thumbs up/down) to help improve
- **Use for efficiency**: Let agent handle research legwork, you add human judgment
- **Escalate quickly**: If agent abstains, don't try to work around it

### ❌ DON'T

- **Don't copy-paste blindly**: Agent outputs are starting points, not final communications
- **Don't share sensitive data**: Never include customer PII or confidential info in queries
- **Don't circumvent abstentions**: If agent says "escalate," respect that
- **Don't use for financial reporting**: Agent doesn't update CRM fields affecting forecasts
- **Don't expect product roadmap info**: Agent only knows publicly documented features

---

## Common Questions

### Q: Can I trust agent-generated follow-up emails?
**A**: Use them as drafts. Always personalize before sending. Agent doesn't know your relationship history or tone preferences.

### Q: What if the agent is wrong?
**A**: Rate it "thumbs down" and provide feedback. This helps us improve. For urgent issues, contact Sales Ops.

### Q: How does the agent know about my accounts?
**A**: Agent accesses CRM data you have permission to see. It does NOT access data outside your territory.

### Q: Can I use the agent for competitive intel?
**A**: Yes, for publicly available information. Agent can summarize known competitor positioning but won't speculate.

### Q: What if I'm not getting useful outputs?
**A**: Try providing more context in your query. If still not helpful, share feedback with Sales Ops for prompt tuning.

### Q: Is my usage tracked?
**A**: Yes, for quality and performance monitoring only. All data is anonymized for analytics. See privacy policy.

---

## Known Limitations

1. **No real-time data**: Agent uses CRM data refreshed every 4 hours. For real-time info, check CRM directly.
2. **No multi-turn conversations (yet)**: Each query is independent. Future versions may support follow-ups.
3. **English only**: Currently supports English language queries and outputs.
4. **Text-based**: Cannot process images, PDFs, or attachments (coming soon).

---

## Getting Help

### Self-Service Resources
- **Knowledge Base**: [Link to internal wiki]
- **Demo Videos**: [Link to training portal]
- **FAQs**: [Link to FAQ doc]

### Live Support
- **Slack Channel**: #ai-agent-support (monitored 9am-5pm PT)
- **Office Hours**: Tuesdays 2-3pm PT, Thursdays 10-11am PT
- **Email**: ai-ops@company.com

### Reporting Issues
If you encounter:
- Hallucinations or incorrect information
- System errors or performance problems
- Suspected security or privacy issues

**Report via**:
- Slack: #ai-agent-support (tag @ai-ops-oncall)
- Emergency: Page AI Ops on-call via PagerDuty

---

## Feedback & Feature Requests

We want to hear from you!

- **Feedback Form**: [Link to form]
- **Feature Requests**: Submit via #ai-agent-feedback Slack channel
- **User Research**: Volunteer for user interviews to shape product roadmap

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-11 | Initial release |

---

**Document Owner**: Sales Operations & AI Ops  
**Last Updated**: 2026-01-11  
**Review Frequency**: Monthly or upon major agent updates

---

**Remember**: The AI agent is a tool to make you more efficient, not a replacement for your judgment. Use it wisely, and don't hesitate to escalate when needed!
