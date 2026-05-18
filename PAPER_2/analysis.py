#!/usr/bin/env python3
"""
UGC NET Psychology Paper 2 — Comprehensive Data Analysis
Analyzes 53 JSON files (2004-2025) for patterns, trends, and era-wise shifts.
"""

import json
import os
from collections import Counter, defaultdict
from pathlib import Path

# ===========================================================================
# 1. LOAD ALL DATA
# ===========================================================================

BASE_DIR = Path("/projects/sandbox/Analysis/PAPER_2")
FOLDERS = ["2004-2008", "2009-2012", "2013-2016", "2017-2020", "2021-2024", "2025-2026"]

all_questions = []
file_metadata = []

for folder in FOLDERS:
    folder_path = BASE_DIR / folder
    if not folder_path.exists():
        continue
    for json_file in sorted(folder_path.glob("*.json")):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        metadata = data.get("paper_metadata", {})
        content = data.get("content", [])
        
        questions_in_file = []
        for block in content:
            if block.get("type") == "questions_block":
                for q in block.get("questions", []):
                    q["_source_file"] = json_file.name
                    q["_folder"] = folder
                    q["_paper_subject"] = metadata.get("subject", "")
                    q["_paper_date"] = metadata.get("date", "")
                    questions_in_file.append(q)
        
        all_questions.extend(questions_in_file)
        file_metadata.append({
            "file": json_file.name,
            "folder": folder,
            "date": metadata.get("date", ""),
            "subject": metadata.get("subject", ""),
            "question_count": len(questions_in_file)
        })

print(f"Total files loaded: {len(file_metadata)}")
print(f"Total questions loaded: {len(all_questions)}")
print()

# ===========================================================================
# 2. DEFINE ERAS
# ===========================================================================

def get_era(year, paper_subject=""):
    """Assign meaningful historical era based on year."""
    if year <= 2012:
        return "Era 1: Early UGC (2004-2012)"
    elif year <= 2017:
        return "Era 2: Split Paper CBSE (2013-2017)"
    elif year <= 2019:
        return "Era 3: NTA Transition (2018-2019)"
    else:
        return "Era 4: Modern NTA (2020-2025)"

for q in all_questions:
    q["_era"] = get_era(q.get("year", 0), q.get("_paper_subject", ""))

# ===========================================================================
# 3. BASIC STATISTICS
# ===========================================================================

print("=" * 80)
print("SECTION 1: BASIC STATISTICS")
print("=" * 80)

# Questions per era
era_counts = Counter(q["_era"] for q in all_questions)
print("\n--- Questions per Era ---")
for era in sorted(era_counts.keys()):
    print(f"  {era}: {era_counts[era]} questions")

# Questions per year
year_counts = Counter(q.get("year", 0) for q in all_questions)
print("\n--- Questions per Year ---")
for year in sorted(year_counts.keys()):
    print(f"  {year}: {year_counts[year]} questions")

# ===========================================================================
# 4. UNIT DISTRIBUTION ANALYSIS
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 2: UNIT DISTRIBUTION")
print("=" * 80)

# Overall unit distribution
unit_counts = Counter(q.get("unit", "Unknown") for q in all_questions)
print("\n--- Overall Unit Distribution ---")
total_q = len(all_questions)
for unit in sorted(unit_counts.keys()):
    pct = (unit_counts[unit] / total_q) * 100
    print(f"  {unit}: {unit_counts[unit]} ({pct:.1f}%)")

# Unit distribution by era
print("\n--- Unit Distribution by Era (percentage) ---")
era_unit_dist = defaultdict(lambda: Counter())
for q in all_questions:
    era_unit_dist[q["_era"]][q.get("unit", "Unknown")] += 1

all_units = sorted(set(q.get("unit", "Unknown") for q in all_questions))
print(f"\n{'Unit':<12}", end="")
for era in sorted(era_unit_dist.keys()):
    era_short = era.split(":")[0].strip()
    print(f"{era_short:>20}", end="")
