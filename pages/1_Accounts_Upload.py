
import pandas as pd
import streamlit as st
import csv

st.header("Accounts Upload")

# Function to replace characters in a string
def replace_chars(string):
    string = string.replace('~', ',')
    string = string.replace('+', ',')

    return string

def main():
    #sidebar
    st.sidebar.title("Business Unit and Group #s")
    st.sidebar.text("Octavia Wealth Advisors: 1")
    st.sidebar.text("Litvak: 2")
    st.sidebar.text("Dakota and Dakore: 3")
    st.sidebar.text("Procyon Advisors: 5")
    st.sidebar.text("Miracle Mile Advisors: 6")
    st.sidebar.text("KLR: 7")
    st.sidebar.text("Imprint: 9")
    st.sidebar.text("Pallas Capital Advisors: 10")
    st.sidebar.text("CVFG LLC: 11")
    st.sidebar.text("Claro Advisors: 12")
    st.sidebar.text("Mayflower Financial Advisors: 13")
    st.sidebar.text("MDRN Capital LLC: 14")
    st.sidebar.text("Chemistry Wealth Management LLC: 15")
    st.sidebar.text("McNamara Financial Services: 16")
    st.sidebar.text("Lakeridge Wealth Management: 17")
    st.sidebar.text("Avaii Wealth Management: 18")
    st.sidebar.text("Del-Sette Capital Management: 19")
    st.sidebar.text("Petra Financial: 20")
    st.sidebar.text("Pacific Point: 21")
    st.sidebar.text("Naviter Wealth: 22")
    st.sidebar.text("MGO: 23")
    st.sidebar.text("EverPar Advisors: 24")
    st.sidebar.text("Evexia: 25")
    st.sidebar.text("Alpine Hill: 26")
    st.sidebar.text("StablePoint: 27")
    st.sidebar.text("Balanced Wealth: 28")
    st.sidebar.text("MKT Advisors: 29")
    st.sidebar.text("Postrock Partners: 30")
    st.sidebar.text("Advantage Retirement Group: 31")
    st.sidebar.text("Northstar Advisory Group: 32")
    st.sidebar.text("RoundRock: 33")
    st.sidebar.text("C2C: 34")
    st.sidebar.text("Great Oak: 35")
    st.sidebar.text("Sapient Capital: 36")
    st.sidebar.text("Permanent Capital: 37")
    st.sidebar.text("Maridea Wealth: 38")
    st.sidebar.text("True Vision MN: 39")
    st.sidebar.text("Yarger Wealth: 40")
    st.sidebar.text("Impact Capital Partners: 41")
    st.sidebar.text("Relation Wealth: 42")


    # File Upload
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

     # Group Number input
    group_number = st.text_input("Group Number", "")

    st.markdown("""
    ### Important Notes
    1. For ease, you can make a copy of the "Account Data" sheet from the onboarding spreadsheet
    2. Use the following column header names
        - account number, account name, name of institution, supervised person email, covered, active
    3. Please convert the Account Data sheet to **.csv** before uploading
    """)


    if uploaded_file is not None:
        # Load and read user data with specified data types
        account_data = pd.read_csv(uploaded_file)


        if st.button("Format"):

            pending_review = "N"
            account_status = "Open"
            
            # Create a new DataFrame with selected columns
            new_data = pd.DataFrame({
                'account number': account_data['account number'].str.replace('-', '').replace(',','').replace("'",""),
                'account name': account_data['account name'],
                'account short name ': account_data['account name'][:30], 
                'blank_1': '',
                'name of institution': account_data['name of institution'],
                'blank_3': '',
                'account data source': account_data.apply(lambda row: "None" if row['covered'] == 'N' else 'Direct Feed From Financial Institution', axis=1),
                'supervised person email': account_data['supervised person email'],
                'covered': account_data['covered'],
                'active': account_data['active'],
                'blank_8': '',
                'account status': account_status,
                'pending review': pending_review,
                'blank_11': '',
                'blank_12': '',
                'blank_13': '',
                'blank_14': '',
                'blank_15': '',
                'blank_16': '',
                'blank_17': '',
                'blank_18': ''
            })

            # Save the DataFrame to a text file with specified naming convention
            output_file_name = f"Account_Data{group_number}_{pd.Timestamp.now().strftime('%Y%m%d%H%M%S')}.txt"
            new_data.to_csv(output_file_name, sep='|', index=False, header=False, quoting=csv.QUOTE_NONE)

            # Replace special characters in the output file
            with open(output_file_name, 'r') as file:
                file_data = file.read()
                file_data = replace_chars(file_data)

            with open(output_file_name, 'w') as file:
                file.write(file_data)

            st.success(f"Account Data Formatted Successfully")

            st.download_button(
                label="Download text File",
                data=file_data.encode('utf-8'),
                file_name=output_file_name,
                mime="text/plain"
            )
if __name__ == "__main__":
    main()
