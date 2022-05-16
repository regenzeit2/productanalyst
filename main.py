import pandas as pd

xls = pd.ExcelFile(r'C:\Users\never\Downloads\claims_provider_data_anonymized.xlsx')
claims = pd.read_excel(xls, 'data_claims_anonymized')
provider = pd.read_excel(xls, 'data_provider_anonymized')

pd.options.display.max_rows = 100
pd.options.display.float_format = '{:.1f}'.format

# claims dataset information
print(claims.shape)
print(claims.describe())
claims.info()

# provider dataset information
print(provider.shape)
print(provider.describe())
provider.info()

# looking for missing values
print(claims.isnull().sum())

# filling missing values
claims["patient_gender"].fillna("No Gender", inplace=True)
claims["patient_age"].fillna(claims["patient_age"].median(), inplace=True)
claims['patient_age'] = claims['patient_age'].apply(lambda x: x if x > 0 else claims["patient_age"].median())

# writing updated datasets to separate csv's
claims.to_csv(r'C:\Users\never\Downloads\claims.csv')
provider.to_csv(r'C:\Users\never\Downloads\provider.csv')