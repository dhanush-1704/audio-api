@app.route("/", methods=["GET", "POST"])
def process_audio():
    if request.method == "GET":
        return "API is running", 200

    data = request.get_json()

    audio_base64 = data["audio_base64"]
    audio_bytes = base64.b64decode(audio_base64)

    arr = np.frombuffer(audio_bytes, dtype=np.uint8)

    result = {
        "rows": int(len(arr)),
        "columns": ["value"],
        "mean": {"value": float(np.mean(arr))},
        "std": {"value": float(np.std(arr))},
        "variance": {"value": float(np.var(arr))},
        "min": {"value": float(np.min(arr))},
        "max": {"value": float(np.max(arr))},
        "median": {"value": float(np.median(arr))},
        "mode": {"value": int(np.bincount(arr).argmax()) if len(arr) else 0},
        "range": {"value": float(np.max(arr) - np.min(arr))},
        "allowed_values": {"value": []},
        "value_range": {"value": [float(np.min(arr)), float(np.max(arr))]},
        "correlation": []
    }

    return jsonify(result)
