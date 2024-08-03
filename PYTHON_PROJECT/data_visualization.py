import matplotlib.pyplot as plt
import streamlit as st
from exception_handling import handle_exception
import pandas as pd
import base64


def visualize_data(data):

    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)
    set_background("C:\\Users\\kohinoor1\\Pictures\\OIP.jpg")


    
    
    st.sidebar.title("_Milk Quality Analysis:_")
    st.sidebar.write("----------------------------------------------")
    try:
    
        st.subheader("_Analysis of Milk Quality:_")
        st.sidebar.subheader("_Select columns :_")
        Choice=st.sidebar.selectbox('_Columns_',data.columns,index=0)
        st.sidebar.write("----------------------------------------------")
    
        if (Choice=="pH"):
            st.subheader("_pH:_")
            st.write("_The pH of milk is a critical parameter in milk quality analysis, providing valuable information about its freshness, safety, and overall quality. The pH scale, which ranges from 0 to 14, measures the acidity or alkalinity of a substance, with 7 being neutral. For milk, the normal pH range is typically between 6.5 and 6.7._")
        elif(Choice=="Temprature"):
            st.subheader("_Temprature:_")
            st.write("_Temperature plays a pivotal role in milk quality analysis, significantly influencing its safety, shelf life, and overall quality. Proper temperature control is crucial at every stage of milk production, from milking to transportation, storage, and processing._ ")
        elif(Choice=="Taste"):
            st.subheader("_Taste:_")
            st.write("_Taste is a crucial aspect of milk quality analysis, influencing consumer preference and satisfaction. It reflects the sensory experience of consuming milk and is indicative of its freshness, composition, and overall quality._")
        elif(Choice=="Odor"):
            st.subheader("_Odor:_")
            st.write("_Odor is a critical aspect of milk quality analysis, playing a significant role in determining freshness, safety, and overall consumer acceptability. The odor of milk is a sensory indicator that reflects its condition and composition, providing valuable insights into potential contamination, spoilage, or processing issues._")
        elif(Choice=="Turbidity"):
            st.subheader("_Turbidity:_")
            st.write("_Turbidity is an important parameter in milk quality analysis that refers to the cloudiness or opacity of milk caused by suspended particles or colloidal matter. It is a critical aspect of assessing milk cleanliness, processing efficiency, and product quality._")
        elif(Choice=="Colour"):
            st.subheader("_Colour:_")
            st.write("_Color is an important attribute in milk quality analysis, influencing consumer perception, product differentiation, and overall marketability of dairy products. The color of milk can vary based on factors such as breed of cow, diet, processing methods, and storage conditions. Understanding and controlling milk color is essential for ensuring product consistency, meeting consumer expectations, and complying with industry standards._")
        elif(Choice=="Grade"):
            st.subheader("_Grade:_")
            st.write("_In the context of milk quality analysis, grade refers to the classification or rating system used to assess the quality and attributes of milk. Grades are typically assigned based on specific criteria such as composition, cleanliness, and safety standards. These grading systems play a crucial role in determining the market value, regulatory compliance, and consumer confidence in milk and dairy products._")
        else:
            st.subheader("_Fat:_")
            st.write("_Fat content is a fundamental component of milk quality analysis, influencing its nutritional value, taste, texture, and suitability for various dairy products. Understanding and monitoring fat content is essential for dairy producers, processors, and consumers alike._")
        
        
        
        
        st.write("#### _1-Histogram of Milk Quality_")
        plt.figure(figsize=(10, 5))
        plt.hist(data[Choice], bins=10, color='lightblue', edgecolor='black')
        plt.title('Histogram of Milk Quality')
        plt.xlabel('Quality')
        plt.ylabel('Frequency')
        st.pyplot(plt)

        
        
        st.write("#### _2-Scatter Plot of Milk Quality_")
        plt.figure(figsize=(10, 5))
        plt.scatter(data[Choice],data[Choice] )
        plt.title('Scatter Plot of Milk Quality')
        plt.xlabel('Quality')
        plt.ylabel('Frequency')
        st.pyplot(plt)

        
        
        st.write("#### _3-Bar Plot of Milk Quality_")
        plt.figure(figsize=(10, 5))
        plt.bar(data[Choice],data[Choice] )
        plt.title('Bar Plot of Milk Quality')
        plt.xlabel('Quality')
        plt.ylabel('Frequency')
        st.pyplot(plt)

        
        
        st.write("#### _4-Pie Plot of Milk Quality_")
        plt.figure(figsize=[8,8])
        plt.pie(data[Choice].head(30).value_counts().values,
        labels=data[Choice].head(30).value_counts().index,
        colors=['lightblue','blue','#87CEEB'],
        autopct='%1.2f%%')
        st.pyplot(plt)
        st.write("-----------------------------------------------")
        st.write("-----------------------------------------------")


        
        st.success("Summary file created successfully!")
        st.write("_Click Button to generate summery.txt_")
        file=pd.read_csv('summary.txt')
        if st.button("Summery.txt:"):
            st.write(file)
        st.write("-----------------------------------------------")
        st.write("-----------------------------------------------")

        
        
        st.subheader("_Conclusion:_")
        st.write("_In this milk quality analysis project, we successfully implemented and demonstrated various key processes including data cleaning, file handling, exception handling, and data visualization using Streamlit._")
        st.write("_1-Data Cleaning:We thoroughly cleaned the dataset to remove any inconsistencies, missing values, and outliers._")
        st.write("_2-File Handling:Efficient file handling techniques were employed to manage and process large datasets seamlessly._")
        st.write("_3-Exception Handling:Comprehensive exception handling mechanisms were incorporated to manage potential errors during data processing and analysis._")
        st.write("_4-Data Visualization:Utilizing Streamlit, we created interactive and dynamic visualizations to present the analysis results._")

        st.write("-----------------------------------------------")
        st.write("-----------------------------------------------")

   
   
   
    except Exception as e:
        handle_exception(e)


