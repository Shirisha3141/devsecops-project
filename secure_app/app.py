import os
from flask import Flask, render_template

app = Flask(__name__)

# --- THE FACULTY DEMO SWITCH ---

# 1. TO GET A "RED" ERROR (FAILED BUILD): 
#    Remove the '#' so the line below is active.
# ADMIN_PASSWORD = "Sreenidhi_Test_Pass_123"

# 2. TO GET A "GREEN" SUCCESS (PASSED BUILD): 
#    Add a '#' to the start of the line above.

@app.route('/')
def home():
    # This 'globals().get' is the secret! 
    # It prevents the "NameError" if the variable is commented out.
    if globals().get('ADMIN_PASSWORD'):
        return render_template('index.html', vulnerable=True, error="CRITICAL: Hardcoded Credential Detected!")
    
    return render_template('index.html', vulnerable=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    # Triggering Pipeline for Faculty Demo.