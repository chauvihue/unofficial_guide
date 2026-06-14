# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | Which main 200-level courses are required for the CS major? | CICS 210, COMPSCI 220, COMPSCI 230, COMPSCI 240, COMPSCI 250 | The main 200-level courses required for the CS major are COMPSCI 220 [5], COMPSCI 230 [5], COMPSCI 240 [5], and COMPSCI 250 [5]. Additionally, CICS 210 [5] is also a required course. Note that COMPSCI 198C is a prerequisite for COMPSCI 230 [5]. Also, CICS 110 and CICS 160 are introductory courses [5]. | Relevant | Accurate |
| 2 | What are some electives I can take for the MS CS? | CS 560, CS 576, CS 589, CS 651, CS 670, CS 690k, 651, CS 514, CS 611 | Some electives for the MS CS include COMPSCI 589 [1], STAT 525 [1], COMPSCI 603, COMPSCI 683, and COMPSCI 687 [2]. Additionally, COMPSCI 611 - Advanced Algorithms, COMPSCI 576, and COMPSCI 670 are also of interest to MS CS students [4]. COMPSCI 689 is another option [4]. | Relevant | Accurate *(Even though the courses didn't match, the courses in the answer are indeed for grad students)*|
| 3 | What are the most common reviews about Professor Parvini?| She's funny, she cares about students and will help students to understand concepts. She is disorganized though | Her course as disorganized. She is kind, funny, and nice, but her teaching style may come off as disorganized and her lecture slides and homework sheets have multiple typos. Some find class to be boring and the homeworks to be challenging. Despite this, she explains concepts clearly and gives helpful responses to questions, and tries to keep people involved. No specific course code is mentioned in the reviews.| Relevant | Accurate |
| 4 | Give me the schedule time for lectures for CS 220 in Fall 2026 | Tue Thu 04:00 PM - 05:15 PM Hasbrck134 Perretta, Tue Thu 02:30 PM - 03:45 PM CMPLABE110 Minea | I couldn't find that in the sources. | Off-target | Inaccurate |
| 5 | What are the prerequisite classes for most 300-level courses?| CICS 210, CS 240, CS 220, CS 230, CS 250, CS 320| For most 300-level courses, the prerequisite classes include COMPSCI 220 [3][4], COMPSCI 230 [7], COMPSCI 240 [1], and COMPSCI 250 [2][8]. Additionally, some courses require CICS 210 [2][5][8] or COMPSCI 187 [2][5][8] as a prerequisite. INFO 248 is also a prerequisite for some courses, particularly for INFORM majors [1][4][5]. ENGLWRIT 112 with a grade of C or better is required for CS majors in CICS 305 [1]. | Relevant | Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
