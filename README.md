# Shipment Simulation Calculator
#### Video Demo: <URL HERE>

## Overview
Shipment Simulation Calculator is a Python-based application designed to assist production planners, supply chain managers, and manufacturers in estimating the completion date of a shipment based on various work schedules. By inputting key manufacturing details, users can quickly determine production timelines and optimize scheduling decisions.

This tool provides a user-friendly graphical interface using **Tkinter** and includes a **tkcalendar** widget for date selection. The application also integrates **Pillow** for handling images. Users can enter product-specific details such as the total production quantity, hourly production rate, hours per shift details, and the number of working days per week. The system then calculates the estimated completion date while accounting for weekends in 5-day and 6-day work weeks.

## Features
- **Intuitive GUI**: Built with Tkinter, the interface is clean and easy to navigate and use.
- **Automated Production Timeline Calculation**: Computes daily output, total required workdays, and estimated completion dates.
- **Configurable Work Schedules**: Supports work weeks of 5, 6, or 7 days (Since other companies decides if what work-week schedule would be the best to achieve the target shipment date).
- **Error Handling**: Ensures users input valid numerical values and select appropriate dates using **tkcalendar**.
- **Lightweight & Fast Execution**: The program is designed to be efficient and run smoothly on most systems.

## Project Structure
The project consists of the following key files:

1. **project.py** - This is the main script/code containing the graphical user interface and all core business logic. It manages user inputs, calculations, and the result displays.
2. **logo.jpg** - A background image used to enhance the visual appeal of the application. The developer can modify the **project.py** if they have different logo that needs to be used.
3. **test_project.py** - A Python script/code that employs `pytest` to test the core functions of the application, ensuring reliability and correctness in the calculations.
4. **requirements.txt** - A file listing the dependencies needed to run the project smoothly.
5. **README.md** -  A file consist of the whole explanation of the project.

## Code Breakdown
The project is structured around a central class:

### `ShipmentSimulation` Class
- It manages the GUI layout and event handling.
- Organizes input fields for production parameters.
- Implements the computation of completion dates based on different work schedules.
- It provides real-time updates to ensure users can see instant feedback on their inputs.

### Key Functions
- `compute_daily_output(hourly_output, hours_per_shift)`: This calculates daily production output by multiplying the hourly output to the hours per shift.
- `compute_total_work_days(total_plan, daily_output)`: It determines the number of workdays required to meet production goals. This can calculate by the total production plan divided by the daily output, and if the number has a remainder, the total work days will add extra number.
- `compute_end_date(start_date, total_work_days, work_days_in_a_week)`: Computes the estimated completion date, accounting for the number of working days in a week. It first set a counter for the number of days and using while loop, it iterates through calendar days, counting only valid workdays while skipping weekends based on the specified schedule. If the workweek consists of 5 days, only Monday to Friday are counted; for a 6-day workweek, Monday to Saturday are included, excluding Sundays; and for a 7-day workweek, every day is counted. The function increments the date until the required number of workdays is reached, at which point it returns the final computed end date.

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
3. Input production details and click **Simulate** to calculate the total work days and estimated completion date.

## Design Decisions
The decision to use **Tkinter** for the GUI was based on its simplicity and built-in support in Python, which allows for easy deployment. The **tkcalendar** library was chosen to facilitate intuitive date selection, reducing the likelihood of user input errors. The application’s flexibility in supporting different work schedules (5, 6, or 7-day weeks) ensures adaptability for various manufacturing setups.

Additionally, the decision to include **Pillow** allows for seamless integration of images, specifically, either logo of the company, making the UI visually appealing without significantly impacting performance. The modular approach of the script makes it easy to extend with additional features in the future.

## Future Enhancements
Several improvements are planned for future releases:
- **Exporting Reports**: Allow users to save results in CSV or Excel format.
- **Enhanced UI**: Introduce additional themes and styling options for a better user experience.
- **Multi-language Support**: Provide options for different languages to make the application more accessible to global users.

## Author
**Kharlein Kaye B. Esconde**

This README.md provides a comprehensive guide to the **Shipment Simulation Calculator** project, ensuring clarity and usability for developers and end-users alike. The project is designed with scalability in mind, ensuring future improvements can be implemented seamlessly.