print()

for unit in all_units:
    print(f"{unit:<12}", end="")
    for era in sorted(era_unit_dist.keys()):
        era_total = sum(era_unit_dist[era].values())
        count = era_unit_dist[era].get(unit, 0)
        pct = (count / era_total * 100) if era_total > 0 else 0
        print(f"{pct:>18.1f}%", end="")
    print()

# ===========================================================================
# 5. TOPIC DISTRIBUTION ANALYSIS
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 3: TOPIC DISTRIBUTION (Top 30 Overall)")
print("=" * 80)

topic_counts = Counter(q.get("topic", "Unknown") for q in all_questions)
print("\n--- Top 30 Topics Overall ---")
for topic, count in topic_counts.most_common(30):
    pct = (count / total_q) * 100
    print(f"  {topic}: {count} ({pct:.1f}%)")

# Top topics per era
print("\n--- Top 10 Topics per Era ---")
for era in sorted(era_unit_dist.keys()):
    era_qs = [q for q in all_questions if q["_era"] == era]
    era_topic_counts = Counter(q.get("topic", "Unknown") for q in era_qs)
    print(f"\n  {era} ({len(era_qs)} questions):")
    for topic, count in era_topic_counts.most_common(10):
        pct = (count / len(era_qs)) * 100
        print(f"    {topic}: {count} ({pct:.1f}%)")

# ===========================================================================
# 6. SUBTOPIC ANALYSIS
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 4: SUBTOPIC ANALYSIS (Top 40 Overall)")
print("=" * 80)

subtopic_counts = Counter(q.get("subtopic", "Unknown") for q in all_questions)
print("\n--- Top 40 Subtopics Overall ---")
for subtopic, count in subtopic_counts.most_common(40):
    pct = (count / total_q) * 100
    print(f"  {subtopic}: {count} ({pct:.1f}%)")

# ===========================================================================
# 7. TOPIC TRENDS ACROSS ERAS (Rising vs Declining)
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 5: TOPIC TRENDS — RISING vs DECLINING")
print("=" * 80)

# Compare Era 1+2 (old) vs Era 3+4 (new)
old_qs = [q for q in all_questions if q["_era"] in ["Era 1: Early UGC (2004-2012)", "Era 2: Split Paper CBSE (2013-2017)"]]
new_qs = [q for q in all_questions if q["_era"] in ["Era 3: NTA Transition (2018-2019)", "Era 4: Modern NTA (2020-2025)"]]

old_topic_pct = {}
new_topic_pct = {}
old_total = len(old_qs)
new_total = len(new_qs)

for topic, count in Counter(q.get("topic", "Unknown") for q in old_qs).items():
    old_topic_pct[topic] = (count / old_total) * 100

for topic, count in Counter(q.get("topic", "Unknown") for q in new_qs).items():
    new_topic_pct[topic] = (count / new_total) * 100

# All topics that appear in either
all_topics = set(old_topic_pct.keys()) | set(new_topic_pct.keys())
topic_changes = []
for topic in all_topics:
    old_pct = old_topic_pct.get(topic, 0)
    new_pct = new_topic_pct.get(topic, 0)
    change = new_pct - old_pct
    topic_changes.append((topic, old_pct, new_pct, change))

topic_changes.sort(key=lambda x: x[3], reverse=True)

print("\n--- RISING TOPICS (Old → New, biggest positive change) ---")
for topic, old_pct, new_pct, change in topic_changes[:20]:
    if change > 0:
        print(f"  {topic}: {old_pct:.1f}% → {new_pct:.1f}% (↑{change:+.1f}%)")

print("\n--- DECLINING TOPICS (Old → New, biggest negative change) ---")
for topic, old_pct, new_pct, change in reversed(topic_changes[-20:]):
    if change < 0:
        print(f"  {topic}: {old_pct:.1f}% → {new_pct:.1f}% (↓{change:+.1f}%)")

