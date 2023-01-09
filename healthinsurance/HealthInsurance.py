import pickle
import numpy  as np
import pandas as pd

class HealthInsurance:
    
    def __init__( self ):
        self.home_path = 'C:/Users/pero/tDocuments/ds_repos/projects/Health_Insurance_Cross_Sell'
        self.annual_premium_scaler = pickle.load( open( self.home_path + '/src/features/annual_premium_scaler.pkl') )
        self.age_scaler = pickle.load( open( self.home_path + '/src/features/age_scaler.pkl') )
        self.vintage_scaler = pickle.load( open( self.home_path + '/src/features/vintage_scaler.pkl') )
        self.target_encode_region_code_scaler = pickle.load( open( self.home_path + '/src/features/target_encode_region_code_scaler.pkl') )
        self.target_encode_gender_scaler = pickle.load( open( self.home_path + '/src/featurestarget_encode_gender_scaler.pkl') )
        self.frequency_encode_policy_sales_scaler = pickle.load( open( self.home_path + '/src/features/frequency_encode_policy_sales_scaler.pkl') )
        return( self )
     
    def data_preparation( df5 ):   
        
    # Ajustando coluna vehicle_age
    df5['vehicle_age'] = df5['vehicle_age'].apply(lambda x: 1 if (x == '< 1 Year') else
                                                            2 if (x == '1-2 Year') else
                                                            3)
    # Ajustando coluna vehicle_damage
    df5['vehicle_damage'] = df5['vehicle_damage'].apply(lambda x: 1 if (x == 'Yes') else 0)

    # Annual Premium
    df5['annual_premium'] = self.annual_premium_scaler.transform( df5[['annual_premium']].values )
    
    # Age
    df5['age'] = self.age_scaler.transform( df5[['age']].values )
 
    # Vintage
    df5['vintage'] = self.vintage_scaler.transform( df5[['vintage']].values )
    
    # gender
    df5.loc[:, 'gender'] = df5['gender'].map( target_encode_gender_scaler )
    
    # region_code - Frequency Encoding / Target Encoding / Weighted Targed Encoding
    df5.loc[:, 'region_code'] = df5['region_code'].map( self.target_encode_region_code_scaler )
    
    # policy_sales_channel - Frequency Encoding / Target Encoding
    df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map( self.frequency_encode_policy_sales_scaler )
    
    # Feature Selection
    cols_selected = ['vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage', 'policy_sales_channel', 'previously_insured']

    return df5[cols_selected]

def get_prediction (self, model, original_data, test_data ):
    # prediction
    pred = model.predict( test_data )
      
    # join pred into the original data
    original_data['score'] = np.expm1( pred )
      
    return original_data.to_json( orient='records', date_format='iso' )