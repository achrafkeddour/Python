from sklearn.tree import DecisionTreeClassifier

# Step 1: Training Data (Features and Labels)
# Features: [Weight (grams)]
features = [[150], [170], [140], [130]]
# Labels: 1 = Orange, 0 = Apple
labels = [1, 1, 0, 0]

# Step 2: Create and Train the Model
model = DecisionTreeClassifier()
model.fit(features, labels)

# Step 3: Accept User Input
weight = float(input("Enter the weight of the fruit (grams): "))

# Step 4: Make a Prediction
prediction = model.predict([[weight]])

# Output the result
result = "Orange" if prediction[0] == 1 else "Apple"
print(f"The fruit is likely an: {result}")