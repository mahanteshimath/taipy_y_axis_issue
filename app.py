from taipy import Gui

# Data for the heatmap
data = {
    "Temperatures": [
        [17.2, 27.4, 28.6, 21.5],
        [5.6, 15.1, 20.2, 8.1],
        [26.6, 22.8, 21.8, 24.0],
        [22.3, 15.5, 13.4, 19.6],
    ],
    "Countries": ["United Kingdom", "United States", "Brazil", "Germany"],
    "Seasons": ["Winter", "Spring", "Summer", "Autumn"],
}

# Using custom settings for margins
md = """
<|{data}|chart|type=heatmap|z=Temperatures|x=Seasons|y=Countries|
layout={{"margin": {{"l": 150, "r": 10, "b": 50, "t": 10}}}}|height=500|width=700|>
"""

Gui(md).run()
