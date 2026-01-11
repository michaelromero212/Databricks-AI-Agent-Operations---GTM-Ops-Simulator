"""
FastAPI Web Application for AI Agent Operations Dashboard
"""
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import sys
import csv
from datetime import datetime
from typing import Optional

# Add agent and analytics to path
sys.path.insert(0, str(Path(__file__).parent.parent / "agent"))
sys.path.insert(0, str(Path(__file__).parent.parent / "analytics"))

from agent import GTMAgent
from load_data import DataLoader

app = FastAPI(title="AI Agent Operations Dashboard")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize agent
agent = GTMAgent()

# Initialize data loader
data_file = Path(__file__).parent.parent / "data" / "sample_agent_runs.csv"


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Home page"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    """KPI Dashboard"""
    # Load data
    loader = DataLoader(":memory:")
    
    try:
        loader.load_csv_to_db(str(data_file))
        
        # Get metrics
        summary = loader.get_summary_stats()
        ab_comparison = loader.get_metrics_by_version()
        by_task = loader.get_metrics_by_task_type()
        trends = loader.get_daily_trends()
        
        # Convert to dicts
        summary_dict = summary.to_dict('records')[0] if len(summary) > 0 else {}
        ab_list = ab_comparison.to_dict('records')
        task_list = by_task.to_dict('records')
        trend_list = trends.to_dict('records')
        
        loader.close()
        
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "summary": summary_dict,
            "ab_comparison": ab_list,
            "by_task": task_list,
            "trends": trend_list
        })
    except Exception as e:
        loader.close()
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "error": str(e)
        })


@app.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):
    """File upload page"""
    return templates.TemplateResponse("upload.html", {"request": request})


@app.post("/upload")
async def upload_file(
    request: Request,
    file: UploadFile = File(...),
    task_type: str = Form(...)
):
    """Handle file upload and process with agent"""
    try:
        # Read uploaded file
        contents = await file.read()
        text_content = contents.decode('utf-8')
        
        # Save to uploaded_inputs
        upload_dir = Path(__file__).parent.parent / "data" / "uploaded_inputs"
        upload_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        saved_file = upload_dir / f"{timestamp}_{file.filename}"
        
        with open(saved_file, 'wb') as f:
            f.write(contents)
        
        # Process with agent (simple demonstration)
        result = agent.process_task(
            task_type=task_type,
            user_id="web_user",
            lead_name="Uploaded Lead",
            company_name="From File",
            industry="Unknown",
            source="File Upload",
            additional_context=text_content[:500]  # First 500 chars
        )
        
        return templates.TemplateResponse("upload.html", {
            "request": request,
            "success": True,
            "filename": file.filename,
            "result": result['response'],
            "confidence": result['confidence'],
            "resolution_time": result['resolution_time_seconds']
        })
        
    except Exception as e:
        return templates. TemplateResponse("upload.html", {
            "request": request,
            "error": str(e)
        })


@app.post("/agent/query")
async def agent_query(
    request: Request,
    task_type: str = Form(...),
    lead_name: Optional[str] = Form(None),
    company_name: Optional[str] = Form(None),
    industry: Optional[str] = Form(None),
    source: Optional[str] = Form(None),
    additional_context: Optional[str] = Form(None),
    customer_name: Optional[str] = Form(None),
    interaction_date: Optional[str] = Form(None),
    interaction_type: Optional[str] = Form(None),
    summary: Optional[str] = Form(None),
    deal_stage: Optional[str] = Form(None),
    deal_name: Optional[str] = Form(None),
    last_activity_date: Optional[str] = Form(None),
    engagement_summary: Optional[str] = Form(None),
    stakeholders: Optional[str] = Form(None)
):
    """Process agent query"""
    try:
        # Build kwargs based on task type
        kwargs = {}
        
        if task_type == "lead_summary":
            kwargs = {
                "lead_name": lead_name or "Unknown",
                "company_name": company_name or "Unknown",
                "industry": industry or "Unknown",
                "source": source or "Manual Entry",
                "additional_context": additional_context or "No additional context"
            }
        elif task_type == "follow_up":
            kwargs = {
                "customer_name": customer_name or "Unknown",
                "interaction_date": interaction_date or datetime.now().strftime("%Y-%m-%d"),
                "interaction_type": interaction_type or "General",
                "summary": summary or "No summary provided",
                "deal_stage": deal_stage or "Unknown"
            }
        elif task_type == "risk_analysis":
            kwargs = {
                "deal_name": deal_name or "Unknown Deal",
                "deal_stage": deal_stage or "Unknown",
                "last_activity_date": last_activity_date or datetime.now().strftime("%Y-%m-%d"),
                "engagement_summary": engagement_summary or "No engagement data",
                "stakeholders": stakeholders or "Unknown"
            }
        
        # Process with agent
        result = agent.process_task(
            task_type=task_type,
            user_id="web_user",
            **kwargs
        )
        
        return {
            "success": True,
            "response": result['response'],
            "confidence": result['confidence'],
            "resolution_time": result['resolution_time_seconds'],
            "abstained": result['abstained']
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
