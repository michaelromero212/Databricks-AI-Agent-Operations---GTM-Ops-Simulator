# Key Performance Indicators (KPIs)

## Document Purpose

This document defines the metrics and KPIs used to monitor AI agent performance, adoption, and business impact in the GTM Operations context.

---

## North Star Metrics

### 1. Task Accuracy
**Definition**: Percentage of agent outputs accepted by users without modification

**Calculation**:
```sql
SELECT 
    COUNT(CASE WHEN user_accepted = TRUE THEN 1 END) * 100.0 / COUNT(*) as accuracy_pct
FROM agent_runs
WHERE task_type IS NOT NULL
```

**Target**: ≥ 85%  
**Review Frequency**: Daily  
**Owner**: AI Ops

---

### 2. Resolution Speed
**Definition**: Median time from user query submission to agent response delivery

**Calculation**:
```sql
SELECT 
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY resolution_time_seconds) as median_resolution_sec
FROM agent_runs
WHERE status = 'completed'
```

**Target**: ≤ 5 seconds  
**Review Frequency**: Daily  
**Owner**: Engineering

---

### 3. User Satisfaction
**Definition**: Average user rating on agent outputs (1-5 scale, where 5 = excellent)

**Calculation**:
```sql
SELECT 
    AVG(user_rating) as avg_satisfaction,
    COUNT(*) as total_ratings
FROM agent_runs
WHERE user_rating IS NOT NULL
```

**Target**: ≥ 4.0  
**Review Frequency**: Weekly  
**Owner**: Sales Ops

---

### 4. Abstention Rate
**Definition**: Percentage of queries where agent correctly escalates to human

**Calculation**:
```sql
SELECT 
    COUNT(CASE WHEN abstained = TRUE THEN 1 END) * 100.0 / COUNT(*) as abstention_pct
FROM agent_runs
```

**Target**: 5% - 15% (too low = risky, too high = not useful)  
**Review Frequency**: Weekly  
**Owner**: AI Ops

---

## Secondary Metrics

### 5. Weekly Active Users
**Definition**: Number of unique users who submitted queries in the past 7 days

**Calculation**:
```sql
SELECT 
    COUNT(DISTINCT user_id) as weekly_active_users
FROM agent_runs
WHERE timestamp >= CURRENT_DATE - INTERVAL '7 days'
```

**Target**: ≥ 70% of target user population  
**Review Frequency**: Weekly  
**Owner**: Sales Ops

---

### 6. Error Rate
**Definition**: Percentage of agent runs that resulted in errors (hallucinations, rule violations, system failures)

**Calculation**:
```sql
SELECT 
    COUNT(CASE WHEN error_occurred = TRUE THEN 1 END) * 100.0 / COUNT(*) as error_pct
FROM agent_runs
```

**Target**: ≤ 2%  
**Review Frequency**: Daily  
**Owner**: Engineering + AI Ops

---

### 7. Task Completion Rate
**Definition**: Percentage of initiated tasks that completed successfully

**Calculation**:
```sql
SELECT 
    COUNT(CASE WHEN status = 'completed' THEN 1 END) * 100.0 / COUNT(*) as completion_pct
FROM agent_runs
```

**Target**: ≥ 95%  
**Review Frequency**: Daily  
**Owner**: Engineering

---

## Business Impact Metrics

### 8. Time Saved per User
**Definition**: Estimated hours saved per user per week based on agent usage

**Calculation**:
```
time_saved_hours = (tasks_completed * avg_manual_time_minutes) / 60
```

**Target**: ≥ 2 hours/user/week  
**Review Frequency**: Monthly  
**Owner**: Sales Ops

---

### 9. Lead Response Time Improvement
**Definition**: Change in median time from lead assignment to first touch (before/after agent)

**Measurement**: Compare pre-agent baseline to post-agent metric  
**Target**: 20% improvement  
**Review Frequency**: Monthly  
**Owner**: Sales Ops

---

### 10. Data Hygiene Score
**Definition**: Percentage of CRM records with complete required fields (influenced by agent suggestions)

**Target**: 15% improvement from baseline  
**Review Frequency**: Monthly  
**Owner**: Sales Ops

---

## A/B Testing Metrics

When comparing Agent A vs Agent B:

### Primary A/B Metrics
1. **Task Accuracy Differential**
   - Agent A accuracy - Agent B accuracy
   - Target: ≥ 5% improvement to declare winner

2. **User Satisfaction Differential**
   - Agent A avg rating - Agent B avg rating
   - Target: ≥ 0.3 point improvement

3. **Error Rate Differential**
   - Agent A error rate - Agent B error rate
   - Target: ≤ 50% of control error rate

### A/B Test Duration
- Minimum: 2 weeks
- Minimum sample size: 500 tasks per variant
- Statistical significance threshold: p < 0.05

---

## Dashboard Requirements

### Real-Time Dashboard (Web App)
Display:
- Current day task accuracy
- Current week active users
- Median resolution speed (24h rolling)
- Error count and rate (24h)
- Top 5 task types by volume

### Weekly Business Review Dashboard
Display:
- Week-over-week trend charts for all North Star metrics
- User satisfaction distribution
- Abstention rate by task type
- A/B test results (if running)
- Top error categories

### Monthly Executive Dashboard
Display:
- Business impact metrics (time saved, response time improvement)
- Adoption trends
- User feedback themes
- ROI estimates
- Roadmap progress

---

## Data Collection & Privacy

### Data Captured per Agent Run
- `run_id` (UUID)
- `timestamp`
- `user_id` (anonymized)
- `task_type` (lead_summary, follow_up, risk_analysis, etc.)
- `agent_version` (A, B, C, etc.)
- `resolution_time_seconds`
- `user_accepted` (boolean)
- `user_rating` (1-5, optional)
- `abstained` (boolean)
- `error_occurred` (boolean)
- `error_type` (if applicable)

### Privacy & Compliance
- No customer PII stored in analytics database
- User IDs anonymized with one-way hash
- Data retention: 90 days for operational data, 1 year for aggregated metrics
- GDPR/CCPA compliance maintained

---

## Alerting Thresholds

Auto-alert when:

| Metric | Threshold | Action |
|--------|-----------|--------|
| Task Accuracy | < 80% for 24h | Page AI Ops on-call |
| Error Rate | > 5% for 1h | Auto-disable agent, page Engineering |
| Resolution Speed | > 10s median for 1h | Investigate performance |
| User Satisfaction | < 3.5 for 7 days | Schedule stakeholder review |
| Abstention Rate | < 3% or > 20% | Review prompt tuning |

---

## Metric Ownership & SLAs

| Metric | Owner | Review SLA | Alert SLA |
|--------|-------|------------|-----------|
| Task Accuracy | AI Ops | Daily | 24h |
| Resolution Speed | Engineering | Daily | 1h |
| User Satisfaction | Sales Ops | Weekly | 7d |
| Error Rate | Engineering + AI Ops | Hourly | 1h |
| Weekly Active Users | Sales Ops | Weekly | 7d |

---

**Document Owner**: AI Ops & Sales Operations  
**Last Updated**: 2026-01-11  
**Review Frequency**: Monthly
