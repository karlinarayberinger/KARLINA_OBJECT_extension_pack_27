#########################################################################################
# file: pi_approximation.py
# type: Python
# date: 29_DECEMBER_2024
# author: karbytes
# license: PUBLIC_DOMAIN 
#########################################################################################
import random
import time

""" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This Python application is a plain-text command line version of the animated 
JavaScript web application featured on the tutorial web page at the following 
Uniform Resource Locator:

https://karbytesforlifeblog.wordpress.com/pi_approximation_two/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def is_in_circle(x, y, radius):
    """Check if a point (x, y) is positioned within a circle of whose radius is centered at (0, 0)."""
    return x**2 + y**2 <= radius**2

def monte_carlo_simulation():
    """Run the Monte Carlo simulation indefinitely, overwriting the log file with the latest snapshot."""
    """Note that one of such snapshots is made per second of the simulation."""

    red_count = 0 # inside of the circle (which is inscribed inside of a square)
    blue_count = 0 # outside of the circle (but inside of the square)

    radius = 200  # equivalent to half the canvas size in pixels
    output_file = "pi_approximation_output.txt"
    
    print("Monte Carlo Simulation for Approximating Pi")
    print("-" * 50)
    
    try:
        while True:
            # Generate a random point in the square.
            x = random.uniform(-radius, radius)
            y = random.uniform(-radius, radius)
            
            # Check if the point lies in the circle.
            if is_in_circle(x, y, radius):
                red_count += 1
            else:
                blue_count += 1
            
            # Calculate Pi approximation.
            total_darts = red_count + blue_count
            pi_approximation = 4 * (red_count / total_darts)
            
            # Convert the result to a string and strip unnecessary trailing zeros
            pi_approximation_str = f"{pi_approximation:.100f}".rstrip('0').rstrip('.')

            # Prepare the output string.
            output = (
                f"------------------------------------\n"
                f"seconds_elapsed: {total_darts}\n"
                f"red_dot_count: {red_count}\n"
                f"blue_dot_count: {blue_count}\n"
                f"Pi approximation: {pi_approximation_str}\n"
                f"------------------------------------\n"
            )
            
            # Print to console.
            print(output, end="")
            
            # Overwrite the file with the (second-by-second) latest snapshot.
            with open(output_file, "w") as file:
                file.write(output)
            
            time.sleep(1)  # Wait for 1 second.
    except KeyboardInterrupt:
        final_message = "\nThe simulation stopped by the user.\n"
        print(final_message)
        with open(output_file, "a") as file:

            file.write(final_message)
        print(f"The latest snapshot was saved to {output_file}.")

if __name__ == "__main__":
    monte_carlo_simulation()

