# What this repository contains
- This repo contains an example project demonstrating how skills can be be used with ADK Agent 2.0
- A Skill is defined inside `skills_app/skills/lucky-color `folder
- This skill when executes, invokes `lucky-color/scripts/find_lucky_color.py` python script
- This skill is used programmatically by ADK Agent 2.0 `(skills_app/agent.py)`

##  How to execute
###  Step 1. Create virtual environment
```
python -m venv .venv
```

###  Step 2. Activate virtual environment
Mac/Linux
```
source .venv/bin/activate         
``` 
Windows
```
.venv\Scripts\activate   
```          

###  Step 3. Install dependencies
```
pip install -r requirements.txt
```

###  Step 4. run
```
adk run skills_app
```
**Prompt**
`Find lucky color of female susane who is 19 years old`

# License or Terms of Use
This project is open-source. However, no part of the source code may be republished, modified, or distributed for commercial or public purposes without giving appropriate credit to the original author.

## GIT REPO URL 
https://github.com/10xroadmap/integrating-skills-with-google-adk-2.0.git 