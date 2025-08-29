# ai-alignment-sandbox

Explorations in AI research, interpretability, and alignment. This repo tracks my study sprints and mini projects toward MATS and OpenAI Residency applications.

## What this is

* A clean place to run small experiments
* Notebooks that show thinking, not just results
* Short writeups that tie code to alignment ideas

## Quick start

1. Create a fresh virtual environment
2. `pip install -r requirements.txt`
3. Launch JupyterLab and open the notebooks in the notebooks folder

## Repo layout

* notes
  Day 1 research mindsets and ML lifecycle  
  Day 2 data cleaning and basic checks  
  Day 3 exploratory data analysis and alignment reflection

* data  
  Tiny sample CSVs only. Larger data stays outside the repo with a link to source

* outputs  
  Saved charts or cleaned CSVs that are safe to version

* README.md  
  You are reading it

* requirements.txt  
  Python package list for a reproducible setup

## How to run

1. `jupyter lab`
2. Open `notebooks/day1_research_mindsets.ipynb`
3. Run top to bottom and add your three to five line reflection at the top markdown cell
4. Repeat for Day 2 and Day 3

## Study notes model

At the top of every notebook add one markdown cell with

* Goal for this session
* What I tried
* What worked and what did not
* One link to alignment context
* One open question for tomorrow

## Roadmap next

* Add a simple agent demo that shows wrong optimization and then inspect the decision steps
* Publish two short blog posts drawn from these notebooks
* Record a short walkthrough video of the demo

## Credits

Built by Shreepad as part of a focused transition into frontier AI safety and interpretability
