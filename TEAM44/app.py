import tkinter as tk
import requests

def get_ip_info():
    url = "https://ipapi.co/json/"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            ip_info = (
                f"IP Address: {data.get('ip')}\n"
                f"City: {data.get('city')}\n"
                f"Region: {data.get('region')}\n"
                f"Country: {data.get('country_name')}\n"
                f"ISP: {data.get('org')}\n"
                f"ASN: {data.get('asn')}"
            )
            result_label.config(text=ip_info)
        else:
            result_label.config(text="Failed to retrieve IP information.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Create the main application window
app = tk.Tk()
app.title("IP Information")
app.geometry("400x300")  # Set window size
app.configure(bg="#f0f0f0")  # Set background color

# Create a title label
title_label = tk.Label(app, text="IP Information", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Create a button to get IP info
get_info_button = tk.Button(app, text="Get IP Information", command=get_ip_info, 
                             font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
get_info_button.pack(pady=20)

# Create a label to display the results
result_label = tk.Label(app, text="", justify=tk.LEFT, font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()