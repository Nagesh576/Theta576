import pandas as pd
sales_data = {
    "Transaction ID": [101, 102, 103, 104],
    "Customer ID": [1, 2, 3, 2],
    "Amount": [250.50, 150.00, 300.75, 200.00],
    "Date": ["2025-01-10", "2025-01-11", "2025-01-12", "2025-01-13"]
}

# Dictionary for customer data
cust_data = {
    "Customer ID": [1, 2, 3, 4],
    "Customer Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [30, 25, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago","Houston"]
}
#Convert data into DataFrame
sales_df = pd.DataFrame(sales_data)
customer_df = pd.DataFrame(cust_data)

# Display the DataFrames
print("Sales Data:")
print(sales_df)
print("\nCustomer Data:")
print(customer_df)
