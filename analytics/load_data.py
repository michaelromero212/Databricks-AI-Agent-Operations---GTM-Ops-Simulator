"""
Data loading and database setup for analytics
Supports both SQLite and DuckDB
"""
import pandas as pd
import duckdb
from pathlib import Path


class DataLoader:
    """Load agent run data into DuckDB for analytics"""
    
    def __init__(self, db_path: str = ":memory:"):
        """
        Initialize data loader
        
        Args:
            db_path: Path to DuckDB database file (use :memory: for in-memory)
        """
        self.db_path = db_path
        self.conn = duckdb.connect(db_path)
        
    def load_csv_to_db(self, csv_path: str, table_name: str = "agent_runs"):
        """
        Load CSV data into database
        
        Args:
            csv_path: Path to CSV file
            table_name: Name of table to create
        """
        # Read CSV
        df = pd.read_csv(csv_path)
        
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Create table
        self.conn.execute(f"""
            CREATE OR REPLACE TABLE {table_name} AS 
            SELECT * FROM df
        """)
        
        print(f"✅ Loaded {len(df)} records into {table_name}")
        return df
    
    def execute_query(self, query: str):
        """
        Execute SQL query and return results as DataFrame
        
        Args:
            query: SQL query string
            
        Returns:
            pandas DataFrame with results
        """
        return self.conn.execute(query).fetchdf()
    
    def get_summary_stats(self):
        """Get basic summary statistics"""
        query = """
        SELECT 
            COUNT(*) as total_runs,
            COUNT(DISTINCT user_id) as unique_users,
            COUNT(DISTINCT task_type) as task_types,
            AVG(resolution_time_seconds) as avg_resolution_time,
            AVG(CASE WHEN user_accepted THEN 1.0 ELSE 0.0 END) * 100 as acceptance_rate,
            AVG(user_rating) as avg_rating,
            AVG(CASE WHEN abstained THEN 1.0 ELSE 0.0 END) * 100 as abstention_rate,
            AVG(CASE WHEN error_occurred THEN 1.0 ELSE 0.0 END) * 100 as error_rate
        FROM agent_runs
        """
        return self.execute_query(query)
    
    def get_metrics_by_version(self):
        """Get KPIs by agent version for A/B comparison"""
        query = """
        SELECT 
            agent_version,
            COUNT(*) as total_tasks,
            AVG(CASE WHEN user_accepted THEN 1.0 ELSE 0.0 END) * 100 as accuracy_pct,
            AVG(user_rating) as avg_satisfaction,
            AVG(resolution_time_seconds) as avg_resolution_time,
            AVG(CASE WHEN error_occurred THEN 1.0 ELSE 0.0 END) * 100 as error_rate,
            AVG(CASE WHEN abstained THEN 1.0 ELSE 0.0 END) * 100 as abstention_rate
        FROM agent_runs
        GROUP BY agent_version
        ORDER BY agent_version
        """
        return self.execute_query(query)
    
    def get_metrics_by_task_type(self):
        """Get KPIs by task type"""
        query = """
        SELECT 
            task_type,
            COUNT(*) as total_tasks,
            AVG(CASE WHEN user_accepted THEN 1.0 ELSE 0.0 END) * 100 as accuracy_pct,
            AVG(user_rating) as avg_satisfaction,
            AVG(resolution_time_seconds) as avg_resolution_time
        FROM agent_runs
        GROUP BY task_type
        ORDER BY total_tasks DESC
        """
        return self.execute_query(query)
    
    def get_daily_trends(self):
        """Get daily trend data"""
        query = """
        SELECT 
            DATE(timestamp) as date,
            COUNT(*) as total_tasks,
            AVG(CASE WHEN user_accepted THEN 1.0 ELSE 0.0 END) * 100 as accuracy_pct,
            AVG(user_rating) as avg_satisfaction,
            COUNT(DISTINCT user_id) as active_users
        FROM agent_runs
        GROUP BY DATE(timestamp)
        ORDER BY date
        """
        return self.execute_query(query)
    
    def close(self):
        """Close database connection"""
        self.conn.close()


def main():
    """Demo the data loader"""
    # Get paths
    data_dir = Path(__file__).parent.parent / "data"
    csv_file = data_dir / "sample_agent_runs.csv"
    
    if not csv_file.exists():
        print(f"❌ Sample data file not found: {csv_file}")
        return
    
    # Load data
    loader = DataLoader(":memory:")
    loader.load_csv_to_db(str(csv_file))
    
    print("\n" + "=" * 70)
    print("📊 OVERALL SUMMARY STATISTICS")
    print("=" * 70)
    summary = loader.get_summary_stats()
    print(summary.to_string(index=False))
    
    print("\n" + "=" * 70)
    print("🔀 A/B TEST COMPARISON (Agent Version)")
    print("=" * 70)
    ab_comparison = loader.get_metrics_by_version()
    print(ab_comparison.to_string(index=False))
    
    print("\n" + "=" * 70)
    print("📋 METRICS BY TASK TYPE")
    print("=" * 70)
    by_task = loader.get_metrics_by_task_type()
    print(by_task.to_string(index=False))
    
    print("\n" + "=" * 70)
    print("📈 DAILY TRENDS")
    print("=" * 70)
    trends = loader.get_daily_trends()
    print(trends.to_string(index=False))
    
    loader.close()
    print("\n✅ Analytics demo complete")


if __name__ == "__main__":
    main()
