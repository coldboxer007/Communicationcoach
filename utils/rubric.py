import re

# Rubric Constants
RUBRIC = {
    "content": {
        "max_score": 40,
        "salutation": {
            "excellent": ["hello everyone", "good morning", "good afternoon", "good evening"],
            "normal": ["hi", "hello"],
            "points": {"excellent": 5, "normal": 2, "none": 0}
        },
        "keywords": {
            "must_include": ["name", "age", "school", "class", "family", "hobbies"],
            "good_to_include": ["origin", "ambition", "fun fact", "strengths"],
            "points": {"must": 4, "good": 2}
        },
        "flow": {
            "order": ["salutation", "basic_details", "additional_details", "closing"],
            "points": 5
        }
    },
    "speech_rate": {
        "max_score": 10,
        "ideal": (111, 140),
        "acceptable": [(81, 110), (141, 160)],
        "points": {"ideal": 10, "acceptable": 6, "poor": 2}
    },
    "grammar": {
        "max_score": 20,
        "grammar_weight": 10,
        "vocabulary_weight": 10
    },
    "clarity": {
        "max_score": 15,
        "fillers": ["um", "uh", "like", "you know", "so", "actually", "basically"],
        "points": {
            "excellent": 15, # 0-3%
            "good": 12,      # 4-6%
            "poor": 3        # >6% (Prompt said 13% = 3pts, assuming >6% scales down or is 3)
            # Clarification from prompt: "13% = 3pts". I will assume > 6% is poor.
        }
    },
    "engagement": {
        "max_score": 15,
        "thresholds": {"high": 0.9, "low": 0.3},
        "points": {"high": 15, "low": 3}
    }
}

def calculate_wpm(word_count, duration_minutes):
    if duration_minutes <= 0:
        return 0
    return word_count / duration_minutes

def get_speech_rate_score(wpm):
    if RUBRIC["speech_rate"]["ideal"][0] <= wpm <= RUBRIC["speech_rate"]["ideal"][1]:
        return RUBRIC["speech_rate"]["points"]["ideal"]
    
    for r in RUBRIC["speech_rate"]["acceptable"]:
        if r[0] <= wpm <= r[1]:
            return RUBRIC["speech_rate"]["points"]["acceptable"]
            
    return RUBRIC["speech_rate"]["points"]["poor"]

def get_filler_score(filler_count, total_words):
    if total_words == 0:
        return RUBRIC["clarity"]["points"]["excellent"]
    
    percentage = (filler_count / total_words) * 100
    
    if percentage <= 3:
        return RUBRIC["clarity"]["points"]["excellent"]
    elif percentage <= 6:
        return RUBRIC["clarity"]["points"]["good"]
    else:
        return RUBRIC["clarity"]["points"]["poor"]
