import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('data/upselling.csv')

# if upsold (purchased product is not the same as viewed)
df['upsold'] = df['product_viewed'] != df['product_purchased']
df['upsold'] = df['upsold'].astype(int)

df_encoded = pd.get_dummies(df[['product_viewed']], drop_first=True)

x = pd.concat([df[['product_price', 'user_income']], df_encoded], axis=1)
y = df['upsold']

model = DecisionTreeClassifier()
model.fit(x, y)

# user views phone worth 20000 with income 60000
test = pd.DataFrame([[20000, 60000, 0, 0]], columns=x.columns)
pred = model.predict(test)

print('recommend upgrade' if pred[0] == 1 else 'no upsell needed')