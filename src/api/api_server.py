from flask import Flask, request, jsonify
from src.orchestrator.orchestrator import MultiModalOrchestrator

app = Flask(__name__)
orch = MultiModalOrchestrator()

@app.route("/api/v1/infer", methods=["POST"])
def infer():
    d = request.get_json(force=True)
    mode, inp = d.get("mode", "text"), d.get("input_data", "")
    return jsonify(result = orch.process_request(inp, mode))

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)