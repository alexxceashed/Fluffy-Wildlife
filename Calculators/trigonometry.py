import re
import sympy as sp

# Define 'pi' as a symbolic variable for clean exact math
pi = sp.Symbol('pi')

def pre_parse_input(user_input):
    """
    Fixes implicit multiplications like '12pi' into '12*pi',
    and handles casing variations like 'PI' or 'Pi'.
    """
    # Standardise to lowercase
    text = user_input.strip().lower()
    
    # Insert '*' between any number and the word 'pi' (e.g., '12pi' -> '12*pi')
    text = re.sub(r'(\d+)(pi)', r'\1*\2', text)
    
    # Insert '*' between 'pi' and any number (e.g., 'pi12' -> 'pi*12')
    text = re.sub(r'(pi)(\d+)', r'\1*\2', text)
    
    return text

while True:
    print("\n" + "="*30)
    print("Select Conversion Mode:")
    print("1. Radians to Degrees")
    print("2. Degrees to Radians")
    print("3. Exit")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "3":
        print("Goodbye!")
        break

    # --- Mode 1: Radians to Degrees ---
    if choice == "1":
        angle_input = input("Enter Radians (e.g., 12pi, 12/pi, pi/12): ")
        try:
            # Clean up implicit multiplication before passing to SymPy
            cleaned_input = pre_parse_input(angle_input)
            
            parsed_angle = sp.sympify(cleaned_input)
            exact_degrees = parsed_angle * 180 / pi
            print(f"\nExact Degrees:   {exact_degrees}")
            
            # Convert to float for decimal and DMS calculation
            total_degrees = float(exact_degrees.subs(pi, sp.pi).evalf())
            print(f"Decimal Degrees: {total_degrees:.4f}°")
            
            # DMS Logic
            degrees = int(total_degrees)
            fractional_minutes = abs(total_degrees - degrees) * 60
            minutes = int(fractional_minutes)
            seconds = (fractional_minutes - minutes) * 60
            
            print(f"DMS Format:      {degrees}° {minutes}' {seconds:.2f}\"")
            
        except Exception as e:
            print(f"\nError parsing input: {e}")

    # --- Mode 2: Degrees to Radians ---
    elif choice == "2":
        angle_input = input("Enter Degrees (e.g., 45, 218.85): ").strip()
        try:
            parsed_degrees = sp.sympify(angle_input)
            exact_radians = parsed_degrees * sp.pi / 180
            print(f"\nExact Radians:   {exact_radians}")
            
            decimal_radians = float(exact_radians.evalf())
            print(f"Decimal Radians: {decimal_radians:.4f} rad")
            
        except Exception as e:
            print(f"\nError parsing input: {e}")
            
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
