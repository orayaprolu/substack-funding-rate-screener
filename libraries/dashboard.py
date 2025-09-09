import pandas as pd
import os

class Dashboard:
    def __init__(self, data):
        self.data = data

    def display(self):
        """Display the funding rate data to console."""
        if self.data is not None and not self.data.empty:
            print(self.data)
        else:
            print("No data available to display.")

    def save_to_csv(self, filename):
        """Save the funding rate data to a CSV file."""
        if self.data is None or self.data.empty:
            print("No data available to save.")
            return

        # Ensure output directory exists
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Create full path to output folder
        output_path = os.path.join(output_dir, filename)
        self.data.to_csv(output_path, index=False)
        print(f"CSV saved to: {output_path}")

    def get_top_assets(self, n=50, sort_by='7 Day Average Funding Rate (Annualized %)'):
        """Get the top N assets sorted by the specified column."""
        if self.data is None or self.data.empty:
            return pd.DataFrame()

        return self.data.nlargest(n, sort_by)

    def filter_by_funding_rate(self, min_rate=None, max_rate=None, column='7 Day Average Funding Rate (Annualized %)'):
        """Filter assets by funding rate range."""
        if self.data is None or self.data.empty:
            return pd.DataFrame()

        filtered_data = self.data.copy()

        if min_rate is not None:
            filtered_data = filtered_data[filtered_data[column] >= min_rate]

        if max_rate is not None:
            filtered_data = filtered_data[filtered_data[column] <= max_rate]

        return filtered_data
