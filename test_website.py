import requests
from bs4 import BeautifulSoup
import json

def test_portfolio_website():
    print("Testing portfolio website...")
    
    # Fetch the HTML content
    url = "http://localhost:8000/index.html"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"❌ Failed to fetch the website. Status code: {response.status_code}")
        return
    
    print(f"✅ Website loaded successfully. Status code: {response.status_code}")
    
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Test 1: Check for animated gradient background
    background = soup.select_one('.background')
    if background:
        print("✅ Animated gradient background is present")
    else:
        print("❌ Animated gradient background is missing")
    
    # Test 2: Check for floating particle system
    particles = soup.select_one('.particles')
    if particles:
        print("✅ Floating particle system is present")
    else:
        print("❌ Floating particle system is missing")
    
    # Test 3: Check for loading screen
    loading = soup.select_one('.loading')
    if loading:
        print("✅ Loading screen is present")
    else:
        print("❌ Loading screen is missing")
    
    # Test 4: Check for scroll indicator
    scroll_indicator = soup.select_one('.scroll-indicator')
    if scroll_indicator:
        print("✅ Scroll indicator is present")
    else:
        print("❌ Scroll indicator is missing")
    
    # Test 5: Check for theme toggle button
    theme_toggle = soup.select_one('.theme-toggle')
    if theme_toggle:
        print("✅ Theme toggle button is present")
    else:
        print("❌ Theme toggle button is missing")
    
    # Test 6: Check for main title with gradient text
    main_title = soup.select_one('.hero h1')
    if main_title and main_title.text.strip() == "YASHVARDHAN":
        print("✅ Main title 'YASHVARDHAN' is present")
    else:
        print("❌ Main title is missing or incorrect")
    
    # Test 7: Check for subtitle with animation
    subtitle = soup.select_one('.subtitle')
    if subtitle:
        print("✅ Subtitle is present")
    else:
        print("❌ Subtitle is missing")
    
    # Test 8: Check for Discord button
    discord_btn = soup.select_one('.btn.discord')
    if discord_btn:
        print("✅ Discord button is present")
    else:
        print("❌ Discord button is missing")
    
    # Test 9: Check for More Links toggle button
    more_links_btn = soup.select_one('.btn.toggle')
    if more_links_btn:
        print("✅ More Links toggle button is present")
    else:
        print("❌ More Links toggle button is missing")
    
    # Test 10: Check for extra links section
    extra_links = soup.select_one('.extra-links')
    if extra_links:
        print("✅ Extra links section is present")
    else:
        print("❌ Extra links section is missing")
    
    # Test 11: Check for projects section
    projects_container = soup.select_one('#projects-container')
    if projects_container:
        print("✅ Projects container is present")
    else:
        print("❌ Projects container is missing")
    
    # Test 12: Check for CSS animations and effects
    css_animations = [
        'gradientShift', 'float', 'textGlow', 'gradientMove', 
        'fadeInUp', 'borderGlow'
    ]
    
    style_tag = soup.select_one('style')
    if style_tag:
        style_content = style_tag.text
        missing_animations = []
        
        for animation in css_animations:
            if animation not in style_content:
                missing_animations.append(animation)
        
        if not missing_animations:
            print("✅ All required CSS animations are present")
        else:
            print(f"❌ Missing CSS animations: {', '.join(missing_animations)}")
    else:
        print("❌ Style tag is missing")
    
    # Test 13: Check for responsive design media queries
    if '@media (max-width: 768px)' in response.text:
        print("✅ Responsive design media queries are present")
    else:
        print("❌ Responsive design media queries are missing")
    
    # Test 14: Check for mouse cursor trail effect
    if 'cursor' in response.text and 'mousemove' in response.text:
        print("✅ Mouse cursor trail effect is present")
    else:
        print("❌ Mouse cursor trail effect is missing")
    
    # Test 15: Check for project cards loading from Logs.json
    if 'fetch(\'./Logs.json\')' in response.text or 'fetch("./Logs.json")' in response.text:
        print("✅ Project cards load from Logs.json")
    else:
        print("❌ Project cards do not load from Logs.json")
    
    # Test 16: Check for high-quality images (not placeholders)
    if 'unsplash.com' in response.text:
        print("✅ High-quality images are used (not placeholders)")
    else:
        print("❌ High-quality images are not used")
    
    # Test 17: Check for glassmorphism effect
    if 'backdrop-filter: blur' in response.text:
        print("✅ Glassmorphism effect is present")
    else:
        print("❌ Glassmorphism effect is missing")
    
    # Test 18: Check for card stats section
    if '.card-stats' in response.text:
        print("✅ Card stats section is present")
    else:
        print("❌ Card stats section is missing")
    
    # Test 19: Check for category titles with # prefix
    if '.category-title::before' in response.text and 'content: \'#\'' in response.text:
        print("✅ Category titles with # prefix are present")
    else:
        print("❌ Category titles with # prefix are missing")
    
    # Test 20: Check for smooth scrolling
    if 'scrollBehavior = \'smooth\'' in response.text:
        print("✅ Smooth scrolling is enabled")
    else:
        print("❌ Smooth scrolling is not enabled")
    
    print("\nTesting completed!")

if __name__ == "__main__":
    test_portfolio_website()