# ===========================================================================
# 8. ERA 4 DEEP DIVE (Most relevant for June 2026)
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 6: ERA 4 DEEP DIVE — MODERN NTA (2020-2025)")
print("=" * 80)

era4_qs = [q for q in all_questions if q["_era"] == "Era 4: Modern NTA (2020-2025)"]
print(f"\nTotal Era 4 questions: {len(era4_qs)}")

# Unit distribution in Era 4
era4_unit = Counter(q.get("unit", "Unknown") for q in era4_qs)
print("\n--- Unit Distribution (Era 4) ---")
for unit in sorted(era4_unit.keys()):
    count = era4_unit[unit]
    pct = (count / len(era4_qs)) * 100
    print(f"  {unit}: {count} ({pct:.1f}%)")

# Topic distribution in Era 4
era4_topic = Counter(q.get("topic", "Unknown") for q in era4_qs)
print("\n--- Top 30 Topics (Era 4) ---")
for topic, count in era4_topic.most_common(30):
    pct = (count / len(era4_qs)) * 100
    print(f"  {topic}: {count} ({pct:.1f}%)")

# Subtopic distribution in Era 4
era4_subtopic = Counter(q.get("subtopic", "Unknown") for q in era4_qs)
print("\n--- Top 40 Subtopics (Era 4) ---")
for subtopic, count in era4_subtopic.most_common(40):
    pct = (count / len(era4_qs)) * 100
    print(f"  {subtopic}: {count} ({pct:.1f}%)")

# ===========================================================================
# 9. YEAR-OVER-YEAR UNIT DISTRIBUTION (Era 4 only)
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 7: YEAR-OVER-YEAR UNIT DISTRIBUTION (2020-2025)")
print("=" * 80)

era4_years = sorted(set(q.get("year", 0) for q in era4_qs))
year_unit_dist = defaultdict(lambda: Counter())
for q in era4_qs:
    year_unit_dist[q.get("year", 0)][q.get("unit", "Unknown")] += 1

print(f"\n{'Unit':<12}", end="")
for year in era4_years:
    print(f"{year:>8}", end="")
print()

for unit in sorted(all_units):
    print(f"{unit:<12}", end="")
    for year in era4_years:
        year_total = sum(year_unit_dist[year].values())
        count = year_unit_dist[year].get(unit, 0)
        pct = (count / year_total * 100) if year_total > 0 else 0
        print(f"{pct:>7.1f}%", end="")
    print()

# ===========================================================================
# 10. PASSAGE-BASED QUESTION ANALYSIS
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 8: PASSAGE-BASED QUESTION ANALYSIS")
print("=" * 80)

passage_qs = [q for q in all_questions if q.get("passage_ref")]
non_passage_qs = [q for q in all_questions if not q.get("passage_ref")]

print(f"\nPassage-based questions: {len(passage_qs)} ({len(passage_qs)/total_q*100:.1f}%)")
print(f"Standalone questions: {len(non_passage_qs)} ({len(non_passage_qs)/total_q*100:.1f}%)")

# Passage questions by era
print("\n--- Passage Questions by Era ---")
for era in sorted(set(q["_era"] for q in all_questions)):
    era_total = len([q for q in all_questions if q["_era"] == era])
    era_passage = len([q for q in passage_qs if q["_era"] == era])
    pct = (era_passage / era_total * 100) if era_total > 0 else 0
    print(f"  {era}: {era_passage}/{era_total} ({pct:.1f}%)")

# Topics in passage questions (Era 4)
era4_passage = [q for q in passage_qs if q["_era"] == "Era 4: Modern NTA (2020-2025)"]
era4_passage_topics = Counter(q.get("topic", "Unknown") for q in era4_passage)
print(f"\n--- Passage Question Topics (Era 4, {len(era4_passage)} questions) ---")
for topic, count in era4_passage_topics.most_common(15):
    print(f"  {topic}: {count}")

