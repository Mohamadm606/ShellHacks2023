from taipy import Gui
import shellhacks2023

# pie chart
data = {
  "label": ["Environmental", "Governance", "Social"],
  "values": [1445674.66, 815312, 72330.4]
}

# Definition of the page
page = """
<|{value}|input|>
<|Search|button|on_action=on_button_action|>

<|{data}|chart|type=pie|values=values|labels=label|>
<h3>Company ESG Risk Factors and their percentages</h3>
"""

value = "Enter Ticker"

def on_button_action(state):
    temp = state.value
    res = shellhacks2023.get_esg_info(temp)
    data["values"] = res[0:3]
    total = res[3]
    Gui(page=page).run(dark_mode=True)

Gui(page=page).run(dark_mode=True)
