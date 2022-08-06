---
layout: post
title: "Modern problems require old solution"
date: 2022-07-23 21:50:00 -0300
author: Doodles
---

Since the times of the Aztecs and the old Greeks some cultures suspected that time is ciclical. Although possibly not phisically correct or at least in practice somewhat wrong I think there's a big lesson to be learnt from looking at our past and trying to assimilate the simillarities of the present and the past.

## Politics: a pendulum

If you think the way our democracies behave today is something unique to our time because of the invention of the internet and social media, or that politicians today do or say stuff much differently than in the past then you should think twice. Democracy is something we've had for centuries and even then we, americans, believe that it's changing constantly.

You only need a little bit more time to think about it and a little bit of reading history to see that in politics there are cycles and patterns that emerge over time. The invention of the press for instance had a very simillar effect to the creation of the internet and social media by facilitating the divulgation of news and making it much faster.

Of course things like changes in way we share information are not \_trully" ciclical in a sense that if it's a change then it's "new", but the point is that the difficulties we find with every change and also the way we find solutions to these problems is sometimes assustadoramente simillar. To exemplify this I'm going to talk about a field I know a little bit more than politics.

## Computer technology: we have small memories

Not the computers, we, the humans, have a very very small memory. Why? Well, we keep reinventhing technologies once every few years and share it like it's something extremelly amazing and rejuvenating, howver most of the times it's just something we used to do in the past that we stopped to do because of some problem with the solution.

One of my favorite examples is the recent reinvention of server side rendering when it comes to web development. Server side rendering was in fact the first way we found to make "dynamic" websites, even before we had JavaScript. CGI scripts and PHP were the big thing a few decades ago, and even though they had awful problems they did the job.

Why did we stop using PHP and CGI? Well because at some time we decided we needed to make our websites feel faster and more like applications because the scope of websites was growing, and so eventually we started scripting our pages with JavaScript and eventually jQuery came along and changed everything.

jQuery was not enough. We wanted to use a single language to develop both the frontend and backend, the silver bullet language, that programmers look for since the dawn of computing (and that is never going to exist) seemed obvious: JavaScript. If we are using some much JavaScript in our applications why don't we "predownload" the pages and "render" them client side with JavaScript? No reloads, very fast, very simple to develop.

Well as it turns out single page applications are hard to develop and have awful SEO, so we take years to try and find ways to work with the awful libraries we have at our hands (if you're not working for yourself): React and AngularJS. Vercel invents NextJS and most other libraries for SPAs follow along, a new amazing reinvigorating technology to fix the hardness of development, the SEO issues and also the overreliance on the user having to run JavaScript to browser: server side rendering.

### Wait, what the \*\*\*\*?

Yes, we just reinvented the past. If you're not convinced by this example think about web assembly, which arguably existed for years with the name Java Applets and XScripts on Internet Explorer CHECK THIS CHECK THIS CHECK THIS. Think about Electron as a way to develop to multiple platforms and the fact we already had Qt, JavaFX, wxWidgets and GL-based applications.

By the way, these cross platforms applications had the same problems Electron applications face now. They are slower and they don't feel at home on the operating system, not respecting your customizations and often not following the interface guidelines of your desktop environment which makes using them confusing more often than not. Even worse is the fact that a Electron application needs to download a whole web browser (which is basically just the reinvention of a networked operating system at this point) to run.

If downloading a whole web browser to run every application doesn't sound insane and something that's going to change soon then you should take a look at the fact we are using Docker to manage dependencies on development environments instead of using package managers or virtual machines (which with KVM or Hyper-V get very fast). I'm pretty sure someone is going to find a way to grab these images and distribute them so I can deploy them. I wish we had something like that, it could be called Ansible because I like the name.

## Am I an idiot?

"What are you on about? All of these technologies you showed don't have feature parity, and the newer ones _do_ solve problems we had with the older options" - That's true, you have a great point and I see you are paying attention. The thing I mean is that we are inventing these problems ourselves. This is something we did for a long time.

Even though we have done these kinds of pendulum swings on the way we want to do things I believe it's specially worrying the field of computing. "If we built bridges like we build computers, I wouldn't need to jump to kill myself" or something along these lines, my memory is very short. Someone should write an article about these kinds of weird repetitions that happen because of our very small memory, that would be really interesting to read about. They could publish the article on some kind of way I can have a copy of the document for myself so I never forget about it.

## Conclusion

I'm not sure I have a conclusion for this. I'm just kind of mad at all of the situation of modern technology (as are most developers) but I have no idea what we could do to fix it. Something I know I'll be doing though: HODL my computer until it explodes.

And as always, have a good one.

