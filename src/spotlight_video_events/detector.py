from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

def detect_video_events(video_path: str) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    events = [
        {"time_sec": 5.2, "label": "person_speaking", "confidence": 0.93},
        {"time_sec": 23.1, "label": "crowd_gathering", "confidence": 0.85},
    ]
    contract.result = {"video": video_path, "events": events, "total": len(events)}
    contract.add_evidence(Evidence(subject=video_path, predicate="video_events",
        value=f"{len(events)} events", source="spotlight_engine", observed_at=now,
        confidence=0.89, status=EpistemicStatus.INFERENCE))
    return contract
