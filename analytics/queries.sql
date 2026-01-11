-- Overall Summary Statistics
-- Total runs, unique users, average metrics
SELECT 
    COUNT(*) as total_runs,
    COUNT(DISTINCT user_id) as unique_users,
    COUNT(DISTINCT task_type) as task_types,
    ROUND(AVG(resolution_time_seconds), 2) as avg_resolution_time_sec,
    ROUND(AVG(CASE WHEN user_accepted THEN 1.0 ELSE 0.0 END) * 100, 1) as task_accuracy_pct,
    ROUND(AVG(user_rating), 2) as avg_user_satisfaction,
    ROUND(AVG(CASE WHEN abstained THEN 1.0 ELSE 0.0 END) * 100, 1) as abstention_rate_pct,
    ROUND(AVG(CASE WHEN error_occurred THEN 1.0 ELSE 0.0 END) * 100, 1) as error_rate_pct
FROM agent_runs;

-- A/B Test Comparison by Agent Version
-- Critical for rollout decisions
SELECT 
    agent_version,
    COUNT(*) as sample_size,
    ROUND(AVG(CASE WHEN user_accepted THEN 1.0 ELSE 0.0 END) * 100, 1) as accuracy_pct,
    ROUND(AVG(user_rating), 2) as avg_satisfaction,
    ROUND(AVG(resolution_time_seconds), 2) as avg_resolution_time_sec,
    ROUND(AVG(CASE WHEN error_occurred THEN 1.0 ELSE 0.0 END) * 100, 1) as error_rate_pct,
    ROUND(AVG(CASE WHEN abstained THEN 1.0 ELSE 0.0 END) * 100, 1) as abstention_rate_pct
FROM agent_runs
GROUP BY agent_version
ORDER BY agent_version;

-- Performance by Task Type
-- Identify which tasks perform best/worst
SELECT 
    task_type,
    COUNT(*) as total_tasks,
    ROUND(AVG(CASE WHEN user_accepted THEN 1.0 ELSE 0.0 END) * 100, 1) as accuracy_pct,
    ROUND(AVG(user_rating), 2) as avg_satisfaction,
    ROUND(AVG(resolution_time_seconds), 2) as avg_resolution_time_sec,
    ROUND(AVG(CASE WHEN abstained THEN 1.0 ELSE 0.0 END) * 100, 1) as abstention_rate_pct
FROM agent_runs
GROUP BY task_type
ORDER BY total_tasks DESC;

-- Daily Trend Analysis
-- Track KPIs over time
SELECT 
    DATE(timestamp) as date,
    COUNT(*) as total_tasks,
    COUNT(DISTINCT user_id) as active_users,
    ROUND(AVG(CASE WHEN user_accepted THEN 1.0 ELSE 0.0 END) * 100, 1) as accuracy_pct,
    ROUND(AVG(user_rating), 2) as avg_satisfaction,
    ROUND(AVG(resolution_time_seconds), 2) as avg_resolution_time_sec
FROM agent_runs
GROUP BY DATE(timestamp)
ORDER BY date;

-- User Engagement Analysis
-- Identify power users and adoption patterns
SELECT 
    user_id,
    COUNT(*) as total_tasks,
    ROUND(AVG(CASE WHEN user_accepted THEN 1.0 ELSE 0.0 END) * 100, 1) as acceptance_rate_pct,
    ROUND(AVG(user_rating), 2) as avg_rating,
    MIN(timestamp) as first_use,
    MAX(timestamp) as last_use
FROM agent_runs
WHERE user_rating IS NOT NULL
GROUP BY user_id
ORDER BY total_tasks DESC
LIMIT 10;

-- Error Analysis
-- Identify failure patterns
SELECT 
    error_type,
    COUNT(*) as error_count,
    task_type,
    agent_version
FROM agent_runs
WHERE error_occurred = true
GROUP BY error_type, task_type, agent_version
ORDER BY error_count DESC;

-- Abstention Analysis
-- Understand when agent escalates
SELECT 
    task_type,
    agent_version,
    COUNT(*) as total_tasks,
    SUM(CASE WHEN abstained THEN 1 ELSE 0 END) as abstained_count,
    ROUND(AVG(CASE WHEN abstained THEN 1.0 ELSE 0.0 END) * 100, 1) as abstention_rate_pct
FROM agent_runs
GROUP BY task_type, agent_version
ORDER BY abstention_rate_pct DESC;

-- Weekly Active Users
-- Adoption metric
SELECT 
    EXTRACT(WEEK FROM timestamp) as week_number,
    EXTRACT(YEAR FROM timestamp) as year,
    COUNT(DISTINCT user_id) as weekly_active_users,
    COUNT(*) as total_tasks
FROM agent_runs
WHERE timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY EXTRACT(WEEK FROM timestamp), EXTRACT(YEAR FROM timestamp)
ORDER BY year, week_number;

-- Satisfaction Distribution
-- Understand rating patterns
SELECT 
    user_rating,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) as percentage
FROM agent_runs
WHERE user_rating IS NOT NULL
GROUP BY user_rating
ORDER BY user_rating DESC;

-- Resolution Time Percentiles
-- Performance SLA tracking
SELECT 
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY resolution_time_seconds), 2) as p50_median,
    ROUND(PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY resolution_time_seconds), 2) as p75,
    ROUND(PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY resolution_time_seconds), 2) as p90,
    ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY resolution_time_seconds), 2) as p95,
    ROUND(MAX(resolution_time_seconds), 2) as max_time
FROM agent_runs;
