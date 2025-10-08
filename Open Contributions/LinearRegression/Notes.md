# Introduction

Linear Regression is a supervised machine learning algorithm used to predict continuous outputs based on one or more inputs.

It finds a line of best fit for the data, which is the line that minimizes the difference between the predicted values and actual values.

Equation:
 
`y=m⋅x+b`

Where:

- `y` → Output / Dependent variable
- `x` → Input / Independent variable
- `m` → Slope of the line
- `b` → Intercept (value of `y` when `x=0`)

## Supervised Machine Learning

Supervised Machine Learning means the model is trained on labeled data (we already know the correct output for each input).

The model learns the mapping between input(s) and output(s) so it can predict future unseen outputs.

### Key Concepts in Supervised Learning

1. Features (Input X): Data you use to make predictions.
   </br>
   Example: Hours studied, house size, temperature.

2. Labels (Output Y): Correct answers you want the model to predict.
   </br>
   Example: Exam score, house price, weather condition.

3. Training Data: Dataset used to teach the model.

4. Testing Data: Dataset used to evaluate how well the model has learned.

## Types Of Linear Regression

1. Simple Linear Regression
   </br>
   - Uses one input variable (x) to predict the output (y). Example -> Predicting exam score based on hours studied.

2. Multiple Linear Regression
   </br>
   - Uses multiple input variables (x₁, x₂, ...) to predict the output. Example -> Predicting house price based on size, location, and number of rooms.

## How Linear Regression Works?

The algorithm finds the best fit line by minimizing the error (difference between actual and predicted values).

Steps in Simple Linear Regression ->

1. Calculate Means
    </br>
    `mean_x = sum(x_i) / n`
    `mean_y = sum(y_i) / n`

2. Find Slope (m)
    </br>
    `m = sum((x_i - mean_x) * (y_i - mean_y)) / sum((x_i - mean_x)^2)`

3. Find Intercept (b)
     </br>
     `b = mean_y - m * mean_x`

4. Prediction
     </br>
     `y_pred = m * x + b`

## Model Evaluation

To check how good our model is, we use metrics:

Mean Squared Error (MSE):
Measures average squared difference between actual and predicted values.

𝑀𝑆𝐸 = ∑(𝑦<sub>𝑖</sub> − 𝑦_𝑝𝑟𝑒𝑑)<sup>2</sup>
     /    𝑛

R² Score (Coefficient of Determination):
Explains how much variance in the output is explained by the model.

𝑅<sup>2</sup> = 1 −   ∑(𝑦<sub>𝑖</sub>  − 𝑦_𝑝𝑟𝑒𝑑)<sup>2</sup>   /     ∑(𝑦<sub>𝑖</sub> − 𝑚𝑒𝑎𝑛_𝑦)<sup>2</sup>
