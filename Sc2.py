#Name: Helber diaz vasquez
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classificatio
def calculate_bmi(weight_lbs, height_feet, height_inches):
    # Convert total height to inches
    total_inches = (height_feet * 12) + height_inches

    # Prevent division by zero
    if total_inches <= 0 or weight_lbs <= 0:
        return "Invalid input. Height and weight must be greater than zero."

    # Calculate and round BMI to 1 decimal place
    bmi = round((weight_lbs / (total_inches ** 2)) * 703, 1)

    # Determine classification
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal Weight"
    elif 25.0 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return f"BMI: {bmi} ({category})"