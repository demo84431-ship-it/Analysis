# Paper 2 — UGC NET Psychology Question Bank: Structure & Inventory

## Overview

| Metric | Value |
|---|---|
| **Total JSON Files** | 53 |
| **Total Questions** | 3,650 |
| **Year Range** | June 2004 — December 2025 |
| **Era Tags** | `UGC` (2004–2017), `NTA` (2018–2025) |
| **Subject** | Psychology — Paper II (all files), Paper III (some 2013–2017 files) |
| **Unique Units** | 10 (Unit 1–Unit 10) |
| **Unique Topics** | 228 |
| **Unique Subtopics** | 1,925 |

---

## Directory Structure

```
Paper 2/
├── 2004-2008/          (10 files, 500 questions)
├── 2009-2012/          ( 8 files, 400 questions)
├── 2013-2016/          (15 files, 900 questions)
├── 2017-2020/          (10 files, 850 questions)
├── 2021-2024/          ( 8 files, 800 questions)
└── 2025-2026/          ( 2 files, 200 questions)
```

---

## Questions Per File — Complete Inventory

### 2004-2008 (10 files, 500 questions)

| File | Questions | Subject |
|---|---|---|
| UGC_NET_Psychology_June_2004.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2004.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_June_2005.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2005.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_June_2006.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2006.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_June_2007.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2007.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_June_2008.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2008.json | 50 | Psychology — Paper II |

### 2009-2012 (8 files, 400 questions)

| File | Questions | Subject |
|---|---|---|
| UGC_NET_Psychology_June_2009.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2009.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_June_2010.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2010.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_June_2011.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2011.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_June_2012.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2012.json | 50 | Psychology — Paper II |

### 2013-2016 (15 files, 900 questions)

| File | Questions | Subject |
|---|---|---|
| UGC_NET_Psychology_June_2013.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2013.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_June_2013_Reconducted_Paper_II.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_June_2013_Reconducted_Paper_III.json | 75 | Psychology — Paper III |
| UGC_NET_Psychology_June_2014.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2014_Paper_II.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2014_Paper_III.json | 75 | Psychology — Paper III |
| UGC_NET_Psychology_June_2015_Paper_II.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_June_2015_Paper_III.json | 75 | Psychology — Paper III |
| UGC_NET_Psychology_December_2015_Paper_II.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2015_Paper_III.json | 75 | Psychology — Paper III |
| UGC_NET_Psychology_July_2016_Paper_II.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_July_2016_Paper_III.json | 75 | Psychology — Paper III |
| UGC_NET_Psychology_December_2016_Paper_II.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_December_2016_Paper_III.json | 75 | Psychology — Paper III |

### 2017-2020 (10 files, 850 questions)

| File | Questions | Subject |
|---|---|---|
| UGC_NET_Psychology_January_2017.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_January_2017_Paper_III.json | 75 | Psychology — Paper III |
| UGC_NET_Psychology_November_2017_Paper_II.json | 50 | Psychology — Paper II |
| UGC_NET_Psychology_November_2017_Paper_III.json | 75 | Psychology — Paper III |
| UGC_NET_Psychology_July_2018.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_December_2018.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_June_2019.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_December_2019.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_June_2020.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_September_2020.json | 100 | Psychology — Paper II |

### 2021-2024 (8 files, 800 questions)

| File | Questions | Subject |
|---|---|---|
| UGC_NET_Psychology_December_2020_January_2021.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_November_2021.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_December_2021_June_2022.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_March_2022_Session_1.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_March_2022_Session_2.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_June_2023.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_December_2023.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_August_2024.json | 100 | Psychology — Paper II |

### 2025-2026 (2 files, 200 questions)

| File | Questions | Subject |
|---|---|---|
| UGC_NET_Psychology_June_2025.json | 100 | Psychology — Paper II |
| UGC_NET_Psychology_December_2025.json | 100 | Psychology — Paper II |

---

## JSON File Structure

### Top-Level Schema

```json
{
  "paper_metadata": { ... },
  "content": [ ... ]
}
```

Some files also have a top-level `"permissions"` key (e.g., `settings.local.json`), but the exam JSON files consistently use only `paper_metadata` and `content`.

### `paper_metadata` Schema

```json
{
  "paper_metadata": {
    "title": "UGC NET/JRF Examination, June 2004",
    "date": "June 2004",
    "subject": "Psychology — Paper II"
  }
}
```

| Field | Type | Description |
|---|---|---|
| `title` | string | Full exam title with month and year |
| `date` | string | Exam session (e.g., "June 2004", "December 2025 - January 2026") |
| `subject` | string | Either `"Psychology — Paper II"` or `"Psychology — Paper III"` |

### `content` Array — Block Types

The `content` array contains two types of blocks:

#### 1. `questions_block`

```json
{
  "type": "questions_block",
  "range": "Q1–Q50",
  "questions": [ ... ]
}
```

| Field | Type | Description |
|---|---|---|
| `type` | string | Always `"questions_block"` |
| `range` | string | Question range (e.g., `"Q1–Q47"`, `"Q48–Q50"`) |
| `questions` | array | Array of question objects |

