import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
import re
import os


def hours_formatter(x, pos):
    """Custom formatter for y-axis ticks to display hours in 'XhXm' format."""
    hours = int(x)
    minutes = int((x - hours) * 60)
    return f'{hours}h{minutes}m'


def convert_xhxmxs_to_hours(input_string):
    """Converts the time format 'XhXm' into hours

    Args:
        hours (str): String in the 'XhXm' format that needs to be converted, where X is an integer

    Returns:
        float: Hours from the input string
        """
    # Define a regular expression pattern to match the input format
    pattern = r'(\d+)h(\d+)m'

    # Use regular expression to extract hours and minutes
    match = re.match(pattern, input_string)

    if not match:
        # Input format does not match
        return None

    hours = int(match.group(1))
    minutes = int(match.group(2))

    # Convert everything to hours
    total_hours = hours + minutes / 60

    return total_hours


def create_time_chart(group, hours, day, month, year):
    """Creates a bar time chart based on the input group and hours

    Args:
        group (int): The group that the chart will represent.
        hours (str): List with the time spent of each member in the group with the following format:
            XhXm, where X is an integer. Example: 1h30m.
    """
    # Initial verifications
    if group < 1 or group > 5:
        print('That group does not exist')
        return

    # Converting the hours in string format to a float format
    converted_hours = []
    for hour in hours:
        converted_hours.append(convert_xhxmxs_to_hours(hour))

    # Dictionary to make it easier choosing which group the chart will be about.
    # If alterations are made to any of these groups this dictionary must be updated,
    # making sure they remain in alphabetical order.
    groups = {1: ['Ana Rocha', 'André Oliveira', 'Gustavo Alves', 'Jóni Pereira', 'Marta Babau', 'Martim Oliveira'],
              2: ['Catarina Araújo', 'Joana Fernandes', 'João Macedo', 'João Silva', 'Luís Salvador', 'Silas Sequeira'],
              3: ['Beatriz Silva', 'Diogo Simões', 'Francisco Pereira', 'Miguel Fazenda', 'Sara Amaral', 'Tiago Henriques'],
              4: ['Johnny Fernandes', 'Laura Caetano', 'Miguel Leopoldo', 'Rafael Arias', 'Raquel Cardoso', 'Sofia Santos'],
              5: ['Eduardo Ferreira', 'João Pereira', 'Miguel Miranda', 'Pedro Moreira', 'Rodrigo Sá', 'Salomé Monteiro']}

    # Dictionary to get the month from the integer that correlates to it
    months = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june',
              7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}

    # Store the colors for each bar depending on the amount of hours worked.
    # This way we can have dynamic colored charts to better distinguish perfomance
    bar_colors = []
    for hour in converted_hours:
        if hour < 1 or hour > 8:
            bar_colors.append('r')
        elif 1 <= hour <= 3:
            bar_colors.append('y')
        else:
            bar_colors.append('g')

    # Creating the bars.
    # Make sure the hours in the 'hours' variable are in alphabetical order based on the members they belong to.
    plt.bar(groups[group], converted_hours,
            width=0.4, color=bar_colors, edgecolor='k')

    # Creates transparent bars behind every bar to make it easier to compare if the weekly goals have been met
    plt.bar(groups[group], [4] * len(groups[group]),
            width=0.4, alpha=0.5, color=bar_colors)

    # Rotates the names in the x axis so they don't overlap
    plt.xticks(rotation=45)

    # Applies a custom y axis formatter to the chart
    plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(hours_formatter))

    # Ensure labels and bars fit within the figure
    plt.tight_layout()

    # Determine the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the full path for saving the file relative to the script's directory
    save_path = os.path.join(
        script_dir, f'week{day:02d}{months[month]}{year}/group{group}')

    # Create the path if it does not already exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Save the figure
    plt.savefig(f'{save_path}/timespent.png', dpi=300)


# Start point of the script
if __name__ == '__main__':
    # To use the function, change the first parameter to the group you are making the chart about.
    # Make sure the hours in the list are in alphabetical order based on the members they belong to.
    # Then input the date in the next parameters.
    # Example:
    # create_time_chart(4, [1h30m, 2h30, 0h20m, 1h50m, 2h10m, 3h00m], 1, 10, 2023)
    # This would create a chart for group 4 about the week that started in October 1st 2023,
    # where 1h30m is Johnny Fernandes's time spent, 2h30 is Laura Caetano's time spent, etc.
    create_time_chart(1,['10h05m', '13h30m', '5h20m','15h45m','5h45m','1h50m'], 8, 10, 2023)
    
    # 1: ['Ana Rocha', 'André Oliveira', 'Gustavo Alves', 'Jóni Pereira', 'Marta Babau', 'Martim Oliveira'],
    # 2: ['Catarina Araújo', 'Joana Fernandes', 'João Macedo', 'João Silva', 'Luís Salvador', 'Silas Sequeira'],
    # 3: ['Beatriz Silva', 'Diogo Simões', 'Francisco Pereira', 'Miguel Fazenda', 'Sara Amaral', 'Tiago Henriques'],
    # 4: ['Johnny Fernandes', 'Laura Caetano', 'Miguel Leopoldo', 'Rafael Arias', 'Raquel Cardoso', 'Sofia Santos'],
    # 5: ['Eduardo Ferreira', 'João Pereira', 'Miguel Miranda', 'Pedro Moreira', 'Rodrigo Sá', 'Salomé Monteiro']}
