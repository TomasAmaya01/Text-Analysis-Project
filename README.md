# Text-Analysis-Project

**Please read the [instructions](instructions.md).**


For part 1 of the project I tried out 2 data sources and ended up choosing Wikipedia.To analyze the text I did characterized by word frecuency, I computed summary statistics(identified top 10 most used words), and I removed stop words so that the top 10 list would be "clean" with only key words.

2. **Implementation (~1-2 paragraphs)**

The architectural part of the project consists of 3 primary components, data ingestion, text processing and frequency analysis.I chose to use the code for wikipedia ingestion ensuring that both title and content were retrieved.For the processing stage I made every word in the text lower case so it wouldnt "categorize" the same word twice and I used regex to retrieve the words.

For the frequency analysis I used Counter module to count and summarize frequency of a word.

3. **Results (~1-3 paragraphs + figures/examples)**

Present what you accomplished in your project:


I was curious about what exactly is mentioned when you look up PGA Tour in wikipedia.Is it the history of the tour itself?The accomplishments that have been made by players throught the years?The biography of the people behind the tour? After analyzing the 10 most used words in the wikipedia site I realized it was more player focused.How much money they have and are making,what tournaments have they won, their season statistics etc...

4.**Reflection (~1-2 paragraphs)**


I think the end output was exactly what I was looking for, I thought it was challeging to merge every part of code that you gave us.I had to tweak the code you gave to acces wikipedia for example and put it under a defined function.I thinlk based on what I wanted to do I choose the appropriate sources and process mechanisms.


I think just going over every GenAi tool was great becuase it widened my perspective on what you can do to analyze text in python code.