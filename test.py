# Basic Inputs
supplyType = int(input("Enter supply type: "))
prepaidBalance = int(input("Enter prepaid balance: "))
contractedLoad = int(input("Enter contracted load: "))
arrearAmount = int(input("Enter arrear amount: "))
minimumCharges = int(input("Enter minimum charges: "))
totalDayofMonth = int(input("Enter total day of month: "))

# Fixed Charges
fixedCharges = 99

# Electricity Charges and Subsidy for ranges
electricityCharges = [
    (100, 5.85, 0.9, 4.95),    # 0 to 100
    (150, 5.85, 0.9, 4.95),    # 101 to 150
    (300, 5.85, 0.45, 5.4),    # 151 to 300
    (float('inf'), 5.85, 0, 5.85)  # 301 and above
]

# Daily consumption input Data
daily_consumptions = []

# Initialize cumm values
cumm_daily_consumption = 0
cumm_electricity_charges_before_subsidy = 0
cumm_electricity_charges_daily_subsidy = 0
cumm_electricity_charges_after_subsidy = 0

print("\nEnter daily consumption values:")

# Loop to take daily consumption data
for day in range(1, totalDayofMonth + 1):
    dailyConsumption = float(input(f"Enter value of Day {day}: "))
    daily_consumptions.append(dailyConsumption)

    # Determine the applicable charge and subsidy for the current consumption
    for limit, before_subsidy, subsidy, after_subsidy in electricityCharges:
        if dailyConsumption <= limit:
            electricity_charge_rate = before_subsidy
            electricity_subsidy_rate = subsidy
            electricity_charge_after_rate = after_subsidy
            break

    # Calculate daily values and round to 2 decimal places
    electricity_charge_before_subsidy = round(electricity_charge_rate * dailyConsumption, 2)
    electricity_charge_daily_subsidy = round(electricity_subsidy_rate * dailyConsumption, 2)
    electricity_charge_after_subsidy = round(electricity_charge_after_rate * dailyConsumption, 2)

    # Update cumm values
    cumm_daily_consumption = round(cumm_daily_consumption + dailyConsumption, 2)
    cumm_electricity_charges_before_subsidy = round(cumm_electricity_charges_before_subsidy + electricity_charge_before_subsidy, 2)
    cumm_electricity_charges_daily_subsidy = round(cumm_electricity_charges_daily_subsidy + electricity_charge_daily_subsidy, 2)
    cumm_electricity_charges_after_subsidy = round(cumm_electricity_charges_after_subsidy + electricity_charge_after_subsidy, 2)

    # Display daily results
    print(f"\nDay {day}:")
    print(f"  1. Cumulative Daily Consumption: {cumm_daily_consumption:.2f}")
    print(f"  2. Electricity Charge Before Subsidy: {electricity_charge_before_subsidy:.2f}")
    print(f"  3. Cumulative Electricity Charge Before Subsidy: {cumm_electricity_charges_before_subsidy:.2f}")
    print(f"  4. Electricity Charge Daily Subsidy: {electricity_charge_daily_subsidy:.2f}")
    print(f"  5. Cumulative Electricity Charge Subsidy: {cumm_electricity_charges_daily_subsidy:.2f}")
    print(f"  6. Daily Electricity Charge After Subsidy: {electricity_charge_after_subsidy:.2f}")
    print(f"  7. Cumulative Electricity Charge After Subsidy: {cumm_electricity_charges_after_subsidy:.2f}")
