from sklearn.ensemble import IsolationForest


FEATURE_KEYS = [
    "error_count",
    "warn_count",
    "packet_loss_count",
    "timeout_count"
]


def _to_vector(feature_dict):
    return [feature_dict.get(k, 0) for k in FEATURE_KEYS]


def train_model(window_feature_list):
    """
    window_feature_list: List[Dict]
    """
    X = [_to_vector(f) for f in window_feature_list]

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )
    model.fit(X)

    return model


def predict_anomaly(model, feature_dict):
    X = [_to_vector(feature_dict)]
    prediction = model.predict(X)
    return prediction[0] == -1

