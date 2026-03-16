import pandas as pd
import re


def process_csv(input_file):
    op = 'cleaned.csv'
    try:
        # 1. Import: Load the CSV into a DataFrame
        # Pandas automatically handles headers and data types
        df = pd.read_csv(input_file)
        print(f"Successfully imported {input_file}")
        clean_csv(df, op)

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def sanitize_name(name):
    """
    Cleans contact names by removing special characters,
    fixing whitespace, and normalizing to Title Case.
    """
    print("Sanitizing...")
    if pd.isna(name):
        return ""

    # 1. Remove non-alphabetic characters (keep spaces and hyphens)
    # 2. Strip leading/trailing whitespace
    # 3. Reduce multiple spaces to a single space
    clean_name = re.sub(r'[^a-zA-Z\s\-]', '', str(name))
    clean_name = re.sub(r'\s+', ' ', clean_name).strip()

    # Return as Title Case (e.g., "jOHN dOE" -> "John Doe")
    return clean_name.title()


def clean_csv(input_file, output_file, name_column='Contact Name'):
    # Load the dataset
    df = pd.read_csv(input_file)

    # Sanitize the names
    df[name_column] = df[name_column].apply(sanitize_name)

    # Remove duplicates
    # 'subset' defines which columns must match to consider it a duplicate
    # 'keep=first' ensures we retain the first occurrence
    #initial_count = len(df)
    df_cleaned = df.drop_duplicates(subset=[name_column], keep='first')

    df_cleaned.to_csv(output_file, index=False)

if __name__ == "__main__":
    close_csv = "https://docs.google.com/spreadsheets/d/1omg1_ZSCMlTLzwv9tON7pkGU10_rDOeJeKmTi_qtf-k/export?format=csv"
    process_csv(close_csv)
