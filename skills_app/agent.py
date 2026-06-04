from google.adk.agents.llm_agent import LlmAgent
from google.adk.skills import load_skill_from_dir
from google.adk.tools import skill_toolset
from pathlib import Path
from google.adk.code_executors.unsafe_local_code_executor import UnsafeLocalCodeExecutor
from pydantic import BaseModel, Field
import warnings
import logging

# Ignore all warnings
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)
# Load Skill
car_sales_skill = load_skill_from_dir(
    Path(__file__).parent / "skills" / "car-sales-generator"
)
# Create toolset using loaded skills
# UnsafeLocalCodeExecutor :A code executor that
# unsafely execute code in the current local context.
skill_toolset = skill_toolset.SkillToolset(
    skills=[car_sales_skill],
    code_executor=UnsafeLocalCodeExecutor(),
)
# gemini-3.5-flash
root_agent = LlmAgent(
    model="gemini-3.1-flash-lite",
    name="car_sales_agent",
    description="car sales Expert",
    instruction="""
    You are a helpful assistant that can generate car sales using year and month.
    You should use tools and skills first.
    """,
    tools=[
        skill_toolset,
    ]
)

"""
Make sure your `.env` file has valid GOOGLE_API_KEY 
Make sure virtual environment is activated.
Please refer to README.ms
How to run
Goto parent folder of 'skills_app' folder
and run
adk run skills_app
Prompt:
Find car sales for the month January 2026
"""
