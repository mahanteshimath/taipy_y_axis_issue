from taipy import Gui

# Data for the heatmap
data = {
    "Temperatures": [
        [17.2, 27.4, 28.6, 21.5],
        [5.6, 15.1, 20.2, 8.1],
        [26.6, 22.8, 21.8, 24.0],
        [22.3, 15.5, 13.4, 19.6],
    ],
    "Countries": [
        "  United Kingdom United Kingdom", 
        " United States United States", 
        "Brazil", 
        "Germany"
    ],
    "Seasons": ["Winter", "Spring", "Summer", "Autumn"],
}

# Calculate the maximum length of the y-axis labels
max_length = max(len(country) for country in data["Countries"])

# Set a base margin and adjust it based on the maximum length
base_margin = 50  # Base margin
dynamic_margin = base_margin + (max_length * 10)  # Adjust margin based on label length

# Create the Markdown for the heatmap with dynamic layout adjustments
layout = {"margin": {"l": dynamic_margin}}


# Create the Markdown for Taipy
md = f"<|{{data}}|chart|type=heatmap|z=Temperatures|x=Seasons|y=Countries|layout={layout}|>"

# Run the GUI
Gui(md).run()
