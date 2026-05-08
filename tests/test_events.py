from spotlight_video_events import detect_video_events

def test_detect_video_events():
    c = detect_video_events("video.mp4")
    assert c.result["total"] > 0
    assert c.confidence > 0.8
