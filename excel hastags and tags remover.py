import pandas as pd
import re

def remove_links_and_tags(text):
    # Regular expression pattern to match URLs, hashtags, and mentions
    pattern = r'https?://\S+|www\.\S+|#\S+|@\S+'
    return re.sub(pattern, '', text)

def remove_links_and_tags_from_excel(file_path, text_column_name):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Apply remove_links_and_tags function to the specified column
    df[text_column_name] = df[text_column_name].apply(lambda x: remove_links_and_tags(str(x)))
    
    # Save the modified DataFrame back to the Excel file
    output_file_path = file_path.split('.')[0] + '_without_links_and_tags.xlsx'
    df.to_excel(output_file_path, index=False)
    
    return output_file_path

# Example usage:
uploaded_file_path = '/content/hindi data set new_without_links.xlsx'

# Modify this line with the correct column name containing the text
text_column_name = input("Enter the name of the column containing the text: ")

output_file_path = remove_links_and_tags_from_excel(uploaded_file_path, text_column_name)
print(f"Links, hashtags, and mentions removed from '{text_column_name}' column.")
print(f"Output saved to '{output_file_path}'")
