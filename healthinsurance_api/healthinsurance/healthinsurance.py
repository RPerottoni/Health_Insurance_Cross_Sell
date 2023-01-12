import pickle
import inflection
import numpy  as np
import pandas as pd

class HealthInsurance:
    
    def __init__( self ):
        self.home_path                            = ''
        self.annual_premium_scaler                = pickle.load( open( self.home_path + 'src/features/annual_premium_scaler.pkl', 'rb') )
        self.age_scaler                           = pickle.load( open( self.home_path + 'src/features/age_scaler.pkl', 'rb') )
        self.vintage_scaler                       = pickle.load( open( self.home_path + 'src/features/vintage_scaler.pkl', 'rb') )
        self.target_encode_region_code_scaler     = pickle.load( open( self.home_path + 'src/features/target_encode_region_code_scaler.pkl', 'rb') )
        self.target_encode_gender_scaler          = pickle.load( open( self.home_path + 'src/features/target_encode_gender_scaler.pkl', 'rb') )
        self.frequency_encode_policy_sales_scaler = pickle.load( open( self.home_path + 'src/features/frequency_encode_policy_sales_scaler.pkl', 'rb') )
     
    def data_cleaning( self, df5 ):
 
        ## rename Columns
        cols_old = ['id', 'Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured', 'Vehicle_Age', 'Vehicle_Damage', 'Annual_Premium', 'Policy_Sales_Channel', 'Vintage']

        snakecase = lambda x: inflection.underscore( x )
        cols_new = list( map( snakecase, cols_old ) )
        
        # rename
        df5.columns = cols_new
        
        return( df5 )

    def data_preparation( self, df5 ):   
        
        # Ajustando coluna vehicle_age
        df5['vehicle_age'] = df5['vehicle_age'].apply(lambda x: 1 if (x == '< 1 Year') else 2 if (x == '1-2 Year') else 3)
        
        # Ajustando coluna vehicle_damage
        df5['vehicle_damage'] = df5['vehicle_damage'].apply(lambda x: 1 if (x == 'Yes') else 0)
       
        # Age
        df5['age'] = self.age_scaler.transform( df5[['age']].values )
    
        # Annual Premium
        df5['annual_premium'] = self.annual_premium_scaler.transform( df5[['annual_premium']].values )

        # Vintage
        df5['vintage'] = self.vintage_scaler.transform( df5[['vintage']].values )
        
        # gender
        df5.loc[:, 'gender'] = df5['gender'].map( self.target_encode_gender_scaler )
        
        # codigo de regiao
        df5.loc[:, 'region_code'] = df5['region_code'].map( self.target_encode_region_code_scaler )
        
        # policy_sales_channel - Frequency Encoding / Target Encoding
        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map( self.frequency_encode_policy_sales_scaler )
        
        # Feature Selection
        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage', 'policy_sales_channel', 'previously_insured']

        return df5[cols_selected]

    def get_prediction( self, model, original_data, test_data ):
        # prediction
        pred = model.predict_proba( test_data )
        
        # join pred into the original data
        original_data['score'] = pred[:, 1].tolist()
        
        return original_data.to_json( orient='records', date_format='iso' )