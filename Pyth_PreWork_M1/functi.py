

# Define the function
def generation_calculator(year_of_birth):
    """Return the generation based on year of birth."""
    if year_of_birth < 1949:
        return "Silent Generation"
    elif 1949 <= year_of_birth <= 1968:
        return "Baby Boomer"
    elif 1969 <= year_of_birth <= 1980:
        return "Generation X"
    elif 1981 <= year_of_birth <= 1993:
        return "Millennial"
    elif year_of_birth >= 1994:
        return "Generation Z"
    else:
        return "Unknown"

# Call the function with different test years and print the results
test_years = [1945, 1955, 1975, 1988, 1997, 2020]

for year in test_years:
    generation = generation_calculator(year)
    print(f"Year: {year} → Generation: {generation}")

