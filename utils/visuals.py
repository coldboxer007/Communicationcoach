import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def create_spider_chart(scores):
    """
    Creates a spider/radar chart for the overall scores.
    scores: dict with keys 'Content', 'Speech', 'Grammar', 'Clarity', 'Engagement'
    """
    categories = list(scores.keys())
    values = list(scores.values())
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='User Score'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100] # Scores are 0-100 (or scaled to it)
            )),
        showlegend=False
    )
    return fig

def create_bar_chart(user_scores):
    """
    Creates a grouped bar chart comparing User vs Ideal scores.
    user_scores: dict of category scores.
    """
    # Ideal scores based on rubric max points
    ideal_scores = {
        "Content": 40,
        "Speech": 10,
        "Grammar": 20,
        "Clarity": 15,
        "Engagement": 15
    }
    
    categories = list(user_scores.keys())
    user_vals = [user_scores[c] for c in categories]
    ideal_vals = [ideal_scores.get(c, 0) for c in categories]
    
    df = pd.DataFrame({
        "Category": categories * 2,
        "Score": user_vals + ideal_vals,
        "Type": ["User"] * len(categories) + ["Ideal"] * len(categories)
    })
    
    fig = px.bar(df, x="Category", y="Score", color="Type", barmode="group",
                 color_discrete_map={"User": "#636EFA", "Ideal": "#EF553B"})
    return fig

def highlight_text(text, fillers, keywords):
    """
    Returns HTML string with fillers in Red and keywords in Green.
    fillers: list of words to highlight red
    keywords: list of words to highlight green
    """
    # Sort by length desc to avoid partial replacements (e.g. replacing 'cat' in 'catch')
    # But for simple highlighting, word boundary checks are better.
    # Using simple replacement for now, but case insensitive.
    
    highlighted = text
    
    # Helper for case-insensitive replacement with keeping original case
    def replace_keep_case(word, text, color):
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        return pattern.sub(lambda m: f'<span style="background-color: {color}; padding: 2px; border-radius: 3px;">{m.group(0)}</span>', text)

    import re
    
    # Highlight keywords (Green) - lighter green for readability
    for kw in keywords:
        highlighted = replace_keep_case(kw, highlighted, "#90EE90")
        
    # Highlight fillers (Red) - lighter red
    for filler in fillers:
        highlighted = replace_keep_case(filler, highlighted, "#FFB6C1")
        
    return highlighted
