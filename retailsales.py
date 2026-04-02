import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Loading the dataset
df = pd.read_csv("Retail_Sales_Data.csv")

# Display first few rows
df.head()

#dataset shaping
df.shape

# check missing values
df.isnull().sum()

# check duplicates
df.duplicated().sum()

# convert datatype to be more structured

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Sales'] = pd.to_numeric(df['Sales'])
df['Quantity'] = pd.to_numeric(df['Quantity'])
df['Unit_Price'] = pd.to_numeric(df['Unit_Price'])

#handle outliers

def remove_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]

df = remove_outliers('Sales')
df = remove_outliers('Quantity')
df = remove_outliers('Unit_Price')

# save cleaned dataset

df.to_csv("Cleaned_Retail_Sales_Data.csv", index=False)

#B. Univariate analysis

# 1. Disbtribution of sales

plt.hist(df['Sales'])
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# 2. Product category frequency

df['Product_Category'].value_counts().plot(kind='bar')
plt.title("Product Category Frequency")
plt.show()

# 3. Age Distribution

plt.hist(df['Age'])
plt.title("Customer Age Distribution")
plt.show()

#4. Payment mode frequency

df['Payment_Mode'].value_counts().plot(kind='bar')
plt.title("Payment Mode Usage")
plt.show()

#C. Bivariate analysis

# 1. Sales VS product strategy
df.groupby('Product_Category')['Sales'].mean().plot(kind='bar')
plt.title("Average Sales by Product Category")
plt.show()

#2. Sales VS Region

df.groupby('Region')['Sales'].sum().plot(kind='bar')
plt.title("Total Sales by Region")
plt.show()

#3. Quantity Vs Unit price

plt.scatter(df['Quantity'], df['Unit_Price'])
plt.xlabel("Quantity")
plt.ylabel("Unit Price")
plt.title("Quantity vs Unit Price")
plt.show()

#4. Gender Vs Average sales

df.groupby('Gender')['Sales'].mean().plot(kind='bar')
plt.title("Average Sales by Gender")
plt.show()

#D. Multivariate Analysis

# 1. Sales by Region & Product Category

pivot = pd.pivot_table(
    df,
    values='Sales',
    index='Region',
    columns='Product_Category',
    aggfunc='sum'
)

sns.heatmap(pivot, annot=True, fmt=".0f")
plt.title("Sales by Region & Product Category")
plt.show()

#2. Age group vs product preference


df['Age_Group'] = pd.cut(df['Age'], bins=[18,25,35,45,55,65])

age_product = pd.crosstab(df['Age_Group'], df['Product_Category'])
age_product.plot(kind='bar', stacked=True)
plt.title("Age Group vs Product Preference")
plt.show()

#3. Monthly sales trend by region

df['Month'] = df['Order_Date'].dt.month

monthly_region = df.groupby(['Month', 'Region'])['Sales'].sum().unstack()

monthly_region.plot()
plt.title("Monthly Sales Trend by Region")
plt.show()

#E. Time-Based Analysis

#1. Monthly sales trend
monthly_sales = df.groupby(df['Order_Date'].dt.month)['Sales'].sum()

monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.show()

#2. yearly sales trend
yearly_sales = df.groupby(df['Order_Date'].dt.year)['Sales'].sum()

yearly_sales.plot()
plt.title("Yearly Sales Trend")
plt.show()


