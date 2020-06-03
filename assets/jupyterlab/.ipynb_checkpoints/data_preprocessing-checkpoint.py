from sklearn.preprocessing import LabelEncoder

class CategoricalEncoder:

    def __init__(self, cat_columns):
        self.encoder_dict = {}
        self.cat_columns = cat_columns
        self.is_encoded = False

    def encode(self, df):
        for column in self.cat_columns:
            encoder = LabelEncoder()
            df[column] = encoder.fit_transform(df[column])
            self.encoder_dict[column] = encoder
        self.is_encoded = True
            
    def decode(self, df):
        if self.is_encoded:
            for column in self.cat_columns:
                encoder = self.encoder_dict[column]
                df[column] = encoder.inverse_transform(df[column])
        else:
            raise ValueError('You should first perform encoding')
            
    def is_encoded(self):
        return self.is_encoded