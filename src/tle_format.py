def calculate_tle_checksum(line):
    """Calculates the checksum for a single TLE line."""
    checksum = 0
    # Process only the first 68 characters (checksum is the 69th character)
    for char in line[:68]:
        if char.isdigit():
            checksum += int(char)
        elif char == '-':
            checksum += 1
    return checksum % 10

def format_tle_line(line):
    """
    Takes an unformatted or incomplete TLE line (without the final checksum),
    calculates the checksum, and returns the full 69-character line.
    """
    # Remove any trailing newline characters
    line = line.strip()
    
    # If the line already includes a placeholder for the checksum, remove it
    if len(line) == 69:
        line = line[:-1]
        
    # TLE lines are exactly 68 characters of data before the checksum
    line = line.ljust(68) 
    
    # Calculate checksum and append it
    checksum = calculate_tle_checksum(line)
    return f"{line}{checksum}"

# --- Example Usage ---

# Line 0 (satellite name)
line_0 = ["UME 1", "Canyon 2", "Rhyolite 1"]
# Line 1 (without the final checksum digit)
line_1 = ["1 25544U 98067A   26153.50000000  .00001234  00000-0  12345-0 0",
          "1 03889U 69036A   26154.43330404  .00000000  00000-0  00000-0 0",
          "1 04418U 70046A   26154.29846710  .00000000  00000-0  00000-0 0" ]

# Line 2 (without the final checksum digit)
line_2 = ["2 25544  51.6432 123.4567 0001234 123.4567 234.5678  1.12345678",
          "2 03889  13.5329  39.2227 0969311 194.3458 162.6999  1.00364372",
          "2 04418   2.2675  83.1368 0007515  52.1171 307.9630  1.00276334"]

for i in range(3):
    formatted_l0 = line_0[i]
    formatted_l1 = format_tle_line(line_1[i])
    formatted_l2 = format_tle_line(line_2[i])

    print("formatted TLE")
    print(formatted_l1)
    print(formatted_l2)

    with open("set_01.tle", "a", encoding="utf-8") as file:
        file.write(f"{formatted_l0}\n")
        file.write(f"{formatted_l1}\n")
        file.write(f"{formatted_l2}\n")

with open("set_01.tle", "a", encoding="utf-8") as file:
    file.close()

