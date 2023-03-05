+++
title = "Umberto Eco's Index Cards in Notion"
slug = "Umberto Eco's Index Cards in Notion"
date = "2020-04-20"
tags = ["notion", "productivity", "workflow", "experience-report"]
category = ["notion", "productivity", "workflow", "experience-report"]
description = "Umberto Eco's Index Cards in Notion"
author = "Sushant Srivastava"
draft = false
+++
{{< figure src="/images/HowToWriteThesis.png" class="mid">}}


Imagine what it was like doing any kind of research before the internet. What would have been the older [tab-switching-browsing-bookmarking](http://www.authorgrahambrown.com/300-year-old-tool-that-lets-you-have-7-tabs-er-books-open-at-once/) equivalent? How would someone who was doing research, selected, copied, and pasted text from the reading material? I imagine they would have copied the text by hand and annotated the source material in their notebook. Doing research was an arduous task in the early days without the internet.

The thought of researching in pre-internet days is what makes reading Umberto Eco's ["How to Write a Thesis"](https://www.goodreads.com/book/show/23461426-how-to-write-a-thesis) much more enjoyable. [Umberto Eco](https://en.wikipedia.org/wiki/Umberto_Eco) was an Italian philosopher and scholar. I read his books, ["In the name of the rose"](https://www.goodreads.com/book/show/119073.The_Name_of_the_Rose) and ["Foucault's pendulum"](https://www.goodreads.com/book/show/17841.Foucault_s_Pendulum) when I was in college. I found his fiction scholarly but inaccessible at times, which made me skeptical about picking his non-fiction book. I was surprised. Far from being a dry, academic run-down of what it entails to author a thesis, it is a fun and engaging read about organizing personal knowledge. It is chock-full of exciting ideas.

The most exciting idea which spoke to me was the idea of having a system of Index Cards. Umberto Eco used an organization of index cards to jot down, elaborate, understand, and ruminate on scholarly publications.

In his book, Umberto Eco describes using different collections of Index Cards. Each group serves a useful purpose, for example, the Quotes Index Card Collection is used to collate, manage, and cross-references quotes from the study material. These are some of the collections of Index Cards that Eco explains:

- **Bibliographic Index Cards**: Bibliographic cards have information about the title of the book or a journal, where the book is found in the library, the information about its authorship, and where the book or journal was published.
- **Reading Index Cards**: These cards are crucial to the entire setup. In this card, Umberto Eco would jot down the summary of the content read and his own thoughts.
- **Connection Index Cards**: Do you recall seeing "Evidence Boards" in investigative fiction where the team tacks pin and threads of evidence between items pinned on the board?  Well, the connection Index card serves the same purpose for drawing a connection between ideas, notes, questions, and quotes.
- **Question Index Cards**: These cards are for the questions that a researcher might have during their research.
- **Quotes Index Cards**: These cards are used to jot down interesting and insightful quotes.

These cards are color-coded and arranged in alphabetical order in a collection of index cardholders.

I am always on the lookout for interesting ideas about organizing information, so I decided to replicate Eco's system using my tool of choice these days - [Notion](https://www.notion.so/).

These two features of "Notion" empower this setup:

- [Databases](https://www.notion.so/Intro-to-databases-fd8cd2d212f74c50954c11086d85997e): We create a new database for each type of Index Card with its own quick add template.
- [Relation Properties](https://www.notion.so/Relations-rollups-fd56bfc6a3f0471a9f0cc3110ff19a79): The Relation property provides a link between any two documents. This is useful because we can then enable connections between two different cards.

In this blog post, I will describe how I set up a simple Index Card Application using Notion.

# The Setup
{{< figure src="/images/TheSetup.png" class="float-right">}}

Lets first create databases for each type of Index Card. We create database for different cards so that we can assign a template for creating new index card of that type. It also helps in managing references between the index cards.

Let us take a look at how we can create databases and template for different index cards.



## Bibliographic Index Card

For creating a collection of Bibliographic Index Cards, we follow the following steps:
1. Create a new page, "Bibliographic Cards."
2. On the newly created page, we create a new database, for now, we will create an inline database.
3. Next, we customize what information is available when we create a new Bibliographic Index Card. Click on "New Template," and in the form that shows up customize the card with properties and page structure.

{{< figure src="/images/Bibliographic.png" class="mid">}}

Notice that I make use of properties extensively here. The "Project" property refers to the
["Project"](http://www.ssushant.in/2020/04/06/using-notion-as-a-productivity-tool/) that I created as part of the ["PARA"](https://fortelabs.co/blog/how-to-build-a-second-brain-in-notion/) workflow.

Also, I was inspired by how Umberto Eco details what should go in the Bibliographic Index card. Take a look:

{{< figure src="/images/EcoBibCard.png" class="mid">}}

### What would dial it up to Eleven

In the movie ["This Is Spinal Tap,"](https://en.wikipedia.org/wiki/This_Is_Spinal_Tap) one of the guitarists had an amplifier with notches that went up to Eleven. The phrase "Up to Eleven" has entered everyday speech where it means - up to a maximum value. What features or auxiliary tooling would amplify our use of this Index Card Application.

- [Zotero](https://www.zotero.org/)-like Chrome Extension which will enable writing a reference directly from a web page.
- I do a lot of my reading on Kindle and Apple Books. If there was a contextual action that would export any books' publishing information into this database, it would be cool!
- Lastly, people who do research are likely to use a reference management annotation called "Reftex." If these bibliographic entries can be exported into [reftex](https://www.gnu.org/software/reftex/)-syntax, then nothing like it.

## Readings Index Card

Readings Index Card collection is made in the same vein as the Bibliographic Index Card Collection. Here is what mine looks like:
{{< figure src="/images/ReadingIndexCard.png" class="mid">}}

Notice that I have sections for writing notes and jotting down my own thoughts. This Index card is for reflection. Umberto Eco calls it the most crucial card in his collection.

My understanding is that whereas Bibliographic cards are placeholders of references, the Reading Cards are for summarising the material after having "chewed" on it. Therefore, the card has a section for presenting our own thoughts. ["Progressive Summarization"](https://fortelabs.co/blog/progressive-summarization-a-practical-technique-for-designing-discoverable-notes/) is a particularly useful technique here. Without summarization and including our personal opinions, the collection becomes just a list of annotated bookmarks.

### What would dial it up to Eleven

- The features from the Bibliographic Cards are useful here as well.
- For people who like [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition), if we had a functionality to export the points to remember in a flash card format, then it would be great.

## Connection Index Card

Umberto Eco explains a research-writing methodology that I like to call "Outline-driven development." Here, we refine and expand on a basic outline which evolves into the entire research. The framework should contain the crucial points of research with supporting arguments.
The connections can be linked by referring to other cards using ["embed"](https://www.notion.so/Embeds-6b7133323590447b9d8e963c136ebce5) or using a link to another page.

{{< figure src="/images/ConnectionIndexCard.png" class="mid">}}


Notice that I have not added too much structure in all the pages. Notion provides this flexibility where I can add as little information as I want to set the ball rolling. The design can evolve as my workflow evolves.

## Question Index Card
{{< tweet user="grantdraws" id= 636539481634418688 >}}
You will have questions in your research. One of the researches have all the outline headings framed as questions. When I created my template from the Questions Index Card, I kept the layout simple. I want this page to grow over time.

{{< figure src="/images/QuestionIndexCard.png" class="mid">}}


## Quote Index Card

Last, but not the least the Quote Index Card is for managing original quotes from the authors.

This is what my setup looks like:

{{< figure src="/images/QuoteIndexCard.png" class="mid">}}


To quote Umberto Eco, this is what managing and growing the collections feels like:

> *The result is something majestic*



### What would dial it up to Eleven

As I mentioned before, I like to read books on Kindle and Apple iBooks. Both pf these applications
have highlighting feature. I like to highlight quotes and insights. If there was a way to export
them to the Quotes cards, then it would be awesome. I am aware of the Github code,
https://github.com/yannick-cw/notionfy which is a step in the right direction.

# The Habit Loop

How do we put this workflow in practice? To answer this question, we should tap into the insights from the book - ["The Power of Habit."](https://charlesduhigg.com/how-habits-work/) Any habit that we want to sustain for a long time should hook into the cue-routine-reward loop. Nowhere does this ring truer than in adopting a new software tool. The triggers or cues for creating index cards should be when we are reading something interesting or relevant to any area where we want our understanding to grow. Everyone's cue-routine-reward is personal. Make sure that you have identified this loop for creating index cards like ours.

# Summary

Notion's Databases is a powerful feature. You can model, organize and collect related data using databases. In this blog post, I modelled an Index card Application for managing research or research-like projects. What I liked about Notion was that it was almost effortless to prototype and iterate on the Index Card Idea. It was also super-easy to put this into practice and test the waters.
