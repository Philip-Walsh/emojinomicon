"""Command-line interface for the emoji SVG generator."""
import argparse
from .generator import EmojiSVGGenerator


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Generate accessible SVG files from emoji Unicode points (using native emoji font stack)"
    )
    parser.add_argument(
        "--emoji-data",
        type=str,
        default="emoji.json",
        help="Path to the JSON file containing emoji data",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Directory to save the generated SVG files",
    )
    args = parser.parse_args()

    # Create generator
    generator = EmojiSVGGenerator(args.emoji_data)

    # Generate SVG files
    print(f"Generating accessible SVG files in {args.output_dir}...")
    svg_paths = generator.generate_all_svgs(args.output_dir)
    print(f"Generated {len(svg_paths)} SVG files.")
    print("Each SVG includes <title> and <desc> for accessibility and uses a native emoji font stack.")


if __name__ == "__main__":
    main()
