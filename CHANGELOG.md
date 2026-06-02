# 🗓️ Major Updates History

### Jan 20, 2026
- You can now simultaneously use chrome, while bot continues applying in a new window

### Jul 20, 2024
- Contributions from community have been added
- Better AI support, minor bug fixes

### Nov 28, 2024
- Patched to work for latest changes in Linkedin.
- Users can now select to follow or not follow companies when submitting application.
- Frameworks for future AI Developments have been added.
- AI can now be used to extract skills from job description. 

### Oct 16, 2024
- Framework for OpenAI API and Local LLMs
- Framework for RAG

### Sep 09, 2024
- Smarter Auto-fill for salaries and notice periods
- Robust Search location filter, will work in window mode (No need for full screen)
- Better logic for Select and Radio type questions
- Proper functioning of Decline to answer questions in Equal Employment opportunity questions
- Checkbox questions select fail bug fixed
- Annotations are clearer in instructions for setup

### Sep 07, 2024
- Annotations for developers
- Robust input validations
- Restructured config file
- Fixed pagination bug

### Aug 21, 2024
- Performance improvements (skip clicking on applied jobs and blacklisted companies)
- Stop when easy apply application limit is reached
- Added ability to discard from pause at submission dialogue box
- Added support for address input
- Bug fixed radio questions, added support for physical disability questions
- Added framework for future config file updates

### June 19, 2024
- Major Bug fixes (Text Area type questions)
- Made uploading default resume as not required

### May 15, 2024
- Added functionality for textarea type questions `summary`, `cover_letter`(Summary, Cover letter); checkbox type questions (acknowledgements)
- Added feature to skip irrelevant jobs based on `bad_words` 
- Improved performance for answering questions
- Logic change for masters students skipping
- Change variable names `blacklist_exceptions` -> `about_company_good_words` and `blacklist_words` -> `about_company_bad_words`
- Added session summary for logs
- Added option to turn off "Pause before Submit" until next run

### May 05, 2024
- For questions similar to "What is your current location?", City posted in Job description will be posted as the answer if `current_city` is left empty in the configuration
- Added option to over write previously saved answers for a question `overwrite_previous_answers`
- Tool will now save previous answer of a question
- Tool will now collect all available options for a Radio type or Select type question
- Major update in answering logic for Easy Apply Application questions
- Added Safe mode option for quick stable launches `safe_mode`

### May 04, 2024
- Added option to fill in "City, state, or zip code" search box `search_location`
- Bug fixes in answering City or location question
