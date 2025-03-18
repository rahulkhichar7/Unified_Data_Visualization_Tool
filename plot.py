import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class UnifiedPlotter:
    def __init__(self):
        self.data = None
        self.x_data = []
        self.y_data = []
        self.y_labels = []
        self.title = ''
        self.x_label = ''
        self.y_label = ''
        self.plot_type = ''
        self.colors = []
        self.line_style = '-'
        self.marker_style = 'o'
        self.plot_types = {
            1: 'line',
            2: 'scatter',
            3: 'bar',
            4: 'histogram',
            5: 'pie',
            6: 'area',
            7: 'box',
            8: 'violin',
            9: 'step',
            10: 'hexbin'
        }
        self.color_options = {
            1: 'red', 2: 'blue', 3: 'green', 4: 'orange', 5: 'purple',
            6: 'pink', 7: 'yellow', 8: 'cyan', 9: 'magenta', 10: 'black'
        }
        self.line_styles = {
            1: '-', 2: '--', 3: '-.', 4: ':', 5: '--.',
            6: '-', 7: 'solid', 8: 'dashed', 9: 'dashdot', 10: 'dotted'
        }
        self.markers = {
            1: 'o', 2: 's', 3: '^', 4: 'd', 5: 'p',
            6: 'x', 7: 'v', 8: '*', 9: '<', 10: '>'
        }

    def get_user_input(self):
        print("Choose data input method:")
        print("1. Fill Data Manually")
        print("2. Generate Random Data")
        print("3. Generate Data in a Range")
        print("4. Load Data from CSV")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            self.fill_data_manually()
        elif choice == '2':
            self.generate_random_data()
        elif choice == '3':
            self.generate_data_in_range()
        elif choice == '4':
            self.load_data_from_csv()

    def fill_data_manually(self):
        while True:
            try:
                x = list(map(float, input("Enter X values (space-separated): ").split()))
                if not x:
                    raise ValueError("X values cannot be empty.")
                self.x_data = x
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

        # Ask for the number of Y datasets first
        while True:
            try:
                num_y_values = int(input("How many Y datasets do you want to enter? "))
                if num_y_values <= 0:
                    raise ValueError("Number of Y datasets must be greater than zero.")
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

        for i in range(num_y_values):
            while True:
                try:
                    y_label = input(f"Enter label for Y{i + 1}: ")
                    y_data = list(map(float, input(f"Enter values for {y_label} (space-separated): ").split()))
                    if len(y_data) != len(self.x_data):
                        raise ValueError(f"Length of {y_label} must be equal to the length of X.")
                    self.y_data.append(y_data)
                    self.y_labels.append(y_label)
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")

    def generate_random_data(self):
        while True:
            try:
                num_y_values = int(input("How many Y datasets do you want to generate? "))
                if num_y_values <= 0:
                    raise ValueError("Number of Y datasets must be greater than zero.")
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

        while True:
            try:
                x_length = int(input("Enter the length of X data: "))
                if x_length <= 0:
                    raise ValueError("Length must be greater than zero.")
                self.x_data = np.linspace(0, 10, x_length)
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

        for i in range(num_y_values):
            while True:
                try:
                    y_label = f"Y{i + 1}"
                    y_data = np.random.rand(x_length) * 10
                    self.y_data.append(y_data)
                    self.y_labels.append(y_label)
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")

    def generate_data_in_range(self):
        while True:
            try:
                start_x = float(input("Enter the start for X: "))
                distance_x = float(input("Enter the distance between two X values: "))
                x_length = int(input("Enter the length of X data: "))
                if x_length <= 0:
                    raise ValueError("Length must be greater than zero.")
                self.x_data = np.arange(start_x, start_x + distance_x * x_length, distance_x)
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

        while True:
            try:
                num_y_values = int(input("How many Y datasets do you want to enter? "))
                if num_y_values <= 0:
                    raise ValueError("Number of Y datasets must be greater than zero.")
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

        for i in range(num_y_values):
            while True:
                try:
                    y_label = input(f"Enter label for Y{i + 1}: ")
                    start_y = float(input(f"Enter the start for {y_label}: "))
                    distance_y = float(input(f"Enter the distance between two {y_label} values: "))
                    y_data = start_y + distance_y * np.arange(x_length)
                    self.y_data.append(y_data)
                    self.y_labels.append(y_label)
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")

    def load_data_from_csv(self):
        while True:
            try:
                file_path = input("Enter CSV file path: ")
                data = pd.read_csv(file_path)
                self.x_data = data.iloc[:, 0].tolist()
                self.y_data = [data.iloc[:, i].tolist() for i in range(1, len(data.columns))]
                self.y_labels = [f"Y{i + 1}" for i in range(len(self.y_data))]
                break
            except Exception as e:
                print(f"Error: {e}. Please try again.")

    def choose_plot_type(self):
        while True:
            try:
                print("Choose a plot type by entering the corresponding number:")
                for key, value in self.plot_types.items():
                    print(f"{key}: {value}")
                plot_choice = int(input("Enter the number corresponding to your plot type: "))
                self.plot_type = self.plot_types[plot_choice]
                break
            except (KeyError, ValueError):
                print("Invalid selection. Please try again.")

    def input_styles(self):
        while True:
            try:
                print("Choose line styles:")
                for key, value in self.line_styles.items():
                    print(f"{key}: {value}")
                line_choice = int(input("Enter the number corresponding to your line style: "))
                self.line_style = self.line_styles[line_choice]
                break
            except (KeyError, ValueError):
                print("Invalid line style selection. Please try again.")

        while True:
            try:
                print("Choose markers:")
                for key, value in self.markers.items():
                    print(f"{key}: {value}")
                marker_choice = int(input("Enter the number corresponding to your marker style: "))
                self.marker_style = self.markers[marker_choice]
                break
            except (KeyError, ValueError):
                print("Invalid marker style selection. Please try again.")

    def input_colors(self):
        while True:
            try:
                print("Choose colors for Y datasets by entering the corresponding numbers:")
                for key, value in self.color_options.items():
                    print(f"{key}: {value}")
                if len(self.y_data) > 1:
                    color_choices = list(map(int, input(f"Enter numbers for {len(self.y_data)} colors (space-separated): ").split()))
                    self.colors = [self.color_options[c] for c in color_choices if c in self.color_options]
                else:
                    color_choice = int(input("Enter a number for the color of Y dataset: "))
                    self.colors = [self.color_options[color_choice]]
                break
            except (KeyError, ValueError):
                print("Invalid color selection. Please try again.")

    def input_labels(self):
        for i in range(len(self.y_data)):
            while True:
                try:
                    label = input(f"Enter label for Y{i + 1} data: ")
                    self.y_labels[i] = label
                    break
                except ValueError:
                    print("Invalid label. Please try again.")
                    
        self.title = input("Enter title for the plot: ")
        self.x_label = input("Enter label for X axis: ")
        self.y_label = input("Enter label for Y axis: ")

    def plot(self):
        plt.figure(figsize=(10, 6))
        if self.plot_type == 'line':
            for i, y in enumerate(self.y_data):
                plt.plot(self.x_data, y, linestyle=self.line_style, marker=self.marker_style, color=self.colors[i], label=self.y_labels[i])
        elif self.plot_type == 'scatter':
            for i, y in enumerate(self.y_data):
                plt.scatter(self.x_data, y, color=self.colors[i], label=self.y_labels[i])
        elif self.plot_type == 'bar':
            width = 0.8 / len(self.y_data)
            for i, y in enumerate(self.y_data):
                plt.bar(np.array(self.x_data) + i * width, y, width=width, color=self.colors[i], label=self.y_labels[i])
        elif self.plot_type == 'histogram':
            for i, y in enumerate(self.y_data):
                plt.hist(y, bins=10, color=self.colors[i], alpha=0.5, label=self.y_labels[i])
        elif self.plot_type == 'pie':
            for i, y in enumerate(self.y_data):
                plt.pie(y, labels=self.y_labels, autopct='%1.1f%%')
                plt.title(self.title)
                plt.axis('equal')
        elif self.plot_type == 'area':
            for i, y in enumerate(self.y_data):
                plt.fill_between(self.x_data, y, color=self.colors[i], label=self.y_labels[i], alpha=0.5)
        elif self.plot_type == 'box':
            plt.boxplot(self.y_data, labels=self.y_labels)
        elif self.plot_type == 'violin':
            plt.violinplot(self.y_data, showmeans=True)
        elif self.plot_type == 'step':
            for i, y in enumerate(self.y_data):
                plt.step(self.x_data, y, where='mid', color=self.colors[i], label=self.y_labels[i])
        elif self.plot_type == 'hexbin':
            plt.hexbin(self.x_data, self.y_data[0], gridsize=30, cmap='Blues')
            plt.colorbar(label='Counts')

        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.legend()
        plt.grid()
        plt.show()

    def run(self):
        self.get_user_input()
        self.choose_plot_type()
        self.input_styles()
        self.input_colors()
        self.input_labels()
        self.plot()

if __name__ == '__main__':
    plotter = UnifiedPlotter()
    plotter.run()
