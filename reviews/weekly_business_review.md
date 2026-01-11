# Weekly Business Review - AI Agent Operations

## Meeting Information

**Date**: 2026-01-11  
**Attendees**: Sales Operations, AI Ops, Engineering, Sales Leadership  
**Review Period**: Week of January 5-11, 2026  
**Review Facilitator**: AI Ops Lead

---

## Executive Summary

**Overall Status**: 🟢 Green - On track

- Agent performance remains strong with 88% task accuracy
- User adoption growing: 10 weekly active users (40% of target cohort)
- A/B test (Agent A vs B) completed - continuing with Agent A pending further iteration
- No critical incidents this week
- Ready to proceed with Phase 2 rollout planning

---

## Key Performance Indicators

### North Star Metrics

| Metric | This Week | Last Week | Target | Status |
|--------|-----------|-----------|--------|--------|
| Task Accuracy | 88.0% | 86.5% | ≥85% | ✅ |
| Avg User Satisfaction | 4.18 / 5 | 4.12 / 5 | ≥4.0 | ✅ |
| Median Resolution Time | 3.3s | 3.5s | ≤5.0s | ✅ |
| Error Rate | 2.0% | 2.5% | ≤2.0% | ✅ |
| Weekly Active Users | 10 | 8 | ≥15 (Phase 1) | 🟡 |
| Abstention Rate | 4.0% | 5.5% | 5-15% | ✅ |

### Trends
- ✅ Task accuracy improving week-over-week
- ✅ User satisfaction stable and above target
- ✅ Performance (resolution time) improving
- 🟡 User adoption growing but below Phase 1 target (10/15)

---

## Usage Analysis

### Task Volume
- **Total Tasks This Week**: 50
- **Day-over-Day**: Consistent usage Mon-Fri, lower on weekends
- **Peak Usage**: 10-11am and 1-3pm PT

### Task Type Breakdown
| Task Type | Count | % of Total | Avg Satisfaction |
|-----------|-------|------------|------------------|
| Lead Summary | 28 | 56% | 4.3 |
| Follow-Up | 14 | 28% | 4.1 |
| Risk Analysis | 6 | 12% | 4.5 |
| Data Hygiene | 2 | 4% | 4.0 |

**Insight**: Lead summary remains dominant use case, aligning with SDR workflow

### User Engagement
- **Power Users** (>5 tasks): user_sdr_001, user_ae_001, user_ops_001
- **New Users This Week**: 2 (user_sdr_009, user_sdr_010)
- **Churned Users**: 1 user inactive for >7 days (user_sdr_007)

---

## Risk & Issues

### Active Risks

1. **🟡 Adoption Below Target**
   - **Risk**: May not hit Phase 1 WAU target (15 users) by end of pilot
   - **Mitigation**: Scheduled enablement session for Jan 13, manager endorsement campaign
   - **Owner**: Sales Ops

2. **🟢 Sample Size for A/B Testing**
   - **Risk**: Insufficient data for statistically significant A/B conclusions
   - **Mitigation**: Extended A/B test timeline, focused on qualitative feedback
   - **Owner**: AI Ops

### Closed Issues
- ✅ Intermittent timeout errors (TC012) - Fixed via API retry logic
- ✅ User feedback form not collecting responses - Form updated, now functional

---

## A/B Test Update

**Test**: Agent A (baseline) vs Agent B (enhanced prompts)  
**Status**: Completed initial analysis  
**Decision**: Continue with Agent A

**Summary**:
- Agent B did not meet success criteria (accuracy and satisfaction targets missed)
- Need to iterate on Agent B design based on user feedback
- Planning Agent C variant for next test cycle

**Next Steps**:
- Qualitative user interviews (week of Jan 13)
- Agent C development (targeting late January launch)

---

## 👥 Stakeholder & Field Feedback
### SDR/AE Sentiment
- **Positive**: "Lead summary is saving 15 mins per lead."
- **Critical**: "Risk analysis misses 'Champion Change' scenarios."
- **Requested**: "Integration with Outreach/Salesloft."

