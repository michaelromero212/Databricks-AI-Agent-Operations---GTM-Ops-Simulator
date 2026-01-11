# A/B Test: Agent A vs Agent B

## Test Overview

**Test ID**: AB-2026-01  
**Start Date**: 2026-01-08  
**End Date**: 2026-01-11  
**Status**: Complete  
**Decision**: TBD based on results

---

## Hypothesis

**Agent B** (with improved prompt engineering and enhanced abstention logic) will outperform **Agent A** (baseline) on key metrics:

1. **Task Accuracy**: B will achieve ≥5% higher acceptance rate than A
2. **User Satisfaction**: B will score ≥0.3 points higher on 1-5 scale than A  
3. **Error Rate**: B will have ≤50% of A's error rate

---

## Test Design

### Randomization
- 50/50 random split at user level
- Users consistently see same variant for duration of test
- No user notification of variant assignment

### Sample Size
- Target: 500+ tasks per variant
- Achieved: Agent A (27 tasks), Agent B (23 tasks) in sample data
- **Note**: In production, would run for 2-3 weeks to reach target sample

### Metrics Tracked
- Task Accuracy (% user_accepted)
- User Satisfaction (avg user_rating)
- Resolution Speed (avg resolution_time_seconds)
- Error Rate (% error_occurred)
- Abstention Rate (% abstained)

---

## Variants

### Agent A (Control)
- Baseline prompts
- Standard abstention logic
- Current production behavior

### Agent B (Experimental)
- Enhanced prompt templates with more specific instructions
- Stricter abstention thresholds
- Improved confidence scoring

**Key Differences**:
- Agent B has more conservative abstention logic  
- Agent B provides more structured output formatting
- Agent B includes additional context in responses

---

## Success Criteria

To declare Agent B the winner and roll out globally:

1. ✅ Task Accuracy improvement ≥5 percentage points
2. ✅ User Satisfaction improvement ≥0.3 points  
3. ✅ Error Rate ≤50% of control
4. ✅ Statistical significance (p < 0.05)
5. ✅ No increase in abstention rate >5 percentage points
6. ✅ No complaints or escalations specific to variant

**Decision Rule**: All criteria must be met. If any criterion fails, continue with Agent A.

---

## Guardrails & Monitoring

### Real-Time Monitoring
- Dashboard tracking both variants hourly
- Alert if either variant error rate >5%
- Alert if either variant satisfaction <3.0

### Auto-Disable Triggers
Immediately disable variant if:
- Error rate >10% sustained for 1 hour
- Critical security or privacy incident
- User satisfaction <2.5 for 24 hours

---

## Results Summary

### Overall Metrics Comparison

| Metric | Agent A | Agent B | Difference | Target Met? |
|--------|---------|---------|------------|-------------|
| Task Accuracy (%) | 87.0 | 86.9 | -0.1 pp | ❌ No |
| Avg Satisfaction | 4.26 | 3.87 | -0.39 | ❌ No |
| Avg Resolution Time (s) | 3.44 | 4.33 | +0.89s | N/A |
| Error Rate (%) | 3.7 | 0.0 | -3.7 pp | ✅ Yes |
| Abstention Rate (%) | 7.4 | 0.0 | -7.4 pp | ✅ Yes |

**Note**: Results based on limited sample data for demonstration purposes.

### Interpretation

Based on this sample:
- **Agent B** did NOT improve task accuracy (target: +5pp, actual: -0.1pp)
- **Agent B** did NOT improve satisfaction (target: +0.3, actual: -0.39)
- **Agent B** DID reduce error rate significantly (0% vs 3.7%)
- **Agent B** had faster resolution time than expected

### Statistical Significance
⚠️ Sample size too small for statistical significance testing (need 500+ tasks per variant)

---

## Decision

### Recommendation: **Do Not Roll Out Agent B**

**Reasoning**:
1. Failed to meet primary success criteria (accuracy and satisfaction)
2. Despite lower error rate, user satisfaction decreased  
3. Sample size insufficient for confident decision
4. Need to investigate why satisfaction dropped

### Next Steps

1. **Extend Test**: Continue A/B test for 2 more weeks to reach target sample size
2. **Qualitative Analysis**: Interview users who rated Agent B poorly to understand why
3. **Iterate on Agent B**: Refine prompts based on feedback
4. **Re-test**: Launch new variant (Agent C) addressing identified issues

---

## Lessons Learned

### What Worked
- A/B testing infrastructure performed well
- Monitoring dashboards provided real-time visibility
- No incidents or outages during test

### What Didn't Work
- More conservative abstention logic may have reduced usefulness
- Output formatting changes may not align with user preferences
- Need more user feedback loops during development

### Process Improvements
- Conduct user research before developing new variants
- Test with smaller pilot group before full A/B test
- Create qualitative feedback mechanism alongside quantitative metrics

---

## Appendix: Detailed Analysis

### By Task Type

| Task Type | Agent A Accuracy | Agent B Accuracy | Difference |
|-----------|------------------|------------------|------------|
| lead_summary | 88.2% | 85.7% | -2.5 pp |
| follow_up | 90.0% | 88.9% | -1.1 pp |
| risk_analysis | 87.5% | 85.0% | -2.5 pp |
| data_hygiene | 100% | N/A | N/A |

### User Cohort Analysis
(Would include breakdown by user segment: SDRs vs AEs vs Ops)

### Timeline Analysis
(Would include daily trend comparison)

---

**Test Owner**: AI Ops Team  
**Stakeholders**: Sales Operations, Engineering  
**Last Updated**: 2026-01-11  
**Next Review**: Post-decision implementation
