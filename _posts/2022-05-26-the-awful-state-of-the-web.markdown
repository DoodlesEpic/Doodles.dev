---
layout: post
title: "The awful state of the web"
date: 2022-05-26 17:30:00 -0300
author: Doodles
---

The web is broken. And most developers and users are making it worse. I'd like to preface this by saying I don't really have the solution to all of the modern web problems, but I know that it's completely broken and that we have to actively look for solutions to fix all of this mess.

If you've never heard of anyone saying the internet is a mess then you just haven't been here for long enough. It doesn't matter if you think the problem is fake news, proprietary software, bloatware, spyware, the splinternet, or any other problem you might think exists, the internet is fundamentally broken and needs to be completely rethought.

Now, I, personally, think that the web is broken because of JavaScript. That's what I most hate about it and all the websites available on the internet. I hold this opinion mostly because of the current over-reliance on running JavaScript to create websites. The React revolution and it's consequences have been a disaster for the human race. No, but really, most of the websites you can go to nowadays will serve you an empty page and require you to run JavaScript to render, will run Google Analytics, will show you Google Ads, etc. It's just ridiculous.

It's not this bad only because people don't care, but also because we have built a system that fundamentally rewards people for setting up websites like this. If your users have to use JavaScript to see the website this means you also get to have analytics data, customized ads that are worth much more money, and all other kinds of stuff you as a business might like. It's also gotten progressively more popular to develop this way and it seems like people don't even know there is another way to develop websites.

So in short what's the solution? In my opinion, the solution is to completely stop using JavaScript-dependent websites. And, obviously, if you are a web developer you should put the focus on making your websites more lightweight, more compatible with a multitude of devices, and avoid using JavaScript were not needed. More on this later.

## How to stop using JavaScript without disconnecting from the internet

The biggest problem to stop using JavaScript as someone who is just browsing the web is that it's just not feasible if you have to access a website like YouTube, or modern Twitter (curiosity: did you know Twitter used to have a version of their website that worked without JavaScript?). There are however ways to access the content on these websites without using their normal frontends:

- [yewtu.be](yewtu.be) (Invidious, which can be self-hosted, is a frontend for YouTube)
- [nitter.net](nitter.net) (Nitter, which can also be self-hosted, is a frontend for Twitter)
- [old.reddit.com](old.reddit.com) (Reddit, but actually bearable)
- RSS feeds and an RSS client (Any news website can now be read without even downloading their HTML)
  - Use [morss.it](morss.it) to convert feeds that only serve you partial content to full-blown articles you can read in the comfort of your RSS reader
- Go outside (A great alternative to [facebook.com](facebook.com))

I honestly believe if you are reading this you should give it a try. Disable JavaScript globally on your web browser and try to survive as much as you can without whitelisting any websites. You'll get better performance, and avoid awful websites, advertising, and tracking. Save on bandwidth. And you'll also get all of the security advantages of not having to run JavaScript from any website you run into.

I haven't really put much into the above list, but honestly, once you start disabling JavaScript on your browser and worrying about it you'll fast start to understand what websites you should bother going to and which websites you shouldn't care about. It has been a very refreshing experience to browse without JavaScript and find out so many good websites that work without it, and also have a laugh at websites that break completely in the face of not being able to run it.

## How to stop relying so much on JavaScript to develop websites

I could go on and on about why JavaScript is also bad for you as a developer, but I myself use it when needed, however, the current trend in development is to over-rely on bloated frameworks such as NextJS, NuxtJS, CRA, etc. While the browsers have become more and more friendly to websites without JavaScript. For instance, Chrome has added paint-holding when switching between pages and backlink caching which means the experience of browsing static websites has improved considerably.

Considering all of these improvements with the modern web, you as a developer should consider the following options to develop websites (although there are many more similar and maybe even better options):

- SSGs like [Jekyll](https://jekyllrb.com/) and [Hugo](https://gohugo.io/), which are awesome for things like blogs and content that constantly changes. This website is built using Jekyll
- Backends built with [PHP/Wordpress](https://wordpress.org/), [Node/Express](https://expressjs.com/), but without using JavaScript or client-side SPAs, just serve pages using the templating engine
- Good-old [static pages](http://info.cern.ch/hypertext/WWW/TheProject.html), for when your content doesn't change constantly and consists of just a few pages
- [Remix](https://remix.run/), when you need the interactivity of a SPA without the work that's needed to do similar stuff on more traditional technologies

Please, seriously consider just old static pages. If you are making a landing page, or just a portfolio that does not have a blog or constantly changing content, then you don't need a framework or a library, or anything else. What you really need is to create a file named index.html and another called styles.css, and start writing your websites. You'll get amazing performance, perfect SEO, and VERY easy deployment, and you (shouldn't) have to learn anything.

Meanwhile, Remix on the list is a weird one I have tested and I give it a pass for newer developers who might not be used to the old way of developing websites. You write your code using JavaScript but the client never has to download any JavaScript to get all the interaction, your website works using all the standard web technologies like forms to send and receive back data from the backend, which is simply amazing.

Last, but not least, static site generators like Jekyll in my opinion are seriously underrated by some developers who haven't really seen them in action. They are just amazing, customizable, fast, and easy. If you need a blog or any kind of content that constantly changes but isn't very interactive then Jekyll and Hugo will be your best friends. And please refrain from using Gatsby, graphQL, headless CMS, and other kinds of stuff that are all overkill for most projects, please, seriously consider if you actually need those before even thinking about starting.

I will write guides on some of these technologies next. Focusing mostly on how you can get to host all of your content for free (without paying for a VPS or similar) because I love free stuff.

Doodles, signing out.