#### 2. `passage`

```json
{
  "type": "passage",
  "id": "passage_48",
  "heading": "### Passage (Questions 48–50)",
  "text": "While standardizing the test..."
}
```

| Field | Type | Description |
|---|---|---|
| `type` | string | Always `"passage"` |
| `id` | string | Unique passage identifier (e.g., `"passage_48"`) |
| `heading` | string | Passage heading with markdown formatting |
| `text` | string | Full passage text that the associated questions reference |

### Question Object Schema

```json
{
  "id": 1,
  "question": "When the membrane of a neuron shows -72 mV...",
  "options": [
    "(A) Excitatory post synaptic potential",
    "(B) Spike potential",
    "(C) Inhibitory post synaptic potential",
    "(D) Rest potential"
  ],
  "correct_answer": 4,
  "correct_text": "Rest potential",
  "unit": "Unit 4",
  "topic": "4.2 Neurons",
  "subtopic": "Action Potential",
  "concept": "Resting membrane potential is the stable voltage...",
  "era": "UGC",
  "year": 2004,
  "passage_ref": null,
  "table_ref": null
}
```

| Field | Type | Description |
|---|---|---|
| `id` | integer | Sequential question number within the file (1-based) |
| `question` | string | Full question text (may include markdown tables, lists, assertions) |
| `options` | array[string] | 4 options, always prefixed with `(A)`, `(B)`, `(C)`, `(D)` |
| `correct_answer` | integer | 1-indexed correct option (1=A, 2=B, 3=C, 4=D) |
| `correct_text` | string | Full text of the correct answer |
| `unit` | string | Unit number (e.g., `"Unit 4"`) |
| `topic` | string | Topic code and name (e.g., `"4.2 Neurons"`) |
| `subtopic` | string | Specific subtopic (e.g., `"Action Potential"`) |
| `concept` | string | Detailed explanation of the concept being tested |
| `era` | string | `"UGC"` (pre-2018) or `"NTA"` (2018 onwards) |
| `year` | integer | Exam year |
| `passage_ref` | string/null | Reference to passage block ID if question is passage-based |
| `table_ref` | string/null | Reference to table if question involves a table |
| `explanation` | string | *(rare)* Additional explanation field (present in some files) |

---

## Categorization by Metadata

### By Era

| Era | Period | Files | Questions |
|---|---|---|---|
| `UGC` | 2004–2017 | 37 | 2,475 |
| `NTA` | 2018–2025 | 16 | 1,175 |

### By Paper Type

| Paper | Files | Questions | Question Count Per File |
|---|---|---|---|
| Paper II | 45 | 3,050 | 50 (2004–2017) or 100 (2018–2025) |
| Paper III | 8 | 600 | Always 75 |

### By Question Count Per File

| Questions Per File | Paper | Files | Total Questions |
|---|---|---|---|
| 50 | Paper II | 29 | 1,450 |
| 75 | Paper III | 8 | 600 |
| 100 | Paper II | 16 | 1,600 |
| **Total** | | **53** | **3,650** |

> Note: The Dec 2004 file has 50 questions but uses ranges like Q1–Q47 + passage Q48–Q50, totaling 50.

### By Unit (10 Units)

| Unit | Domain |
|---|---|
| Unit 1 | History of Psychology / Schools of Psychology / Indian Psychology |
| Unit 2 | Research Methodology / Statistics / Experimental Design |
| Unit 3 | Psychological Testing / Assessment / Psychometrics |
| Unit 4 | Biological Basis of Behaviour / Physiological Psychology |
| Unit 5 | Attention, Perception, Learning, Memory |
| Unit 6 | Thinking, Intelligence, Creativity |
| Unit 7 | Personality, Motivation, Emotion, Stress |
| Unit 8 | Social Psychology / Organizational Behaviour |
| Unit 9 | Developmental Psychology / Educational Psychology |
| Unit 10 | Applied Psychology / Clinical / Counseling / Health |

---

## Structural Notes

1. **Consistent schema**: All 53 files follow the same `paper_metadata` + `content` structure. The question field set is uniform across all files.

2. **Format evolution**: The exam format changed from 2018 onwards — Paper III was discontinued and Paper II expanded from 50 to 100 questions. This is reflected in the data as the `NTA` era files consistently have 100 questions.

3. **Passage blocks**: Present in earlier files (2004–2012 primarily). They contain a passage text and heading, and the associated questions have `passage_ref` pointing to the passage ID.

4. **Topic naming varies across eras**: The same domain area may have slightly different topic names in UGC vs NTA era files (e.g., `"4.1 Biological Basis"` vs `"4.1 Biological Basis of Behaviour"` vs `"4.1 Brain Structure and Function"`).

5. **Subtopic granularity**: 1,925 unique subtopics across 3,650 questions indicates highly specific tagging — nearly every question has a distinct subtopic label.

6. **Reconducted exams**: The June 2013 session has both original and "Reconducted" versions for Paper II and Paper III, representing a rare case of exam re-administration.
