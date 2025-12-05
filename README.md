Here is a quick Ai genrated guide to running your SustainSwift prototype.

Since this architecture simulates a decentralized network (a Utility Provider, a Blockchain Node, and a Client Dashboard), you will need to run three separate processes simultaneously.

-------
1. Prerequisites
Ensure you have Python installed. Open your terminal/command prompt and install the required libraries:

"pip install flask streamlit pandas requests"

-------
2. File Setup
Save the code you provided into three separate files in the same folder:

utility_api.py (The mock Data Provider)

caffeine_node.py (The mock ICP Blockchain Node)

sustainswift_dashboard.py (The User Interface)

-------

3. Running the System
You need to open 3 separate terminal windows (or tabs) to simulate the different network components running at the same time.

Terminal 1: The Utility Provider
This mimics Duke Energy's API.

python utility_api.py
You will see: ⚡ Utility API Provider running on port 5000...

Terminal 2: The Blockchain Node
This mimics the Caffeine AI Canister on ICP.

python caffeine_node.py
You will see: 🌍 Caffeine AI Protocol Node running on port 5001...

Terminal 3: The Dashboard
This is the frontend you will interact with.

streamlit run sustainswift_dashboard.py
This will automatically open your web browser to http://localhost:8501.

-------

4. How to Use the Demo
Once the dashboard is open in your browser:

Left Column (Supplier): Click "🔗 Connect to Utility API".

What happens: The dashboard talks to utility_api.py (Terminal 1) to fetch "private" energy data.

Generate Proof: Click "⚙️ Run GenOptima + Generate ZK Proof".

What happens: It calculates emissions locally and creates a JSON "proof."

Right Column (Verifier): Click "🔍 Verify On-Chain".

What happens: The dashboard sends the proof to caffeine_node.py (Terminal 2).

Check Terminal 2: You will see the blockchain "mining" logs (Block processing, consensus checks) in real-time!

-------

Troubleshooting
Connection Failed? Ensure utility_api.py and caffeine_node.py are actually running in the background. If you close those terminals, the dashboard buttons will fail.

Port Errors? Make sure no other application is using ports 5000 or 5001.
