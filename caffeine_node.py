from flask import Flask, request, jsonify
import time
import hashlib
import random

# This mocks the Caffeine AI Canister on ICP
app = Flask(__name__)

# Simulated state
current_block = 99281
merkle_root = "0x" + hashlib.sha256(b"genesis").hexdigest()[:40]


@app.route('/canister/verify_proof', methods=['POST'])
def verify():
    global current_block, merkle_root
    
    data = request.json
    
    # Input validation
    if not data:
        return jsonify({"status": "ERROR", "message": "No JSON payload provided"}), 400
    
    proof_id = data.get('proof_id')
    if not proof_id:
        return jsonify({"status": "ERROR", "message": "Missing proof_id"}), 400
    
    # Simulate block increment
    current_block += 1
    
    print(f"\n⛓️ [ICP Consensus] Block #{current_block}: Processing Proof {proof_id}...")
    print("   > Verifying zktls signature... [OK]")
    print("   > Verifying Nitro Enclave Attestation... [OK]")
    print("   > Checking GenOptima Weights... [OK]")
    
    time.sleep(2)  # Simulate consensus delay
    
    # Update Merkle root (simulated)
    new_leaf = hashlib.sha256(proof_id.encode()).hexdigest()
    merkle_root = "0x" + hashlib.sha256((merkle_root + new_leaf).encode()).hexdigest()[:40]
    
    response = {
        "status": "COMMITTED",
        "block_number": current_block,
        "tx_hash": "0x" + hashlib.sha256(f"{proof_id}{time.time()}".encode()).hexdigest()[:40],
        "merkle_root_update": merkle_root,
        "action": "INTEREST_RATE_ADJUSTMENT_TRIGGERED"
    }
    
    print("✅ [Settlement] Proof Validated. Smart Contract Triggered.")
    return jsonify(response)


@app.route('/canister/status', methods=['GET'])
def status():
    """Health check endpoint"""
    return jsonify({
        "status": "ONLINE",
        "network": "Internet Computer (ICP)",
        "current_block": current_block,
        "merkle_root": merkle_root
    })


if __name__ == '__main__':
    print("🌍 Caffeine AI Protocol Node running on port 5001...")
    app.run(port=5001)