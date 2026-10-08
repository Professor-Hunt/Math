# PhD Qualifying Exam - Mathematics Prep

A growing, freely readable route from familiar mathematics to ideas used in PhD qualifying exams. The current four lessons cover foundations; the planned advanced modules remain future work.

## 🎓 About

This repository contains a series of mathematics lessons covering fundamental topics needed for PhD qualifying exams. Each lesson features:

- **Beautiful formatting** with KaTeX for math rendering
- **Mobile-responsive design** for studying anywhere
- **Detailed examples and solutions**
- **Practice problems** ranging from basic to exam-level
- **Four depth levels in every topic**: high-school, undergraduate, master's, and PhD-level connections, with prerequisites explained at the point of use
- **Expandable symbol explanations**: read-aloud wording, meaning in context, and a concrete example, available by touch or keyboard
- **Professional typography** optimized for reading

The level names describe the depth of the mathematics, not a reader's ability or the difficulty of the prose. A short bridge to an advanced result is an invitation to study its prerequisites, not a substitute for a full course.

## 📚 Current Lessons

### Module M1: Foundations

1. **[Lesson M1.1: Real Numbers, Properties, and Order](lesson_m1_1.html)**
   - Duration: ~2 hours
   - Prerequisites: None
   - Topics: Number classification, algebraic properties, inequalities, absolute value, completeness

2. **[Lesson M1.2: Algebraic Manipulation and Factoring](lesson_m1_2.html)**
   - Duration: ~3 hours
   - Prerequisites: M1.1
   - Topics: Polynomial arithmetic, factoring techniques, rational expressions, rationalizing denominators

3. **[Lesson M1.3: Equations and Inequalities](lesson_m1_3.html)**
   - Duration: ~4 hours
   - Prerequisites: M1.1, M1.2
   - Topics: Polynomial equations, rational equations, radical equations, absolute value equations, inequalities, sign analysis

4. **[Lesson M1.4: Functions: Definitions and Notation](lesson_m1_4.html)**
   - Duration: ~3 hours
   - Prerequisites: M1.1–M1.3
   - Topics: Functions, domain and range, composition, inverses, transformations

## 🌐 View Online

**Visit the live site: [https://professor-hunt.github.io/Math/](https://professor-hunt.github.io/Math/)**

## 🚀 Getting Started

### View Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Professor-Hunt/Math.git
   cd Math
   ```

2. Open `index.html` in your web browser

### Study on Your Phone

Simply visit the GitHub Pages URL from any mobile browser. The lessons are fully responsive and optimized for mobile reading.

## 📱 Features

- **Mobile-First Design**: Optimized for reading on phones and tablets
- **Static published pages**: Open the HTML directly; no server or runtime build is needed
- **Plain-language fallback**: Expandable explanations remain readable when the KaTeX CDN is unavailable; formatted mathematics and web fonts require a connection unless cached
- **Beautiful Math**: KaTeX renders mathematical notation perfectly
- **Dark/Light Mode**: Comfortable reading in any environment (coming soon)

## 🛠️ Technology Stack

- Pure HTML5, CSS3, and JavaScript
- [KaTeX](https://katex.org/) for mathematical notation rendering
- Google Fonts: Cormorant Garamond and Crimson Pro
- Responsive CSS Grid and Flexbox layouts

## 📖 Lesson Structure

Each lesson includes:

- **Learning Objectives**: Clear goals for the lesson
- **Table of Contents**: Navigate easily through sections
- **Theory**: Comprehensive explanations with examples
- **Practice Problems**: Basic, intermediate, and exam-level challenges
- **Full Solutions**: Detailed step-by-step solutions
- **Summary**: Key takeaways and common mistakes
- **Symbol notes**: Native expandable controls beside selected expressions, with context-specific meanings and a full plain-language reading

The maintained source for M1.1 is `lesson_m1_1.md`; the original `.txt` working note is retained. M1.2–M1.4 have Markdown sources beside their HTML. To regenerate all four HTML lessons after editing the sources, install `Markdown==3.8.2` and run `python tools/render_lessons.py`. The published site itself stays static.

## 🤝 Contributing

This is a personal study repository, but suggestions and corrections are welcome! Feel free to:

- Report errors or typos via Issues
- Suggest additional topics
- Share study tips

## 📝 License

This content is provided for educational purposes. Feel free to use these materials for your own study.

## 🎯 Roadmap

- [ ] Complete Module M1: Foundations (Lessons M1.5-M1.8)
- [ ] Add Module M2: Functions and Graphs
- [ ] Add Module M3: Calculus I
- [ ] Add Module M4: Calculus II
- [ ] Add search functionality
- [ ] Add progress tracking
- [ ] Add dark mode toggle

## 💡 Study Tips

- Work through examples before looking at solutions
- Complete practice problems at the end of each lesson
- Keep a notebook for working through problems
- Review the summary sections regularly
- Build connections between topics as you progress

---

**Happy studying!** 📐✏️
