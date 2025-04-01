# Work by Esconde, Kharlein Kaye B.

# Standard library imports
import os
from datetime import datetime, timedelta

# Tkinter imports
import tkinter as tk
from tkinter import ttk, messagebox

# Third-party library imports
from tkcalendar import DateEntry
from PIL import Image, ImageTk

class ShipmentSimulationCalc:
    def __init__(self):
        
        """Initializes the main window and frame of the GUI."""
        self.main_window = tk.Tk()
        self.main_window.title("Shipment Simulation")
        
        # Set the background color to match the logo image
        self.main_window.configure(bg="#ffffff") 
        # Set the size of the main window not be resizable
        self.main_window.resizable(False, False)
        
        # Command for the close button
        self.closebtn = tk.Menu(self.main_window)
        self.closebtn.add_command(label="Close", command=self.on_closing)
        
        # Command for the logo image
        img_path = os.path.join(os.path.dirname(__file__), "logo.jpg")
        img = Image.open(img_path)
        resized_img = img.resize ((200,200))
        img = ImageTk.PhotoImage(resized_img)
        panel = tk.Label(self.main_window, image=img, bg="#ffffff")
        panel.image = img
        panel.pack(side="top", anchor="n", padx=5, pady=5)


        # This part is for the Main Frame of the GUI
        self.frame = tk.Frame(self.main_window, bg="#ffffff") 
        self.frame.pack()
       
        # Create the GUI components
        self.create_GUI()
    
    def create_GUI(self):
        
        """ This function will create the main GUI window and components"""
        self.create_shipment_info()
        self.create_result_info() 
        self.main_window.protocol("WM_DELETE_WINDOW", self.on_closing) # Command for the close button
        self.main_window.mainloop()
    
    def create_shipment_info(self):
        
        """ This will create the shipment information section in the GUI"""
        # Shipment Information Frame  
        shipment_info_frame = tk.LabelFrame(self.frame, text="Shipment Information:", font=("Arial", 18), bg="#ffffff")
        shipment_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)
        # Product Name Label and Entry (row 0-1, column 0)
        self.product_name_entry = self.create_labels_with_entries(shipment_info_frame, "Product Name:", 0, 0 )
        # Total Production Plan Label and Entry (row 0-1, column 1)
        self.total_plan_entry = self.create_labels_with_entries(shipment_info_frame, "Total Production Plan:", 0, 1, initial_value="0")
        # Target Date of Manufacturing Label and Entry (row 2-3, column 0)
        self.start_date_entry = self.create_labels_with_date_entry(shipment_info_frame, "Target Date of Manufacturing (MM-DD-YYYY):", 2, 0)
        # Hourly Output Label and Entry (row 2-3, column 1)
        self.hourly_output_entry = self.create_labels_with_entries(shipment_info_frame, "Hourly Output (units/hr):", 2, 1, initial_value="0")
        # Hours per Shift Label and Entry (row 4-5, column 0)
        self.hours_per_shift_entry = self.create_labels_with_entries(shipment_info_frame, "Hours per Shift (hrs):", 4, 0, initial_value="0")
        # Days in a Week Label and Entry (row 4-5, column 1)
        self.days_in_week_entry = self.create_labels_with_combobox(shipment_info_frame, "Days in a Week:", 4, 1, ["5", "6", "7"], initial_value="5")
   
        # Simulate Button
        self.simulate_button = tk.Button(shipment_info_frame, text="Simulate", font=("Arial", 12), command=self.run_simulation)
        self.simulate_button.grid(row=6, column=0, columnspan=2, pady=20)
    
    def create_result_info(self):
        
        """ This function will create the result information section in the GUI."""
        # Result Information Frame
        result_info_frame = tk.LabelFrame(self.frame, text="Result Information:", font=("Arial", 18), bg="#ffffff")
        result_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
        # Product Name Label (row 0, column 0)
        self.product_name_label = self.create_labels_only(result_info_frame, "Product Name:", 0, 0)
        # Total Days Label (row 2, column 0)
        self.total_days_label = self.create_labels_only(result_info_frame, "Total Days of Manufacturing:", 2, 0)
        # Completion Date Label (row 4, column 0)
        self.completion_date_label = self.create_labels_only(result_info_frame, "Completion Date:", 4, 0)

    def create_labels_with_entries(self, parent, label_text, row, column, width=20, initial_value=""):
        
        """Standard specufucations in creating labeled entry widgets"""
        label = tk.Label(parent, text = label_text, font = ("Arial", 12), bg="#ffffff")
        label.grid(row=row, column=column, sticky = "w", padx=10, pady=5)
        
        entry_var = tk.StringVar(value=initial_value)  # Set initial value
        entry = tk.Entry(parent, width=width, font=("Arial", 12), textvariable=entry_var, highlightthickness=1, highlightbackground="#949494",highlightcolor="#949494", relief="flat")
        entry.grid(row=row+1, column=column, sticky="w", padx=10, pady=5)
        entry_var.trace_add("write", lambda *args: self.format_number(entry_var))  # Format number on change
        return entry
    
    def format_number(self, entry_var):
       
        """Formats entry input to have commas and ensures numbers only."""
        value = entry_var.get().replace(",", "")  # Remove existing commas
        if value.isdigit():  # Only format if it's a valid number
            formatted_value = f"{int(value):,}"
            entry_var.set(formatted_value)

    def create_labels_with_combobox(self, parent, label_text, row, column, values, width=18, initial_value=None):
       
        """Standard specifications in creating labeled combobox widgets"""
        label = tk.Label(parent, text=label_text, font=("Arial", 12), bg="#ffffff")
        label.grid(row=row, column=column, sticky="w", padx=10, pady=5)
        combobox = ttk.Combobox(parent, values=values, width=width, font=("Arial", 12))
        combobox.grid(row=row+1, column=column, sticky="w", padx=10, pady=5)

        if initial_value:  
            combobox.set(initial_value)

        return combobox
    
    def create_labels_with_date_entry(self, parent, label_text, row, column, width=18):

        """Standard specifications in creating labeled date entry widgets"""
        label = tk.Label(parent, text=label_text, font=("Arial", 12), bg="#ffffff")
        label.grid(row=row, column=column, sticky="w", padx=10, pady=5)
        date_entry = DateEntry(parent, width=width, font=("Arial", 12), date_pattern="mm-dd-yyyy")
        date_entry.grid(row=row+1, column=column, sticky="w", padx=10, pady=5)
        return date_entry

    def create_labels_only(self, parent, label_text, row, column):
        
        """Standard specifications in creating labeled widgets without entry or combobox"""
        label = tk.Label(parent, text=label_text, font=("Arial", 12), bg="#ffffff")
        label.grid(row=row, column=column, sticky="w", padx=10, pady=5)
        return label
             
    def on_closing(self):
        
        """ This function will ask the user if they want to quit the application."""
        if messagebox.askokcancel(title="Quit", message="Do you want to quit?"):
            self.main_window.destroy()

    def run_simulation(self):
        
        """ This function will run the simulation and display the results."""
        
        # Validate the input fields and show error messages if any field is invalid
        errors = [] # Initialize an empty list to store error messages
        
        product_name = self.product_name_entry.get().strip()
        if not product_name:
            errors.append("product name is required.")

        try:
            total_plan = int(self.total_plan_entry.get().replace(",", ""))
            if total_plan <= 0:
                errors.append("total production plan must be greater than zero.")
        except ValueError:
            errors.append("total production plan must be a valid number.")

        start_date_str = self.start_date_entry.get()
        try:
            start_date = datetime.strptime(start_date_str, "%m-%d-%Y")
        except ValueError:
            errors.append("date format must be in 'MM-DD-YYYY'.")

        try:
            hourly_output = int(self.hourly_output_entry.get().replace(",", ""))
            if hourly_output <= 0:
                errors.append("hourly output must be greater than zero.")
        except ValueError:
            errors.append("hourly output must be a valid number.")

        try:
            hours_per_shift = int(self.hours_per_shift_entry.get().replace(",", ""))
            if hours_per_shift <= 0:
                errors.append("hours per shift must be greater than zero.")
        except ValueError:
            errors.append("hours per shift must be a valid number.")

        try:
            work_days_in_a_week = int(self.days_in_week_entry.get())
            if work_days_in_a_week not in [5, 6, 7]:
                errors.append("work days must be 5, 6, or 7.")
        except ValueError:
            errors.append("work days must be a valid number.")

        if errors:
            if len(errors) == 1:
                error_message = errors[0]  # Show the single error message
            else:
                error_message = "please check your input." # Show multiple error messages
            
            self.product_name_label.config(text="")
            self.total_days_label.config(text=f"Error: Invalid input, {error_message}")
            self.completion_date_label.config(text="")
            return

        # If there's no errors, proceed with calculations
        daily_output = compute_daily_output(hourly_output, hours_per_shift)
        total_work_days = compute_total_work_days(total_plan, daily_output)
        completion_date = compute_end_date(start_date, total_work_days, work_days_in_a_week)

        self.product_name_label.config(text=f"Product Name: {product_name}")
        self.total_days_label.config(text=f"Total Days of Manufacturing: {total_work_days}")
        self.completion_date_label.config(text=f"Completion Date: {completion_date.strftime('%B %d, %Y')}")
    

