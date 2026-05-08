from spotlight_video_events.detector import detect_video_events

def test_detect_video_events():
    c = detect_video_events("video.mp4")
    assert c.result["total_events_detected"] > 0
    assert c.confidence > 0.8
