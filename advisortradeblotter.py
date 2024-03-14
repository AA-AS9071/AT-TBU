import pandas as pd
import streamlit as st

# Function to replace characters in a string
def replace_chars(string):
    string = string.replace('~', ',')
    string = string.replace('+', ',')
    return string

# Function to format dates
def format_date(date):
    if pd.isnull(date):  # Check for missing values
        return ''  # Return an empty string if date is missing
    return pd.to_datetime(date).strftime('%m/%d/%Y')

def main():
    st.title("Trade Blotter Formatting Tool")

    #sidebar
    st.sidebar.title("Group Numbers")
    st.sidebar.text("Octavia: 1")
    st.sidebar.text("Litvak: 2")
    st.sidebar.text("Dakota/Dakore: 3")
    st.sidebar.text("Procyon: 5")
    st.sidebar.text("Miracle Mile: 6")
    st.sidebar.text("KLR: 7")
    st.sidebar.text("Imprint: 9")
    st.sidebar.text("Pallas: 10")
    st.sidebar.text("CVFG: 11")
    st.sidebar.text("Claro: 12")
    st.sidebar.text("Mayflower: 13")
    st.sidebar.text("MDRN: 14")
    st.sidebar.text("Chemistry: 15")
    st.sidebar.text("McNamara: 16")
    st.sidebar.text("Lakeridge: 17")
    st.sidebar.text("Avaii: 18")
    st.sidebar.text("Del-Sette: 19")
    st.sidebar.text("Petra: 20")
    st.sidebar.text("Pacific Point: 21")
    st.sidebar.text("Naviter: 22")
    st.sidebar.text("MGO: 23")
    st.sidebar.text("EverPar: 24")
    st.sidebar.text("Evexia: 25")
    st.sidebar.text("Alpine Hill: 26")
    st.sidebar.text("Stablepoint: 27")
    st.sidebar.text("Balanced Wealth: 28")
    st.sidebar.text("MKT: 29")
    st.sidebar.text("PostRock: 30")
    st.sidebar.text("Advantage Retirement: 31")
    st.sidebar.text("Northstar: 32")
    st.sidebar.text("Round Rock: 33")
    st.sidebar.text("C2C: 34")
    st.sidebar.text("Great Oak: 35")
    st.sidebar.text("Sapient: 36")
    st.sidebar.text("Permanent: 37")
    st.sidebar.text("Meridea: 38")
    st.sidebar.text("True Vision: 39")
    st.sidebar.text("Yarger: 40")
    st.sidebar.text("Impact: 41")
    st.sidebar.text("Relation: 42")


    # File Upload
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])


    st.markdown(""" 
    ### Important Notes
    1. Use the following column headers
        - account number, cusip, ticker, action, quantity, price, trade date 
        - Please note, cusip is optional
    2. Please convert the trade blotter to **.csv** before uploading
    """)


    if uploaded_file is not None:
        # Load and read trade blotter with specified data types
        trade_blotter = pd.read_csv(uploaded_file, dtype={'trade date': str})

        # Group Number input
        group = st.text_input("Group Number", "")

        # Button to process
        if st.button("Process"):
            # Create a new DataFrame with selected columns
            new_data = pd.DataFrame({
                'account number': trade_blotter['account number'].str.replace('-', ''),
                'blank_0': '',
                'cusip': trade_blotter['cusip'] if 'cusip' in trade_blotter.columns else '',
                'blank_1': '',
                'blank_2': '',
                'ticker': trade_blotter['ticker'],
                'blank_4': '',
                'action': trade_blotter['action'].apply(lambda x: 'B' if x == 'buy' else 'S'),
                'quantity': trade_blotter['quantity'].abs().round(3),  # Make quantity absolute and round to 3 decimals
                'blank_3': '',
                'price': trade_blotter['price'].abs().round(2),  # Make price absolute and round to 2 decimals
                'blank_4': '',
                'blank_5': '',
                'trade date': trade_blotter['trade date'].apply(format_date),
                'blank_6': '',
                'blank_7': '',
                'blank_8': '',
                'blank_9': '',
                'group': group,
                'blank_10': '',
                'blank_11': '',
                'blank_12': '',
                'blank_13': '',
                'blank_14': '',
                'blank_15': '',
                'blank_16': '',
                'blank_17': '',
                'blank_18': '',
                'blank_19': '',
                'blank_20': '',
                'blank_21': '',
                'blank_22': '',
                'blank_23': '',
                'blank_24': '',
                'blank_25': '',
                'blank_26': '',
                'blank_27': '',
                'blank_28': '',
                'blank_29': ''
            })

            # Save the DataFrame to a text file with specified naming convention
            output_file_name = f"F02240_FTR_{group}_{pd.Timestamp.now().strftime('%Y%m%d%H%M%S')}.txt"
            new_data.to_csv(output_file_name, sep='|', index=False, header=False)

            # Replace special characters in the output file
            with open(output_file_name, 'r') as file:
                file_data = file.read()
                file_data = replace_chars(file_data)

            with open(output_file_name, 'w') as file:
                file.write(file_data)

            st.success(f"Output file created successfully: {output_file_name}")

if __name__ == "__main__":
    main()
