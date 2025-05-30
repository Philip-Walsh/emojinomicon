### Emojinomicon 📜✨

**Welcome to the Emojinomicon, a mystical repository of SVG emoji assets!** Just like the legendary Necronomicon, this collection contains powerful symbols that can transform your digital realms. Use these emojis to add flair, whimsy, and character to your projects. 

---

#### 🌟 **What's Inside?**
- A treasure trove of SVG emojis ready for diverse uses:
  - **Backgrounds**
  - **Cursors**
  - **Icons**
  - **Decorative Elements**

---

#### 🔮 **Example Uses**

1. **Using an Emoji as a Background**
   ```css
   .emoji-background {
	    background: url("https://raw.githubusercontent.com/Philip-Walsh/emojinomicon/main/src/robot.svg"), linear-gradient(135deg, #0f2027, #203a43);
	    background-size: 30px 30px, cover;
       height: 100vh; /* Full viewport height */
       width: 100vw; /* Full viewport width */
   }
   ```

2. **Using an Emoji as a Cursor**
   ```css
   .emoji-cursor {
       cursor: url("https://raw.githubusercontent.com/Philip-Walsh/emojinomicon/src/grinning-face.svg"), auto;
   }
   ```

3. **Adding an Emoji Icon to Buttons**
   ```css
   .emoji-button {
       background: url("https://raw.githubusercontent.com/Philip-Walsh/emojinomicon/src/thumbs-up.svg") no-repeat;
       padding-left: 30px; /* Space for emoji */
       height: 50px; /* Height of the button */
       border: none;
       cursor: pointer;
   }
   ```

4. **Decorating a Header with Emojis**
   ```css
   .emoji-header {
       background-image: url("https://raw.githubusercontent.com/Philip-Walsh/emojinomicon/src/sparkles.svg");
       background-size: 50px; /* Adjust size */
       padding: 20px;
       text-align: center;
   }
   ```

---

#### 📜 **How to Get Started**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Philip-Walsh/emojinomicon.git
   cd emojinomicon
   ```

2. **Integrate the Emojis in Your CSS**
   Copy the URL of your desired emoji from the repository and use the examples above to incorporate them into your styles.

---

#### 🔄 **Automated SVG Generation**

The repository includes an automated workflow to generate SVGs with accessibility features. Here's how to use it:

1. **Local Generation**
   ```bash
   # Install the package
   pip install -e .
   
   # Generate SVGs
   python -m emojinomicon --emoji-data emoji.json --output-dir output
   ```

2. **Automated Generation via GitHub Actions**
   To trigger SVG generation in CI/CD:
   - Make your changes to `emoji.json` or the source code
   - Include `[generate-svgs]` in your commit message:
     ```bash
     git commit -m "Update emoji data [generate-svgs]"
     ```
   - Push to the master branch
   
   The workflow will:
   - Generate new SVGs with accessibility features
   - Commit them with the message "Update generated SVGs [skip ci]"
   - Push them back to the repository

   Note: The workflow only runs when:
   - Changes are made to `emoji.json`, `src/` directory, or the workflow file
   - The commit message contains `[generate-svgs]`
   - The changes are pushed to the master branch

---

#### ✨ **Unleash Your Creativity!**
The Emojinomicon is more than just a collection—it's a source of inspiration! Mix and match emojis to create your own unique designs. Explore the magic within, and let your projects shine! 🌈

---

**Join the journey into the Emojinomicon!** Happy coding! 🧙‍♂️💻
