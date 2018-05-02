![Force directed graph](force_directed_graph.png)

## Overview
This Python project uses Python3, pandas and NumPy. I chose only to represent emails that have totaled in over 400 email exchanges because otherwise rendering the visualization would take an extremely long time.

## Setup

1. Make Python3 virtual environment (optional)
`python3 -m virtualenv --python=python3 env`

2. Source new virtual environment
`source env/bin/activate`

3. Pip install packages

`pip install pandas`
`pip install numpy`

4. Run houston_data.py to get all the information needed for visualization (houstoncommunity.json)

`python houston_data.py`

5. Run Python server then navigate over to localhost:8000 (or whatever your server's configurations are) to view visualization. Hover over circle to see email address.

`python3 -m http.server`

## My Solutions

*Communities*: this is depicted in the data visualization. The lines between the points indicate that there have been email exchanges between the two email addresses. The shorter the distances are, the more emails have been exchanged.

*Machine Generated Emails*: These are the email addresses that send a lot of emails but don't receive many emails. They can be found in generated.csv after step #4 in the setup process.

*Well-Connected People*: These are the points in the visualization that have many lines connected to them.