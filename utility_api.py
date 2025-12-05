from flask import Flask, jsonify
import random
import time

# This mocks the "National Grid" or Utility Provider API
app = Flask(__name__)

@app.route('/v1/meter/<meter_id>', methods=['GET'])
def get_meter_reading(meter_id):
    # Simulate a verified TLS endpoint
    print(f"🔌 [Network] Incoming SSL Handshake for Meter: {meter_id}")
    time.sleep(0.5) 
    
    # Generate realistic/messy data
    data = {
        "provider": "Duke Energy Secure Gateway",
        "timestamp": time.time(),
        "usage_kwh": random.randint(45000, 55000),
        "mix": {
            "solar_percentage": 85,
            "grid_coal_percentage": 0,
            "nuclear_percentage": 15
        },
        "signature": "sha256_rsa_4096_verified_root_ca"
    }
    return jsonify(data)

if __name__ == '__main__':
    print("⚡ Utility API Provider running on port 5000...")
    app.run(port=5000)