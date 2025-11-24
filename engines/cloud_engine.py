import google.generativeai as genai
import json
import os
from utils.rubric import RUBRIC

def process_cloud(audio_path, text_input, api_key):
    """
    Processes audio/text using Gemini 1.5 Flash.
    Returns a JSON object with scores and feedback.
    """
    if not api_key:
        return {"error": "API Key is missing."}
        
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-flash-latest')
        
        # Construct the System Prompt based on the Rubric
        rubric_text = json.dumps(RUBRIC, indent=2)
        
        prompt = f"""
        You are a Communication Coach. Analyze the provided audio/text based on the following STRICT Rubric.
        
        RUBRIC JSON:
        {rubric_text}
        
        INSTRUCTIONS:
        1. Analyze the input for:
           - Content & Structure (Salutation, Keywords, Flow)
           - Speech Rate (Calculate WPM if audio, estimate if text)
           - Language & Grammar (Grammar errors, Vocabulary TTR)
           - Clarity (Filler words count)
           - Engagement (Sentiment)
        2. Assign scores strictly according to the points in the Rubric.
        3. Return the result as a VALID JSON object with this structure:
        {{
            "overall_score": <0-100>,
            "category_scores": {{
                "Content": <0-40>,
                "Speech": <0-10>,
                "Grammar": <0-20>,
                "Clarity": <0-15>,
                "Engagement": <0-15>
            }},
            "feedback": {{
                "Content": "...",
                "Speech": "...",
                "Grammar": "...",
                "Clarity": "...",
                "Engagement": "..."
            }},
            "transcript": "The transcribed text...",
            "fillers_found": ["um", ...],
            "keywords_found": ["name", ...]
        }}
        """
        
        content = [prompt]
        
        if audio_path:
            # Upload file to Gemini
            audio_file = genai.upload_file(path=audio_path)
            content.append(audio_file)
        elif text_input:
            content.append(f"Input Text: {text_input}")
        else:
            return {"error": "No input provided."}
            
        response = model.generate_content(content)
        
        # Parse JSON from response
        try:
            # Clean up markdown code blocks if present
            text_res = response.text.strip()
            if text_res.startswith("```json"):
                text_res = text_res[7:]
            if text_res.endswith("```"):
                text_res = text_res[:-3]
            
            result = json.loads(text_res)
            return result
        except json.JSONDecodeError:
            return {"error": "Failed to parse Gemini response.", "raw_response": response.text}
            
    except Exception as e:
        return {"error": str(e)}
