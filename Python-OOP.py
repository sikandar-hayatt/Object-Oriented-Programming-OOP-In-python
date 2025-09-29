from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

content = """
Bivariate Normal Distribution

1. Introduction
The Bivariate Normal Distribution describes the relationship between two continuous variables (X and Y) that are both normally distributed. It's used in many fields like economics, biology, and engineering.

2. Definition
Two random variables X and Y follow a bivariate normal distribution if every linear combination of them is also normally distributed.

Mathematically:
(X, Y) ~ N ( [μX, μY], [[σX^2, ρσXσY], [ρσXσY, σY^2]] )

Where:
- μX and μY are the means of X and Y
- σX^2 and σY^2 are their variances
- ρ is the correlation coefficient

3. Probability Density Function (PDF)
The PDF is:
f(x, y) = (1 / (2πσXσY√(1−ρ²))) * exp{ ... }

This describes the probability of getting a pair (x, y).

4. Key Properties
- Marginal Distributions: X and Y are normally distributed individually.
- Conditional Distributions: Also normal.
- Independence: X and Y are independent if ρ = 0.
- Contours of constant probability form ellipses.

5. Visualization
The shape is a 3D bell surface, centered at (μX, μY). Its spread depends on σX, σY, and ρ.

6. Applications
- Finance: Modeling returns of two assets.
- Engineering: Joint analysis of variables.
- Biology: Study of two measurements jointly.

7. Example: ACT Scores
Let X be math score, Y be verbal score:
μX = 22.7, σX^2 = 17.64, μY = 22.7, σY^2 = 12.25, ρ = 0.78

Find P(18.5 < Y < 25.5):
Z1 = (18.5 - 22.7)/sqrt(12.25) = -1.20
Z2 = (25.5 - 22.7)/sqrt(12.25) = 0.80

From Z-tables:
P(Z < 0.80) = 0.7881
P(Z < -1.20) = 0.1151

So, P(18.5 < Y < 25.5) = 0.7881 - 0.1151 = 0.673

Conclusion:
The bivariate normal distribution is key to modeling relationships between two normal variables.
"""

for line in content.strip().split("\n"):
    pdf.multi_cell(0, 10, line)

pdf.output("Bivariate_Normal_Distribution.pdf")




user_name=input("enter your name")
user_father_name=input("enter your father name")
user_age=input("enter your age")

print(user_name)
print(user_father_name)
print(user_age)