# ===========================================================================
# 11. CONCEPT ANALYSIS — Most tested concepts
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 9: CONCEPT DENSITY & QUESTION COMPLEXITY")
print("=" * 80)

# Average concept length by era (proxy for question complexity)
era_concept_lengths = defaultdict(list)
for q in all_questions:
    concept = q.get("concept", "")
    if concept:
        era_concept_lengths[q["_era"]].append(len(concept))

print("\n--- Average Concept Explanation Length by Era ---")
for era in sorted(era_concept_lengths.keys()):
    lengths = era_concept_lengths[era]
    avg = sum(lengths) / len(lengths) if lengths else 0
    print(f"  {era}: avg {avg:.0f} chars ({len(lengths)} questions with concepts)")

# Average question text length by era
era_q_lengths = defaultdict(list)
for q in all_questions:
    q_text = q.get("question", "")
    era_q_lengths[q["_era"]].append(len(q_text))

print("\n--- Average Question Text Length by Era ---")
for era in sorted(era_q_lengths.keys()):
    lengths = era_q_lengths[era]
    avg = sum(lengths) / len(lengths) if lengths else 0
    print(f"  {era}: avg {avg:.0f} chars")

# ===========================================================================
# 12. MOST RECENT PAPERS ANALYSIS (2023-2025) — Direct exam prep relevance
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 10: MOST RECENT PAPERS (2023-2025) — HIGHEST PREP RELEVANCE")
print("=" * 80)

recent_qs = [q for q in all_questions if q.get("year", 0) >= 2023]
print(f"\nTotal recent questions (2023-2025): {len(recent_qs)}")

# Unit distribution
recent_unit = Counter(q.get("unit", "Unknown") for q in recent_qs)
print("\n--- Unit Distribution (2023-2025) ---")
for unit in sorted(recent_unit.keys()):
    count = recent_unit[unit]
    pct = (count / len(recent_qs)) * 100
    print(f"  {unit}: {count} ({pct:.1f}%)")

# Topic distribution
recent_topic = Counter(q.get("topic", "Unknown") for q in recent_qs)
print("\n--- Top 25 Topics (2023-2025) ---")
for topic, count in recent_topic.most_common(25):
    pct = (count / len(recent_qs)) * 100
    print(f"  {topic}: {count} ({pct:.1f}%)")

# Subtopic distribution
recent_subtopic = Counter(q.get("subtopic", "Unknown") for q in recent_qs)
print("\n--- Top 30 Subtopics (2023-2025) ---")
for subtopic, count in recent_subtopic.most_common(30):
    pct = (count / len(recent_qs)) * 100
    print(f"  {subtopic}: {count} ({pct:.1f}%)")

# ===========================================================================
# 13. UNIT-WISE TOPIC BREAKDOWN FOR ERA 4
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 11: UNIT-WISE TOPIC BREAKDOWN (ERA 4)")
print("=" * 80)

for unit in sorted(set(q.get("unit", "Unknown") for q in era4_qs)):
    unit_qs = [q for q in era4_qs if q.get("unit") == unit]
    unit_topics = Counter(q.get("topic", "Unknown") for q in unit_qs)
    print(f"\n  {unit} ({len(unit_qs)} questions):")
    for topic, count in unit_topics.most_common(15):
        pct = (count / len(unit_qs)) * 100
        print(f"    {topic}: {count} ({pct:.1f}%)")
    
    # Top subtopics for this unit
    unit_subtopics = Counter(q.get("subtopic", "Unknown") for q in unit_qs)
    print(f"    --- Top subtopics:")
    for subtopic, count in unit_subtopics.most_common(10):
        print(f"      {subtopic}: {count}")

# ===========================================================================
# 14. CROSS-YEAR CONSISTENCY CHECK — Which topics appear EVERY year?
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 12: TOPIC CONSISTENCY — Topics appearing in EVERY Era 4 year")
print("=" * 80)

