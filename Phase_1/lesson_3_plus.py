def main():
    detections = [
        {"label": "person", "conf": 0.88},
        {"label": "car", "conf": 0.92},
        {"label": "dog", "conf": 0.45}
    ]
    for idx, item in enumerate(detections):
        if item["conf"] > 0.5:
            print(f"Index {idx}: {item['label']} detected with confidence {item['conf']}")
            # ""注意内双外单



if __name__ == "__main__":
    main()