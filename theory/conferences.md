---
layout: page
title: "Conferences"
permalink: /conferences/
---

{% assign currentTime = site.time | date: "%s" %}

## Upcoming

{% for conference in site.data.conferences %}

  {% assign confTime = conference.endDate | date: "%s" %}
  <ul>
  {% if currentTime < confTime %}
    <li><a href="{{ conference.url }}">{{ conference.title }}: {{ conference.startDate }}-{{ conference.endDate }}</a></li>
  {% endif %}
  </ul>
  
{% endfor %}

## Past Conferences & Meetings

{% for conference in site.data.conferences %}

  {% assign confTime = conference.endDate | date: "%s" %}
  <ul>
  {% if currentTime > confTime %}
    <li><a href="{{ conference.url }}">{{ conference.title }}: {{ conference.startDate }}-{{ conference.endDate }}</a></li>
  {% endif %}
  </ul>
  
{% endfor %}
