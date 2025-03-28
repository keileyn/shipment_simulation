# Shipment Simulation
#### Video Demo: <URL HERE>

## Overview
Shipment Simulation is a Python-based application designed to assist production planners, supply chain managers, and manufacturers in estimating the completion date of a shipment based on various work schedules. By inputting key manufacturing details, users can quickly determine production timelines and optimize scheduling decisions.

This tool provides a user-friendly graphical interface using **Tkinter** and includes a **tkcalendar** widget for date selection. The application also integrates **Pillow** for handling images. Users can enter product-specific details such as the total production quantity, hourly production rate, work shift details, and the number of working days per week. The system then calculates the estimated completion date while accounting for weekends in 5-day and 6-day work weeks.

## Features
- **Intuitive GUI**: Built with Tkinter, the interface is clean and easy to navigate.
- **Automated Production Timeline Calculation**: Computes daily output, total required workdays, and estimated completion dates.
- **Configurable Work Schedules**: Supports work weeks of 5, 6, or 7 days.
- **Error Handling**: Ensures users input valid numerical values and select appropriate dates.
- **Lightweight & Fast Execution**: The program is designed to be efficient and run smoothly on most systems.

## Project Structure
The project consists of the following key files:

1. **project.py** - This is the main script containing the graphical user interface and all core business logic. It manages user inputs, calculations, and result displays.
2. **bg.jpg** - A background image used to enhance the visual appeal of the application.
3. **test_project.py** - A Python script that employs `pytest` to test the core functions of the application, ensuring reliability and correctness.
4. **requirements.txt** - A file listing the dependencies needed to run the project smoothly.
5. **README.md** -  A file consist of the whole explanation of the project

## Code Breakdown
The project is structured around a central class:

### `ShipmentSimulation` Class
- Manages the GUI layout and event handling.
- Organizes input fields for production parameters.
- Implements the computation of completion dates based on different work schedules.
- Provides real-time updates to ensure users can see instant feedback on their inputs.

### Key Functions
- `compute_daily_output(hourly_output, hours_per_shift)`: Calculates daily production output.
- `compute_total_work_days(total_plan, daily_output)`: Determines the number of workdays required to meet production goals.
- `compute_end_date(start_date, total_work_days, work_days_in_a_week)`: Computes the estimated completion date, accounting for the number of working days in a week.
- `validate_inputs()`: Ensures all user inputs are properly formatted and within reasonable ranges.

## Installation & Usage
To run the application, follow these steps:

1. Install the necessary dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Execute the main script:
   ```sh
   python project.py
   ```
3. Input production details and click **Simulate** to calculate the estimated completion date.

## Design Decisions
The decision to use Tkinter for the GUI was based on its simplicity and built-in support in Python, which allows for easy deployment. The **tkcalendar** library was chosen to facilitate intuitive date selection, reducing the likelihood of user input errors. The application’s flexibility in supporting different work schedules (5, 6, or 7-day weeks) ensures adaptability for various manufacturing setups.

Additionally, the decision to include **Pillow** allows for seamless integration of images, making the UI visually appealing without significantly impacting performance. The modular approach of the script makes it easy to extend with additional features in the future.

## Future Enhancements
Several improvements are planned for future releases:
- **Exporting Reports**: Allow users to save results in CSV or Excel format.
- **Real-time Data Visualization**: Display graphical representations of production progress.
- **Enhanced UI**: Introduce additional themes and styling options for a better user experience.
- **Cloud Integration**: Enable users to store and retrieve production data from cloud-based platforms.
- **Multi-language Support**: Provide options for different languages to make the application more accessible to global users.

## Author
**Kharlein Kaye B. Esconde**

This README.md provides a comprehensive guide to the **Shipment Simulation** project, ensuring clarity and usability for developers and end-users alike. The project is designed with scalability in mind, ensuring future improvements can be implemented seamlessly.