era4_year_topics = defaultdict(set)
for q in era4_qs:
    era4_year_topics[q.get("year", 0)].add(q.get("topic", "Unknown"))

# Topics present in all Era 4 years
consistent_topics = None
for year, topics in era4_year_topics.items():
    if consistent_topics is None:
        consistent_topics = topics.copy()
    else:
        consistent_topics &= topics

print(f"\nTopics appearing in ALL Era 4 years ({len(era4_years)} years):")
print(f"Total consistent topics: {len(consistent_topics)}")
for topic in sorted(consistent_topics):
    # Get average questions per year for this topic
    counts = []
    for year in era4_years:
        year_qs = [q for q in era4_qs if q.get("year") == year and q.get("topic") == topic]
        counts.append(len(year_qs))
    avg = sum(counts) / len(counts)
    print(f"  {topic}: avg {avg:.1f} questions/year (range: {min(counts)}-{max(counts)})")

# ===========================================================================
# 15. NEWLY EMERGING TOPICS (Only in Era 4, not in earlier eras)
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 13: NEWLY EMERGING TOPICS (Era 4 only, absent in Era 1+2)")
print("=" * 80)

old_topics = set(q.get("topic", "Unknown") for q in old_qs)
new_only_topics = set(q.get("topic", "Unknown") for q in era4_qs) - old_topics

era4_new_topic_counts = Counter()
for q in era4_qs:
    if q.get("topic", "Unknown") in new_only_topics:
        era4_new_topic_counts[q.get("topic", "Unknown")] += 1

print(f"\nTopics that exist ONLY in Era 4 (not in pre-2018 papers):")
for topic, count in era4_new_topic_counts.most_common(30):
    print(f"  {topic}: {count} questions")

# ===========================================================================
# 16. DISAPPEARING TOPICS (In Era 1+2, absent in Era 4)
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 14: DISAPPEARING TOPICS (Present in Era 1+2, absent in Era 4)")
print("=" * 80)

era4_topics = set(q.get("topic", "Unknown") for q in era4_qs)
disappeared_topics = old_topics - era4_topics

old_disappeared_counts = Counter()
for q in old_qs:
    if q.get("topic", "Unknown") in disappeared_topics:
        old_disappeared_counts[q.get("topic", "Unknown")] += 1

print(f"\nTopics that appeared in old eras but are ABSENT in Era 4:")
for topic, count in old_disappeared_counts.most_common(20):
    print(f"  {topic}: {count} questions (in old era)")

# ===========================================================================
# 17. CORRECT ANSWER DISTRIBUTION
# ===========================================================================

print("\n" + "=" * 80)
print("SECTION 15: CORRECT ANSWER DISTRIBUTION")
print("=" * 80)

answer_dist = Counter(q.get("correct_answer", 0) for q in all_questions)
print("\n--- Overall Correct Answer Distribution ---")
for ans in sorted(answer_dist.keys()):
    labels = {1: "A", 2: "B", 3: "C", 4: "D"}
    pct = (answer_dist[ans] / total_q) * 100
    print(f"  ({labels.get(ans, '?')}) Option {ans}: {answer_dist[ans]} ({pct:.1f}%)")

# By era
print("\n--- Correct Answer Distribution by Era ---")
for era in sorted(set(q["_era"] for q in all_questions)):
    era_qs_local = [q for q in all_questions if q["_era"] == era]
    era_ans = Counter(q.get("correct_answer", 0) for q in era_qs_local)
    era_total_local = len(era_qs_local)
    print(f"  {era}:")
    for ans in sorted(era_ans.keys()):
        labels = {1: "A", 2: "B", 3: "C", 4: "D"}
        pct = (era_ans[ans] / era_total_local) * 100
        print(f"    ({labels.get(ans, '?')}): {pct:.1f}%", end="  ")
    print()

print("\n\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
