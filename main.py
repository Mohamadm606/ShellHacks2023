from taipy import Gui
import pandas as pd
import getData

def get_data(path_to_csv: str):
    # pandas.read_csv() returns a pd.DataFrame
    dataset = pd.read_csv(path_to_csv)
    dataset["Date"] = pd.to_datetime(dataset["Date"])
    return dataset

# Read the dataframe

path_to_csv = "dataset.csv"
dataset = get_data(path_to_csv)

value = "Search company"

# Initial value
n_week = 10
dataset_week = dataset[dataset["Date"].dt.isocalendar().week == n_week]

# pie chart
data = {
  "Country": ["Apple","Micosoft",...,"Meta"],
  "Area": [1445674.66,815312,...,72330.4]
}

num = getData.get_esg_info()


# Definition of the page
page = """
# Search your stock

<|{value}|input|> <|Search|button|>

Week number: *<|{n_week}|>*

Interact with this slider to change the week number:

<|{n_week}|slider|min=1|max=52|>

## Dataset:

Display the last three months of data:

<|{dataset_week}|chart|type=bar|x=Date|y=Value|>

<|{dataset}|table|width=100%|>

Dataset in Pie chart:

<|{data}|chart|type=pie|values=Area|labels=Country|>

"""
# on_change is the function that is called when any variable is changed
def on_change(state, var_name: str, var_value):
    if var_name == "n_week":
        # Update the dataset when the slider is moved
        state.dataset_week = dataset[dataset["Date"].dt.isocalendar().week == var_value]

# Create a Gui object with our page content
Gui(page=page).run(dark_mode=False)
