---
layout: post
title: “Modern problems require old solutions”
date: 2022-08-06 00:55:00 -0300
author: Doodles
---

Since the Aztecs and the old Greeks, some cultures thought that time is cyclical. Although possibly not physically correct, or at least in practice somewhat wrong, I believe there's a big lesson to learn from looking at our past and trying to assimilate the similarities between the present and the past.

Warning: This is a rant, and I have not proofread it. It probably has factual and historical errors (please point them out if you can), but the point I'm trying to make should still come across.

## Politics: a pendulum

If you think how our democracies behave today is unique to our time because of the invention of the internet and social media. Or if you think that politicians today do or say stuff much differently than in the past, you should think twice. Democracy is something we've had for centuries and even then we, Americans, believe that it's changing constantly. That's one of the reasons I, Aaron Swartz, and others avoid the news.

You only need a little more time to think about it and a bit of reading history to see that in politics, cycles, and patterns emerge over time. The invention of the press for instance had a very similar effect to the creation of the internet and social media by facilitating the divulgation of news and making it much faster.

Of course, things like changes in the way we share information are not “truly” cyclical in a sense that if it's a change then it's “new”. However, the point is that the difficulties we find with every change and also the way we find solutions to these problems is sometimes frighteningly similar. To exemplify this, I'm going to talk about a field I know a bit more than politics.

## Computer technology: we have small memories

Not the computers, we, the humans, have a very, very small memory. Why? Well, we keep reinventing technologies once every few years and share it like it's something extremely amazing and rejuvenating. However, most of the time it's just something we used to do in the past that we stopped to do because of some difficulties with the solution.

One of my favorite examples is the recent reinvention of server-side rendering when it comes to web development. Server-side rendering was the first way we found to make “dynamic” websites, even before we had JavaScript. CGI scripts and PHP were the big things a few decades ago, and even though they had awful problems, they did the job.

Why did we stop using PHP and CGI? Well, because at some moment we decided we needed to make our websites feel faster and more like applications because the scope of websites was growing. So eventually we started scripting our pages with JavaScript, and eventually jQuery came along and changed everything.

jQuery was not enough. We wanted to use a single language to develop both the frontend and backend, a silver bullet language, that programmers have looked for since the dawn of computing (and that is never going to exist) seemed obvious: JavaScript. If we are using so much JavaScript in our applications, why don't we “prefetch” the pages and “render” them client-side with JavaScript? No reloads, very fast, very simple to develop.

Well, as it turns out, single-page applications are hard to develop and have awful SEO. So we take years to try to find ways to work with the awful libraries we have at our hands (if you're not working for yourself): React and AngularJS. Vercel invents NextJS and most other libraries for SPAs follow along, a new amazing reinvigorating technology to fix the hardness of development, the SEO issues, and also the overreliance on the user having to run JavaScript on the browser: server-side rendering.

### Wait, what the \*\*\*\*?

Yes, we just reinvented the past, but now it's worse and harder to work on. So much for technology and the future. If you're not convinced by this example, think about web assembly, which arguably existed for years with the names: Java Applets, and ActiveX, on Internet Explorer. Think about Electron as a way to develop to multiple platforms and the fact we already had Qt, JavaFX, wxWidgets, and GL-based applications.

By the way, these cross platforms applications had the same problems Electron applications face now. They are slower, and they don't feel at home on the operating system, not respecting your customizations and often not following the interface guidelines of your desktop environment, which makes using them confusing more often than not. Even worse is that an Electron application needs to download a whole web browser (just the reinvention of a networked operating system at this point) to run.

I think Electron is completely crazy, but if downloading an entire web browser to run every application doesn't sound insane: look at the fact we are using Docker to manage dependencies in development environments instead of using package managers or virtual machines, which with KVM or Hyper-V get very fast. 
I'm pretty sure someone is going to find a way to grab these images and distribute them, so I can deploy them. I wish we had something like that, it could be called Ansible because I like the name. Orr we could be using “containers” and a super complex borg-inspired monstrosity to manage small deployments, simply because Docker Swarm was never actually adopted by anyone.
Maybe even having a common target (instead of all the different operating systems and architectures) would be enough: “If WASM+WASI existed in 2008, we wouldn't have needed to created Docker. That's how important it is. WebAssembly on the server is the future of computing. A standardized system interface was the missing link. Let's hope WASI is up to the task!” — Solomon Hykes

## Am I an idiot?

“What are you talking about? All of these technologies you showed don't have feature parity, and the newer ones _do_ solve problems we had with the older options” — That's true, you have a great point, and I see you are paying attention. What I mean is: we are inventing these problems ourselves; this is something we have done for a long time.

Even though we have done these kinds of pendulum swings in how we want to do things, I believe it's especially worrying in the field of computing. “If we built bridges like we build computers, I wouldn't need to jump to kill myself” or something along these lines, my memory is very small. Someone should write an article about these kinds of weird repetitions that happen because of our small memory, that would be fascinating to read about. They could publish the article in some kind of way, and I can have a copy of the document for myself, so I never forget about it.

## Conclusion

I'm not sure whether I have a conclusion for this. (To be fair, I'm probably just being lazy and not proofreading anything, just so I get done with this already). I'm kind of mad at all the situation of modern technology (as are most developers), and I have no idea what we could do to fix it. Something I know I'll be doing, however: HODL my computer until it explodes.

And as always, have a good one.
