# Set initial limits and step size
MIN_BRIGHTNESS = 0
MAX_BRIGHTNESS = 1
STEP_SIZE = 0.1

# Initial brightness level
brightness = 0.5

def display_brightness(brightness):
    # Scale brightness to a 0-10 range for display
    brightness_level = int(brightness * 10)
    print(f"Current Brightness: {'|' * brightness_level}{' ' * (10 - brightness_level)} {brightness * 100:.0f}%")

print("LED Brightness Control")
print("Commands: ")
print("  '+' to increase brightness")
print("  '-' to decrease brightness")
print("  'exit' to exit the program")

while True:
    display_brightness(brightness)

    command = input("Enter command: ").strip().lower()

    if command == '+':
        if brightness + STEP_SIZE <= MAX_BRIGHTNESS:
            brightness += STEP_SIZE
        else:
            print("Brightness is already at maximum!")
    elif command == '-':
        if brightness - STEP_SIZE >= MIN_BRIGHTNESS:
            brightness -= STEP_SIZE
        else:
            print("Brightness is already at minimum!")
    elif command == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Invalid command! Please enter '+', '-', or 'exit'.")