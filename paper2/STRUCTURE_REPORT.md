# UGC NET Psychology Paper 2 — Dataset Structure Report

## Directory Structure

```
Paper 2/
├── 2004-2008/          (10 files)
├── 2009-2012/          (8 files)
├── 2013-2016/          (15 files)
├── 2017-2020/          (10 files)
├── 2021-2024/          (8 files)
└── 2025-2026/          (2 files)
```

**Total JSON files: 53**
**Total questions: 3,650**

---

## JSON File Structure

### Top-Level Schema

```json
{
  "paper_metadata": {
    "title": "UGC NET/JRF Examination, <Month> <Year>",
    "date": "<Month> <Year>",
    "subject": "Psychology — Paper II"  // or "Paper III"
  },
  "content": [
    // Array of content blocks (questions_block and passage types)
  ]
}
```

### Content Block Types

#### 1. `questions_block`

```json
{
  "type": "questions_block",
  "range": "Q1–Q50",
  "questions": [
    {
      "id": 1,
      "question": "Question text here...",
      "options": [
        "(A) Option A",
        "(B) Option B",
        "(C) Option C",
        "(D) Option D"
      ],
      "correct_answer": 2,           // 1-indexed option number
      "correct_text": "Option B",    // Full text of correct answer
      "unit": "Unit 4",             // Syllabus unit
      "topic": "4.2 Neurons",       // Topic within unit
      "subtopic": "Action Potential", // Specific subtopic
      "concept": "Explanation of the concept...", // Detailed concept explanation
      "era": "UGC",                 // "UGC" (2004-2019) or "NTA" (2020+)
      "year": 2004,                 // Exam year
      "passage_ref": "passage_48",  // Links to passage block (null if standalone)
      "table_ref": null             // Reserved field (unused in current data)
    }
  ]
}
```

#### 2. `passage`

```json
{
  "type": "passage",
  "id": "passage_48",               // Unique passage identifier
  "heading": "Passage (Questions 48–50)",
  "text": "Passage text content..."
}
```

---

## Question Count by Folder

| Folder | Files | Questions | Questions per File |
|--------|-------|-----------|-------------------|
| 2004-2008 | 10 | 500 | 50 (all files) |
| 2009-2012 | 8 | 400 | 50 (all files) |
| 2013-2016 | 15 | 900 | 50 (Paper II), 75 (Paper III) |
| 2017-2020 | 10 | 850 | 50-100 (varies) |
| 2021-2024 | 8 | 800 | 100 (all files) |
| 2025-2026 | 2 | 200 | 100 (all files) |
| **Total** | **53** | **3,650** | — |

---

## Per-File Question Counts

### 2004-2008 (10 files, 500 questions)
| File | Questions |
|------|-----------|
| UGC_NET_Psychology_December_2004.json | 50 |
| UGC_NET_Psychology_December_2005.json | 50 |
| UGC_NET_Psychology_December_2006.json | 50 |
| UGC_NET_Psychology_December_2007.json | 50 |
| UGC_NET_Psychology_December_2008.json | 50 |
| UGC_NET_Psychology_June_2004.json | 50 |
| UGC_NET_Psychology_June_2005.json | 50 |
| UGC_NET_Psychology_June_2006.json | 50 |
| UGC_NET_Psychology_June_2007.json | 50 |
| UGC_NET_Psychology_June_2008.json | 50 |

### 2009-2012 (8 files, 400 questions)
| File | Questions |
|------|-----------|
| UGC_NET_Psychology_December_2009.json | 50 |
| UGC_NET_Psychology_December_2010.json | 50 |
| UGC_NET_Psychology_December_2011.json | 50 |
| UGC_NET_Psychology_December_2012.json | 50 |
| UGC_NET_Psychology_June_2009.json | 50 |
| UGC_NET_Psychology_June_2010.json | 50 |
| UGC_NET_Psychology_June_2011.json | 50 |
| UGC_NET_Psychology_June_2012.json | 50 |

