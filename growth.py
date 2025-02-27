import streamlit as st
import pandas as pd
import os
from io import BytesIO 


st.set_page_config(page_title == "Data Sweeper", layout = 'wide')

# CSS 

st.mardown(
    """
    <style>
    .stApp{
    background-color: black;
    color: white;
    }
    </style>
    """,
    unsafe_allow_html = True
)

# title and descripition
st.title("🚀Data Sweeper")
st.write ("🌟Transform your file between CSV to Excel formats with built-in data and Visulization!")

# file uploader
uploaded_files = st.file_uploader("Upload Files to CSV or Excel : ", type= ["cvs","xlsx"], accept_multiple_files= True)
if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".cvs":
            df =pd.read_csv(file)
        elif file_ext == "xlsx":
            df =pd.read_excel(file)
        else:
            st.error(f"unsupported file type:   {file_ext}")
            continue

        # file details 
        st.write("Preview the head of the DataFrame")
        st.dataframe(df.head())
        
        # data chleaning options 
        st.subheader("Data Cleaning Options:")

        if st.checkbox("Clean data for {file.name}"):
            coll, col2 = st.columns(2)

            with coll:
                if st.button (f"Remove Duplicates from the file : {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✔️Duplicates Remove!")

                    with col2:
                        if st.button (f"fill missing values for {file.name}"):
                            numeric_cols =df.select_dtypes(includes=['number']).colums
                            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                            st.write("✔️missing value Have been filled")
            st.subheader("🎯 Select Coulumn to convert")
            colums = st.multiselect(f"choose column for {file.name}",df.columns, default=colums)
            df = df[colums]


            # data visualization 
            st.subheader(" 🎀 Data visualization")
            if st.checkbox(f"show visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])



    # Conversion Option
    st.subheader("Conversion Options")
    conversion_type = st.radio(f"convert {file.name} to:" , ["CSV" ,"Excel"], key = file.name )

    if st.button("Convert{file.name}"):
        buffer = BytesIO()
        if conversion_type == "CSV" :
            df.to.csv(buffer ,  index = False)
            file_name = file.name.replace(file_ext, "csv")
            mime_type = "text/csv"

        elif conversion_type == "Excel":
            df.to.do_excel(buffer , index = False)
            file_name = file.name.replace(file_ext, "xlsx")
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        buffer.seek(0)

        st.download_button (
            label= f"Download {file.name} as {conversion_type}" ,
            date = buffer ,
            file_name= file_name ,
            mime = mime_type
        )
        
    st.successc("🎉 All files processed successfully! ✨🎉")  




