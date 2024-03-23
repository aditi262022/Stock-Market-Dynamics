import os
import subprocess

def main():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Step 1: Run scrape_cryptocurrency_data.py
    print("Running scrape_cryptocurrency_data.py...")
    subprocess.run(["python", os.path.join(current_dir, "scrape_cryptocurrency_data.py")], check=True)

    # Step 2: Run technical_cryptocurrency_analysis.py
    print("\nRunning technical_cryptocurrency_analysis.py...")
    subprocess.run(["python", os.path.join(current_dir, "technical_cryptocurrency_analysis.py")], check=True)

    # Step 3: Run decision_cryptocurrency.py
    print("\nRunning decision_cryptocurrency.py...")
    subprocess.run(["python", os.path.join(current_dir, "decision_cryptocurrency.py")], check=True)

    print("\nAll scripts executed successfully.")

if __name__ == "__main__":
    main()
