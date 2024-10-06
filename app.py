from taipy import Gui 


data = {
    "Temperatures": [[17.2, 27.4, 28.6, 21.5],
                     [5.6, 15.1, 20.2, 8.1],
                     [26.6, 22.8, 21.8, 24.0],
                     [22.3, 15.5, 13.4, 19.6]],
    "Countries": ["United Kingdom United Kingdom United Kingdom United Kingdom United Kingdom United Kingdom", "United States United States", "Brazil", "Germany"],
    "Seasons": ["Winter", "Spring", "Summer", "Autumn"]
}


# Calculate the maximum length of the y-axis labels
max_length = max(len(country) for country in data["Countries"])

dynamic_margin =  (max_length * 10)  # Adjust margin based on label length

layout = {"margin": {"l": dynamic_margin}}

md = "<|{data}|chart|type=heatmap|z=Temperatures|x=Seasons|y=Countries|layout={layout}|>"

Gui(md).run()