![image](https://github.com/RPerottoni/Health_Insurance_Cross_Sell/blob/main/reports/figures/Screenshot_20230206_182309.png)

# Health_Insurance_Cross_Sell

#### This project was made by Ricardo Perottoni.

# 1. Business Problem.

Insurance All is a company that provides health insurance to its customers and the product team is analyzing the possibility of offering its insured a new product: A car insurance.

Just like the health insurance, the customers of this new car insurance plan need to pay an annual fee to Insurance All to receive an insured value from the company, intended for the costs of an eventual accident or damage to the vehicle.

Insurance All conducted a survey with approximately 380,000 customers about their interest in joining a new car insurance product last year. All customers demonstrated interest or not in acquiring car insurance and these answers were saved in a database along with other customer attributes.

The product team selected 127,000 new customers who did not respond to the survey to participate in a campaign, in which they will receive the offer of the new car insurance product. The offer will be made by the sales team through phone calls.

However, the sales team has a capacity to make 20,000 calls within the campaign period.

In this context, you have been hired as a Data Science consultant to build a model that predicts if the customer would be interested or not in car insurance.

With your solution, the sales team expects to prioritize people with higher interest in the new product and thus optimize the campaign by only contacting the customers most likely to make the purchase.

As a result of your consultancy, you will need to deliver a report containing some analyses and answers to the following questions:

1. Main Insights about the most relevant attributes of customers interested in acquiring car insurance.

2. What percentage of customers interested in acquiring car insurance will the sales team be able to contact by making 20,000 calls?

3. And if the sales team's capacity increases to 40,000 calls, what percentage of customers interested in acquiring car insurance will the sales team be able to contact?

4. How many calls does the sales team need to make to contact 80% of the customers interested in acquiring car insurance?

# 2. Business Assumptions.

- Every customer that shows an interest greater than 50% will be classified as interested on purchase vehicle insurance.
- This new product will cost $2.000,00 for each new customer.
- This new product will cost $100.00 a call to contact each interested customer.

# 3. Solution Strategy

My strategy to solve this challenge was:

**Step 01. Data Description:**
 On this step, were checked many informations, as described bellow:
 - Number of columns and lines;
 - NAN values;
 - Descriptive Statistics;
 - Data distribuition;
 
**Step 02. Feature Engineering:**
On this step, were created new features, and some datas were changed, aiming the improvement of the analysis.

**Step 03. Data Filtering:**
N.A

**Step 04. Exploratory Data Analysis:**
On this step, were done:
- Univariate Analysis
![image]()
- Bivariate Analysis - According insights on Step 10.
- Multivariate Analysis
![image]()

**Step 05. Data Preparation:**
On this step, were made a train-test slipt besides the dataset balancing and transformation.
The dataset balancing were done by randon undersample.
For data transformation were used:
- Standardization
- Reescaling
- Target Encoder
- Frequency Encoder


**Step 06. Feature Selection:**
Feature selection were made by using Extra Trees Classifier.


**Step 07. Machine Learning Modelling:**

**Step 08. Hyperparameter Fine Tunning:**

**Step 09. Convert Model Performance to Business Values:**

**Step 10. Deploy Modelo to Production:**

# 4. Data Insights

**1. The interest on purchase the vehicle insurance is greater for customers that damaged their vehicle before and doesn't have insurance.**
    False, of the customers that damaged their car and doesn't have insurance, only 25% show interest in acquire vehicle insurance.

**2. The interest on purchase the vehicle insurance is greater for woman than men.**
   False, only 10% of women show interest in acquire vehicle insurance, whereas 13% of the men show interest on acquire vehicle insurance.

**3. The interest on purchase vehicle insurance is greater for vintage customers ( 7 months or more ).**
    False, the period that customers are on the company doensn't show influency on interest in buying vehicle insurance.

**4. The interest on purchase the vehicle insurance is greater for young customers.(Between 18 and 30 years old.)**
    False, customers that spend more than 30k yearly show greter interest on purchase vehicle insurance.

**5. The interest on purchase the vehicle insurance is greater for young customers.(Between 18 and 30 years old.)**
    False, adults and elderlies show greater interest on buying vehicle insurance.

**6. The interest on purchase the vehicle insurance is greater for customers that have driver license.**
    True, arround 12% of customers that hold a driving license show interest in buying the vehicle insurance.

**7. The interest on purchase the vehicle insurance is greater for customers that have new cars.**
    False, the interest is greater for customers that own an old car.

**8. The interest on purchase the vehicle insurance is greater for customers that have new cars and have damaged their vehicles.**
    False, of the customers who damaged their car, the ones that own a old car show greater interest in buying the vehicle insurance (29%), followed by customers that own used cars (27%).

**9. The interest on purchase the vehicle insurance is greater for elderly women.**
    False, adult women show greater interest in buying the vehicle insurance.

**10. The interest on purchase the vehicle insurance is lower for customers that are already insured.**
    True, less than 1% of customers already insured show interest on purchase the vehicle insurance.

# 5. Machine Learning Model Applied

# 6. Machine Learning Modelo Performance

# 7. Business Results

# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve

# LICENSE

# All Rights Reserved - Comunidade DS 2022
