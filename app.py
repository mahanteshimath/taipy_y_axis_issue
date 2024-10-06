from taipy import Gui

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

# Adjust chart width and height or padding around it
md = """
<|{data}|chart|type=heatmap|z=Temperatures|x=Seasons|y=Countries|width=800|height=600|padding=10px 20px 10px 100px|>
"""

Gui(md).run()

