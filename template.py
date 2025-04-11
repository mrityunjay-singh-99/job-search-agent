import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

list_of_files = [
    "agents/__init__.py",
    "agents/interview_agent.py",
    "agents/jobsearch_agent.py",
    "agents/resume_agent.py",
    "utils/__init__.py",
    "utils/job_scraper.py",
    "utils/job_storage.py",
    "utils/resume_keyword_extractor.py",
    "utils/resume_parser.py",
    "utils/serper_api_search.py",
    ".env",
    "requirements.txt",
    "config.py",
    "app.py",
    "ui_utils.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Createing directory; {filedir} for the file:{filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exists.")