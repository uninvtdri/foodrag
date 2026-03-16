My 15 New Food Items

Filipino Cultural Cuisine
1. Sinigang - Sour tamarind soup with pork or shrimp
2. Igado - Ilocano pork and organ meat stew
3. Caldereta - Beef stew in tomato sauce with liver spread
4. Tinolang Manok - Ginger chicken soup with green papaya
5. Bulalo - Slow-cooked beef bone marrow soup from Batangas

Healthy Foods
6. Oatmeal - High fiber, sustained energy
7. Boiled Egg - Complete protein, 75 calories
8. Air-Fried Chicken Breast - 31g protein per 100g
9. Tofu - Complete plant protein
10. Steamed Fish - High protein, omega-3 rich

International Dishes
11. Lasagna - Italian layered baked pasta
12. Sushi - Japanese vinegared rice with raw fish
13. Hamburger - American ground beef patty in a bun
14. Croissant - French laminated butter pastry
15. Tacos - Mexican corn tortilla street food

How to Run
1. Install Ollama and pull models: `ollama pull mxbai-embed-large` and `ollama pull llama3.2`
2. Clone repo: `git clone https://github.com/uninvtdri/food-rag-web-app.git`
3. Install deps: `pip3 install chromadb requests`
4. Run: `python3 rag_run.py`

Personal Reflection
This project was harder than I expected. I thought it was just about adding food data and running a script but there were a lot of steps involved. Setting up Ollama, downloading the models, forking the repo, and dealing with GitHub tokens took a while to figure out.

The GitHub token part was new to me. I did not know you could not use your regular password to push code and that you needed a personal access token instead.

When the system finally worked it was cool to see it retrieve the right food when I asked about it. When I asked what is sinigang it found the correct entry and used it to answer. It does not just look for the exact word, it finds things related in meaning. That is what vector embeddings do and it made more sense after actually seeing it work.

Adding Filipino foods was the part I enjoyed the most. Sinigang, igado, caldereta, tinolang manok, and bulalo are dishes I grew up with so it felt good to see the AI answer questions about them.

Overall I learned that AI is not magic. It is just data, tools, and a process you have to set up correctly.
