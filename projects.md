---
layout: default
title: Projects
description: Research projects organized by theme. Cross-domain bridges first.
permalink: /projects/
---

# Projects

Organized by theme. Cross-domain bridges (LLM ↔ biology) first, then
AI internals, then biological aging, oscillatory dynamics, and finally
methods and cognition (including a deliberate negative result).

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
