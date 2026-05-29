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


# Output Schema
class ColorName(BaseModel):
    color: str = Field(description="Color Name")


# Load Skill
lucky_color_skill = load_skill_from_dir(
    Path(__file__).parent / "skills" / "lucky-color"
)

# Create toolset using loaded skills
# UnsafeLocalCodeExecutor :A code executor that
# unsafely execute code in the current local context.
skill_toolset = skill_toolset.SkillToolset(
    skills=[lucky_color_skill],
    code_executor=UnsafeLocalCodeExecutor(),
)
root_agent = LlmAgent(
    model="gemini-2.5-flash-lite",
    name="lucky_agent",
    description="""
    You are a helpful assistant that can guess lucky color using age and gender.
    Return color name only. nothing else.
    """,
    tools=[
        skill_toolset,
    ],
    output_schema=ColorName,  # Binds the agent to the schema
)

"""
How to run
Goto parent folder of 'skills_app' folder
and run
adk run skills_app
Prompt:
Find lucky color of female susane who is 19 years old
"""
