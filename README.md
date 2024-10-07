This issue can be solved with work arround as is not issue in taipy here complete example

Function that accepts any data along with the x, y, and z axis labels. Here is the modified code:

```python
from taipy import Gui

def create_heatmap(data, x_axis, y_axis, z_axis):
    """
    Create and display a heatmap using the provided data and axis labels.

    Parameters:
    - data (dict): A dictionary containing the data for the heatmap.
    - x_axis (str): The key in the data dictionary for the x-axis labels.
    - y_axis (str): The key in the data dictionary for the y-axis labels.
    - z_axis (str): The key in the data dictionary for the z-axis values.
    """
    # Calculate the maximum length of the y-axis labels
    max_length = max(len(label) for label in data[y_axis])

    # Set a dynamic margin based on the maximum length of the y-axis labels
    dynamic_margin = max_length * 10  # Adjust margin based on label length

    # Define the layout with the dynamic margin
    layout = {"margin": {"l": dynamic_margin}}

    # Create the markdown string for the heatmap chart
    md = f"<|{{data}}|chart|type=heatmap|z={z_axis}|x={x_axis}|y={y_axis}|layout={{layout}}|>"

    # Initialize and run the GUI with the defined markdown string
    Gui(md).run()

# Example usage
data = {
    "Temperatures": [
        [17.2, 27.4, 28.6, 21.5],  # Temperatures for the United Kingdom
        [5.6, 15.1, 20.2, 8.1],    # Temperatures for the United States
        [26.6, 22.8, 21.8, 24.0],  # Temperatures for Brazil
        [22.3, 15.5, 13.4, 19.6]   # Temperatures for Germany
    ],
    "Countries": [
        "United Kingdom United Kingdom United Kingdom United Kingdom United Kingdom United Kingdom", 
        "United States United States", 
        "Brazil", 
        "Germany"
    ],
    "Seasons": ["Winter", "Spring", "Summer", "Autumn"]
}

# Call the function with the example data
create_heatmap(data, x_axis="Seasons", y_axis="Countries", z_axis="Temperatures")
```

### Explanation of the Function:

1. **Function Definition**:
   - `def create_heatmap(data, x_axis, y_axis, z_axis):`: This defines a function named `create_heatmap` that takes four parameters: `data`, `x_axis`, `y_axis`, and `z_axis`.

2. **Calculating the Maximum Length of the y-axis Labels**:
   - `max_length = max(len(label) for label in data[y_axis])`: This line calculates the maximum length of the labels for the y-axis.

3. **Setting a Dynamic Margin**:
   - `dynamic_margin = max_length * 10`: This line sets a dynamic margin for the layout based on the length of the longest y-axis label.

4. **Defining the Layout**:
   - `layout = {"margin": {"l": dynamic_margin}}`: This line creates a layout dictionary with a left margin (`"l"`) set to the dynamically calculated margin.

5. **Creating the Markdown String for the Heatmap Chart**:
   - `md = f"<|{{data}}|chart|type=heatmap|z={z_axis}|x={x_axis}|y={y_axis}|layout={{layout}}|>"`: This line creates a markdown string that defines a heatmap chart using the provided data and axis labels.

6. **Running the GUI**:
   - `Gui(md).run()`: This line initializes and runs the GUI with the defined markdown string, displaying the heatmap chart.

### Example Usage:

The example usage demonstrates how to call the `create_heatmap` function with a sample data dictionary and specify the keys for the x, y, and z axes. This makes the function flexible and reusable for different datasets and axis configurations.




Example :

![image](https://github.com/user-attachments/assets/8a262f61-2088-4c2a-8229-170750ad5f59)
