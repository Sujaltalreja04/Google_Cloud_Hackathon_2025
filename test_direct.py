#!/usr/bin/env python3
"""
Pure Python test without Streamlit
"""
import requests
import json

def test_ollama_direct():
    """Test Ollama directly without any Streamlit imports"""
    print("Testing Ollama API directly...")
    
    # Test 1: Check if Ollama is available
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print(f"✅ Ollama is running with {len(models)} models")
            for model in models[:3]:  # Show first 3 models
                print(f"   - {model['name']}")
        else:
            print(f"❌ Ollama API returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to Ollama: {e}")
        return False
    
    # Test 2: Simple AI generation
    try:
        payload = {
            "model": "tinyllama:1.1b",
            "prompt": "Generate 3 resume improvement tips:",
            "stream": False,
            "options": {
                "temperature": 0.3,
                "num_predict": 200
            }
        }
        
        print("🚀 Testing AI generation...")
        response = requests.post(
            "http://localhost:11434/api/generate", 
            json=payload, 
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            ai_response = result.get('response', '').strip()
            if ai_response:
                print("✅ AI generation successful!")
                print(f"📝 Response length: {len(ai_response)} chars")
                print("🎯 Sample output:")
                print("-" * 40)
                print(ai_response[:200] + "..." if len(ai_response) > 200 else ai_response)
                print("-" * 40)
                return True
            else:
                print("❌ Empty response from AI")
                return False
        else:
            print(f"❌ AI generation failed with status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ AI generation error: {e}")
        return False

def test_resume_enhancement_direct():
    """Test resume enhancement without Streamlit"""
    print("\n" + "="*50)
    print("Testing Resume Enhancement Feature")
    print("="*50)
    
    resume_text = """John Doe - Software Engineer
    
    Experience:
    • Developed Python web applications
    • Worked with databases and APIs
    • Team collaboration on software projects
    """
    
    jd_text = """Senior Python Developer
    Requirements:
    • Machine Learning experience
    • FastAPI and REST APIs
    • Docker containerization
    • AWS cloud platforms
    • Large-scale systems
    """
    
    missing_skills = ["machine learning", "fastapi", "docker", "aws"]
    
    prompt = f\"\"\"You are an expert resume writer. Analyze this resume and job description, then provide specific improvements.

RESUME:
{resume_text}

JOB REQUIREMENTS:
{jd_text}

MISSING SKILLS: {', '.join(missing_skills)}

Provide 5 actionable resume improvements:\"\"\"
    
    payload = {
        "model": "tinyllama:1.1b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 400
        }
    }
    
    try:
        print("🎯 Generating resume improvements...")
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            improvements = result.get('response', '').strip()
            
            if improvements:
                print("✅ Resume enhancement successful!")
                print("\n📋 RESUME IMPROVEMENTS:")
                print("="*60)
                print(improvements)
                print("="*60)
                return True
            else:
                print("❌ Empty improvements generated")
                return False
        else:
            print(f"❌ Failed with status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Enhancement failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 AI-Powered Career Counselor - Direct Test")
    print("="*60)
    
    # Test Ollama connection
    if not test_ollama_direct():
        print("\n❌ Ollama connection failed. Please ensure Ollama is running.")
        exit(1)
    
    # Test resume enhancement
    if test_resume_enhancement_direct():
        print("\n🎉 All tests passed! The resume enhancement feature is working.")
        print("✅ The timeout issue has been resolved.")
    else:
        print("\n❌ Resume enhancement test failed.")