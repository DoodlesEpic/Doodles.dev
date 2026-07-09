---
layout: post
title: "Introduction to Computing is dead"
date: 2026-07-09 19:48:30 -0300
author: Doodles
---

After quite a few years trying to join the best university in Latin America (at least [according to Times Higher Education](https://www.timeshighereducation.com/student/best-universities/best-universities-south-america)), I'd come to expect that computing and programming courses would've been my favorites. After all, that's what I most love studying. Reality, however, rarely meets expectations.

## Introduction to Computing

In Computer Engineering, Electrical Engineering, Computer Science, and even in various Engineering courses that are not directly related to computing, it's very common to have a course offering that allows students to have their first interactions with programming logic and experiment with writing their first programs, starting from printing "Hello, World!" and going up to, maybe, implementing some simple games in Scratch, Python, and/or the C programming language.

At the Polytechnic School of the University of São Paulo (the leading engineering school in Brazil), that course is called MAC2166. Analogous, perhaps, to Harvard's well-known CS50x (which I've already recommended to beginners in this blog before). The idea is simple: teach the basics of a programming language, get the students to solve handwritten tests, ensuring they understand the syntax and logic, and give them exercises to solve at home, which will be evaluated according to automated tests and will compose a huge part of their grades.

WHAT?! Yes... The principle of most programming courses nowadays relies on the (utopic) idea that students will have the utmost academic integrity to implement these programs at home... exactly the kind of programs that large language models, such as [GPT](https://chatgpt.com/), [Claude](https://claude.ai/), [Google's Gemini,](https://gemini.google.com/) and open models such as [GLM 5.2,](https://huggingface.co/zai-org/GLM-5.2) implement one-shot given the PDF of the exercise. And these programs will be part of the students grades.

Now, if you know a bit about [game theory](https://en.wikipedia.org/wiki/Game_theory) or, perhaps, have _just a little bit of common sense_ (i.e., you're not braindead), you understand that this is an absolutely flawed idea from the get-go, which will lead to frustration and horrible teaching results: no one will learn anything, and the highest grades will be assigned to the most dishonest students.

## Preventing cheating

Now, you know teachers at good universities, having orders of magnitude higher wages than the average person in the country, will be smart and will have thought about this. Surely, they have _something_ to prevent academic dishonesty. Right? Well, I present to you PDF prompt injection.

Wait, that's not what you expected? Nothing grandiose? That's it. The only strategies to prevent cheating in the programming subjects are things like tiny white-on-white text and metadata on the PDF that instructs LLM to write code with variable names and comments, which, while they look inoffensive, serve as [canaries](https://www.reddit.com/r/todayilearned/comments/1gq7dhp/til_the_term_canary_in_software_deployment_comes/) alerting that the student has cheated.

The big problem is that neither ChatGPT 5.5 high nor Claude Opus 4.8 will get caught in these injection attempts. Worse yet, whenever told to look for them, ChatGPT 5.5 high is pretty good at dissecting the PDF metadata, comparing the PDF to PNGs generated from it, and finding stuff that shouldn't be there. And, well, I mean... If you just convert the PDF to PNG using something like [CloudConvert](https://cloudconvert.com/pdf-to-png), there's not much chance any injection attempts will remain, and LLMs are pretty good at reading crystal-clear PNGs with text.

## No one's learning anything

While I got into university with more than 10 years of baggage programming, working with embedded, web, mobile, games, and other kinds of computing applications, some people get into computing courses with no beforehand baggage and _need_ a good foundational course to get going instead of just becoming React-monkeys or, worse yet, MonkeyGPT.

And, honestly, we already know all of this is a disaster. Take a look at these:
- [Professor denounces mass AI fraud on an exam at Brown](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html)
- [Failing grades soar with AI usage, dwindling math skills in Berkeley CS classes](https://www.dailycal.org/news/campus/academics/failing-grades-soar-as-professors-see-greater-ai-usage-dwindling-math-skills-in-uc-berkeley/article_16fad0bf-02cb-4b8c-8d88-888ffd9f8608.html)

After reading through tons of different articles that show the AI has simply made academic dishonesty way too easy and way too worth it, it's time to reevaluate a lot of the current strategies we use to teach and to evaluate students.

## What's left for the future

While, at first, I'll admit that take-home tests were never a good idea to begin with, to just stay with them in computing courses is simply to admit defeat and embrace academic dishonesty. No student in a competitive environment, with multiple hard subjects, maybe looking into getting an internship, an exchange, or a double diploma, will, in their right mind, not use LLMs to augment their take-home tests, get them done faster, or fix issues they're struggling with.

That means take-home tests have to go away. For good. So what's left to evaluate students other than pen-and-paper tests that no student that's been learning programming for a few months and has had no previous experience will manage?

With all of this said, in my opinion, programming labs, where students use an IDE or decent code editor on a school-provided computer in a room with other students and monitors, are a _great_ way to get things going well. Allow them to talk with each other, show code, and ask questions to teachers and monitors. Get'em talking and excited about completing a challenge or learning how to get the computer to do certain things, while not grading them based on whether they completed the task perfectly or not, but, rather, by actual human-perceived performance improvement, which is measured by simply looking at the students.

In American and European universities, with classes that are composed of hundreds of students, that probably means dividing classes into multiple groups. However, here at the University of São Paulo, only about 70 students compose the Computer Engineering class of 2026 (of which I'm part of). That's a perfectly reasonable amount of people to provide one or two synchronous labs for everyone and use them for teaching and evaluation.

## A brief note for the future

If you're worried about AI taking your job (you should be) or preoccupied with whether we should regulate these AI companies (we can't), keep this in mind: technological advancement has always been scary and will always be. At its core, scientific and technological advancement means becoming more and more knowledgeable about the world around us and abusing reality to conform to what we'd like it to be. That is, what's to be scared of is not the science or technology we produce today and tomorrow, but, rather, who owns it and what we decide to do with it.

I hope that serves as a reminder that we still live, ultimately, in a flawed, unequal, and beautiful human world, and as always, I wish you a good one!

## AI disclaimer

I do not use large language models to produce writing. I'm also not very fond of re-reading my texts multiple times, so I'm sorry if the writing is a bit sloppy or messy at times. I do, however, utilize [LanguageTool](https://languagetool.org/), which IS AI-based, to correct grammar and ~~ortography~~ orthography mistakes, as I have done ever since I've started publishing texts to this blog. Hopefully, that makes the text better to read without ever removing from it my writing style and logical ~~idiossincracies~~ idiosyncrasies that make it ultimately my writing and my thinking.
