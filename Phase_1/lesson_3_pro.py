def main():
    confidence = 0.4
    # threshold = 0.3
    threshold = 0.5
    if confidence >= threshold:
        print("Detection Accepted.")
    else:
        print("Detection Reject.")


if __name__ == "__main__":
    main()