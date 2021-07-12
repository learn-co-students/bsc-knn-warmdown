import matplotlib.pyplot as plt
from ipywidgets import Dropdown, Button, VBox, Output
from IPython.display import Markdown, display, clear_output

class PlotPopulation:
    
    def __init__(self, data, indices):
        self.data = data
        self.indices = indices
        cities = self.data.index.tolist()
        self.options = [x[::-1] for x in list(enumerate(cities))]
        self.components()
        
    def components(self):
        
        self.prompt =  Output()
        with self.prompt:
            display(Markdown("### Select a city to plot the population change for the 5 most similar communities!"))

        self.plot_space = Output()
        self.dropdown = Dropdown(options = self.options)

        self.button = Button(description = 'Create Plot!')
        self.button.button_style = 'info'

        def plot_cities(object):
            with self.plot_space:
                clear_output(True)
                neighbors = self.indices[self.dropdown.value]
                self.data.iloc[neighbors].T.plot(figsize=(15,6), lw=3)
                plt.grid()
                plt.show()


        self.button.on_click(plot_cities)

        self.box = VBox([self.prompt, self.dropdown, self.button, self.plot_space])        
        
    def display(self):
        return self.box