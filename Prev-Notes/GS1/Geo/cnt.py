from pathlib import Path

# Set your directory path
directory = Path(".")

# Match files in the current directory and up to 3 levels deep
patterns = [
    "*.md",       # Current directory (Level 0)
    "*/*.md",     # 1 nested folder deep (Level 1)
    "*/*/*.md",   # 2 nested folders deep (Level 2)
    "*/*/*/*.md"  # 3 nested folders deep (Level 3)
]

# Count all matching files
file_count = 0
for pattern in patterns:
    file_count += sum(1 for f in directory.glob(pattern) if f.is_file())

print(f"Total .md files (up to 3 levels deep): {file_count}")