""" This part is the formulas for the shipment simulation calculations"""
def compute_daily_output(hourly_output, hours_per_shift):
    
    """Calculates the daily output based on the hourly output and hours per shift.
    Daily output = hourly output * hours per shift"""
    return hourly_output * hours_per_shift

def compute_total_work_days(total_plan, daily_output):
    
    """Calculates the total work days needed to complete the total plan.
    Total work days = total plan / daily output"""

    total_days = total_plan // daily_output

    # If there's a remainder, add 1 extra to the total days
    if total_plan % daily_output != 0:
        total_days += 1

    return total_days

def compute_end_date(start_date, total_work_days, work_days_in_a_week):
    
    """Calculates the end date based on the start date, total work days, and the work days in a week.
    It will skip the weekends based on the work days in a week (5-day, 6-day, 7-day)."""

    current_date = start_date         
    count_days = 0 # Counter for the number of days

    while count_days < total_work_days: # Loop until the total work days is reached
        
        # Check if the current day is a valid work day (based on the work days in a week: 5-day, 6-day, 7-day)
        if work_days_in_a_week == 5:
            if current_date.weekday() < 5: # Monday to Friday
                count_days += 1
        elif work_days_in_a_week == 6:
            if current_date.weekday() != 6: # Monday to Saturday
                count_days += 1
        elif work_days_in_a_week == 7: # Monday to Sunday
            count_days += 1

        if count_days < total_work_days:
            current_date += timedelta(days=1)

    return current_date

if __name__ =="__main__":
    shipment_simulation = ShipmentSimulationCalc()