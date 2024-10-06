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

# Custom CSS to apply padding to the chart
css = """
<style>
    .taipy-chart {
        padding-left: 100px;  /* Increase left padding to prevent y-axis labels from being cut off */
    }
</style>
"""

# Heatmap configuration with custom CSS for better label visibility
md = f"""
{css}
<|{{data}}|chart|type=heatmap|z=Temperatures|x=Seasons|y=Countries|height=500|width=700|>
"""

# Run the GUI
Gui(md).run()