### Field Adoption Metrics
- **Wau (Weekly Active Users)**: 19 (Target: 25)
- **Top User Group**: Enterprise AEs (92% adoption)
- **Training Status**: 85% of pilot group completed `enablement.md` training.

## 🛠️ Operational Health
- **Uptime**: 99.9%
- **API Response Time (Avg)**: 3.70s
- **Critical Incidents**: 0
- **Cost/Run**: $0.00 (HF Free Tier)

## 📋 Decisions & Action Items
- [ ] **DECISION**: Continue Agent A rollout; pause Agent B indefinitely.
- [ ] **ACTION**: Refine Risk Analysis prompt to include "Champion" sentiment detection.
- [ ] **ACTION**: Schedule enablement session for SDR managers on "Prompt Best Practices."

### Issues Reported
- Issue: One user reported agent suggested outdated case study (escalated to content team)
- Issue: Confidence scores not always clear (added to product backlog)

---

## User Feedback Highlights

### Positive Feedback
- "Saves me 20 minutes per lead - love it!" - SDR user
- "Follow-up suggestions are spot-on" - AE user
- "Great for data cleanup" - Ops user

### Improvement Requests
- Request: Support for multi-lead batch processing
- Request: Slack integration for agent outputs
- Request: Ability to save favorite queries/templates

### Issues Reported
- Issue: One user reported agent suggested outdated case study (escalated to content team)
- Issue: Confidence scores not always clear (added to product backlog)

---

## Operational Health

### Infrastructure
- **Uptime**: 99.8% (brief maintenance window Tuesday)
- **API Response Time**: p50 = 3.1s, p95 = 6.2s (within SLA)
- **Error Budget**: 98% remaining (healthy)

### Incidents
- **P3**: Brief API timeout on Jan 8 (1 user affected, resolved in 10 minutes)
- **No P0, P1, or P2 incidents**

---

## Decisions Made

1. ✅ **Continue Agent A, pause Agent B rollout**
   - Rationale: A/B test results inconclusive, need iteration
   - Decision Owner: AI Ops Lead
   
2. ✅ **Schedule Phase 2 planning for Jan 15**
   - Rationale: Phase 1 metrics strong, ready to expand scope
   - Decision Owner: Sales Ops Director

3. ✅ **Approve Slack integration scope for Q1**
   - Rationale: Top user request, high value-add
   - Decision Owner: Engineering Manager

---

## Action Items

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Host enablement session for new users | Sales Ops | Jan 13 | In Progress |
| Conduct user interviews for Agent B feedback | AI Ops | Jan 18 | Not Started |
| Develop Agent C variant | AI Ops | Jan 27 | Not Started |
| Phase 2 rollout planning meeting | Sales Ops | Jan 15 | Scheduled |
| Slack integration technical design | Engineering | Jan 20 | Not Started |

---

## Next Week Priorities

1. **Drive Adoption**: Enablement session, manager outreach, success story sharing
2. **User Research**: Qualitative interviews for Agent B improvement
3. **Phase 2 Planning**: Define scope, timeline, and success criteria for SDR team expansion
4. **Product Backlog**: Prioritize feature requests (batch processing, Slack integration, templates)

---

## Appendix: Detailed Metrics

### Daily Trend Data
| Date | Tasks | Active Users | Accuracy % | Satisfaction |
|------|-------|--------------|------------|--------------|
| Jan 8 | 14 | 6 | 85.7% | 4.07 |
| Jan 9 | 11 | 7 | 90.9% | 4.36 |
| Jan 10 | 16 | 8 | 87.5% | 4.19 |
| Jan 11 | 9 | 5 | 88.9% | 4.14 |

### User Satisfaction Distribution
- 5 stars: 48%
- 4 stars: 42%
- 3 stars: 8%
- 2 stars: 2%
- 1 star: 0%

---

**Next Review**: January 18, 2026  
**Document Owner**: AI Ops Lead  
**Distribution**: Sales Operations, Engineering, Sales Leadership
