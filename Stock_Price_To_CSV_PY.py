import pandas as pd
import json
import requests
from IPython.display import display
import time
import tkinter as tk
import matplotlib.pyplot as plt

def create_url(ticker_symbol, start_date, end_date, api_key):
    
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker_symbol.upper()}/range/1/day/{start_date}/{end_date}?apiKey={api_key}"
    return url

def create_dataframe(url):
    
    # Retrieve data in JSON format
    results = requests.get(url).json()

    # Create Dataframe
    df = pd.DataFrame(results["results"])
    renamed_df = df.rename(columns={'c': 'Close Price', 'h': 'Highest Price',
                                    'l': 'Lowest Price', 'n': 'Number of Transactions',
                                    'o': 'Opening Price', 't': 'Start Date/Time',
                                    'v': 'Trading Volume', 'vw': 'Volume Weighted Average'})

    # calculations
    renamed_df.at[0,"Average Price"] = renamed_df["Volume Weighted Average"].mean()
    renamed_df.at[0,"Highest Overall Price"] = renamed_df['Highest Price'].max()
    renamed_df.at[0,"Average High"] = renamed_df['Highest Price'].mean()
    renamed_df.at[0,"Lowest Overall Price"] = renamed_df['Lowest Price'].min()
    renamed_df.at[0,"Average Low"] = renamed_df['Lowest Price'].mean()

    # Convert time and date
    renamed_df['Start Date/Time']=(pd.to_datetime(renamed_df['Start Date/Time'],unit='ms'))
    return renamed_df

def create_csv(ticker_symbol, start_date, end_date, api_key):
    
    url = create_url(ticker_symbol, start_date, end_date, api_key)
    dataframe = create_dataframe(url)
    display(dataframe)
    dataframe.to_csv(f"{ticker_symbol} Stock prices {start_date} to {end_date}.csv")


def fetch_data():
    
    ticker_symbol = ticker_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    api_key = api_key_entry.get()

    create_csv(ticker_symbol, start_date, end_date, api_key)

def create_plot():
    
    ticker_symbol = ticker_entry.get().upper()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    
    plot_df = pd.read_csv(f'{ticker_symbol} Stock prices {start_date} to {end_date}.csv')
    dates_list = list(plot_df["Start Date/Time"])
    dates_list = list(map(lambda x: x[:10],dates_list))
    highs_list = list(plot_df["Highest Price"])
    lows_list = list(plot_df["Lowest Price"])

    # Plot the first line
    plt.plot(dates_list, highs_list, label='Highs')

    # Plot the second line
    plt.plot(dates_list, lows_list, label='Lows')

    # Add labels and a legend
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{ticker_symbol} Stock prices {start_date} to {end_date}')

    plt.xticks(rotation='vertical')
    plt.legend()

    # Show the plot
    plt.show()


root = tk.Tk()
root.title("Stock Price to CSV")

# Create and place labels and entry widgets for each field
tk.Label(root, text="Ticker Symbol:").grid(row=0, column=0, padx=10, pady=10)
ticker_entry = tk.Entry(root)
ticker_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="End Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)
end_date_entry = tk.Entry(root)
end_date_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="API Key:").grid(row=3, column=0, padx=10, pady=10)
api_key_entry = tk.Entry(root)
api_key_entry.grid(row=3, column=1, padx=10, pady=10)

# Create and place the button
fetch_button = tk.Button(root, text="Generate CSV File", command=fetch_data)
fetch_button.grid(row=4, column=0, columnspan=2, pady=10)

# Createa dna place generate plot button
fetch_button = tk.Button(root, text="Generate Plot", command=create_plot)
fetch_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()