### 2013-2016 (15 files, 900 questions)
| File | Questions |
|------|-----------|
| UGC_NET_Psychology_December_2013.json | 50 |
| UGC_NET_Psychology_December_2014_Paper_II.json | 50 |
| UGC_NET_Psychology_December_2014_Paper_III.json | 75 |
| UGC_NET_Psychology_December_2015_Paper_II.json | 50 |
| UGC_NET_Psychology_December_2015_Paper_III.json | 75 |
| UGC_NET_Psychology_December_2016_Paper_II.json | 50 |
| UGC_NET_Psychology_December_2016_Paper_III.json | 75 |
| UGC_NET_Psychology_July_2016_Paper_II.json | 50 |
| UGC_NET_Psychology_July_2016_Paper_III.json | 75 |
| UGC_NET_Psychology_June_2013.json | 50 |
| UGC_NET_Psychology_June_2013_Reconducted_Paper_II.json | 50 |
| UGC_NET_Psychology_June_2013_Reconducted_Paper_III.json | 75 |
| UGC_NET_Psychology_June_2014.json | 50 |
| UGC_NET_Psychology_June_2015_Paper_II.json | 50 |
| UGC_NET_Psychology_June_2015_Paper_III.json | 75 |

### 2017-2020 (10 files, 850 questions)
| File | Questions |
|------|-----------|
| UGC_NET_Psychology_December_2018.json | 100 |
| UGC_NET_Psychology_December_2019.json | 100 |
| UGC_NET_Psychology_January_2017.json | 50 |
| UGC_NET_Psychology_January_2017_Paper_III.json | 75 |
| UGC_NET_Psychology_July_2018.json | 100 |
| UGC_NET_Psychology_June_2019.json | 100 |
| UGC_NET_Psychology_June_2020.json | 100 |
| UGC_NET_Psychology_November_2017_Paper_II.json | 50 |
| UGC_NET_Psychology_November_2017_Paper_III.json | 75 |
| UGC_NET_Psychology_September_2020.json | 100 |

### 2021-2024 (8 files, 800 questions)
| File | Questions |
|------|-----------|
| UGC_NET_Psychology_August_2024.json | 100 |
| UGC_NET_Psychology_December_2020_January_2021.json | 100 |
| UGC_NET_Psychology_December_2021_June_2022.json | 100 |
| UGC_NET_Psychology_December_2023.json | 100 |
| UGC_NET_Psychology_June_2023.json | 100 |
| UGC_NET_Psychology_March_2022_Session_1.json | 100 |
| UGC_NET_Psychology_March_2022_Session_2.json | 100 |
| UGC_NET_Psychology_November_2021.json | 100 |

### 2025-2026 (2 files, 200 questions)
| File | Questions |
|------|-----------|
| UGC_NET_Psychology_December_2025.json | 100 |
| UGC_NET_Psychology_June_2025.json | 100 |

---

## Metadata-Based Categorization

### By Era
| Era | Questions | Period |
|-----|-----------|--------|
| UGC | 2,250 | 2004–2019 |
| NTA | 1,400 | 2020–2026 |

### By Paper Type
| Paper Type | Questions | Notes |
|------------|-----------|-------|
| Paper II (single) | 2,700 | Standard 50 or 100 question papers |
| Paper II (split) | 350 | Part of Paper II+III combination |
| Paper III | 600 | Extended 75-question papers |

### Content Block Structure by Era

**2004-2012 (50 questions):**
- 3 content blocks: `questions_block` (Q1-Q47) → `passage` → `questions_block` (Q48-Q50)

**2013-2016 (50 or 75 questions):**
- Paper II: 3 blocks: `questions_block` (Q1-Q45) → `passage` → `questions_block` (Q46-Q50)
- Paper III: 3 blocks: `questions_block` (Q1-Q70) → `passage` → `questions_block` (Q71-Q75)

**2017-2020 (50, 75, or 100 questions):**
- 50-question: Same as 2013-2016 Paper II
- 75-question: Same as 2013-2016 Paper III
- 100-question: 6 blocks: `questions_block` (Q1-Q45) → `passage` → `questions_block` (Q46-Q50) → `questions_block` (Q51-Q95) → `passage` → `questions_block` (Q96-Q100)

**2021-2026 (100 questions):**
- 5 blocks: `questions_block` (Q1-Q90) → `passage` → `questions_block` (Q91-Q95) → `passage` → `questions_block` (Q96-Q100)

