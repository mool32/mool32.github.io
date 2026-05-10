---
layout: default
title: Projects
description: Research projects organized by theme. Cross-domain bridges first.
permalink: /projects/
---

# Projects

Six directions, in this order. Cellular perception (the perceptome framework
and toolkit) is currently the active center. Comparative biology of neural
networks and aging research are the two long-running substantive threads.
Cognition and social projects, methodological work (including a deliberate
negative result), and an AI-collaborative research methodology framework
round out the portfolio.

{% for section in site.data.projects %}
<section class="proj-section">
  <h2>{{ section.category }}</h2>
  {% if section.blurb %}<p class="proj-blurb">{{ section.blurb }}</p>{% endif %}
  <ul class="proj-list">
    {% for proj in section.projects %}
    <li class="proj-item">
      <div class="proj-title"><a href="{{ proj.url }}">{{ proj.title }}</a></div>
      <div class="proj-summary">{{ proj.summary }}</div>
      <div class="proj-status">{{ proj.status }}</div>
    </li>
    {% endfor %}
  </ul>
</section>
{% endfor %}
