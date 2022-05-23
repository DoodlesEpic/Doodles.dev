---
layout: page
title: Projects
permalink: /projects/
---

Follow me on [my GitHub](https://github.com/DoodlesEpic/) to have more information about my projects.

{% for project in site.data.projects %}

{% if project.topics.size > 1 %}

## [{{ project.name}}]({{project.url}})

{{ project.description}}

Project created on {{ project.createdAt }}

{% if project.language %}
Coded mainly with {{project.language}}
{% endif %}

{% if project.license %}
Licensed under {{project.license.name}}
{% endif %}

<!--
{% for topic in project.topics %}
{% if forloop.last %}
{% else %}

{{topic}},{% endif %}

{% endfor %}
 -->

{% endif%}

{% endfor %}
