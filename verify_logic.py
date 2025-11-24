import os
from engines.local_engine import process_local
from engines.cloud_engine import process_cloud

def test_local_engine():
    print("Testing Local Engine with Text Input...")
    text = "Hello everyone. My name is John. I am 15 years old. I study at Lincoln High School. My hobbies are reading and coding. Um, actually, I like football too."
    
    result = process_local(None, text)
    
    print("Overall Score:", result.get("overall_score"))
    print("Category Scores:", result.get("category_scores"))
    print("Fillers Found:", result.get("fillers_found"))
    print("Keywords Found:", result.get("keywords_found"))
    
    # Assertions
    assert result.get("overall_score") > 0, "Score should be positive"
    assert "um" in result.get("fillers_found"), "Should detect 'um'"
    assert "actually" in result.get("fillers_found"), "Should detect 'actually'"
    assert "name" in result.get("keywords_found"), "Should detect keyword 'name'"
    
    print("Local Engine Test Passed!")

def test_cloud_engine_no_key():
    print("\nTesting Cloud Engine (No Key)...")
    result = process_cloud(None, "test", "")
    print("Result:", result)
    assert "error" in result, "Should return error for missing key"
    print("Cloud Engine Error Handling Passed!")

if __name__ == "__main__":
    test_local_engine()
    test_cloud_engine_no_key()
