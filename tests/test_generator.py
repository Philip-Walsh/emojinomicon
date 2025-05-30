"""Tests for the emoji SVG generator."""
import json
import os
import tempfile
from pathlib import Path

import pytest

from emojinomicon.generator import EmojiSVGGenerator


@pytest.fixture
def sample_emoji_data():
    """Create a temporary JSON file with sample emoji data."""
    data = {
        "emojis": [
            {
                "emoji": "😀",
                "name": "grinning face",
                "unicode": "1f600",
                "category": "Smileys & Emotion",
            },
            {
                "emoji": "❤️",
                "name": "red heart",
                "unicode": "2764",
                "category": "Smileys & Emotion",
            },
        ]
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(data, f)
        temp_path = f.name

    yield temp_path

    # Cleanup
    os.unlink(temp_path)


@pytest.fixture
def generator(sample_emoji_data):
    """Create an EmojiSVGGenerator instance with sample data."""
    return EmojiSVGGenerator(sample_emoji_data)


def test_load_emoji_data(generator):
    """Test loading emoji data from JSON file."""
    data = generator.emoji_data
    assert len(data) == 2
    assert data[0]["name"] == "grinning face"
    assert data[1]["name"] == "red heart"


def test_create_svg_content(generator):
    """Test creating SVG content from Unicode points with accessibility tags."""
    svg_content = generator._create_svg_content(
        "1f600", name="grinning face", desc="grinning face")
    assert "<?xml version=" in svg_content
    assert "<svg" in svg_content
    assert "<text" in svg_content
    assert "<title" in svg_content
    assert "<desc" in svg_content
    assert ">grinning face<" in svg_content


def test_generate_svg(generator):
    """Test generating a single SVG file with accessibility tags."""
    with tempfile.TemporaryDirectory() as temp_dir:
        emoji_entry = generator.emoji_data[0]
        svg_path = generator.generate_svg(emoji_entry, temp_dir)

        assert svg_path is not None
        assert os.path.exists(svg_path)
        assert svg_path.endswith(".svg")

        # Check file contents
        with open(svg_path, "r", encoding="utf-8") as f:
            content = f.read()
            assert "<?xml version=" in content
            assert "<svg" in content
            assert "<text" in content
            assert "<title" in content
            assert "<desc" in content
            assert ">grinning face<" in content


def test_generate_all_svgs(generator):
    """Test generating SVG files for all emojis with accessibility tags."""
    with tempfile.TemporaryDirectory() as temp_dir:
        svg_paths = generator.generate_all_svgs(temp_dir)

        assert len(svg_paths) == 2
        for i, path in enumerate(svg_paths):
            assert os.path.exists(path)
            assert path.endswith(".svg")
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                assert "<title" in content
                assert "<desc" in content
                assert f">{generator.emoji_data[i]['name']}<" in content


def test_convert_svg_to_png(generator):
    """Test converting SVG to PNG."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # First generate an SVG
        emoji_entry = generator.emoji_data[0]
        svg_path = generator.generate_svg(emoji_entry, temp_dir)

        # Then convert it to PNG
        png_path = generator.convert_svg_to_png(svg_path, temp_dir)

        assert png_path is not None
        assert os.path.exists(png_path)
        assert png_path.endswith(".png")


def test_invalid_emoji_data():
    """Test handling of invalid emoji data."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as f:
        json.dump({"invalid": "data"}, f)
        f.flush()

        generator = EmojiSVGGenerator(f.name)
        assert len(generator.emoji_data) == 0
