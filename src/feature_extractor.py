from collections import defaultdict


def extract_features(events):
    features = defaultdict(int)

    for event in events:
        features["total_events"] += 1

        if event["level"] == "ERROR":
            features["error_count"] += 1

        if event["level"] == "WARN":
            features["warn_count"] += 1

        if "Packet Loss" in event["message"]:
            features["packet_loss_count"] += 1

        if "Timeout" in event["message"]:
            features["timeout_count"] += 1

    return dict(features)
