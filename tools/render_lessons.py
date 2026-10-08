"""Render the four lesson Markdown sources to the static GitHub Pages site.

Install the authoring dependency with ``python -m pip install Markdown==3.8.2``.
Readers only need the generated HTML; the site has no runtime build step.
"""

from __future__ import annotations

from html import escape
from pathlib import Path
import re

import markdown


ROOT = Path(__file__).resolve().parents[1]
LESSONS = (
    ("lesson_m1_1.md", "Real Numbers, Properties, and Order", "None", "~2 hours"),
    ("Lesson_M1_2_Algebraic_Manipulation_and_Factoring.md", "Algebraic Manipulation and Factoring", "M1.1", "~3 hours"),
    ("lesson_m1_3.md", "Equations and Inequalities", "M1.1, M1.2", "~4 hours"),
    ("lesson_m1_4.md", "Functions: Definitions and Notation", "M1.1–M1.3", "~3 hours"),
)


def protect_math(source: str) -> tuple[str, list[str]]:
    """Protect TeX from Markdown's backslash and underscore processing."""
    spans: list[str] = []

    def save(match: re.Match[str], display: bool) -> str:
        spans.append((r"\[" if display else r"\(") + match.group(1) + (r"\]" if display else r"\)"))
        return f"MATHPLACEHOLDER{len(spans) - 1:05d}END"

    patterns = (
        (r"\$\$(.*?)\$\$", True),
        (r"\\\[(.*?)\\\]", True),
        (r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", False),
        (r"\\\((.*?)\\\)", False),
    )
    for pattern, display in patterns:
        source = re.sub(pattern, lambda match, d=display: save(match, d), source, flags=re.S)
    return source, spans


def render(source: str) -> tuple[str, list[tuple[str, str]], int]:
    protected, spans = protect_math(source)
    body = markdown.markdown(protected, extensions=["tables", "toc", "fenced_code"])
    for number, span in enumerate(spans):
        body = body.replace(f"MATHPLACEHOLDER{number:05d}END", escape(span))
    if "MATHPLACEHOLDER" in body:
        raise ValueError("An unexpanded math placeholder remains")
    body = re.sub(r"\A<h1[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.S)
    body = re.sub(
        r"<table>.*?</table>",
        lambda m: '<div class="table-scroll" role="region" tabindex="0" aria-label="Table; scroll horizontally if needed">' + m.group(0) + "</div>",
        body,
        flags=re.S,
    )
    headings = re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>', body)
    toc = [(anchor, label) for anchor, label in headings if label.startswith(("High-school", "Undergraduate", "Master", "PhD", "Practice", "Solutions", "Summary"))]
    return body, toc, len(spans)


def main() -> None:
    for number, (source_name, title, prereqs, duration) in enumerate(LESSONS, start=1):
        source = (ROOT / source_name).read_text(encoding="utf-8")
        body, toc, math_count = render(source)
        toc_html = "\n".join(
            f'                <li><a href="#{escape(anchor)}">{escape(label)}</a></li>'
            for anchor, label in toc
        )
        previous = f' <a href="lesson_m1_{number-1}.html">← Previous lesson</a>' if number > 1 else ""
        next_link = f' <a href="lesson_m1_{number+1}.html">Next lesson →</a>' if number < len(LESSONS) else ""
        page = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lesson M1.{number}: {escape(title)} | PhD Qualifying Exam Prep</title>
    <link rel="stylesheet" href="lesson.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
</head>
<body>
    <div class="container">
        <header class="lesson-header">
            <h1>Lesson M1.{number}: {escape(title)}</h1>
            <div class="lesson-meta">
                <span class="lesson-meta-item">Module M1: Foundations</span>
                <span class="lesson-meta-item">Prerequisites: {escape(prereqs)}</span>
                <span class="lesson-meta-item">Duration: {duration}</span>
            </div>
        </header>
        <p class="level-key">The four levels mark <strong>mathematical depth</strong>. Every level explains its notation and names the background it uses. Expand the notes beside expressions for a plain-language reading and an example.</p>
        <nav class="toc" aria-label="Lesson contents">
            <h2>Contents</h2>
            <ul>
{toc_html}
            </ul>
        </nav>
        <main id="main-content">
{body}
        </main>
        <nav class="lesson-navigation" aria-label="Lesson navigation"><a href="index.html">All lessons</a>{previous}{next_link}</nav>
        <footer class="lesson-footer">PhD Qualifying Exam Preparation Series · Module M1 · Lesson {number} of 8</footer>
    </div>
    <script>
        document.addEventListener("DOMContentLoaded", () => {{
            if (typeof renderMathInElement === "function") {{
                renderMathInElement(document.body, {{
                    delimiters: [
                        {{left: "\\\\[", right: "\\\\]", display: true}},
                        {{left: "\\\\(", right: "\\\\)", display: false}}
                    ],
                    throwOnError: false
                }});
            }}
        }});
    </script>
</body>
</html>
'''
        page = "\n".join(line.rstrip() for line in page.splitlines()) + "\n"
        output = ROOT / f"lesson_m1_{number}.html"
        output.write_text(page, encoding="utf-8")
        print(f"{output.name}: {len(toc)} main links, {math_count} math expressions")


if __name__ == "__main__":
    main()
