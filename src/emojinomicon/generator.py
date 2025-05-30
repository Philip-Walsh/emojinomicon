"""Module for generating SVG files from emoji Unicode points."""
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional

import emoji
from cairosvg import svg2png


class EmojiSVGGenerator:
    """Class for generating SVG files from emoji Unicode points."""

    def __init__(self, emoji_data_path: str):
        """Initialize the generator with emoji data.

        Args:
            emoji_data_path: Path to the JSON file containing emoji data
        """
        self.emoji_data_path = emoji_data_path
        self.emoji_data = self._load_emoji_data()

    def _load_emoji_data(self) -> List[Dict]:
        """Load emoji data from JSON file.

        Returns:
            List of dictionaries containing emoji data
        """
        with open(self.emoji_data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("emojis", [])

    def _is_valid_unicode(self, unicode_points: str) -> bool:
        """Check if the Unicode points are valid.

        Args:
            unicode_points: Space-separated Unicode points

        Returns:
            True if the Unicode points are valid, False otherwise
        """
        try:
            for point in unicode_points.split():
                # Skip if it's not a valid hex number
                if not re.match(r'^[0-9A-Fa-f]+$', point):
                    return False
                # Check if it's a valid Unicode point
                int(point, 16)
            return True
        except ValueError:
            return False

    def _create_svg_content(self, unicode_points: str, name: str, desc: Optional[str] = None) -> str:
        """Create SVG content for an emoji with accessibility features.

        Args:
            unicode_points: Space-separated Unicode points
            name: Name of the emoji
            desc: Description of the emoji (optional)

        Returns:
            SVG content as a string
        """
        emoji_char = "".join(chr(int(point, 16))
                             for point in unicode_points.split())
        title = name
        description = desc or name
        svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="72" height="72" viewBox="0 0 72 72" 
     role="img" 
     aria-labelledby="title desc"
     aria-label="{title}"
     aria-description="{description}"
     aria-hidden="false"
     focusable="true">
  <title id="title">{title}</title>
  <desc id="desc">{description}</desc>
  <text x="50%" y="50%" 
        dominant-baseline="middle" 
        text-anchor="middle" 
        font-size="48" 
        font-family="'Segoe UI Emoji', 'Apple Color Emoji', 'Noto Color Emoji', sans-serif"
        aria-hidden="true">
    {emoji_char}
  </text>
</svg>'''
        return svg_content

    def generate_svg(self, emoji_entry: Dict, output_dir: str) -> Optional[str]:
        """Generate SVG file for a single emoji.

        Args:
            emoji_entry: Dictionary containing emoji data
            output_dir: Directory to save the SVG file

        Returns:
            Path to the generated SVG file if successful, None otherwise
        """
        try:
            unicode_points = emoji_entry["unicode"]
            if not self._is_valid_unicode(unicode_points):
                print(
                    f"Skipping {emoji_entry.get('name', 'unknown')}: Invalid Unicode points")
                return None
            name = emoji_entry["name"].replace(" ", "_").lower()
            desc = emoji_entry.get("name", name)
            os.makedirs(output_dir, exist_ok=True)
            svg_content = self._create_svg_content(
                unicode_points, name=emoji_entry["name"], desc=desc)
            output_path = os.path.join(output_dir, f"{name}.svg")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(svg_content)
            return output_path
        except Exception as e:
            print(
                f"Error generating SVG for {emoji_entry.get('name', 'unknown')}: {e}")
            return None

    def generate_all_svgs(self, output_dir: str) -> List[str]:
        """Generate SVG files for all emojis.

        Args:
            output_dir: Directory to save the SVG files

        Returns:
            List of paths to generated SVG files
        """
        generated_files = []
        for emoji_entry in self.emoji_data:
            if svg_path := self.generate_svg(emoji_entry, output_dir):
                generated_files.append(svg_path)
        return generated_files

    def convert_svg_to_png(self, svg_path: str, output_dir: str) -> Optional[str]:
        """Convert an SVG file to PNG.

        Args:
            svg_path: Path to the SVG file
            output_dir: Directory to save the PNG file

        Returns:
            Path to the generated PNG file if successful, None otherwise
        """
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            # Generate PNG path
            png_path = os.path.join(output_dir, Path(svg_path).stem + ".png")

            # Convert SVG to PNG
            svg2png(url=svg_path, write_to=png_path)

            return png_path
        except Exception as e:
            print(f"Error converting {svg_path} to PNG: {e}")
            return None
