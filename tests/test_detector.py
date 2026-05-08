# test de la détection d'événements vidéo Spotlight
from spotlight_video_events.detector import detect_video_events

def test_detect_video_events():
    contract = detect_video_events("surveillance.mp4")
    assert contract is not None
    assert len(contract.result["events"]) >= 1
    assert len(contract.evidence) >= 1