---

## Question Field Reference

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Sequential question number within the paper |
| `question` | string | Full question text (may include markdown tables for match-the-list questions) |
| `options` | string[4] | Four options labeled (A) through (D) |
| `correct_answer` | integer | 1-indexed correct option number (1=A, 2=B, 3=C, 4=D) |
| `correct_text` | string | Full text of the correct answer |
| `unit` | string | Syllabus unit (e.g., "Unit 4") |
| `topic` | string | Topic within unit (e.g., "4.2 Neurons") |
| `subtopic` | string | Specific subtopic (e.g., "Action Potential") |
| `concept` | string | Detailed explanation of the tested concept |
| `era` | string | "UGC" (pre-2020) or "NTA" (2020+) |
| `year` | integer | Exam year |
| `passage_ref` | string\|null | Links to passage block ID (null for standalone questions) |
| `table_ref` | string\|null | Reserved field (currently unused — always null) |

### Passage Block Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always "passage" |
| `id` | string | Unique passage identifier (e.g., "passage_48") |
| `heading` | string | Passage heading with question range |
| `text` | string | Full passage text |

---

## Topic Distribution (Sample: June 2025)

| Unit | Topic | Questions |
|------|-------|-----------|
| Unit 1 | 1.1 Eastern Psychological Systems | 8 |
| Unit 1 | 1.2 Western Schools of Psychology | 2 |
| Unit 1 | 1.3 Knowledge Paradigms | 1 |
| Unit 2 | 2.1 Foundations of Research | 2 |
| Unit 2 | 2.5 Methods of Research | 1 |
| Unit 2 | 2.6 Descriptive Statistics | 2 |
| Unit 2 | 2.7 Inferential Statistics | 6 |
| Unit 3 | 3.1 Principles of Testing | 2 |
| Unit 3 | 3.2 Test Construction | 1 |
| Unit 3 | 3.4 Validity | 2 |
| Unit 3 | 3.5 Norms and Standardization | 1 |
| Unit 3 | 3.6 Types of Tests by Domain | 2 |
| Unit 3 | 3.7 Applications | 1 |
| Unit 4 | 4.2 Neurons | 1 |
| Unit 4 | 4.3 Nervous System | 6 |
| Unit 4 | 4.6 Genetics and Behavior | 2 |
| Unit 4 | 4.7 Neuroplasticity | 1 |
| Unit 5 | 5.1 Attention | 2 |
| Unit 5 | 5.2 Perception | 3 |
| Unit 5 | 5.3 Learning | 6 |
| Unit 5 | 5.4 Memory | 3 |
| Unit 5 | 5.5 Forgetting | 1 |
| Unit 6 | 6.1 Thinking | 3 |
| Unit 6 | 6.2 Intelligence | 5 |
| Unit 7 | 7.1 Personality | 6 |
| Unit 7 | 7.2 Motivation | 4 |
| Unit 7 | 7.3 Emotion | 1 |
| Unit 7 | 7.4 Stress and Coping | 3 |
| Unit 8 | 8.2 Social Perception | 2 |
| Unit 8 | 8.4 Social Influence | 1 |
| Unit 8 | 8.5 Group Dynamics | 2 |
| Unit 8 | 8.7 Prosocial Behavior and Aggression | 1 |
| Unit 9 | 9.2 Major Developmental Theories | 2 |
| Unit 9 | 9.3 Psychopathology | 1 |
| Unit 9 | 9.5 Psychotherapies | 4 |
| Unit 10 | 10.2 Poverty and Marginalization | 1 |
| Unit 10 | 10.3 Disability Psychology | 1 |
| Unit 10 | 10.5 Peace Psychology | 1 |
| Unit 10 | 10.6 Wellbeing and Positive Psychology | 2 |
| Unit 10 | 10.7 Health Psychology | 3 |
| Unit 10 | 10.8 Psychology and Technology | 1 |

---

## Cross-References

- **321 questions** have `passage_ref` linking to a passage block
- **0 questions** use `table_ref` (reserved for future use)
- Each paper has exactly **1-2 passages** with **3-5 questions** each
