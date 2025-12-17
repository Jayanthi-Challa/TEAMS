from sklearn.cluster import KMeans

def identify_hotspots(data, n_clusters=3):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    data["cluster"] = model.fit_predict(data[["lat", "lon"]])
    return data