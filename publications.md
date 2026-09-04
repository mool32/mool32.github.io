---
layout: default
title: Publications
description: "Preprints, manuscripts, software and pre-registered negative results by Theodor Spiro — grouped by publication stage, with a DOI and code behind each entry."
permalink: /publications/
---

# Publications

All entries are authored by Theodor Spiro
(ORCID [0009-0004-5382-9346](https://orcid.org/0009-0004-5382-9346)).

They are grouped by **what stage each one is actually at**, so the list cannot read as
stronger than it is: a self-archived Zenodo preprint is not a peer-reviewed paper, and
is not presented as one. Where a DOI resolves to Zenodo, that is the archived
manuscript and its code — not a journal record.

The canonical BibTeX file is served at [`/papers.bib`]({{ '/papers.bib' | relative_url }})
and is the single source of truth for citation export; everything on this page is
generated from it.

## Under review at a journal

{% assign under_review = site.data.publications | where: "stage", "under-review" %}
{% include pub-list.html pubs=under_review %}

## Preprints

Publicly posted, not peer reviewed. `arXiv` entries are on arXiv; the rest are
self-archived on Zenodo with a permanent DOI.

{% assign preprints = site.data.publications | where: "stage", "preprint" %}
{% include pub-list.html pubs=preprints %}

## Manuscripts in progress

Complete or near-complete write-ups that are not yet posted.

{% assign ready = site.data.publications | where: "stage", "submission-ready" %}
{% assign prep = site.data.publications | where: "stage", "in-preparation" %}
{% assign running = site.data.publications | where: "stage", "in-progress" %}
{% assign manuscripts = ready | concat: prep | concat: running %}
{% include pub-list.html pubs=manuscripts %}

## Software and instruments

{% assign software = site.data.publications | where: "stage", "software-release" %}
{% assign live = site.data.publications | where: "stage", "live" %}
{% assign tools = software | concat: live %}
{% include pub-list.html pubs=tools %}

## Reports and pre-registered negatives

Results that did not go the way the pre-registration predicted, written up in full
rather than dropped.

{% assign reports = site.data.publications | where: "stage", "report" %}
{% include pub-list.html pubs=reports %}
