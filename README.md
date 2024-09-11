---

# **BarberBot: A Distributed Real-time Automated Inquiry System**

## **Project Overview**

This project was developed to tackle the challenges faced by small barbershops in handling customer inquiries efficiently and using the data to create customized marketing campaigns. By combining an automated inquiry system with a data analytics dashboard, the project allows barbershops to automate customer data collection, analyze customer trends, and create targeted ad campaigns. 

The solution is built to be scalable and distributed using **Apache Kafka**, **MySQL**, **MongoDB**, and **Kubernetes**, and has been successfully deployed in two local barbershops to enhance their marketing efforts.

---

## **Problem Statement**

Barbershops often lack efficient systems to:
- Manage customer inquiries.
- Analyze customer behavior to drive business decisions.
- Launch targeted marketing campaigns based on real data.
- Scale their operations and adapt to increasing demand.

Without a solution, they miss opportunities for customer engagement and business growth.

---

## **Solution**

This system provides:
1. **Automated Customer Inquiry System**: An easy-to-use inquiry form integrated into the shop’s website, capturing essential customer details like name, age, gender, and inquiry type. The data is stored in a central database for easy access.
   
2. **Data Analysis for Targeted Marketing**: The data is analyzed to identify trends and patterns. Based on this analysis, barbershops can launch customized marketing campaigns, promoting relevant services to specific customer groups (e.g., age, gender).

3. **Scalable Distributed Architecture**: Leveraging technologies such as **Apache Kafka**, **MySQL**, **MongoDB**, and **Kubernetes**, the system can scale across multiple barbershops and handle large data volumes.

4. **Visual Analytics Dashboard**: A dashboard visualizes the collected data, helping barbershop owners understand their customer base. They can view metrics such as the age distribution, gender breakdown, and inquiry types.

---

## **Tech Stack & System Architecture**

Here’s an overview of the technologies and how they interact:

### 1. **Customer Inquiry System**
   - **Frontend**: A graphical user interface (GUI) form is built using **Tkinter** (for offline use) and integrated into websites for production environments.
   - **Backend Data Handling**:
     - During prototyping, inquiries are stored in **Excel** files using **OpenPyXL**.
     - In production, the data is stored in a **MySQL** database for long-term storage and easy access.

   **OpenPyXL** is used to:
   - Automatically store the inquiries in an Excel file during the initial phase.
   - Provide a lightweight, easily deployable solution for testing before integrating with the full backend.
   - The library is used to open, modify, and save Excel files efficiently.

   ![GUI PREVIEW](GUI.gif)

### 2. **Automated CSV Generation**
   - The data from inquiries is processed and automatically saved into CSV format using **Pandas** for easy access, allowing barbershop owners to download the data for offline analysis.
   
   ![Automated CSV](CSV.png)

### 3. **Data Streaming & Processing (Apache Kafka)**
   - **Apache Kafka** is used for real-time data streaming between multiple barbershop locations and the central database.
   - Inquiries are submitted via Kafka topics, ensuring the reliable delivery and processing of data for analysis and storage.

### 4. **Database**
   - **MySQL**: All customer inquiries are stored in a MySQL database for long-term storage and retrieval. This provides a scalable and secure solution for managing customer data.
   - **MongoDB**: In case of semi-structured data, such as custom forms or complex inquiries, **MongoDB** is used to store flexible datasets, allowing for a broader range of information capture.

### 5. **Data Analysis & Visualization**
   - **Data Cleaning & Analysis**: **Pandas** and **Seaborn** are used to process the data, clean it, and identify key trends such as the most common inquiries, age demographics, and gender breakdown.
   - **Dashboard**: The data is visualized using **Dash** and **Plotly**, providing barbershop owners with insights into their customer base through interactive graphs and reports.
   
   ![Dashboard PREVIEW](dashboard.gif)

### 6. **Containerization & Scalability**
   - **Kubernetes**: The entire system is containerized and deployed using **Kubernetes** to ensure scalability and reliability. This allows the system to handle increasing traffic and data as more barbershops join the platform.

---

## **Business Impact**

Implementing this system has provided significant benefits to the two local barbershops:
- **Automated Inquiry Processing**: No more manual handling of inquiries. The system automatically logs and processes customer details.
- **Data-Driven Decisions**: The data analysis helps identify trends such as peak age groups and popular services, enabling personalized promotions.
- **Targeted Marketing Campaigns**: By analyzing customer demographics, barbers can send tailored promotions to specific customer segments, driving higher engagement and retention.
- **Increased Efficiency**: The dashboard provides a visual representation of key metrics, helping barbers quickly identify business opportunities.

---

## **Conclusion**

This project showcases how small businesses like barbershops can leverage technology to improve their operations and marketing efforts. By automating customer inquiries and analyzing the data, barbershops can offer personalized services and grow their customer base. With distributed architecture using **Kafka**, **MySQL**, **MongoDB**, and **Kubernetes**, the system is scalable and ready for broader implementation across multiple locations.

---

