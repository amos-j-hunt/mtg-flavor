import sys
from pathlib import Path
import shutil
import pandas as pd

# Ensure src package importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import main


def test_run_pipeline_redownloads(tmp_path, monkeypatch):
    # path where pipeline will expect the JSON file
    raw_path = tmp_path / "AllPrintings.json"

    # Create an empty file so initial exists check passes
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_text("{}")

    sample = Path(__file__).parent / "test_data" / "sample_cards.json"

    downloads = []

    def fake_download(dest: Path):
        downloads.append(dest)
        shutil.copy(sample, dest)

    call_count = {"loads": 0}

    def fake_load_and_clean(path: Path):
        call_count["loads"] += 1
        if call_count["loads"] == 1:
            # Simulate file missing when first attempt occurs
            path.unlink()
            raise FileNotFoundError
        # second attempt should succeed
        return [{"flavorText": "test", "color_identity": "U"}]

    # patch helpers
    monkeypatch.setattr(main, "download_all_printings", fake_download)
    monkeypatch.setattr(main, "load_and_clean_cards", fake_load_and_clean)
    monkeypatch.setattr(main, "score_texts", lambda texts: [{"textblob_polarity":0, "vader_compound":0,
                                                             "vader_pos":0, "vader_neg":0, "vader_neu":0} for _ in texts])
    monkeypatch.setattr(main, "by_color", lambda df: pd.DataFrame())
    monkeypatch.setattr(main, "plot_average_sentiment", lambda *a, **k: None)

    main.run_pipeline(raw_path=raw_path)

    # ensure download happened once and load attempted twice
    assert len(downloads) == 1
    assert call_count["loads"] == 2
